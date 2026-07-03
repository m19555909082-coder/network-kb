// 将 review-outline.md 转换为 Word 文档
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun,
  HeadingLevel, AlignmentType, LevelFormat,
  BorderStyle, ShadingType, WidthType,
  Header, Footer, PageNumber, PageBreak
} = require("docx");

const MD_PATH = "docs/review-outline.md";
const OUT_PATH = "复习大纲.docx";

let raw = fs.readFileSync(MD_PATH, "utf-8");
// 清理无效XML字符（如垂直制表符等控制字符）
raw = raw.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F]/g, "");
const lines = raw.split("\n");

// ---------- 字体 ----------
const FONT_BODY = "SimSun";       // 宋体
const FONT_HEADING = "SimHei";    // 黑体
const FONT_CODE = "Consolas";
const FONT_SIZE = 21;             // 10.5pt (五号)
const LINK_COLOR = "1565C0";

// ---------- helpers ----------
function boldRun(text) {
  return new TextRun({ text, bold: true, font: FONT_BODY, size: FONT_SIZE });
}
function codeRun(text) {
  return new TextRun({ text, font: FONT_CODE, size: 19, color: "C7254E" });
}
function bodyRun(text) {
  return new TextRun({ text, font: FONT_BODY, size: FONT_SIZE });
}
function boldBodyRun(text) {
  return new TextRun({ text, bold: true, font: FONT_BODY, size: FONT_SIZE });
}
function italicRun(text) {
  return new TextRun({ text, italics: true, font: FONT_BODY, size: FONT_SIZE, color: "616161" });
}

// 解析行内格式：**bold** 和 `code`
function parseInline(text) {
  const runs = [];
  // 每次匹配 **...** 或 `...` 或普通文字
  const re = /(\*\*(.+?)\*\*)|(`(.+?)`)|([^`*]+|\*[^*]|`[^`]*$)/g;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m[1] !== undefined) {
      // **bold**
      runs.push(boldRun(m[2]));
    } else if (m[3] !== undefined) {
      // `code`
      runs.push(codeRun(m[4]));
    } else if (m[5]) {
      runs.push(bodyRun(m[5]));
    }
  }
  if (runs.length === 0) runs.push(bodyRun(text));
  return runs;
}

// 解析blockquote中的bold
function parseBlockquoteInline(text) {
  // blockquote 里可能也有 **bold**
  const re = /(\*\*(.+?)\*\*)|(`(.+?)`)|([^*`]+|\*)/g;
  const runs = [];
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m[1] !== undefined) {
      runs.push(new TextRun({ text: m[2], bold: true, italics: true, font: FONT_BODY, size: FONT_SIZE, color: "616161" }));
    } else if (m[3] !== undefined) {
      runs.push(new TextRun({ text: m[4], font: FONT_CODE, size: 19, italics: true, color: "795548" }));
    } else if (m[5]) {
      runs.push(new TextRun({ text: m[5], italics: true, font: FONT_BODY, size: FONT_SIZE, color: "616161" }));
    }
  }
  return runs;
}

// ---------- 构建文档 ----------
const children = [];
let i = 0;

// 处理标题行
function isH1(l) { return l.startsWith("# ") && !l.startsWith("## "); }
function isH2(l) { return l.startsWith("## "); }
function isHR(l)  { return l.trim() === "---"; }
function isBlockquote(l) { return l.startsWith("> "); }
function isListItem(l) { return l.startsWith("- ") || l.match(/^\d+\.\s/); }
function isCodeFence(l) { return l.startsWith("```"); }
function isEmpty(l) { return l.trim() === ""; }

while (i < lines.length) {
  const line = lines[i];

  // 空行
  if (isEmpty(line)) {
    i++;
    // 如果前面不是空行，添加段落间距
    continue;
  }

  // 水平线
  if (isHR(line)) {
    children.push(new Paragraph({
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: "BDBDBD", space: 8 } },
      spacing: { before: 200, after: 200 }
    }));
    i++;
    continue;
  }

  // H1 标题
  if (isH1(line)) {
    const text = line.replace(/^# /, "");
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_1,
      alignment: AlignmentType.CENTER,
      spacing: { before: 600, after: 400 },
      children: [new TextRun({ text, bold: true, font: FONT_HEADING, size: 36 })]
    }));
    i++;
    continue;
  }

  // H2 问题标题
  if (isH2(line)) {
    const text = line.replace(/^## /, "");
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_2,
      spacing: { before: 400, after: 200 },
      children: [new TextRun({ text, bold: true, font: FONT_HEADING, size: 28 })]
    }));
    i++;
    continue;
  }

  // Blockquote
  if (isBlockquote(line)) {
    const text = line.replace(/^> /, "");
    children.push(new Paragraph({
      spacing: { before: 60, after: 60 },
      indent: { left: 720 },
      border: { left: { style: BorderStyle.SINGLE, size: 12, color: "757575", space: 8 } },
      children: parseBlockquoteInline(text)
    }));
    i++;
    continue;
  }

  // 代码块
  if (isCodeFence(line)) {
    i++; // skip opening ```
    const codeLines = [];
    while (i < lines.length && !isCodeFence(lines[i])) {
      codeLines.push(lines[i]);
      i++;
    }
    i++; // skip closing ```
    if (codeLines.length > 0) {
      children.push(new Paragraph({
        spacing: { before: 80, after: 80 },
        indent: { left: 360 },
        shading: { fill: "F5F5F5", type: ShadingType.CLEAR },
        border: {
          left: { style: BorderStyle.SINGLE, size: 6, color: "BDBDBD", space: 8 },
        },
        children: [new TextRun({
          text: codeLines.join("\n"),
          font: FONT_CODE,
          size: 18,
          color: "37474F"
        })]
      }));
    }
    continue;
  }

  // 列表项（连续的 list items 合并为一个组）
  if (isListItem(line)) {
    const listItems = [];
    while (i < lines.length && isListItem(lines[i])) {
      let text = lines[i].replace(/^- /, "").replace(/^\d+\.\s/, "");
      listItems.push(text);
      i++;
    }
    for (const item of listItems) {
      children.push(new Paragraph({
        spacing: { before: 40, after: 40 },
        indent: { left: 720, hanging: 360 },
        children: parseInline(item),
        bullet: { level: 0 }
      }));
    }
    continue;
  }

  // 普通段落
  const paraLines = [];
  while (i < lines.length && !isEmpty(lines[i]) && !isH1(lines[i]) && !isH2(lines[i])
         && !isHR(lines[i]) && !isBlockquote(lines[i]) && !isListItem(lines[i])
         && !isCodeFence(lines[i])) {
    paraLines.push(lines[i]);
    i++;
  }
  if (paraLines.length > 0) {
    const text = paraLines.join("");
    children.push(new Paragraph({
      spacing: { before: 40, after: 40 },
      children: parseInline(text)
    }));
  }
}

// ---------- 文档配置 ----------
const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: FONT_BODY, size: FONT_SIZE }
      }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: FONT_HEADING },
        paragraph: { spacing: { before: 600, after: 400 }, alignment: AlignmentType.CENTER, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: FONT_HEADING },
        paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 1 }
      },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },  // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "BDBDBD", space: 4 } },
          children: [new TextRun({ text: "计算机网络 — 复习大纲", font: FONT_BODY, size: 18, color: "9E9E9E" })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ text: "第 ", font: FONT_BODY, size: 18, color: "9E9E9E" }),
                     new TextRun({ children: [PageNumber.CURRENT], font: FONT_BODY, size: 18, color: "9E9E9E" }),
                     new TextRun({ text: " 页", font: FONT_BODY, size: 18, color: "9E9E9E" })]
        })]
      })
    },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT_PATH, buf);
  console.log(`[OK] Word 文档已生成: ${OUT_PATH}`);
  console.log(`  总段落数: ${children.length}`);
});
