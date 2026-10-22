# AI-Image-Generator

> 来源：[uupm.cc AI Image Generator Demo](https://www.uupm.cc/demo/ai-image-generator)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `ai-image-generator` |
| 显示名称 | AI Image Generator |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 深色 AI 创作平台，紫粉渐变品牌色，交互式提示词输入，社区画廊展示，学分制定价。 |

## 布局创意 (Layout Ideas)

### Hero

居中布局。顶部"Powered by Stable Diffusion XL"胶囊标签（紫色半透明背景+边框），超大标题"Turn Words Into Stunning Art"其中"Stunning Art"使用紫→粉→青渐变文字，副标题描述。下方为内嵌式提示词输入卡片：深色输入框 + "Generate"渐变按钮 + 建议标签（Cosmic nebula、Anime character 等）+ 四张风格预览色块（Fantasy Art、Sci-Fi、Abstract、Realistic）。底部四列统计数据（10M+、500K+、50+、< 10s），数值使用紫粉渐变。

### Gallery

"Explore Amazing Creations"标题，"Amazing"使用渐变文字。瀑布流式图片网格（含 tall 和 wide 变体），悬停显示遮罩层。底部"View More"描边按钮。

### Art Styles

"Choose Your Creative Style"标题，"Creative Style"渐变。筛选标签栏（All / Digital Art / Photography / Fantasy & Sci-Fi），四列风格卡片网格（Oil Painting、Watercolor、Pencil Sketch、Impressionist），每张含图标、标题和描述。下方为"Style Mixing & Customization"双栏面板：左侧文字说明+特性列表，右侧 2x2 预览图网格。

### Prompt Library

"Master the Art of Prompting"标题，"Prompting"渐变。三个编号分类（Characters、Landscapes、Abstract），每个分类下三列提示词卡片，卡片含引号文本和标签。底部三列 Pro Tips 卡片（Be Specific、Reference Artists、Iterate & Refine）。

### Pricing

"Simple Credit-Based Pricing"标题，"Credit-Based"渐变。四列定价卡片网格（Free / Creator / Pro / Enterprise），中间"Creator"档位高亮（紫色边框+渐变背景+"Most Popular"标签）。下方为学分包购买区，四档学分卡片。

### CTA Banner

卡片式横幅，"Ready to Create Something Amazing?"标题，"Amazing"渐变。双按钮（渐变主按钮+描边次按钮），底部三列勾选说明。背景含紫色径向光晕。

### Footer

深色卡片背景+顶部边框，五列布局（品牌+社交图标 / Product / Resources / Company / Legal），底部版权行+品牌标语。

---

## 完整提示词 (Full Prompt)

# 设计风格：AI-Image-Generator / 深色 AI 创作平台

## 设计哲学

**核心原则**：以深邃的暗色画布为基底，让紫粉渐变的创造力如极光般流动。这是一种**沉浸式创作体验**的设计——用户进入页面即感受到 AI 艺术的神秘与力量。深色背景不只是美学选择，更是为了让生成的图像和渐变色彩成为绝对的视觉焦点。

**气质**：神秘、创造力、前沿科技、沉浸感、艺术性、未来感。

**AI-Image-Generator 的承诺**：这是一个 AI 艺术创作工具的门面。提示词输入本身就是 Hero 视觉的核心，用户无需滚动即可理解产品核心价值。紫粉渐变不只是装饰，而是"AI 创造力"的视觉编码。深色背景让每一张生成的图像都如宝石般闪耀。

---

## 设计 Token 系统（DNA）

### 色彩系统（深色极光）

**基础色**：
- **background**：`#0A0E1A`（深空蓝黑）— 页面底色，营造沉浸感
- **backgroundCard**：`#111827`（深蓝灰）— 卡片、内容区背景
- **backgroundCardHover**：`#1A2035`（微亮深蓝）— 卡片悬停态
- **foreground**：`#FFFFFF`（纯白）— 主要文字
- **muted**：`#9CA3AF`（中灰）— 次要文字、描述
- **subtle**：`#6B7280`（深灰）— 更次要的文字
- **border**：`rgba(255, 255, 255, 0.08)`（极淡白）— 细腻边框
- **borderHover**：`rgba(255, 255, 255, 0.15)`（微亮白）— 悬停边框

**品牌色**：
- **primary**：`#A855F7`（紫色）— 主品牌色
- **primaryPink**：`#EC4899`（粉色）— 品牌辅助色
- **primaryCyan**：`#22D3EE`（青色）— 品牌点缀色
- **gradientBrand**：`linear-gradient(135deg, #A855F7, #EC4899, #22D3EE)` — 三色渐变
- **gradientPurplePink**：`linear-gradient(135deg, #A855F7, #EC4899)` — 双紫粉渐变
- **gradientSoft**：`linear-gradient(135deg, rgba(168, 85, 247, 0.15), rgba(236, 72, 153, 0.15))` — 柔和渐变背景

**功能色**：
- **success**：`#10B981`（翡翠绿）— 成功指示
- **warning**：`#F59E0B`（琥珀）— 警告、注意

**用色规则**：
1. **对比度**：白色文字对深色背景保持 15:1+，次要文字最低 4.5:1
2. **分层策略**：深色卡片叠加于更深底色之上，边框用极淡白色分隔
3. **渐变应用**：所有主要交互元素（按钮、标题高亮、标签）使用紫粉渐变
4. **克制原则**：渐变仅用于关键词、CTA 按钮、品牌标识
5. **光晕效果**：紫色径向光晕用于背景氛围和 CTA 区域

### 字体系统

**字族**：
- **标题字体**：`"Space Grotesk", sans-serif` — 几何感无衬线，现代科技感
- **正文字体**：`"DM Sans", sans-serif` — 圆润友好，高可读性

**字号阶梯与层级**：
- **展示标题**：`clamp(36px, 5.5vw, 64px)`，Space Grotesk，`font-weight: 700`，`line-height: 1.1`
- **区块标题**：`clamp(28px, 4vw, 42px)`，Space Grotesk，`font-weight: 700`
- **子标题**：`24px`，Space Grotesk，`font-weight: 600-700`
- **正文**：`15px-18px`，DM Sans，`line-height: 1.7`
- **小字/标签**：`12px-14px`，DM Sans，`font-weight: 500`

**字重分布**：
- 标题：Bold/ExtraBold（600-700）
- 正文：Regular/Medium（400-500）
- 按钮：SemiBold（600）

**特殊排印模式**：
1. **渐变文字**：标题中的关键词使用紫→粉→青三色渐变
   ```css
   background: linear-gradient(135deg, #A855F7, #EC4899, #22D3EE);
   -webkit-background-clip: text;
   -webkit-text-fill-color: transparent;
   ```

2. **胶囊标签**：顶部小标签使用紫色半透明背景+边框
   ```css
   background: rgba(168, 85, 247, 0.12);
   border: 1px solid rgba(168, 85, 247, 0.25);
   color: #C084FC;
   border-radius: 999px;
   padding: 6px 16px;
   font-size: 14px;
   ```

### 圆角与边框系统

**圆角值**：
- **按钮/标签**：`12px`（标准圆角）
- **卡片**：`16px`（柔和大圆角）
- **大卡片**：`20px`（Hero 输入卡、CTA 横幅）
- **胶囊**：`999px`（标签、筛选器）

**边框样式**：
- **粗细**：标准 `1px`，高亮 `1.5px`
- **颜色**：标准 `rgba(255, 255, 255, 0.08)`，交互 `#A855F7`
- **样式**：实线

### 阴影与深度

**阴影哲学**：在深色背景下，阴影用于营造发光感和悬浮感而非传统深度。

**阴影配方**：

1. **紫色光晕**（按钮、交互元素）：
   ```
   box-shadow: 0 0 40px rgba(168, 85, 247, 0.3);
   ```

2. **卡片默认**：
   ```
   box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
   ```

3. **卡片悬停**：
   ```
   box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
   ```

### 纹理与氛围效果

**1. 极光背景**：
- 页面固定背景层，两个径向渐变椭圆
- 公式：`radial-gradient(ellipse, rgba(168, 85, 247, 0.12) 0%, transparent 70%)`
- 动画：缓慢缩放+旋转，12-15 秒循环

**2. 磨砂玻璃导航**：
- 导航栏使用半透明深色背景+背景模糊
- 公式：`background: rgba(10, 14, 26, 0.8); backdrop-filter: blur(24px);`
- 底部细边框分隔

**3. 渐变文字**：
- 标题关键词使用紫→粉→青三色渐变
- 作为视觉焦点，引导注意力

**4. CTA 径向光晕**：
- CTA 横幅底部含紫色径向光晕
- 公式：`radial-gradient(ellipse, rgba(168, 85, 247, 0.15) 0%, transparent 70%)`

---

## 组件样式原则

### 按钮

**主按钮**（紫粉渐变实心，主要操作）：
- 背景：`linear-gradient(135deg, #A855F7, #EC4899)`
- 文字：白色
- 圆角：`12px`
- 内边距：`14px 32px`
- 悬停：紫色光晕 + 微上浮 `translateY(-1px)`

**次按钮**（描边，备选操作）：
- 背景：透明
- 边框：`1.5px solid rgba(255, 255, 255, 0.08)`
- 文字：白色
- 悬停：边框变紫色，背景微变紫色透明

**Generate 按钮**（Hero 区特色）：
- 同主按钮样式，内联于输入框右侧

### 卡片与容器

**标准卡片**：
- 背景：`rgba(255, 255, 255, 0.03)` 或 `#111827`
- 边框：`1px solid rgba(255, 255, 255, 0.08)`
- 圆角：`16px`
- 内边距：`24px-32px`
- 悬停：边框变亮，微上浮

**高亮卡片**（定价 Featured）：
- 边框：`1px solid #A855F7`
- 背景：`rgba(168, 85, 247, 0.08)`
- 顶部含"Most Popular"渐变标签

**提示词输入卡**（Hero 区特色）：
- 背景：`#111827`
- 边框：`1px solid rgba(255, 255, 255, 0.08)`
- 圆角：`20px`
- 内含输入框、建议标签、风格预览

### 表单输入

**提示词输入框**：
- 背景：`rgba(0, 0, 0, 0.3)`
- 边框：`1px solid rgba(255, 255, 255, 0.08)`
- 圆角：`12px`
- 高度：`48px`
- 占位符：`#6B7280`

**聚焦状态**：
- 边框：`#A855F7`

### 标签与筛选器

**建议标签**：
- 背景：`rgba(255, 255, 255, 0.06)`
- 边框：`1px solid rgba(255, 255, 255, 0.08)`
- 圆角：`999px`
- 悬停：边框变紫色，文字变紫色

**筛选标签**：
- 同建议标签样式
- 激活态：紫粉渐变背景，白色文字

### 导航栏

- 背景：`rgba(10, 14, 26, 0.8)` + `backdrop-filter: blur(24px)`
- 底部边框：`1px solid rgba(255, 255, 255, 0.08)`
- 高度：`65px`
- Logo 左侧，导航链接居中，Sign In + CTA 右侧
- 固定定位 `position: fixed; top: 0; z-index: 50`

---

## 布局原则

### 间距节奏

**基础网格**：8px 间距系统
- 微观间距：`4px-8px`
- 元素间距：`16px-24px`
- 卡片间距：`24px-32px`
- 区块间距：`80px` 垂直内边距

**内容宽度**：
- 标准内容：`max-width: 1152px`
- 窄内容：`max-width: 672px`
- 提示词卡：`max-width: 896px`

**网格模式**：
- 四列：风格预览、画廊、风格卡片、定价、学分包
- 三列：提示词卡片、Pro Tips
- 双列：Style Mixing 面板、统计数据（移动端）

### 章节节奏

- Hero 区：`80px 0 64px` 内边距
- 内容区块：`80px 0` 内边距
- 区块交替背景：深色 / 深色卡片 交替

---

## "大胆要素"（非通用性）

这些是定义 AI-Image-Generator 的**强制性标志性元素**：

### 1. **提示词输入即 Hero**
Hero 区必须包含一个模拟提示词输入卡片，展示产品核心交互。输入框 + Generate 按钮 + 建议标签 + 风格预览色块，四位一体。

### 2. **紫粉青三色渐变文字**
标题中的关键词必须使用紫→粉→青三色渐变（`#A855F7` → `#EC4899` → `#22D3EE`），作为视觉焦点。

### 3. **极光背景动画**
页面固定背景层含两个缓慢运动的径向渐变椭圆，营造神秘氛围。

### 4. **磨砂玻璃深色导航**
导航栏使用半透明深色背景+背景模糊效果，滚动时保持可见。

### 5. **胶囊标签系统**
顶部标签使用紫色半透明背景+边框，筛选标签使用相同样式但激活态为渐变。

### 6. **深色卡片层次**
所有卡片使用深色背景+极淡白色边框，在深色页面上营造微妙层次。

### 7. **紫色光晕交互**
按钮悬停时产生紫色光晕效果，传递"AI 能量"感。

### 8. **瀑布流画廊**
社区画廊使用不规则网格（含 tall 和 wide 变体），模拟真实艺术展示。

### 9. **编号分类提示词库**
提示词库使用编号分类（1/2/3），每类三列卡片，卡片含引号文本和标签。

### 10. **CTA 径向光晕**
CTA 横幅底部含紫色径向光晕，增强视觉吸引力。

---

## 动画与运动

**运动哲学**：流畅、神秘、有力量感。AI 创作工具应感觉充满能量。

**缓动函数**：
- 默认：`ease-out`
- 按钮：`cubic-bezier(0.4, 0, 0.2, 1)`

**时长层级**：
- 快速交互：`150ms`
- 标准过渡：`200ms`
- 入场动画：`300ms`

**变换模式**：
- 按钮悬停：微上浮 `translateY(-1px)` + 紫色光晕
- 卡片悬停：微上浮 `translateY(-2px)` + 边框变亮
- 画廊图片：悬停 `scale(1.03)` + 遮罩渐显
- 极光背景：缓慢缩放+旋转，12-15 秒循环

**关键帧动画**：
- `aurora`：背景极光缓慢脉动
- `gradient`：渐变文字背景位置移动
- `float`：元素轻微上下浮动

---

## 图标

**图标库**：使用内联 SVG 图标

**样式规则**：
- 描边宽度：`2`（清晰可读）
- 颜色：主色 `#A855F7`，次要 `#9CA3AF`，图标容器背景用半透明品牌色
- 尺寸：`18px-24px`

**图标用途**：
- 导航：Logo 图标
- 特性：功能图标（带彩色背景容器）
- 社交：平台 Logo（X、Discord、Instagram、GitHub）

---

## 反模式（应避免之事）

### 切勿：
1. **使用浅色背景**——这是深色沉浸式体验，浅色会破坏氛围
2. **使用暖色调为主色**——保持紫/粉/青冷色调的神秘感
3. **过度装饰**——每个元素都有功能目的，渐变克制使用
4. **使用硬边框**——边框必须极淡（0.08 透明度），保持精致感
5. **忽略提示词输入**——这是核心差异化元素，必须突出
6. **使用传统阴影**——在深色背景下使用光晕而非传统阴影
7. **圆角过小**——保持 12px+ 的圆角，传递现代感
8. **导航不透明**——必须使用磨砂玻璃效果
9. **渐变滥用**——仅用于关键词和 CTA
10. **忘记响应式**——画廊和网格在移动端需适配

---

## 响应式策略

### 移动端（< 768px）：
- **所有列变为单列**
- **导航链接隐藏**，仅保留 Logo 和 CTA
- **提示词输入**改为垂直布局
- **标题字号缩小**至 36px
- **画廊网格**变为 2 列，tall/wide 变体取消
- **定价卡片**垂直堆叠
- **CTA 按钮**垂直排列

### 平板（768px - 1024px）：
- **双列网格**用于风格卡片和定价
- **画廊**变为 3 列
- **页脚**变为 3 列

### 桌面（> 1024px）：
- **完整四列网格**
- **提示词卡**最大宽度 896px
- **完整导航**和所有装饰元素

---

## 可访问性考量

### 对比度要求：
- **白色文字对深色背景**：15:1+（远超 WCAG AAA）
- **灰色次要文字对深色背景**：最低 4.5:1（达 WCAG AA）
- **渐变按钮上的白色文字**：需确保渐变最暗处仍有足够对比度

### 聚焦指示器：
- **始终可见**：2px 紫色环
- **高对比**：在所有深色背景上清晰可见

### 语义化 HTML：
- 使用正确的标题层级
- 导航用 `<nav>`，内容用 `<main>`/`<section>`
- 图片使用适当的 alt 文本

---

## 设计 Token 参考（快速复制）

```javascript
export const aiImageGeneratorTokens = {
  colors: {
    bg: "#0A0E1A",
    bgCard: "#111827",
    bgCardHover: "#1A2035",
    fg: "#FFFFFF",
    fgMuted: "#9CA3AF",
    fgSubtle: "#6B7280",
    border: "rgba(255, 255, 255, 0.08)",
    borderHover: "rgba(255, 255, 255, 0.15)",
    primary: "#A855F7",
    primaryPink: "#EC4899",
    primaryCyan: "#22D3EE",
    gradientBrand: "linear-gradient(135deg, #A855F7, #EC4899, #22D3EE)",
    gradientPurplePink: "linear-gradient(135deg, #A855F7, #EC4899)",
    success: "#10B981",
  },
  fonts: {
    heading: "'Space Grotesk', sans-serif",
    body: "'DM Sans', sans-serif",
  },
  radius: {
    sm: "8px",
    base: "12px",
    lg: "16px",
    xl: "20px",
    pill: "999px",
  },
  shadows: {
    glow: "0 0 40px rgba(168, 85, 247, 0.3)",
    card: "0 4px 24px rgba(0, 0, 0, 0.3)",
    cardHover: "0 8px 32px rgba(0, 0, 0, 0.4)",
  },
  transitions: {
    fast: "150ms ease-out",
    base: "200ms ease-out",
    slow: "300ms ease-out",
  },
  spacing: {
    section: "80px",
    card: "24px",
    element: "16px",
  },
};
```

---

## 总结

AI-Image-Generator 风格由**提示词输入即 Hero**、**紫粉青三色渐变品牌色**、**极光背景动画**和**深色卡片层次**所定义。

当提示词输入自然融入 Hero 区、紫粉渐变恰到好处地点缀关键词、极光背景营造神秘氛围、整体感觉沉浸而充满创造力时，此风格即告成功。当它感觉像套了深色主题的通用 SaaS 页面时，即告失败。

提示词输入是产品的灵魂展示。紫粉渐变是 AI 创造力的视觉编码。极光背景是沉浸感的签名。三者共同营造出连贯、神秘、充满创造力的 AI 艺术创作体验。
