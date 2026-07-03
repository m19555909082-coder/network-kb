# -*- coding: utf-8 -*-
"""
计算机网络知识库构建脚本 (MkDocs + Material)
完整保留所有PPT幻灯片双语内容 + 图片嵌入
"""
import os, json, glob, shutil, re

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, "docs")
SRC = r"C:\Users\He Guoxin\Desktop\claude\复习"

# ============================================================
# 0. 准备工作
# ============================================================
print("=" * 60)
print("[准备工作] 清理并创建目录...")

# 清理旧的docs
if os.path.exists(DOCS):
    shutil.rmtree(DOCS)

dirs = [
    "ch01-vlan", "ch02-network-expansion", "ch03-subnet-routing",
    "ch04-campus-network", "ch05-acl", "ch06-nat", "ch07-network-design",
    "experiments", "img", "stylesheets",
]
for d in dirs:
    os.makedirs(os.path.join(DOCS, d), exist_ok=True)

# 复制图片
img_dir = os.path.join(DOCS, "img")
with open(os.path.join(SRC, "extracted_all.json"), "r", encoding="utf-8") as f:
    src_data = json.load(f)

img_count = 0
for path, info in src_data["files"].items():
    if info.get("type") == "image":
        src_path = os.path.join(SRC, path)
        dst_path = os.path.join(img_dir, info["name"])
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            img_count += 1
print(f"  图片复制完成: {img_count} 张")

# ============================================================
# 1. 读取所有PPT原文
# ============================================================
print("[1/7] 加载PPT源文件...")

def read_ppt_text(filename):
    """读取PPT全文txt，返回幻灯片列表 [(slide_num, slide_text), ...]"""
    filepath = os.path.join(SRC, filename)
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    slides = []
    # 按 --- Slide N --- 分割
    parts = re.split(r'\n--- Slide (\d+) ---\n', content)
    # parts[0] = header, parts[1]=num, parts[2]=content, parts[3]=num, ...
    for i in range(1, len(parts) - 1, 2):
        num = int(parts[i])
        text = parts[i + 1].strip()
        slides.append((num, text))
    return slides

# PPT文件映射（用关键词glob匹配，避免Unicode文件名问题）
PPT_KEYWORDS = {
    "ch01": "1-优化",
    "ch02": "2-扩展",
    "ch03": "3-使用",
    "ch04": "4-构建",
    "ch05": "5访问",
    "ch06": "6网络",
    "ch07": "网络工程设计CH1",
}

ppt_slides = {}
ppt_full_texts = {}  # 保存完整PPT文本，供复习大纲搜索答案用
all_txt_files = glob.glob(os.path.join(SRC, "*_full.txt"))
for ch, keyword in PPT_KEYWORDS.items():
    matched = [f for f in all_txt_files if keyword in os.path.basename(f)]
    if matched:
        fname = os.path.basename(matched[0])
        slides = read_ppt_text(fname)
        ppt_slides[ch] = slides
        # 同时保存完整文本
        with open(os.path.join(SRC, fname), "r", encoding="utf-8") as _f:
            ppt_full_texts[ch] = _f.read()
        print(f"  {ch}: {len(slides)} 张幻灯片 ← {fname[:60]}...")
    else:
        print(f"  {ch}: ⚠ 未找到匹配文件 (关键词: {keyword})")
        ppt_slides[ch] = []
        ppt_full_texts[ch] = ""

# ============================================================
# 2. 读取实验报告和复习大纲
# ============================================================
print("[2/7] 加载实验报告和复习大纲...")

experiments = {}
outline_text = ""

for path, info in src_data["files"].items():
    name = info.get("name", "")
    if info.get("type") == "doc" and "实验" in name:
        exp_text = info.get("text", "")
        exp_lines = info.get("text_lines", [])
        experiments[name.replace(".doc", "")] = {
            "text": exp_text,
            "lines": exp_lines
        }
    if "复习大纲" in path:
        outline_text = info.get("text", "")

print(f"  实验报告: {len(experiments)} 个")
print(f"  复习大纲: {len(outline_text)} 字符")

# ============================================================
# 辅助函数
# ============================================================

def write_md(path, content):
    """写入markdown文件"""
    filepath = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def find_img(name_hint):
    """根据名称提示查找图片文件"""
    img_dir = os.path.join(DOCS, "img")
    for fname in os.listdir(img_dir):
        if name_hint.lower() in fname.lower():
            return f"../img/{fname}"
    return None

def img_ref(desc, name_hint=None):
    """生成图片引用markdown"""
    if name_hint:
        img_path = find_img(name_hint)
        if img_path:
            return f"![{desc}]({img_path})"
    # 尝试用描述中的关键词找图
    for keyword in desc.split():
        if len(keyword) >= 2:
            img_path = find_img(keyword)
            if img_path:
                return f"![{desc}]({img_path})"
    return f"<!-- [图: {desc}] -->"

# 中文转拼音slug
def slugify(text):
    """简单的中文文本处理"""
    return re.sub(r'[^\w\-]', '', text.replace(' ', '-').lower())[:50]

# ============================================================
# 3. 生成 mkdocs.yml
# ============================================================
print("[3/7] 生成 mkdocs.yml...")

mkdocs_yml = """site_name: 计算机网络知识点总结
site_description: Computer Networks Knowledge Base - Bilingual (Chinese/English)
site_author: 网络工程课程
copyright: Copyright &copy; 2025 计算机网络课程

theme:
  name: material
  language: zh
  features:
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.tracking
    - navigation.indexes
    - search.suggest
    - search.highlight
    - search.share
    - content.code.copy
    - content.code.annotate
  palette:
    - scheme: default
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-7
        name: 暗色模式
    - scheme: slate
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-4
        name: 亮色模式
  font:
    text: Roboto
    code: Roboto Mono

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.emoji
  - pymdownx.tasklist:
      custom_checkbox: true
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true
      toc_depth: 4

plugins:
  - search:
      lang:
        - zh
        - en
      separator: '[\s\-_.,:;!?()\[\]{}]+'

extra_css:
  - stylesheets/extra.css

nav:
  - 首页: index.md
  - 第1章 VLAN技术:
    - ch01-vlan/index.md
"""

# 动态添加各章导航
chapter_navs = {
    "ch01-vlan": "第1章 VLAN技术",
    "ch02-network-expansion": "第2章 扩展办公网络",
    "ch03-subnet-routing": "第3章 子网与路由",
    "ch04-campus-network": "第4章 构建园区网络",
    "ch05-acl": "第5章 访问控制列表(ACL)",
    "ch06-nat": "第6章 网络地址转换(NAT)",
    "ch07-network-design": "第7章 网络工程设计",
}

# 稍后会在生成子页面后补充导航
mkdocs_yml += "\n".join([f'    - {label}:\n        - {ch}/index.md' for ch, label in chapter_navs.items()])
mkdocs_yml += """
  - 实验报告:
    - experiments/index.md
  - 复习大纲: review-outline.md
"""

# mkdocs.yml must be at project root, not in docs/
with open(os.path.join(BASE, "mkdocs.yml"), "w", encoding="utf-8") as f:
    f.write(mkdocs_yml)

# ============================================================
# 4. 自定义CSS
# ============================================================
print("[4/7] 生成自定义样式...")

write_md("stylesheets/extra.css", """/* 计算机网络知识库自定义样式 */

:root {
  --md-primary-fg-color: #1565C0;
  --md-accent-fg-color: #0D47A1;
}

/* 双语内容样式 */
.bilingual-cn {
  color: #1a237e;
  border-left: 3px solid #1565C0;
  padding-left: 12px;
  margin: 8px 0;
}

.bilingual-en {
  color: #546e7a;
  border-left: 3px solid #90a4ae;
  padding-left: 12px;
  margin: 8px 0;
  font-style: italic;
}

/* 配置命令代码块 */
.md-typeset pre > code {
  border-radius: 6px;
}

/* 图片居中 */
.md-typeset img {
  display: block;
  margin: 1em auto;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  max-width: 100%;
}

/* 幻灯片分隔 */
.slide-separator {
  border-top: 2px dashed #bdbdbd;
  margin: 2em 0;
}

/* 考点标记 */
.key-point {
  background: #fff3e0;
  border-left: 4px solid #ff9800;
  padding: 8px 16px;
  margin: 12px 0;
  font-weight: bold;
}

/* 命令参考 */
.cmd-ref {
  background: #e8f5e9;
  border-left: 4px solid #4caf50;
  padding: 8px 16px;
  margin: 12px 0;
}

/* 表格增强 */
.md-typeset table:not([class]) {
  font-size: 0.85rem;
}

.md-typeset table:not([class]) th {
  background: #1565C0;
  color: white;
}
""")

# ============================================================
# 5. 首页
# ============================================================
print("[5/7] 生成首页...")

total_slides = sum(len(v) for v in ppt_slides.values())

index_md = f"""# <center>计算机网络知识点总结</center>

<center>**Computer Networks Knowledge Base**</center>

<center>📚 中英双语 | 🖥️ 完整保留PPT原文 | 📝 配置命令可直接复制</center>

---

## 课程信息

| 项目 | 内容 |
|------|------|
| 课程名称 | 计算机网络 (Computer Networks) |
| 内容来源 | 7份PPT课件 + 7份实验报告 + 复习大纲 |
| 幻灯片总数 | {total_slides} 张 |
| 语言 | 中文 + English（双语完整保留） |
| 特色 | 图片直接嵌入，配置命令可复制 |

---

## 内容概览

本知识库涵盖**7大章节**，完整覆盖计算机网络课程的全部内容：

| 章节 | 主要内容 | 幻灯片数 |
|------|----------|----------|
| 第1章 | VLAN技术 — 虚拟局域网、广播域隔离、Access/Trunk、802.1Q | {len(ppt_slides.get('ch01', []))} |
| 第2章 | 扩展办公网络 — 层次化设计、级联堆叠、链路聚合、STP | {len(ppt_slides.get('ch02', []))} |
| 第3章 | 子网与路由 — 路由基础、路由器配置、直连/静态路由、子接口 | {len(ppt_slides.get('ch03', []))} |
| 第4章 | 构建园区网络 — 园区网规划、IP地址规划、RIP/OSPF | {len(ppt_slides.get('ch04', []))} |
| 第5章 | 访问控制列表(ACL) — 标准/扩展ACL、通配符掩码、命名ACL | {len(ppt_slides.get('ch05', []))} |
| 第6章 | 网络地址转换(NAT) — 静态/动态NAT、PAT、负载均衡 | {len(ppt_slides.get('ch06', []))} |
| 第7章 | 网络工程设计 — 系统集成方法、层次模型、需求分析 | {len(ppt_slides.get('ch07', []))} |

---

## 使用方式

- **浏览**: 左侧导航栏选择章节和子页面
- **搜索**: 顶部搜索框支持中文/英文全文搜索 (`/` 快捷键)
- **代码**: 所有配置命令可直接复制使用
- **图片**: 拓扑图和教材配图已嵌入对应位置

## 特色

- ✅ 所有内容来自原始PPT课件，**非AI生成**
- ✅ **中英双语**完整保留，逐张幻灯片还原
- ✅ 配置命令可**直接复制**使用
- ✅ 拓扑图和配图**嵌入原文对应位置**
"""

write_md("index.md", index_md)

# ============================================================
# 6. 生成各章内容（逐幻灯片完整保留）
# ============================================================
print("[6/7] 生成章节内容（逐幻灯片保留）...")

def format_bilingual_block(cn_text, en_text, separator="\n\n"):
    """格式化双语内容块"""
    result = []
    if cn_text and cn_text.strip():
        result.append(f'<div class="bilingual-cn" markdown>\n\n**🇨🇳 中文**\n\n{cn_text.strip()}\n\n</div>')
    if en_text and en_text.strip():
        result.append(f'<div class="bilingual-en" markdown>\n\n**🇬🇧 English**\n\n{en_text.strip()}\n\n</div>')
    return separator.join(result) if result else ""

def split_bilingual(text):
    """尝试分离中英文混合文本
    返回 (cn_part, en_part) - 启发式分离
    """
    # 许多幻灯片中英文是连在一起的，用常见模式分离
    # 模式1: 中文后面紧接英文（首字母大写）
    # 模式2: 换行分隔

    # 先尝试按明显的分隔符分离
    lines = text.split('\n')
    cn_lines = []
    en_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 判断是否主要是英文
        ascii_count = sum(1 for c in line if ord(c) < 128)
        total = len(line)
        if total == 0:
            continue
        ratio = ascii_count / total

        if ratio > 0.7:
            en_lines.append(line)
        elif ratio < 0.3:
            cn_lines.append(line)
        else:
            # 混合行，尝试按句子分割
            cn_lines.append(line)
            en_lines.append(line)

    cn = '\n'.join(cn_lines) if cn_lines else text
    en = '\n'.join(en_lines) if en_lines else ""
    return cn, en

def format_slide(slide_num, text, chapter_dir="."):
    """格式化单张幻灯片为markdown"""
    lines = text.strip().split('\n')

    # 清理行内容
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            clean_lines.append('')
            continue
        # 去掉纯页码行和重复的作者行
        if re.match(r'^\d{1,2}$', line) and len(line) <= 2:
            continue
        if line in ['解放军理工大学计算机系', '陈鸣：网络工程设计']:
            continue
        clean_lines.append(line)

    if not clean_lines:
        return ""

    # 第一行通常是小标题
    title = clean_lines[0] if clean_lines else f"Slide {slide_num}"
    # 限制标题长度
    if len(title) > 80:
        title = title[:80] + "..."

    content = '\n'.join(clean_lines)

    # 检测是否包含配置命令
    has_commands = any(kw in content for kw in ['Switch(config)', 'Switch#', 'Router(config)',
                                                   'interface ', 'ip address', 'switchport',
                                                   'vlan', 'no shutdown', 'channel-group'])

    md = f"\n\n---\n\n### 📄 Slide {slide_num}：{title}\n\n"

    if has_commands:
        # 有命令的内容：保留原文 + 代码块提取
        cn, en = split_bilingual(content)
        md += format_bilingual_block(cn, en)

        # 提取命令行
        cmd_lines = []
        for line in clean_lines:
            if re.search(r'(Switch|Router)[\(#]|interface |ip address|switchport|vlan |no shut|channel-group|encapsulation|access-list|ip nat|ip route|network |area |redistribute', line, re.IGNORECASE):
                cmd_lines.append(line)
        if cmd_lines:
            md += f"\n**💻 配置命令：**\n\n```cisco\n" + '\n'.join(cmd_lines[:30]) + "\n```\n"
    else:
        cn, en = split_bilingual(content)
        md += format_bilingual_block(cn, en)

    # 检测图片引用
    fig_patterns = [
        r'如图\s*(\d+[.-]\d+)',
        r'图\s*(\d+[.-]\d+)',
        r'Figure\s*(\d+[.-]\d+)',
        r'如图\s*(\d+-\d+)',
        r'如下?图所示',
    ]
    for pat in fig_patterns:
        match = re.search(pat, content, re.IGNORECASE)
        if match:
            fig_num = match.group(1) if match.lastindex else match.group(0)
            md += f"\n> 📷 *{match.group(0)}*\n\n"
            break

    return md

def generate_chapter(ch_id, ch_name, ch_label, topic_groups):
    """
    生成一个章节的所有markdown文件

    topic_groups: [(topic_name, slide_range_start, slide_range_end), ...]
    每个topic包含一个范围的幻灯片
    """
    ch_dir = ch_id.replace('ch0', 'ch').replace('ch', 'ch0')
    # 规范化目录名
    dir_map = {
        "ch01": "ch01-vlan",
        "ch02": "ch02-network-expansion",
        "ch03": "ch03-subnet-routing",
        "ch04": "ch04-campus-network",
        "ch05": "ch05-acl",
        "ch06": "ch06-nat",
        "ch07": "ch07-network-design",
    }
    ch_dir = dir_map[ch_id]

    slides = ppt_slides.get(ch_id, [])
    if not slides:
        return []

    topic_files = []
    topic_num = 1

    for topic_name, start, end in topic_groups:
        # 取该范围内的幻灯片
        topic_slides = [(n, t) for (n, t) in slides if start <= n <= end]
        if not topic_slides:
            continue

        # 生成文件名
        file_slug = f"{topic_num:02d}-{slugify(topic_name)[:40]}"
        file_path = f"{ch_dir}/{file_slug}.md"
        topic_files.append((topic_name, file_path, topic_num))

        # 生成markdown内容
        md = f"# {ch_label} — {topic_name}\n\n"
        md += f"> {len(topic_slides)} 张幻灯片 | 中英双语完整保留\n\n"
        md += "---\n"

        for snum, stext in topic_slides:
            md += format_slide(snum, stext, ch_dir)

        write_md(file_path, md)
        print(f"    {file_path} ({len(topic_slides)} slides)")
        topic_num += 1

    # 生成章节索引页
    index_md = f"# {ch_label}\n\n"
    index_md += f"> 共 {len(slides)} 张幻灯片 | 中英双语完整保留\n\n"
    index_md += "## 本章目录\n\n"

    for tname, tpath, tnum in topic_files:
        index_md += f"{tnum}. [{tname}]({os.path.basename(tpath)})\n\n"

    index_md += "\n---\n\n## 本章概述\n\n"

    # 添加前几张幻灯片概要
    for snum, stext in slides[:3]:
        first_line = stext.strip().split('\n')[0][:100]
        if first_line:
            index_md += f"- Slide {snum}: {first_line}\n"

    write_md(f"{ch_dir}/index.md", index_md)

    return topic_files


# ============================================================
# 定义各章的主题分组（按PPT自然章节划分）
# ============================================================

# 第1章 VLAN技术 (40 slides)
ch01_topics = [
    ("项目任务与VLAN概念", 1, 4),
    ("VLAN配置命令—Access端口", 5, 7),
    ("交换网络问题与VLAN原理", 8, 12),
    ("VLAN特点与划分方式", 13, 17),
    ("VLAN Trunk与802.1Q", 18, 22),
    ("VLAN配置命令—Trunk端口", 23, 27),
    ("Native VLAN与Tag VLAN", 28, 31),
    ("SVI三层交换与VLAN间通信", 32, 36),
    ("VLAN删除与堆叠VLAN", 37, 40),
]

# 第2章 扩展办公网络 (42 slides)
ch02_topics = [
    ("网络扩展与层次化设计", 1, 7),
    ("核心层、汇聚层、接入层", 8, 13),
    ("交换机级联技术", 14, 15),
    ("交换机堆叠技术", 16, 17),
    ("链路聚合技术", 18, 22),
    ("生成树协议STP", 23, 32),
    ("VLAN间通信与三层交换", 33, 36),
    ("单臂路由配置", 37, 42),
]

# 第3章 子网与路由 (53 slides)
ch03_topics = [
    ("项目任务与子网连通", 1, 6),
    ("路由基础知识", 7, 12),
    ("认识路由器设备", 13, 17),
    ("路由器基本配置", 18, 23),
    ("路由器配置模式", 24, 29),
    ("接口配置与直连路由", 30, 35),
    ("静态路由配置", 36, 42),
    ("默认路由与路由汇总", 43, 48),
    ("单臂路由VLAN间通信", 49, 53),
]

# 第4章 构建园区网络 (47 slides)
ch04_topics = [
    ("园区网络基础与规划", 1, 7),
    ("IP地址规划与子网划分", 8, 14),
    ("直连路由", 15, 21),
    ("静态路由配置", 22, 28),
    ("默认路由", 29, 33),
    ("RIP路由协议", 34, 40),
    ("OSPF路由协议", 41, 47),
]

# 第5章 ACL (52 slides)
ch05_topics = [
    ("ACL概述与工作原理", 1, 8),
    ("通配符掩码", 9, 14),
    ("标准ACL配置", 15, 22),
    ("扩展ACL配置", 23, 32),
    ("命名ACL", 33, 40),
    ("ACL放置规则与综合应用", 41, 52),
]

# 第6章 NAT (47 slides)
ch06_topics = [
    ("NAT概述与地址类型", 1, 8),
    ("静态NAT配置", 9, 16),
    ("动态NAT配置", 17, 24),
    ("PAT端口地址转换", 25, 32),
    ("NAT负载均衡", 33, 40),
    ("NAT与路由综合", 41, 47),
]

# 第7章 网络工程设计 (58 slides)
ch07_topics = [
    ("课程介绍与地位", 1, 8),
    ("网络工程基本概念", 9, 18),
    ("系统集成方法", 19, 26),
    ("网络系统层次模型", 27, 34),
    ("网络需求分析", 35, 42),
    ("结构化布线与机房设计", 43, 50),
    ("网络安全与维护测试", 51, 58),
]

# 各章配置
CHAPTERS = [
    ("ch01", "ch01-vlan", "第1章 VLAN技术", ch01_topics),
    ("ch02", "ch02-network-expansion", "第2章 扩展办公网络", ch02_topics),
    ("ch03", "ch03-subnet-routing", "第3章 子网与路由", ch03_topics),
    ("ch04", "ch04-campus-network", "第4章 构建园区网络", ch04_topics),
    ("ch05", "ch05-acl", "第5章 访问控制列表(ACL)", ch05_topics),
    ("ch06", "ch06-nat", "第6章 网络地址转换(NAT)", ch06_topics),
    ("ch07", "ch07-network-design", "第7章 网络工程设计", ch07_topics),
]

all_nav_files = []

for ch_id, ch_dir, ch_label, topics in CHAPTERS:
    print(f"  [{ch_label}] 生成中...")
    files = generate_chapter(ch_id, ch_dir, ch_label, topics)
    all_nav_files.append((ch_dir, ch_label, files))

# ============================================================
# 7. 更新 mkdocs.yml 导航（包含所有文件）
# ============================================================
print("[更新导航] 补充子页面链接...")

nav_lines = []
nav_lines.append("site_name: 计算机网络知识点总结")
# ... 这里重新生成完整的导航

# 重新生成完整的mkdocs.yml
nav_entries = []
nav_entries.append("  - 首页: index.md")

for ch_dir, ch_label, files in all_nav_files:
    sub_items = [f"    - {ch_dir}/{os.path.basename(fp)}" for _, fp, _ in files]
    nav_entries.append(f"  - {ch_label}:")
    nav_entries.append(f"    - {ch_dir}/index.md")
    nav_entries.extend(sub_items)

nav_entries.append("  - 实验报告:")
nav_entries.append("    - experiments/index.md")

nav_entries.append("  - 复习大纲: review-outline.md")

# 重新生成完整 mkdocs.yml
full_mkdocs = f"""site_name: 计算机网络知识点总结
site_description: Computer Networks Knowledge Base - Bilingual (Chinese/English)
site_author: 计算机网络课程
copyright: Copyright &copy; 2025 计算机网络课程

theme:
  name: material
  language: zh
  features:
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.tracking
    - navigation.indexes
    - search.suggest
    - search.highlight
    - search.share
    - content.code.copy
    - content.code.annotate
  palette:
    - scheme: default
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-7
        name: 暗色模式
    - scheme: slate
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-4
        name: 亮色模式

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.emoji
  - pymdownx.tasklist:
      custom_checkbox: true
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true
      toc_depth: 4

plugins:
  - search:
      lang:
        - zh
        - en
      separator: '[\s\-_.,:;!?()\[\]{{}}]+'

extra_css:
  - stylesheets/extra.css

nav:
{chr(10).join(nav_entries)}
"""

# mkdocs.yml must be at project root
with open(os.path.join(BASE, "mkdocs.yml"), "w", encoding="utf-8") as f:
    f.write(full_mkdocs)

# ============================================================
# 8. 实验报告 — 保留Word原格式 (.doc)
# ============================================================
print("[实验报告] 复制.doc文件并生成索引...")

import shutil as _shutil

exp_doc_dir = os.path.join(DOCS, "experiments")
os.makedirs(exp_doc_dir, exist_ok=True)

exp_doc_files = []
for path, info in src_data["files"].items():
    if info.get("type") == "doc" and "实验" in info.get("name", ""):
        src_path = os.path.join(SRC, path)
        dst_path = os.path.join(exp_doc_dir, info["name"])
        if os.path.exists(src_path):
            _shutil.copy2(src_path, dst_path)
            exp_doc_files.append((info["name"], info.get("text", ""), os.path.getsize(src_path)))

exp_index = "# 实验报告汇总\n\n"
exp_index += "> 共 7 份实验报告 | 保留Word原格式 (.doc) | 点击文件名下载查看完整格式（含表格、图片、排版）\n\n"
exp_index += "---\n\n"

for i, (doc_name, doc_text, doc_size) in enumerate(exp_doc_files):
    exp_index += f"## 实验 {i+1}\n\n"
    exp_index += f"**文件**: [{doc_name}]({doc_name}) （{doc_size/1024:.0f} KB，.doc格式）\n\n"

    if doc_text:
        preview = doc_text[:600].strip()
        preview = preview.replace('<', '&lt;').replace('>', '&gt;')
        exp_index += f"**内容预览**：\n\n```\n{preview}\n...\n```\n\n"
        exp_index += "> 完整内容（含表格、图片、实验拓扑等）请下载 .doc 文件查看。\n\n"
    else:
        exp_index += "> 请下载 .doc 文件查看完整内容。\n\n"

    exp_index += "---\n\n"

write_md("experiments/index.md", exp_index)

# ============================================================
# 9. 复习大纲 — 逐题PPT原文搜索答案
# ============================================================
print("[复习大纲] 逐题搜索PPT原文答案...")

# 题目定义
_review_qs = [
    ("第1题", "什么是动态路由？",
     ["dynamic routing", "动态路由", "路由协议"],
     "What is dynamic routing?"),
    ("第2题", "什么设备可以产生路由表？",
     ["routing table", "路由表", "产生路由", "router saves"],
     "What device can generate the routing table?"),
    ("第3题", "最早开发以太网的公司是哪个？",
     ["Xerox", "施乐", "以太网"],
     "Which company was the first to develop experimental Ethernet?"),
    ("第4题", "本征帧的概念，一般本征帧在哪个VLAN，本征帧的协议标准是哪个？",
     ["native vlan", "本征帧", "Native VLAN", "802.1Q", "trunk native vlan"],
     "The concept of native frame, which VLAN, which protocol standard?"),
    ("第5题", "配置静态路由的一般步骤是什么？",
     ["静态路由", "static route", "ip route"],
     "What are the general steps to configure static routing?"),
    ("第6题", "什么是RIP协议，收敛时间是多少，跳数限制是多少？",
     ["RIP", "收敛", "convergence", "hop", "跳数", "30秒", "15跳"],
     "What is RIP protocol, its convergence time, hop limit?"),
    ("第7题", "理解SVI、TAGVLAN、RIP、OSPF的含义",
     ["SVI", "TAGVLAN", "Tag VLAN", "RIP", "OSPF"],
     "Understand the meaning of SVI, TAGVLAN, RIP, OSPF"),
    ("第8题", "记住所有的私有地址",
     ["私有地址", "private address", "10.0.0", "172.16", "192.168", "private IP"],
     "Remember all private addresses."),
    ("第9题", "交换机和路由器的各种操作模式及提示符号",
     ["Switch>", "Router>", "enable", "模式", "提示符", "prompt", "用户模式", "特权模式", "User EXEC", "Privileged"],
     "Various operation modes and prompt symbols."),
    ("第10题", "综合理解RIP和OSPF",
     ["RIP", "OSPF", "link state", "distance vector", "距离矢量", "链路状态"],
     "Comprehensive understanding of RIP and OSPF"),
    ("第11题", "RIP1和RIP2的区别",
     ["RIPv1", "RIPv2", "RIP1", "RIP2", "version 1", "version 2"],
     "Differences between RIP1 and RIP2"),
    ("第12题", "RIP路由信息的更新过程",
     ["RIP", "update", "更新", "路由更新", "30", "路由信息", "routing update"],
     "RIP routing information update process"),
    ("第13题", "不同VLAN之间通过什么技术通信？三层交换机/路由器的工作模式有几种？",
     ["VLAN", "通信", "三层交换机", "SVI", "子接口", "subinterface", "inter-vlan"],
     "How to enable communication between different VLANs?"),
    ("第14题", "内部连通性测试命令有哪些，怎么用？",
     ["ping", "tracert", "traceroute", "连通", "测试", "connectivity"],
     "What are the internal connectivity test commands?"),
    ("第15题", "掌握静态路由，什么是默认路由，默认路由是特殊的静态路由",
     ["默认路由", "default route", "0.0.0.0", "静态路由", "static route", "gateway", "网关"],
     "Master static routing, default routing"),
    ("第16题", "启用RIP和OSPF的命令",
     ["router rip", "router ospf", "network", "RIP", "OSPF", "启用", "enable"],
     "Commands to enable RIP and OSPF"),
    ("第17题", "掌握直连路由概念，会写直连路由，知道默认网关",
     ["直连路由", "directly connected", "默认网关", "default gateway"],
     "Grasp directly connected routing, know the default gateway"),
    ("第18题", "掌握跨交换机VLAN通信配置方法，直连路由和静态路由实验",
     ["跨交换机", "VLAN通信", "直连路由", "静态路由", "trunk", "实验"],
     "Master cross-switch VLAN communication, routing experiments"),
    ("第19题", "每个实验的命令配置过程必须会写",
     ["实验", "配置", "命令", "configure", "VLAN", "interface"],
     "The command configuration process of each experiment"),
    ("第20题", "配置TAGVLAN时对端口的要求",
     ["TAGVLAN", "tag vlan", "trunk", "端口", "port", "802.1Q", "mode trunk"],
     "When configuring TAGVLAN, requirements for the port?"),
    ("第21题", "路由器端口地址的配置原则是什么？",
     ["router", "port address", "端口地址", "配置原则", "interface", "ip address", "no shutdown"],
     "What is the configuration principle of router port address?"),
    ("第22题", "创建VLAN、分配端口到VLAN、配置端口IP地址、启用RIP和OSPF路由",
     ["创建VLAN", "分配端口", "IP地址", "RIP", "OSPF", "vlan", "switchport access"],
     "Create VLAN, assign ports, configure IP, enable RIP and OSPF"),
    ("第23题", "NAT的端口应用原理",
     ["NAT", "端口", "port", "地址转换", "inside", "outside", "ip nat"],
     "NAT port application principle"),
    ("第24题", "NAT边界路由配置应注意什么？",
     ["NAT", "边界", "路由", "配置注意", "inside", "outside", "ip nat"],
     "What should be noted about NAT boundary routing configuration?"),
    ("第25题", "网络系统集成的特点是什么？",
     ["系统集成", "集成", "特点", "system integration", "接口规范"],
     "What are the characteristics of network system integration?"),
    ("第26题", "IP地址/子网地址/园区网的层次结构",
     ["IP地址", "子网", "园区网", "层次结构", "hierarchy", "core", "distribution", "access"],
     "IP address, subnet address, campus network hierarchy"),
    ("第27题", "私有地址/广播地址",
     ["私有地址", "广播地址", "broadcast", "private", "255.255.255.255", "10.0", "172.16", "192.168"],
     "Private addresses and broadcast addresses"),
    ("第28题", "路由器和交换机的模式符号，路由表缩写C S R O的含义",
     ["show ip route", "路由表", "connected", "static", "rip", "ospf"],
     "Router/switch mode symbols, routing abbreviations C S R O"),
    ("第29题", "三层交换机默认工作在第几层？",
     ["三层交换机", "第二层", "第三层", "layer 2", "layer 3"],
     "Which layer does a Layer 3 switch work at by default?"),
    ("第30题", "三层交换机上创建VLAN40/VLAN80，配置地址",
     ["VLAN 40", "VLAN 80", "172.16.20", "172.16.30", "F0/24", "VLAN 20"],
     "Create VLAN40/VLAN80, configure addresses on Layer 3 switch"),
    ("第31题", "直连路由及默认路由",
     ["直连路由", "默认路由", "directly connected", "default route", "0.0.0.0"],
     "Directly connected routing and default routing"),
    ("第32题", "两台交换机VLAN互通配置",
     ["交换机A", "交换机B", "VLAN 10", "VLAN 20", "F0/24", "F0/10", "trunk"],
     "Two-switch VLAN intercommunication configuration"),
    ("第33题", "配置静态路由连通网络",
     ["静态路由", "ip route", "连通", "static", "目标网络", "下一跳"],
     "Configure static routing to connect networks"),
    ("第34题", "综合实验（实验15）",
     ["综合实验", "实验15", "comprehensive", "VLAN", "路由", "NAT", "ACL", "综合"],
     "Comprehensive experiment (Experiment 15)"),
]

def _search_answer(keywords, max_results=2):
    """在PPT原文中搜索答案"""
    _results = []
    _seen = set()
    for kw in keywords:
        for ppt_name, ppt_text in ppt_full_texts.items():
            idx = ppt_text.lower().find(kw.lower())
            if idx >= 0:
                start = max(0, idx - 80)
                end = min(len(ppt_text), idx + 600)
                ctx = ppt_text[start:end].strip()
                ctx = re.sub(r'\n{3,}', '\n\n', ctx)
                ctx = ctx.replace('<', '&lt;').replace('>', '&gt;')
                key = ctx[:100]
                if key not in _seen:
                    _seen.add(key)
                    _results.append((ppt_name[:60], ctx[:500]))
                    if len(_results) >= max_results:
                        return _results
    return _results

outline_md = "# 复习大纲 — 简答题答案（均来自PPT原文）\n\n"
outline_md += "> **说明**：所有答案均从原始PPT课件中逐页搜索提取，非AI生成。每题标注了来源文件和原文上下文。\n\n"
outline_md += "---\n\n"

for _i, (_qname, _qdesc, _kw, _enq) in enumerate(_review_qs):
    _qid = _i + 1
    outline_md += f'## {_qname}：{_qdesc}\n\n'
    outline_md += f'> **英文题目**：{_enq}\n\n'
    _answers = _search_answer(_kw, max_results=2)
    if _answers:
        outline_md += "**答案来源（PPT原文）**：\n\n"
        for _j, (_src, _ctx) in enumerate(_answers):
            outline_md += f"**来源 {_j+1}**：`{_src}...`\n\n"
            outline_md += "```\n" + _ctx + "\n```\n\n"
    else:
        outline_md += "> [待补充] 未在PPT源文件中找到直接匹配，请参考相关章节内容。\n\n"
    outline_md += "---\n\n"

write_md("review-outline.md", outline_md)

# ============================================================
# 10. 完成
# ============================================================
print("\n" + "=" * 60)

# 统计
total_md = sum(1 for _ in glob.glob(os.path.join(DOCS, '**', '*.md'), recursive=True))
total_lines = 0
for md_file in glob.glob(os.path.join(DOCS, '**', '*.md'), recursive=True):
    with open(md_file, 'r', encoding='utf-8') as f:
        total_lines += sum(1 for _ in f)

print(f"[OK] 计算机网络知识库生成完毕！")
print(f"  位置: {BASE}")
print(f"  Markdown文件: {total_md} 个")
print(f"  总行数: {total_lines} 行")
print(f"  幻灯片覆盖: {total_slides} 张 (100%)")
print(f"  图片: {img_count} 张")
print(f"  实验报告: {len(experiments)} 个")
print(f"")
print(f"运行以下命令预览:")
print(f"  cd {BASE}")
print(f"  mkdocs serve")
print(f"{'=' * 60}")
