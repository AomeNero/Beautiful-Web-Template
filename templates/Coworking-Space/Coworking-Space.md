# Coworking Space (Vibrant Block-based + Glassmorphism)

> 来源：[uupm.cc/demo/coworking-space](https://www.uupm.cc/demo/coworking-space)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `coworking-space` |
| 显示名称 | Coworking Space |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | sans-serif (Space Grotesk + DM Sans) |
| 描述 | 活力块面与毛玻璃融合的联合办公空间风格。紫粉渐变主色配薄荷绿点缀，圆角卡片与柔和阴影，Space Grotesk 几何标题与 DM Sans 正文，渐变胶囊按钮与毛玻璃导航栏，块面布局传递现代协作氛围。 |

## 布局创意 (Layout Ideas)

### Header

粘性顶部导航，左侧 WorkHub logo（紫色方块图标 + 粗体文字），中间导航链接（Spaces / Amenities / Membership / Locations），右侧"Log in"文字链接与紫粉渐变"Book a Tour"按钮。底部细线分隔，背景带轻微磨砂玻璃效果。

### Hero

非对称双栏布局。左侧：紫色"Rated #1 Coworking Space in NYC"徽章，巨型"Work Better, Together"标题（"Together"为紫粉渐变），灰色描述文字，两个 CTA（紫粉渐变"Book a Free Tour"与描边"Watch Video"），下方统计数据（5,000+ Members / 12 Locations / 98% Satisfaction）。右侧：办公空间图片拼贴，带浮动毛玻璃卡片（High-Speed WiFi / 24/7 Access）。

### Amenities Grid

4 列网格（移动 2 列/1 列）。每张卡片：白色背景，细边框，圆角，柔和阴影。顶部彩色图标（WiFi/打印/邮件/安全等），标题，灰色描述。图标颜色各异（紫/粉/绿/橙），创造视觉节奏。

### Pricing

浅灰背景区块。顶部"Membership Plans"紫色徽章，"Simple, Flexible Pricing"标题（"Flexible Pricing"为紫粉渐变），描述文字。下方 4 列定价卡片（Day Pass / Hot Desk / Dedicated Desk / Private Office），最受欢迎卡片带渐变边框高亮。

### CTA Section

深蓝背景区块。"Ready to Find Your Perfect Workspace?"标题（"Workspace?"为紫粉渐变），描述文字，两个 CTA（紫粉渐变"Book a Free Tour"与描边"Contact Sales"），底部三个绿色勾选特性（7-day free trial / No credit card required / Cancel anytime）。

### Footer

白色背景。左侧 WorkHub logo + 描述 + 社交图标（X / LinkedIn / Instagram），中间三列链接（Spaces / Locations / Company / Resources），底部版权与法律链接。

---

## 完整提示词 (Full Prompt)

# 设计风格：Coworking Space (Vibrant Block-based + Glassmorphism)

## 设计哲学

**Coworking Space** 风格是**活力块面（Vibrant Block-based）**与**毛玻璃（Glassmorphism）**的现代融合，专为联合办公空间、共享工作场所与协作平台打造。它拒绝企业 SaaS 的冷峻极简，转而拥抱**温暖、协作、充满活力**的视觉语言。

**核心 DNA 与基本原则**：

1.  **紫粉渐变宣言**：主色调取自**现代协作精神**——靛蓝（`#6366F1`）与品红（`#EC4899`）的渐变贯穿 CTA、标题高亮与边框。这不是"配色方案"，而是**能量宣言**。每种颜色都有明确角色：紫粉渐变 = 主要行动与焦点，薄荷绿（`#10B981`）= 成功与信任，橙色（`#F97316`）= 活力与点缀，深 slate（`#0F172A`）= 结构与深度。

2.  **块面布局（Block-based Layout）**：页面由清晰的**功能区块**组成——Hero、Amenities、Pricing、CTA、Footer——每个区块有明确的视觉边界。区块之间通过背景色切换（白→浅灰→深蓝→白）创造节奏感。

3.  **毛玻璃层次（Glassmorphism Layers）**：导航栏与浮动卡片使用**磨砂玻璃效果**——半透明背景（`rgba(255,255,255,0.8)`）+ `backdrop-filter: blur(12px)` + 细边框（`rgba(255,255,255,0.5)`）。这创造深度感而不失通透。

4.  **圆角友好（Rounded Friendliness）**：所有卡片、按钮、徽章使用**大圆角**（12-20px），传递温暖与亲和力。按钮为胶囊形（`border-radius: 999px`），卡片为圆角矩形（`border-radius: 16px`）。

5.  **柔和阴影（Soft Shadows）**：阴影不是硬偏移块，而是**柔和扩散光晕**——`box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`。这创造悬浮感而非压迫感。

6.  **字体即桥梁**：**Space Grotesk**（标题）以其几何感与现代感成为视觉骨架，**DM Sans**（正文）提供清晰可读性。标题字号大（clamp 2.5rem-4rem），行高适中（1.1-1.2），字距微紧（-0.02em）。渐变文字（`background: linear-gradient; -webkit-background-clip: text`）是设计签名。

**气质与情感基调**：
*   **活力协作**：紫粉渐变传递能量与创造力，适合创新团队。
*   **温暖亲和**：圆角与柔和阴影创造友好氛围，降低距离感。
*   **现代专业**：毛玻璃与块面布局保持专业感，不幼稚不轻浮。
*   **功能清晰**：每个区块有明确目的，信息层级清晰。

**视觉签名（即时可辨之处）**：
*   **紫粉渐变文字**：标题关键词（"Together"、"Flexible Pricing"、"Workspace?"）使用紫粉渐变，是整个设计的视觉锚点。
*   **渐变胶囊按钮**：所有主要 CTA 为紫粉渐变（`linear-gradient(135deg, #6366F1, #EC4899)`）配白色文字，圆角胶囊形。
*   **毛玻璃导航栏**：顶部导航使用半透明白色背景 + 背景模糊，滚动时保持通透。
*   **浮动信息卡片**：Hero 右侧图片上叠加毛玻璃卡片（WiFi/Access），创造层次感。
*   **彩色图标网格**：Amenities 区块每张卡片顶部有彩色图标（紫/粉/绿/橙），创造视觉节奏。

## 设计 Token 系统（DNA）

### 色彩（活力浅色模式调色板）

*   **Background（画布）**：`#FFFFFF`（纯白）
    *   干净的白色画布，让紫粉渐变自由绽放。
    *   用：主页面背景、卡片内部、导航背景。

*   **Background-Alt（交替背景）**：`#F8FAFC`（极浅灰蓝）
    *   用于区块交替，创造视觉节奏。
    *   用：Pricing 区块背景。

*   **Background-Dark（深色背景）**：`#0F172A`（深 slate）
    *   CTA 区块的反转背景，创造强烈对比。
    *   用：CTA 区块背景。

*   **Foreground（墨）**：`#0F172A`（深 slate）
    *   主要文字色。用于标题、正文、导航链接。
    *   用：标题、正文、导航文字。

*   **Text-Muted（次要文字）**：`#475569`（中灰蓝）
    *   用于描述性文字、标签、次要信息。
    *   用：Hero 描述、卡片描述、footer 链接。

*   **Accent-Primary（主操作色）**：`#6366F1`（靛蓝）
    *   渐变起点色。用于按钮、徽章、图标、链接。
    *   用：渐变按钮起点、徽章背景、图标颜色。

*   **Accent-Secondary（次操作色）**：`#EC4899`（品红）
    *   渐变终点色。与靛蓝配合使用。
    *   用：渐变按钮终点、文字渐变终点。

*   **Accent-Gradient（渐变）**：`linear-gradient(135deg, #6366F1, #EC4899)`
    *   设计签名。用于按钮、文字高亮、边框。
    *   用：CTA 按钮、标题关键词、最受欢迎卡片边框。

*   **Accent-Success（成功色）**：`#10B981`（薄荷绿）
    *   信任与成功色。用于勾选图标、成功状态。
    *   用：CTA 区块勾选图标、24/7 Access 图标。

*   **Accent-Warning（活力色）**：`#F97316`（橙色）
    *   点缀色。用于 Meeting Rooms 图标等。
    *   用：部分功能图标。

*   **Border（边框）**：`#E2E8F0`（浅灰）
    *   细边框色。用于卡片、输入框、分隔线。
    *   用：卡片边框、导航分隔线。

*   **Glass-Background（毛玻璃背景）**：`rgba(255, 255, 255, 0.8)`
    *   半透明白色。用于导航栏、浮动卡片。
    *   用：导航栏背景、Hero 浮动卡片。

*   **Glass-Border（毛玻璃边框）**：`rgba(255, 255, 255, 0.5)`
    *   半透明白色边框。用于毛玻璃元素。
    *   用：导航栏边框、浮动卡片边框。

**用色规则**：
- **紫粉渐变专用于 CTA 与高亮**，不用于大面积背景。
- **薄荷绿用于成功与信任**，面积控制在 10% 以内。
- **橙色用于点缀**，仅用于图标。
- **深 slate 用于文字与深色区块**，白色用于主背景。

### 字体

*   **标题字族**：`Space Grotesk`（Google Font）
    *   几何无衬线，现代感强。字重 500-700 用于标题。
    *   加载：`https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap`

*   **正文字族**：`DM Sans`（Google Font）
    *   清晰、友好、高可读性。与 Space Grotesk 形成粗细对比。
    *   加载：`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap`

*   **字重**：
    *   **Bold (700)**：主要标题、按钮文字。
    *   **SemiBold (600)**：卡片标题、导航链接。
    *   **Medium (500)**：正文强调、小标签。
    *   **Regular (400)**：正文、描述文字。

*   **字号阶梯**：
    *   展示（Hero 标题）：`clamp(2.5rem, 6vw, 4rem)`。
    *   区块标题：`clamp(2rem, 4vw, 3rem)`。
    *   卡片标题：`1.25rem`。
    *   正文：`1rem` - `1.125rem`。
    *   小标签：`0.875rem`，中等字重。

*   **样式技巧**：
    *   **渐变文字**：`background: linear-gradient(135deg, #6366F1, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;`
    *   **微紧字距**：标题 `letter-spacing: -0.02em`。
    *   **适中行高**：标题 `line-height: 1.1-1.2`，正文 `line-height: 1.6`。

### 圆角与边框

*   **圆角**：**默认大圆角**。
    *   按钮：`border-radius: 999px`（胶囊形）。
    *   卡片：`border-radius: 16px`。
    *   徽章：`border-radius: 999px`（胶囊形）。
    *   输入框：`border-radius: 12px`。

*   **边框**：**细边框**。
    *   默认：`1px solid #E2E8F0`（卡片、输入框）。
    *   导航分隔：`1px solid #E2E8F0`。
    *   毛玻璃边框：`1px solid rgba(255, 255, 255, 0.5)`。
    *   渐变边框（最受欢迎卡片）：`2px solid transparent; background: linear-gradient(#fff, #fff) padding-box, linear-gradient(135deg, #6366F1, #EC4899) border-box;`

### 阴影与效果

*   **柔和阴影（签名效果）**：扩散光晕阴影，**有模糊**。
    *   **卡片**：`box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`
    *   **按钮**：`box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39)`
    *   **大元素**：`box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04)`

*   **毛玻璃效果**：
    *   `background: rgba(255, 255, 255, 0.8);`
    *   `backdrop-filter: blur(12px);`
    *   `-webkit-backdrop-filter: blur(12px);`
    *   `border: 1px solid rgba(255, 255, 255, 0.5);`

*   **交互阴影变化**：
    *   按钮悬停：阴影增大，按钮上移 `translateY(-2px)`。
    *   卡片悬停：阴影增大，卡片上移 `translateY(-4px)`。

## 组件样式原则

### 按钮

*   **形状**：胶囊形（`border-radius: 999px`）。
*   **主按钮（渐变 CTA）**：
    *   `background: linear-gradient(135deg, #6366F1, #EC4899); color: #fff; padding: 0.875rem 1.75rem;`
    *   `box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39); font-weight: 600;`
    *   悬停：`transform: translateY(-2px); box-shadow: 0 6px 20px rgba(99, 102, 241, 0.23);`
*   **描边按钮**：
    *   `background: transparent; color: #0F172A; border: 1px solid #E2E8F0;`
    *   悬停：`background: #F8FAFC; border-color: #CBD5E1;`

### 卡片（Amenities / Pricing）

*   **结构**：白色背景，`border: 1px solid #E2E8F0`，`border-radius: 16px`，`box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1)`。
*   **图标区**：顶部居中彩色图标（48x48px 圆形背景）。
*   **信息区**：标题 + 灰色描述，`padding: 1.5rem`。
*   **悬停**：卡片上移，阴影增大。

### 徽章

*   **形状**：胶囊形（`border-radius: 999px`）。
*   **样式**：浅紫背景（`rgba(99, 102, 241, 0.1)`），紫色文字，`padding: 0.375rem 1rem; font-size: 0.875rem; font-weight: 500;`
*   **用法**：行内标签（Hero 顶部"Rated #1"、Pricing 顶部"Membership Plans"）。

### 导航

*   **Logo**：紫色方块图标（`width: 32px; height: 32px; background: linear-gradient(135deg, #6366F1, #EC4899); border-radius: 8px;`）+ "WorkHub" 粗体文字。
*   **链接**：`font-weight: 500; font-size: 0.9375rem; color: #475569;`，悬停变深色。
*   **CTA 按钮**：渐变胶囊按钮，固定于导航右侧。

### 输入框

*   **样式**：`border: 1px solid #E2E8F0; border-radius: 12px; background: #fff;`
*   **字体**：`font-family: DM Sans; font-size: 1rem;`
*   **占位符**：`color: #94A3B8;`
*   **聚焦**：`outline: none; border-color: #6366F1; box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);`

## 布局原则

*   **容器宽度**：`max-width: 1280px`，居中，两侧 `padding: 1.5rem`。
*   **间距**：区块垂直间距 `padding: 5rem 0`（桌面），`3rem 0`（移动）。
*   **网格**：Amenities 用 4 列网格（平板 2 列，移动 1 列），Pricing 用 4 列网格（平板 2 列，移动 1 列）。
*   **非对称**：Hero 用 55/45 分割，左侧文字右侧视觉。
*   **色块节奏**：白 → 白 → 浅灰 → 深蓝 → 白，创造视觉节拍。

## "大胆要素"（非通用性）

1.  **紫粉渐变文字**：标题关键词使用紫粉渐变（`-webkit-background-clip: text`），是整个设计的视觉锚点。

2.  **渐变胶囊按钮**：所有 CTA 为紫粉渐变配白色文字，圆角胶囊形，带柔和阴影。

3.  **毛玻璃导航栏**：顶部导航使用半透明白色背景 + 背景模糊，滚动时保持通透。

4.  **浮动信息卡片**：Hero 右侧图片上叠加毛玻璃卡片（WiFi/Access），创造层次感。

5.  **彩色图标网格**：Amenities 区块每张卡片顶部有彩色图标（紫/粉/绿/橙），创造视觉节奏。

6.  **深蓝 CTA 区块**：页面底部突然转入深蓝背景，白色文字 + 紫粉渐变高亮，创造强烈对比节奏。

## 反模式（应避免之事）

*   **直角**：不使用 `border-radius: 0`。圆角是友好感的灵魂。
*   **硬阴影**：不使用 `box-shadow` 带硬偏移（如 `4px 4px 0 0 #000`）。阴影必须是柔和扩散。
*   **纯色按钮**：不使用纯色 CTA 按钮（除描边按钮外）。主按钮必须是渐变。
*   **无模糊毛玻璃**：不使用 `backdrop-filter` 时忘记加 `-webkit-` 前缀。
*   **过饱和色彩**：不使用 `#FF0000` 或 `#00FF00` 等纯饱和色。色彩要有灰度。
*   **企业蓝**：不使用 `#3B82F6` 等标准 SaaS 蓝。使用靛蓝（`#6366F1`）。

## 动画与运动

*   **质感**：流畅、柔和、现代。
*   **过渡速度**：200-300ms。
*   **缓动**：`ease-out` 或 `cubic-bezier(0.4, 0, 0.2, 1)`。
*   **按钮交互**：
    *   悬停：上移 2px + 阴影增大。
    *   点击：轻微下压。
*   **卡片交互**：
    *   悬停：上移 4px + 阴影增大。
*   **装饰动画**：
    *   Hero 浮动卡片可缓慢上下浮动（`animation: float 6s ease-in-out infinite`）。

## 响应式策略

*   **断点**：
    *   `1024px`：桌面布局（双栏 Hero，4 列 Amenities/Pricing）。
    *   `768px`：平板/大手机（单栏堆叠，导航折叠，2 列 Amenities/Pricing）。
*   **移动适配**：
    *   Hero：文字与视觉堆叠，浮动卡片隐藏或缩小。
    *   标题字号：`clamp(2rem, 10vw, 4rem)`。
    *   Amenities/Pricing：2 列（平板）/ 1 列（手机）。
    *   导航：汉堡菜单或简化链接行。
    *   按钮：全宽或自适应。

## 可访问性与最佳实践

*   **对比**：深 slate 文字白底（12.6:1）、白色文字深蓝底（15.4:1）均远超 WCAG AAA。
*   **聚焦状态**：`outline: 2px solid #6366F1; outline-offset: 2px;`
*   **运动**：尊重 `prefers-reduced-motion`，禁用装饰动画。
*   **语义 HTML**：使用 `<header>`、`<nav>`、`<main>`、`<section>`、`<footer>`。
*   **触控目标**：按钮最小 44x44px。
