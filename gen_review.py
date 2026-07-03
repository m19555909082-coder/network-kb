# -*- coding: utf-8 -*-
"""生成复习大纲——在PPT原文中按完整slide搜索每道题的答案"""
import glob, re, os

SRC = r"C:\Users\He Guoxin\Desktop\claude\复习"
OUT = r"C:\Users\He Guoxin\Desktop\claude\network-kb\docs\review-outline.md"

# 读取所有PPT全文
ppt_texts = {}
for f in sorted(glob.glob(os.path.join(SRC, "*_full.txt"))):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    name = os.path.basename(f).replace('_full.txt', '')
    ppt_texts[name] = text


def search_answer(keywords, min_slide_len=30):
    """
    在PPT原文中按完整slide搜索答案。
    - 使用re.finditer找到所有匹配位置
    - 返回包含匹配的完整slide（从 --- Slide N --- 到下一个 --- Slide M ---）
    - 跳过内容过短（<min_slide_len）的标题页
    - 按匹配关键词数量+slide内容长度排序
    """
    results = []
    seen_slides = set()  # (ppt_name, slide_num) 去重

    for kw in keywords:
        try:
            for ppt_name, ppt_text in ppt_texts.items():
                for m in re.finditer(re.escape(kw), ppt_text, re.IGNORECASE):
                    idx = m.start()
                    # 找到当前slide的起始位置
                    prev_break = ppt_text.rfind('--- Slide ', 0, idx)
                    if prev_break == -1:
                        prev_break = 0
                    # 找到下一个slide的起始位置
                    next_break = ppt_text.find('\n--- Slide ', idx)
                    if next_break == -1:
                        next_break = len(ppt_text)
                    else:
                        next_break = ppt_text.find('\n', next_break + 1)
                        if next_break == -1:
                            next_break = len(ppt_text)

                    slide_content = ppt_text[prev_break:next_break].strip()

                    # 提取slide编号用于去重
                    slide_match = re.match(r'--- Slide (\d+) ---', slide_content)
                    slide_num = slide_match.group(1) if slide_match else '?'
                    slide_key = (ppt_name, slide_num)

                    if slide_key in seen_slides:
                        continue
                    seen_slides.add(slide_key)

                    # 跳过内容太少或纯图片的slide
                    text_only = re.sub(r'--- Slide \d+ ---', '', slide_content).strip()
                    text_only = re.sub(r'!\[.*?\]\(.*?\)', '', text_only)
                    if len(text_only) < min_slide_len:
                        continue

                    # 计算匹配度：匹配关键词数 + 内容长度加分
                    match_count = sum(1 for k in keywords if k.lower() in slide_content.lower())
                    score = match_count * 100 + min(len(text_only), 500)

                    results.append((score, ppt_name, slide_content))

        except re.error:
            # 关键词有特殊字符时降级为普通find
            for ppt_name, ppt_text in ppt_texts.items():
                idx = 0
                while True:
                    idx = ppt_text.lower().find(kw.lower(), idx)
                    if idx == -1:
                        break
                    prev_break = ppt_text.rfind('--- Slide ', 0, idx)
                    if prev_break == -1:
                        prev_break = 0
                    next_break = ppt_text.find('\n--- Slide ', idx)
                    if next_break == -1:
                        next_break = len(ppt_text)
                    else:
                        next_break = ppt_text.find('\n', next_break + 1)
                        if next_break == -1:
                            next_break = len(ppt_text)
                    slide_content = ppt_text[prev_break:next_break].strip()
                    slide_match = re.match(r'--- Slide (\d+) ---', slide_content)
                    slide_num = slide_match.group(1) if slide_match else '?'
                    slide_key = (ppt_name, slide_num)
                    idx += 1
                    if slide_key in seen_slides:
                        continue
                    seen_slides.add(slide_key)
                    text_only = re.sub(r'--- Slide \d+ ---', '', slide_content).strip()
                    text_only = re.sub(r'!\[.*?\]\(.*?\)', '', text_only)
                    if len(text_only) < min_slide_len:
                        continue
                    match_count = sum(1 for k in keywords if k.lower() in slide_content.lower())
                    score = match_count * 100 + min(len(text_only), 500)
                    results.append((score, ppt_name, slide_content))

    # 去重排序，合并为一个最佳答案
    results.sort(key=lambda x: x[0], reverse=True)
    seen_content = set()
    merged_slides = []
    for score, ppt_name, content in results:
        key = content[:120]
        if key not in seen_content:
            seen_content.add(key)
            short_name = ppt_name[:80]
            filtered = filter_cn_only(content)
            if filtered.strip():
                merged_slides.append((short_name, filtered, score))
            if len(merged_slides) >= 1:  # 只取最佳1个slide
                break

    if not merged_slides:
        return None

    # 只取最佳匹配的slide，不合并多个（避免无关内容混入）
    best_source = merged_slides[0][0]
    best_content = merged_slides[0][1]
    return (best_source, best_content)


def filter_cn_only(content):
    """过滤slide内容，只保留中文行/命令/分隔符，去掉英文翻译"""
    lines = content.split('\n')
    result = []
    has_cjk = re.compile(r'[一-鿿]')
    is_cmd = re.compile(r'^(Switch|Router|Red-Giant)[>#(]')
    is_config = re.compile(r'^\s*(ip\s|no\s|interface\s|switchport\s|access-list\s|vlan\s|end\b|exit\b|router\s|network\s|version\s)')
    is_sep = re.compile(r'^--- Slide \d+ ---$')

    for line in lines:
        stripped = line.strip()
        # 保留slide分隔符
        if is_sep.match(stripped):
            result.append(line)
            continue
        # 含中文的行：剥离尾部英文
        if has_cjk.search(line):
            cleaned = line
            # 去掉中文后跟的英文翻译尾巴（至少20个英文字符才算翻译文本）
            # 保留短英文缩写（如MD5、VLSM、RIPv2等）
            cleaned = re.sub(
                r'([一-鿿　-〿＀-￯])'
                r'\s*[A-Z][A-Za-z].{18,}$',
                r'\1', cleaned)
            if len(cleaned.strip()) >= 3:
                result.append(cleaned)
            continue
        # 保留以命令提示符开头的行
        if is_cmd.search(stripped):
            result.append(line)
            continue
        # 保留以配置关键字开头的行
        if is_config.search(stripped):
            result.append(line)
            continue
        # 跳过纯英文解释行

    return '\n'.join(result)


def merge_slides(slides):
    """合并多个slide内容为简洁的简答题答案"""
    if len(slides) == 1:
        return slides[0]

    # 提取每个slide的核心文本（去掉分隔符行）
    all_lines = []
    for slide in slides:
        for line in slide.split('\n'):
            stripped = line.strip()
            if stripped.startswith('--- Slide'):
                continue
            if stripped and stripped not in all_lines:
                all_lines.append(stripped)

    return '\n'.join(all_lines)


questions_def = [
    ("Q1", "什么是动态路由？",
     ["动态路由", "dynamic routing", "路由协议自动", "动态路由协议分类"]),

    ("Q2", "什么设备可以产生路由表？",
     ["路由表", "routing table", "路由器保存", "router saves", "路由表中保存"]),

    ("Q3", "最早开发以太网的公司是哪个？",
     ["Xerox", "施乐", "Xerox开发的", "70年代开发", "DIX", "DEC", "Intel", "以太网最早"]),

    ("Q4", "本征帧的概念，一般本征帧在哪个VLAN，本征帧的协议标准是哪个？",
     ["native vlan", "Native VLAN", "本征帧", "本帧VLAN", "native VLAN是VLAN 1",
      "802.1Q", "缺省native VLAN", "Trunk口都属于"]),

    ("Q5", "配置静态路由的一般步骤是什么？",
     ["静态路由是指", "静态路由", "static routing", "ip route",
      "管理员手工配置", "配置静态路由", "manually configured"]),

    ("Q6", "什么是RIP协议，收敛时间是多少，跳数限制是多少？",
     ["RIP（Routing", "路由信息协议", "15跳", "16跳",
      "距离矢量", "distance vector", "Xerox"]),

    ("Q7", "理解SVI、TAGVLAN、RIP、OSPF的含义",
     ["SVI", "switch virtual interface", "TAGVLAN", "Tag VLAN", "tag vlan",
      "RIP协议", "OSPF协议", "OSPF简介", "链路状态", "link state"]),

    ("Q8", "记住所有的私有地址",
     ["私有地址", "private address", "专用IP地址", "10.0.0", "172.16",
      "192.168", "private IP", "专用地址", "局域网专用IP"]),

    ("Q9", "交换机和路由器的各种操作模式及提示符号",
     ["用户模式", "特权模式", "全局模式", "端口模式", "Router>", "Router#",
      "Switch>", "Switch#", "User EXEC", "Privileged", "config)#", "enable"]),

    ("Q10", "综合理解RIP和OSPF",
     ["RIP协议", "OSPF协议", "RIP", "OSPF", "距离矢量", "distance vector",
      "链路状态", "link state", "开放最短路径优先", "路由信息协议"]),

    ("Q11", "RIP v1和RIP v2的区别",
     ["RIPv1", "RIPv2", "有类路由", "无类路由", "VLSM", "广播", "组播",
      "version 1", "version 2", "RIP路由协议的版本"]),

    ("Q12", "RIP路由信息的更新过程",
     ["RIP路由信息", "路由更新", "update", "路由信息更新", "30秒",
      "routing update", "路由器之间相互通信", "更新路由器表"]),

    ("Q13", "不同VLAN之间通过什么技术通信？三层交换机/路由器的工作模式有几种？",
     ["VLAN间通信", "inter-vlan", "三层交换机", "SVI", "子接口", "subinterface",
      "不同VLAN之间", "vlan间路由", "单臂路由"]),

    ("Q14", "内部连通性测试命令有哪些，怎么用？",
     ["ping命令", "ping ", "tracert", "traceroute", "连通性测试",
      "测试命令", "测试连通性", "ping命令使用的是ICMP"]),

    ("Q15", "掌握静态路由，什么是默认路由，默认路由是特殊的静态路由",
     ["默认路由", "default route", "0.0.0.0", "缺省路由",
      "静态路由是指", "static route", "gateway of last resort"]),

    ("Q16", "启用RIP和OSPF的命令",
     ["router rip", "router ospf", "network", "配置RIP协议",
      "Configuring RIP", "启用RIP", "启用OSPF", "OSPF配置",
      "router(config)#router ospf", "router ospf 1"]),

    ("Q17", "掌握直连路由概念，会写直连路由，知道默认网关",
     ["直连路由", "directly connected", "默认网关", "default gateway",
      "自动生成", "配置完路由器网络接口"]),

    ("Q18", "掌握跨交换机VLAN通信配置方法，直连路由和静态路由实验",
     ["跨交换机", "VLAN通信", "trunk", "直连路由", "静态路由", "跨交换机VLAN"]),

    ("Q19", "每个实验的命令配置过程必须会写",
     ["Switch(config)", "Router(config)", "interface", "vlan",
      "ip address", "switchport", "no shutdown", "配置命令"]),

    ("Q20", "配置TAGVLAN时对端口的要求",
     ["TAGVLAN", "tag vlan", "trunk", "Trunk端口", "802.1Q",
      "mode trunk", "switchport mode"]),

    ("Q21", "路由器端口地址的配置原则是什么？",
     ["端口地址", "ip address", "配置原则", "no shutdown",
      "router interface", "接口配置", "接口IP地址"]),

    ("Q22", "创建VLAN、分配端口到VLAN、配置端口IP地址、启用RIP和OSPF路由",
     ["创建VLAN", "vlan 10", "vlan 20", "switchport access",
      "分配端口", "ip address", "router rip", "router ospf",
      "指定端口到划分好VLAN"]),

    ("Q23", "NAT的端口应用原理",
     ["NAT", "地址转换", "inside", "outside", "ip nat",
      "端口转换", "PAT", "端口地址转换", "NAPT"]),

    ("Q24", "NAT边界路由配置应注意什么？",
     ["NAT边界", "边界路由", "NAT路由器", "静态路由", "默认路由",
      "自治系统", "不能配置路由协议"]),

    ("Q25", "网络系统集成的特点是什么？",
     ["系统集成", "接口规范", "整体性能", "工程规范", "质量管理",
      "用户关系", "系统集成的特点"]),

    ("Q26", "IP地址/子网地址/园区网的层次结构",
     ["IP地址规划", "子网划分", "层次化", "核心层", "汇聚层", "接入层",
      "Core Layer", "Distribution Layer", "Access Layer", "hierarchy"]),

    ("Q27", "私有地址/广播地址",
     ["私有地址", "广播地址", "broadcast", "专用IP地址",
      "255.255.255.255", "10.0", "172.16", "192.168"]),

    ("Q28", "路由器和交换机的模式符号，路由表缩写C S R O的含义",
     ["show ip route", "C  ", "S  ", "R  ", "O  ",
      "管理距离", "路由源", "directly connected",
      "C    192", "S    192", "R    192", "O    192"]),

    ("Q29", "三层交换机默认工作在第几层？",
     ["三层交换机", "第二层", "工作在第二层", "第三层",
      "layer 2", "layer 3", "交换机默认", "多层交换机"]),

    ("Q30", "三层交换机上创建VLAN40/VLAN80，配置地址",
     ["VLAN 40", "VLAN 80", "172.16", "F0/24", "VLAN 20",
      "SVI", "interface vlan", "三层交换机"]),

    ("Q31", "直连路由及默认路由",
     ["直连路由", "默认路由", "directly connected", "default route",
      "0.0.0.0", "自动生成", "缺省路由"]),

    ("Q32", "两台交换机VLAN互通配置",
     ["交换机A", "交换机B", "VLAN 10", "VLAN 20", "F0/24", "F0/10",
      "trunk", "跨交换机", "switchport mode trunk"]),

    ("Q33", "配置静态路由连通网络",
     ["静态路由", "ip route", "连通", "目标网络", "下一跳",
      "next hop", "静态路由配置", "static route"]),

    ("Q34", "综合实验（实验15）",
     ["综合实验", "实验15", "comprehensive", "VLAN", "路由", "NAT", "ACL",
      "综合", "项目实施", "组建园区网"]),
]

def extract_key_lines(content):
    """从slide内容中提取关键行，去掉分隔符和碎片"""
    lines = []
    is_sep = re.compile(r'^--- Slide \d+ ---$')
    has_cjk = re.compile(r'[一-鿿]')
    is_cmd = re.compile(r'^(Switch|Router|Red-Giant)[>#(]')
    is_config = re.compile(r'^\s*(ip\s|no\s|interface\s|switchport\s|access-list\s|vlan\s|end\b|exit\b|router\s|network\s|version\s|encapsulation\s)')
    for line in content.split('\n'):
        stripped = line.strip()
        if not stripped:
            continue
        if is_sep.match(stripped):
            continue
        # 保留含中文的行
        if has_cjk.search(line):
            # 清理每行末尾残留的长英文翻译
            cleaned = re.sub(r'([一-鿿。，；：！？、\)）])[A-Za-z].{15,}$', r'\1', stripped)
            cleaned = re.sub(r'\s{2,}', ' ', cleaned)
            if len(cleaned) >= 4:
                lines.append(cleaned)
            continue
        # 保留命令提示符行和配置命令
        if is_cmd.search(stripped) or is_config.search(stripped):
            lines.append(stripped)
            continue
        # 保留短英文标签（如RIPv1、RIPv2、Native VLAN等）
        if len(stripped) < 40 and re.match(r'^[A-Za-z0-9].{2,35}$', stripped):
            lines.append(stripped)
    return lines


def format_cn_answer(qname, qdesc, slide_lines, source_name):
    """将提取的关键行格式化为简答题答案"""
    # 合并相邻的碎片行
    merged = []
    for line in slide_lines:
        if merged and len(merged[-1]) < 40 and len(line) < 40:
            merged[-1] = merged[-1] + '；' + line
        else:
            merged.append(line)

    # 过滤明显无关的内容
    relevant = []
    for line in merged:
        low = line.lower()
        # 跳过任务描述、设备清单等无关内容
        if any(w in low for w in ['任务描述', 'task description', '设备清单', 'equipment list',
                                   '工作过程', 'course of work', '知识准备', 'knowledge preparation',
                                   '网络拓扑', 'network topology', '任务目标', 'task object',
                                   '王先生', '学校网络中心为解决']):
            continue
        relevant.append(line)

    if not relevant:
        return None
    return '\n'.join(relevant)


# 手动补充知识库（PPT中缺失或不完整的知识点）
manual_supplements = {
    "Q4": """**答案来源**：PPT原文 + 整理补充

- **本征帧（Native VLAN）**：在Trunk链路上，不需要打4字节802.1Q标签就可以直接传输的帧
- **默认Native VLAN**：每个Trunk口的缺省Native VLAN是**VLAN 1**
- **协议标准**：**IEEE 802.1Q**
- 配置命令：`Switch(config-if)# switchport trunk native vlan [VLAN号]`
- 注意事项：Trunk链路两端必须配置相同的Native VLAN""",

    "Q3": """**答案来源**：PPT原文 + 补充知识

- 以太网最早由**施乐公司（Xerox）**在20世纪70年代开发
- 1980年，DEC、Intel、Xerox三家公司联合提出了以太网标准（DIX标准）
- 1983年，IEEE 802.3标准正式发布，成为以太网的国际标准""",

    "Q8": """**答案来源**：PPT原文 + 补充知识（RFC 1918）

私有IP地址范围（RFC 1918定义）：
- **A类**：10.0.0.0 ~ 10.255.255.255（10.0.0.0/8）
- **B类**：172.16.0.0 ~ 172.31.255.255（172.16.0.0/12）
- **C类**：192.168.0.0 ~ 192.168.255.255（192.168.0.0/16）

这些地址只能在局域网内部使用，不能直接在Internet上路由。""",

    "Q14": """**答案来源**：PPT原文 + 补充知识

常用连通性测试命令：
- **ping**：使用ICMP协议发送回显请求，测试网络连通性和延迟
  - 用法：`ping 目标IP地址`（Windows默认4次，Cisco持续发送）
- **tracert/traceroute**：追踪数据包从源到目的地经过的路径（每一跳）
  - Windows：`tracert 目标IP地址`
  - Cisco路由器：`traceroute 目标IP地址`

说明：ping命令使用的是ICMP协议，除网络探查外还用于传输错误信息，路由器上不应禁止该协议。""",

    "Q29": """**答案来源**：PPT原文 + 补充知识

- 三层交换机**默认工作在第二层（数据链路层）**
- 三层交换机本质是"二层交换机 + 路由模块"，数据转发优先使用硬件交换（二层）
- 只有开启路由功能（`ip routing`）后，才能进行三层路由转发
- 三层交换机用于核心层/汇聚层，连接所有区域的核心设备""",

    "Q7": """**答案来源**：PPT原文 + 整理补充

- **SVI（Switch Virtual Interface，交换机虚拟接口）**：为交换机中VLAN创建的虚拟三层接口，可配置IP地址作为该VLAN的网关，实现VLAN间路由
- **TAG VLAN（标签VLAN）**：基于IEEE 802.1Q标准，在以太网帧中插入4字节VLAN标签（Tag），包含12位VLAN ID（支持4096个VLAN）、3位优先级、1位格式指示符。Trunk端口传输多VLAN数据时给帧打标签
- **RIP（Routing Information Protocol，路由信息协议）**：距离矢量路由协议，以跳数作为度量值，最大15跳（16跳不可达），每隔30秒更新，适用于小型网络
- **OSPF（Open Shortest Path First，开放最短路径优先）**：链路状态路由协议，克服了RIP收敛慢（240秒以上）和15跳规模限制的弱点，采用区域概念（骨干区域Area 0），由RFC 2328定义""",

    "Q10": """**答案来源**：PPT原文 + 整理补充

**RIP（路由信息协议）**：
- 距离矢量路由协议，Xerox在70年代开发
- 以跳数为度量，最大15跳，16跳不可达
- 每30秒发送更新报文，180秒未收到→标记不可达，240秒→删除路由
- 适用于小型同类网络，配置简单但收敛慢

**OSPF（开放最短路径优先）**：
- 链路状态路由协议，克服了RIP收敛慢和规模限制
- 采用分区域概念：骨干区域Area 0 + 非骨干区域
- 基于SPF算法计算最短路径，收敛速度快
- RFC 2328定义，适用于中大型网络""",

    "Q2": """**答案来源**：PPT原文 + 整理补充

- **路由器**是产生和维护路由表的主要设备
- 路由器保存着各种传输路径的地址信息表，俗称**路由表（Routing Table）**，供数据包路由时选择
- 路由表中保存着到达各子网的标志信息：路由标识、获得路由方式、目标网络、转发路由器地址和经过路由器的个数等内容
- 路由表中包含有该路由器知道的目的网络地址以及通过此路由器到达这些网络的最佳路径，如某个接口或下一跳的地址
- **三层交换机**开启路由功能（`ip routing`）后也可产生路由表
- 典型的路由表产生方式有三种：直连路由、静态路由、动态路由""",

    "Q23": """**答案来源**：PPT原文 + 整理补充

**PAT（Port Address Translation，端口地址转换/端口复用）**：
- PAT是复用NAT池的特例，通过**端口复用技术**用一个合法IP地址映射内网所有私有IP地址
- 这个合法地址往往就是路由器出口的IP地址（如S0/0口IP）
- 工作原理：将内网多个私有IP地址和端口号映射到同一个公网IP地址的不同端口号上
- 理论上一个IP地址可映射约**65000个会话**，实际路由器通常支持约**4000个**（Cisco）

**PAT配置方法一**（建立NAT池，起始=结束）：
```
R1(config)# ip nat pool 池名 起始地址 结束地址 netmask 子网掩码
R1(config)# access-list 表号 permit 内部地址条件
R1(config)# ip nat inside source list 表号 pool 池名 overload
```

**PAT配置方法二**（不建立NAT池，直接使用出口接口）：
```
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 interface s0/0 overload
```

- 优点：最大限度节省IP地址
- 缺点：只能同时支持几千个会话，易造成拥塞；缓解方法：多申请IP地址建大NAT池、限制占用会话数多的应用（如BT）""",

    "Q27": """**答案来源**：PPT原文 + 补充知识

**私有地址**（RFC 1918定义，只能在局域网内部使用，不能直接在Internet上路由）：
- **A类**：10.0.0.0 ~ 10.255.255.255（10.0.0.0/8）
- **B类**：172.16.0.0 ~ 172.31.255.255（172.16.0.0/12）
- **C类**：192.168.0.0 ~ 192.168.255.255（192.168.0.0/16）

**广播地址**：
- **子网广播地址（直接广播）**：子网中主机位全为1的地址，用于向该子网内所有主机发送数据。如192.168.1.0/24的广播地址为192.168.1.255
- **有限广播地址**：255.255.255.255，用于本地网络广播，路由器默认不会转发（隔离广播域）
- **广播域**：网络中能接收同一广播帧的所有节点的集合。VLAN技术可分割广播域，控制广播风暴
- NAT边界路由器需处理私有地址与公网地址的转换，私有地址在公网上不可路由""",

    "Q34": """**答案来源**：PPT原文 + 整理补充

综合实验（实验15）目标是**组建园区网，实现园区网互通**，涵盖网络工程全流程。

**实验场景**：学校合并两个校区，需要在两个不同子网规划的校园网之间实现互联互通，并与外网连接。

**实验内容与步骤**：

1. **使用静态路由实现园区网互通**：
   - 配置路由器各接口IP地址
   - 为每个非直连网段添加静态路由（`ip route 目标网络 子网掩码 下一跳`）
   - 验证两个校区网络连通性

2. **使用动态路由（RIP）实现园区网互通**：
   - 配置RIP协议：`router rip` → `network 网段` → `version 2` → `no auto-summary`
   - 实现自动路由学习和更新

3. **实现园区网络与外网互连**：
   - 配置NAT边界路由器
   - 使用RIPv2动态路由实现子网之间、子网与外网之间的互联互通
   - 配置默认路由指向外网

**涉及的全部技术**：VLAN划分与Trunk配置、SVI接口地址配置、直连路由与静态路由、默认路由、RIP动态路由协议、RIPv1与RIPv2、NAT/PAT地址转换、ACL访问控制列表""",
}

supplement_extra = {}  # 需要追加到slide内容后的补充信息

# 在已有slide内容基础上追加补充信息
supplement_extra["Q3"] = "> **补充**：以太网最早由施乐（Xerox）在70年代开发。1980年DEC、Intel、Xerox联合提出DIX以太网标准。"

supplement_extra["Q6"] = "> **补充**：RIP收敛速度较慢（240秒以上），路由更新周期30秒，180秒未收到更新即标记不可达，240秒后删除路由。"

supplement_extra["Q8"] = "> **补充**：完整私有地址范围 — A类10.0.0.0/8、B类172.16.0.0/12、C类192.168.0.0/16（RFC 1918）。"

supplement_extra["Q12"] = "> **补充**：第1步 — RIP协议每隔30秒定期向外发送一次更新报文。"

supplement_extra["Q14"] = "> **补充**：另外tracert（Windows）/ traceroute（Cisco）命令用于追踪数据包路径。"

supplement_extra["Q16"] = "> **补充（OSPF命令）**：Router(config)#router ospf 1 → Router(config-router)#network 网段 反掩码 area 区域号"

supplement_extra["Q28"] = "> **补充**：路由表中 C=直连路由(Connected)、S=静态路由(Static)、R=RIP、O=OSPF。"

supplement_extra["Q29"] = "> **补充**：三层交换机默认工作在第二层（数据链路层），开启ip routing后才进行三层转发。"

# ========== 生成Markdown ==========
md = "# 复习大纲 — 简答题答案\n\n"
md += "> **说明**：答案优先从PPT原文提取并整理；PPT中缺失的内容已通过补充知识完善。\n\n"
md += "---\n\n"

for qname, qdesc, keywords in questions_def:
    md += f'## {qname}：{qdesc}\n\n'

    # 优先使用手动补全答案
    if qname in manual_supplements:
        md += manual_supplements[qname] + "\n\n"
        md += "---\n\n"
        continue

    result = search_answer(keywords)

    if result:
        src_name, context = result
        lines = extract_key_lines(context)
        formatted = format_cn_answer(qname, qdesc, lines, src_name)

        if formatted:
            md += f"**答案来源**：`{src_name}...`\n\n"
            md += formatted + "\n\n"
            if qname in supplement_extra:
                md += supplement_extra[qname] + "\n\n"
        else:
            md += "> 提取失败，请参考相关章节内容。\n\n"
    else:
        md += "> 未在PPT源文件中找到直接匹配，请参考相关章节内容。\n\n"

    md += "---\n\n"

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"[OK] 复习大纲已生成: {OUT}")
print(f"  总字符数: {len(md)}")
print(f"  题目数: {len(questions_def)}")
