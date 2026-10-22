# AI Writing Assistant

> 来源：https://www.uupm.cc/demo/ai-writing-assistant

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `ai-writing-assistant` |
| 显示名称 | AI Writing Assistant |
| 模式 | Light（支持 Dark 翻转） |
| 字体类型 | sans-serif（Space Grotesk + DM Sans） |
| 描述 | AI 原生写作工具落地页，紫罗兰渐变主色，磨砂玻璃导航，编辑器 Mockup 展示，深色页脚。 |

## 布局创意 (Layout Ideas)

### Navigation

固定顶部导航栏，`backdrop-filter: blur(12px)` 磨砂玻璃效果，半透明背景 `rgba(250,245,255,0.8)`。左侧品牌 Logo（渐变方块图标 + 文字），中间导航链接（Features / Use Cases / Integrations / Pricing），右侧 Sign In 文字链接 + 紫色主按钮 CTA。底部 1px 分割线。

### Hero

居中布局，顶部 "Powered by Advanced AI" 胶囊徽章（浅紫底 + 紫文字 + 闪电图标）。超大标题 "Write Better, Faster"，其中 "Faster" 使用紫罗兰渐变文字（`linear-gradient(135deg, #7C3AED, #A78BFA)` + `background-clip: text`）。副标题灰色居中，最大宽度 640px。双 CTA 按钮（主按钮 + 描边按钮）。下方为编辑器 Mockup 展示区：macOS 风格窗口（红黄绿圆点 + 标题栏 + 状态指示），内含 prompt 输入框（浅紫底）和 AI 生成文本输出区。整体带紫色辉光阴影 `0 0 40px rgba(124,58,237,0.15)`。

### Features

白色背景区块，3 列网格卡片布局。每张卡片：浅紫底图标方块（48x48，圆角 12px）+ 标题（Space Grotesk 700）+ 描述文字。卡片带 1px 边框，悬停时边框变紫 + 微上浮 2px + 阴影。

### Use Cases

浅紫底背景，左右 2 列布局。左侧为用例列表（4 项），每项为白底卡片（图标 + 标题 + 描述）。右侧为 AI 输出 Demo 展示（白底卡片，含 prompt 和生成内容）。

### Integrations

白色背景区块，4 列网格。每张集成卡片：彩色图标方块（不同品牌色 8% 透明度底）+ 平台名 + 描述。悬停上浮效果。

### Pricing

浅紫底背景，3 列定价卡片。中间卡片为推荐款（紫色边框 + 辉光阴影 + "Most Popular" 渐变徽章）。每张卡片含名称、价格、描述、功能列表（带勾选标记）、CTA 按钮。

### CTA Banner

全宽紫色渐变横幅（`linear-gradient(135deg, #7C3AED, #9B6DFF, #A78BFA)`），圆角 16px。白色大标题 + 半透明白副标题 + 双 CTA（白色主按钮 + 半透明描边按钮）+ 信任指标行（3 项带勾选）。装饰性半透明圆形背景。

### Footer

深色背景（`#1E1B4B`），5 列网格布局。左侧品牌区（Logo + 描述 + 社交图标），右侧 4 列链接（Product / Resources / Company / Legal）。底部版权行 + "Made with heart" 标语，1px 半透明白分割线。

---

## 完整提示词 (Full Prompt)

# 设计风格：AI Writing Assistant

## 设计哲学

### 核心原则

此设计追求"AI 原生"的现代 SaaS 美学——以紫罗兰色系建立品牌识别，用编辑器 Mockup 直观展示产品价值，以清晰的层级引导用户从认知到转化。设计语言干净、专业但不冰冷，通过柔和的紫色调和圆角元素传递友好感。

### 视觉气质

**情感关键词**：
- *智能* — 紫色渐变与编辑器 Mockup 暗示 AI 能力
- *专业* — 克制的排版、清晰的层级、充分的留白
- *友好* — 圆角卡片、柔和阴影、温暖的紫色调

**此设计不是什么**：
- 不是深色科技风（避免纯黑背景 + 霓虹色）
- 不是极简主义（有充足的装饰元素和渐变）
- 不是企业严肃风（紫色调带来活力和创造力感）

### 此风格的 DNA

#### 1. 紫罗兰渐变主色
`#7C3AED` 到 `#A78BFA` 的 135deg 线性渐变贯穿全页——标题文字、按钮背景、CTA 横幅、徽章边框。这是品牌的视觉锚点。

#### 2. 编辑器 Mockup 展示
Hero 区下方的 macOS 风格编辑器窗口是核心视觉元素，红黄绿圆点 + 标题栏 + prompt/output 分区，直观展示产品功能。

#### 3. 磨砂玻璃导航
固定导航栏使用 `backdrop-filter: blur(12px)` + 半透明背景，滚动时保持内容可见性的同时提供层次感。

#### 4. 交替背景节奏
页面区块在白色（`#FFFFFF`）和浅紫（`#FAF5FF`）之间交替，创造视觉节奏感，避免单调。

#### 5. 辉光阴影系统
关键元素（编辑器 Mockup、推荐定价卡片）使用紫色辉光阴影 `0 0 40px rgba(124,58,237,0.15)`，而非传统黑色阴影。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：以紫罗兰（`#7C3AED`）为品牌主色，通过透明度变化（8%、15%）创建层次，配合白色和浅紫背景交替建立节奏。深色页脚（`#1E1B4B`）提供视觉锚定。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `--accent` | `#7C3AED` | 主按钮、渐变起点、图标、链接 |
| `--accent-light` | `#A78BFA` | 渐变终点、悬停态 |
| `--accent-soft` | `rgba(124,58,237,0.08)` | 图标背景、prompt 框底、徽章底 |
| `--accent-glow` | `rgba(124,58,237,0.15)` | 辉光阴影、编辑器外阴影 |
| `--bg` | `#FAF5FF` | 浅紫背景区块、页面底色 |
| `--bg-white` | `#FFFFFF` | 白色背景区块、卡片背景 |
| `--bg-dark` | `#1E1B4B` | 页脚深色背景 |
| `--text` | `#0F172A` | 正文文字 |
| `--text-heading` | `#1E1B4B` | 标题文字（深蓝） |
| `--text-muted` | `#6B7280` | 副标题、描述文字 |
| `--border` | `#E2E8F0` | 卡片边框、分割线 |
| `--border-accent` | `#DDD6FE` | 悬停边框、徽章边框 |

**签名渐变**：
```css
background: linear-gradient(135deg, #7C3AED, #A78BFA);
```

**CTA 横幅渐变**：
```css
background: linear-gradient(135deg, #7C3AED 0%, #9B6DFF 50%, #A78BFA 100%);
```

### 字体系统

**字体配对**：
- **展示字体**：`Space Grotesk` — 标题、品牌名、定价数字，几何感强，现代科技气质
- **UI/正文字体**：`DM Sans` — 正文、导航、按钮文字，圆润友好，高可读性
- **辅助字体**：`Manrope` — 标签、小字说明，紧凑清晰

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | `clamp(2.5rem, 5vw, 4rem)` | Space Grotesk | 700 | -0.02em | 渐变文字 |
| 区块标题 | `clamp(1.75rem, 3vw, 2.5rem)` | Space Grotesk | 700 | -0.02em | 部分渐变 |
| 卡片标题 | `1.125rem` | Space Grotesk | 700 | 0 | — |
| 正文 | `0.938rem` | DM Sans | 400 | 0 | 行高 1.7 |
| 副标题 | `1.125rem` | DM Sans | 400 | 0 | 灰色，max-width 640px |
| 标签/徽章 | `0.813rem` | Manrope | 500 | 0 | 大写或常规 |
| 导航链接 | `0.938rem` | Manrope | 500 | 0 | 灰色，悬停变深 |
| 页脚标题 | `0.938rem` | Space Grotesk | 700 | 0 | 白色 |
| 页脚链接 | `0.875rem` | DM Sans | 400 | 0 | 半透明白 |

### 间距与布局

- **区块间距**：垂直内边距 `80px`（桌面），`48px`（平板），响应式缩减
- **容器宽度**：`max-width: 1152px`，水平 padding `32px`
- **网格间隙**：Features/Pricing `24px`，Integrations `24px`，Use Cases `48px`
- **卡片内边距**：`24px`（标准），`32px`（大卡片）

**常见间距值**：`4px` / `8px` / `16px` / `24px` / `32px` / `48px` / `64px` / `80px`

### 边框、表面与阴影

**圆角策略**：
- 小元素（图标、徽章）：`8px`
- 卡片、按钮：`12px`
- 大容器（编辑器、CTA 横幅）：`16px`
- 胶囊徽章：`9999px`（全圆）

**边框**：`1px solid` 为主，颜色 `#E2E8F0`（默认）/ `#DDD6FE`（悬停/强调）

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | 微卡片 |
| `--shadow-md` | `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)` | 卡片悬停 |
| `--shadow-lg` | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` | 弹窗/大卡片 |
| `--shadow-accent` | `0 0 40px rgba(124,58,237,0.15)` | 编辑器 Mockup、推荐卡片 |

---

## 组件样式与交互

### 按钮

**主按钮（Primary）**：
- 背景：`#7C3AED`，文字：`#FFFFFF`
- 圆角：`12px`，内边距：`12px 28px`
- 阴影：`0 2px 8px rgba(124,58,237,0.3)`
- 悬停：背景 `#6D28D9`，上浮 1px，阴影加深
- 激活：恢复原位

**描边按钮（Outline）**：
- 背景：透明，边框：`1.5px solid #E2E8F0`，文字：`#0F172A`
- 悬停：边框变紫 `#7C3AED`，文字变紫，背景 `rgba(124,58,237,0.08)`

**白色按钮（White，用于深色背景）**：
- 背景：`#FFFFFF`，文字：`#7C3AED`
- 悬停：上浮 1px，阴影加深

**禁用按钮**：
- 背景：`#E2E8F0`，文字：`#6B7280`，透明度 0.6，`cursor: not-allowed`

### 卡片
- 背景：`#FFFFFF`，边框：`1px solid #E2E8F0`，圆角：`16px`
- 内边距：`24px` 或 `32px`
- 悬停：边框变 `#DDD6FE`，阴影 `var(--shadow-md)`，上浮 `translateY(-2px)`
- 过渡：`250ms cubic-bezier(0.4, 0, 0.2, 1)`

### 输入框
- 背景：`#FFFFFF`，边框：`1.5px solid #E2E8F0`，圆角：`12px`
- 内边距：`12px 16px`，字体：`0.938rem`
- 聚焦：边框变 `#7C3AED`，外发光 `0 0 0 3px rgba(124,58,237,0.08)`

### 导航
- 固定顶部，高度 `65px`
- 背景：`rgba(250,245,255,0.8)` + `backdrop-filter: blur(12px)`
- 底部边框：`1px solid #E2E8F0`
- 链接：灰色 `#6B7280`，悬停变深
- CTA 按钮：紫色主按钮

### 徽章/标签
- 背景：`rgba(124,58,237,0.08)`，边框：`1px solid #DDD6FE`
- 文字：`#7C3AED`，圆角：`9999px`（胶囊形）
- 内边距：`6px 16px`，字体：`0.813rem` 500

---

## "大胆要素"（签名元素）

1. **渐变文字标题**：Hero 标题中关键词使用 `linear-gradient(135deg, #7C3AED, #A78BFA)` + `background-clip: text`，在纯文本中创造视觉焦点
2. **编辑器 Mockup**：macOS 风格窗口（红黄绿圆点 + 标题栏 + 状态指示器）展示产品核心功能，带紫色辉光阴影
3. **紫色辉光阴影**：关键元素使用 `0 0 40px rgba(124,58,237,0.15)` 而非传统黑色阴影，建立品牌色关联
4. **交替背景节奏**：白色与浅紫（`#FAF5FF`）区块交替，创造视觉韵律
5. **CTA 渐变横幅**：全宽紫色渐变背景 + 装饰性半透明圆形 + 白色内容，强转化引导
6. **磨砂玻璃导航**：`backdrop-filter: blur(12px)` 半透明导航，滚动时保持内容可见
7. **推荐卡片突出**：定价区中间卡片使用紫色边框 + 辉光阴影 + 顶部渐变徽章，视觉引导至推荐方案

---

## 效果与动画

**运动哲学**：克制而流畅，以微交互为主，避免过度动画。

**过渡默认**：
- 标准：`250ms cubic-bezier(0.4, 0, 0.2, 1)`
- 快速：`150ms cubic-bezier(0.4, 0, 0.2, 1)`
- 入场：`IntersectionObserver` 触发，`translateY(8px)` + `opacity 0→1`，`600ms ease`
- 悬停：`translateY(-2px)` + 阴影变化

**关键帧动画**：
```css
@keyframes gradient {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
@keyframes glow {
  0% { box-shadow: rgba(37,99,235,0.3) 0px 0px 20px; }
  100% { box-shadow: rgba(37,99,235,0.6) 0px 0px 40px; }
}
```

**毛玻璃效果**：
```css
backdrop-filter: blur(12px);
-webkit-backdrop-filter: blur(12px);
```

---

## 响应式策略

**断点哲学**：桌面优先，1024px 和 768px 两档断点。

- **导航**：768px 以下隐藏链接，显示汉堡菜单按钮
- **Features 网格**：1024px → 2 列，768px → 1 列
- **Use Cases**：768px 以下从左右 2 列变为上下堆叠
- **Integrations 网格**：1024px → 2 列，768px → 2 列
- **Pricing 网格**：1024px → 2 列（最后一张居中），768px → 1 列
- **Footer**：1024px → 3 列，768px → 2 列
- **Hero 标题**：`clamp(2.5rem, 5vw, 4rem)` 自动缩放
- **CTA 按钮**：768px 以下垂直堆叠
- **区块间距**：桌面 `80px`，平板 `48px`

**关键适配**：
- 标题尺寸使用 `clamp()` 流体缩放
- 装饰性元素（CTA 横幅圆形背景）在小屏保持但缩小
- 信任指标行在小屏垂直排列

---

## 可访问性与最佳实践

**色彩对比**：主文字 `#0F172A` 在白色背景上对比度 > 15:1，灰色文字 `#6B7280` 对比度约 4.6:1（接近 AA 标准）。紫色 `#7C3AED` 在白色上对比度约 4.6:1。

**聚焦状态**：输入框聚焦时使用 `box-shadow: 0 0 0 3px rgba(124,58,237,0.08)` 外发光环。

**触控目标**：按钮最小高度 44px（`padding: 12px 28px` + 字体行高），符合 WCAG 建议。

**运动**：`prefers-reduced-motion: reduce` 时禁用所有过渡和动画，`.reveal` 元素直接显示。

---

## 实现说明

- **组件结构**：单文件 HTML，零构建依赖。`:root` CSS 自定义属性管理所有 Token，`html[data-theme="dark"]` 实现深浅模式翻转
- **CSS 自定义属性**：完整 Token 系统（色彩、间距、圆角、阴影、字体、过渡），页面中所有组件只引用变量
- **字体加载**：Google Fonts CDN 加载 Space Grotesk（400-700）、DM Sans（400-700）、Manrope（400-700）
- **动画**：IntersectionObserver 触发入场动画，`prefers-reduced-motion` 降级
- **图标**：内联 SVG，无外部图标库依赖
