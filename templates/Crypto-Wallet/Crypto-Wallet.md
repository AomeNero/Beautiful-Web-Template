<!--
  web2template 提示词输出模板
  Agent 根据此模板结构，将提取的设计数据与视觉分析结果填入对应章节。
  保持核心结构，根据源页面特点增减章节。
  所有 {{PLACEHOLDER}} 由 Agent 替换为实际内容。
-->

# Crypto-Wallet

> 来源：[uupm.cc/demo/crypto-wallet](https://www.uupm.cc/demo/crypto-wallet)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `crypto-wallet` |
| 显示名称 | Crypto Wallet |
| 模式 | Dark |
| 字体类型 | sans-serif (Space Grotesk + DM Sans) |
| 描述 | 深空暗色加密钱包风格，青蓝到紫色渐变主色，玻璃拟态卡片与霓虹辉光，Space Grotesk 几何标题搭配 DM Sans 正文，专业金融科技质感。 |

## 布局创意 (Layout Ideas)

### Header / Nav

固定顶部导航栏，左侧为品牌 logo（蓝色圆角方块 + "VaultX" 文字），中间为导航链接（Features / Chains / Security / Download），右侧为渐变胶囊 CTA 按钮 "Launch App"。导航栏底部有 1px 半透明白色分隔线，背景为深暗色半透明磨砂玻璃效果。

### Hero

双栏布局：左侧为文案区，右侧为钱包 UI 模型卡片。左侧顶部有绿色圆点 + "Secure & Non-Custodial" 标签，下方是超大标题 "Your Keys, Your Crypto"（"Crypto" 使用青蓝到紫色渐变文字），副标题描述多链钱包功能。底部有两个 CTA 按钮："Download Wallet"（渐变填充）和 "Web App"（描边）。再下方是一排链标签徽章（Ethereum、Bitcoin、Solana、Polygon、Arbitrum、+45）。右侧钱包卡片展示总余额 $98,546.50，今日涨幅 +4.32%，四个操作按钮（Send、Receive、Swap、Bridge），以及 BTC/ETH/SOL 资产列表。卡片底部有 "Swap Complete" 通知浮层。

### Features

三列网格布局展示核心功能卡片，每张卡片包含图标、标题和描述文字。卡片使用深色背景 + 半透明边框 + 柔和阴影。

### Chains / Multi-Chain

顶部有 "Multi-Chain" 标签，标题 "50+ Blockchains, One Wallet"（"One Wallet" 使用渐变文字）。下方是 4x2 网格的链卡片，每张卡片包含链 logo 圆形图标、链名称和 TVL 数据。底部有 "View All 50+ Chains" 描边按钮。

### Security

安全特性展示区块，使用图标 + 文字组合，强调非托管、加密等安全特性。

### Download / CTA

居中大卡片区块，标题 "Start Your Crypto Journey"，描述文字，四个平台下载按钮（iOS、Android、Chrome、Desktop），底部展示 2M+ Downloads、4.9 App Rating、$10B+ Assets Secured 三个数据指标。

### Footer

深色底部，左侧品牌 logo + 标语，中间四列链接（Product / Resources / Company / Legal），底部版权信息 + 社交媒体图标（X、Discord、GitHub）。

---

## 完整提示词 (Full Prompt)

# 设计风格：Crypto-Wallet

## 设计哲学

### 核心原则

Crypto-Wallet 风格追求**专业金融科技与未来科技感的融合**。它借鉴了加密钱包和 DeFi 应用的视觉语言，以深空暗色为画布，用青蓝到紫色的霓虹渐变作为视觉焦点，营造安全、先进、可信赖的数字金融体验。设计拒绝花哨装饰和多余元素，每一个视觉选择都服务于"资产安全"和"技术先进"两个核心信息。

### 视觉气质

**情感关键词**：
- *安全可信* — 深色背景传递稳定感，玻璃拟态卡片暗示透明与保护
- *科技前沿* — 霓虹渐变和辉光效果暗示区块链技术的先进性
- *专业精炼* — 克制的配色和清晰的层级传递金融级专业感

**此设计不是什么**：
- 不是消费级社交应用的活泼配色
- 不是传统银行网站的保守灰蓝
- 不是赛博朋克的过度霓虹堆砌

### 此风格的 DNA

#### 1. 青蓝-紫色渐变签名
从 #00D4FF（青蓝）到 #7B61FF（紫色）的对角线渐变贯穿整个设计——用于 CTA 按钮、标题高亮文字、logo 图标背景。这是品牌识别的核心。

#### 2. 深空暗色基底
背景色 #0A0E17（近黑深蓝）作为主画布，配合 #111827 的卡片表面，创造层次分明的暗色空间。

#### 3. 玻璃拟态卡片
所有 UI 卡片使用半透明背景 + 1px 半透明白色边框 + 柔和弥散阴影，模拟磨砂玻璃质感。

#### 4. 霓虹辉光阴影
关键元素（CTA 按钮、重要卡片）使用彩色辉光阴影——青色 #00D4FF 或紫色 #7B61FF 的 60px 弥散光晕，创造"发光"效果。

#### 5. 绿色数据强调
正值数据（涨幅、余额）使用 #00FF88 亮绿色，负值使用 #FF4757 红色，形成清晰的数据可视化语义。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：深空暗色基底 + 青蓝紫渐变主色 + 绿色数据强调。整体为冷色调，渐变提供视觉活力，绿色/红色用于数据语义。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `background` | `#0A0E17` | 页面主背景，深空暗蓝 |
| `background-alt` | `#111827` | 交替区块背景，略浅的暗色 |
| `surface` | `rgba(255,255,255,0.05)` | 卡片表面，半透明白色 |
| `surface-hover` | `rgba(255,255,255,0.08)` | 卡片悬停态 |
| `foreground` | `#FFFFFF` | 主要文字 |
| `foreground-muted` | `#94A3B8` | 次要文字、描述 |
| `accent-cyan` | `#00D4FF` | 渐变起点、链接、图标 |
| `accent-purple` | `#7B61FF` | 渐变终点、品牌色 |
| `accent-green` | `#00FF88` | 正值数据、成功状态 |
| `accent-red` | `#FF4757` | 负值数据、警告 |
| `accent-orange` | `#F7931A` | Bitcoin 品牌色 |
| `border` | `rgba(255,255,255,0.1)` | 卡片边框 |
| `border-strong` | `rgba(255,255,255,0.2)` | 强调边框 |

**签名渐变**：
```css
/* 主渐变 - 青蓝到紫色 */
background: linear-gradient(135deg, #00D4FF 0%, #7B61FF 100%);

/* 文字渐变 */
background: linear-gradient(to right bottom, #00D4FF 0%, #7B61FF 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;

/* 辉光渐变 */
background: linear-gradient(to right bottom, rgba(0, 212, 255, 0.2) 0%, rgba(123, 97, 255, 0.2) 100%);
```

### 字体系统

**字体配对**：
- **展示字体**：`Space Grotesk` — 几何感无衬线，用于标题和品牌文字，字重 400-700
- **UI/正文字体**：`DM Sans` — 现代人文无衬线，用于正文和 UI 标签，字重 400-700

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 4rem (64px) | Space Grotesk | 700 | -0.02em | 超大标题，部分文字渐变 |
| 区块标题 | 2.5rem (40px) | Space Grotesk | 700 | -0.02em | 部分文字渐变 |
| 卡片标题 | 1.25rem (20px) | Space Grotesk | 600 | 0 | 链名称等 |
| 正文 | 1rem (16px) | DM Sans | 400 | 0 | 描述文字 |
| 标签 | 0.875rem (14px) | DM Sans | 500 | 0 | 徽章、导航链接 |
| 数据数值 | 1.5rem (24px) | Space Grotesk | 700 | 0 | 余额、TVL 等 |

### 间距与布局

- **区块间距**：垂直内边距 96px（`py-24`），区块间交替背景色
- **容器宽度**：max-width 1280px，两侧 padding 32px
- **网格间隙**：24px-32px（卡片网格），8px-16px（小组件间距）
- **非对称模式**：Hero 区左文右图约 55:45 比例

**常见间距值**：8px、12px、16px、20px、24px、28px、32px、48px、64px、96px

### 边框、表面与阴影

**圆角策略**：
- 小圆角：8px（小按钮、标签）
- 中圆角：12px（卡片、输入框）
- 大圆角：20px（大卡片、模态框）
- 胶囊：50px（CTA 按钮、徽章）

**边框**：1px solid，颜色为 `rgba(255,255,255,0.1)`，悬停时加深至 `0.2`

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `shadow-card` | `rgba(0,0,0,0.4) 0px 4px 6px -1px, rgba(0,0,0,0.3) 0px 2px 4px -2px` | 标准卡片 |
| `shadow-glow-cyan` | `rgba(0,212,255,0.2) 0px 0px 60px 0px` | 青色辉光 |
| `shadow-glow-purple` | `rgba(123,97,255,0.2) 0px 0px 60px 0px` | 紫色辉光 |

**纹理与图案**：无显式纹理，依赖渐变和辉光创造深度。

---

## 组件样式与交互

### 按钮

**主按钮（渐变填充）**：
- 背景：`linear-gradient(135deg, #00D4FF, #7B61FF)`
- 文字：白色，字重 600
- 圆角：50px（胶囊形）
- 内边距：14px 28px
- 悬停：亮度提升 + 辉光阴影增强
- 激活：轻微下压

**次按钮（描边）**：
- 背景：透明
- 边框：1px solid `rgba(255,255,255,0.2)`
- 文字：白色
- 圆角：50px
- 悬停：背景变为 `rgba(255,255,255,0.05)`

**图标按钮（操作按钮）**：
- 背景：`rgba(255,255,255,0.05)`
- 边框：1px solid `rgba(255,255,255,0.1)`
- 圆角：12px
- 尺寸：约 64x64px
- 悬停：背景加深

### 卡片

- 背景：`rgba(255,255,255,0.05)` 或 `#111827`
- 边框：1px solid `rgba(255,255,255,0.1)`
- 圆角：12px 或 20px
- 阴影：标准卡片阴影
- 悬停：边框加深 + 轻微上浮

### 徽章/标签

- 背景：对应链色的 12.5% 透明度（如 `rgba(247,147,26,0.125)` 为 Bitcoin 橙）
- 文字：对应链色
- 圆角：50px（胶囊形）
- 内边距：6px 14px
- 字体：DM Sans 500，14px

### 导航

- 背景：`rgba(10,14,23,0.9)` + `backdrop-filter: blur(20px)`
- 底部边框：1px solid `rgba(255,255,255,0.1)`
- 链接文字：`#94A3B8`，悬停变白
- CTA 按钮：渐变填充胶囊

### 输入框

- 背景：`rgba(255,255,255,0.05)`
- 边框：1px solid `rgba(255,255,255,0.1)`
- 圆角：12px
- 聚焦：边框变为渐变色 + 辉光

---

## "大胆要素"（签名元素）

1. **渐变文字标题**：Hero 和区块标题中的关键词（"Crypto"、"One Wallet"）使用青蓝到紫色渐变填充，`background-clip: text` 实现，创造视觉焦点和品牌识别。

2. **霓虹辉光阴影**：关键 CTA 和卡片使用 60px 弥散的彩色辉光（青色或紫色），在暗色背景上创造"发光"效果，暗示数字/加密主题。

3. **玻璃拟态导航栏**：固定顶部导航使用 `backdrop-filter: blur(20px)` + 半透明背景，滚动时内容在导航栏下模糊透出。

4. **链色编码系统**：每条区块链使用专属颜色（BTC 橙 #F7931A、ETH 蓝 #627EEA、SOL 绿 #00FFA3 等），在徽章背景、图标、数据标签中一致使用。

5. **钱包 UI 模型**：Hero 右侧直接展示产品界面（余额卡片、资产列表、操作按钮），用真实产品 UI 作为视觉主体而非抽象插图。

6. **数据语义色彩**：涨幅用 #00FF88 绿色、跌幅用 #FF4757 红色，在暗色背景上形成高对比数据可视化。

---

## 效果与动画

**运动哲学**：克制而精致。以微妙的悬停过渡和入场动画为主，避免过度动效干扰金融产品的专业感。

**过渡默认**：
- 标准：`all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`
- 入场：IntersectionObserver 触发，8px 位移 + 透明度渐变
- 悬停：边框颜色加深 + 背景微亮 + 轻微上浮（translateY(-2px)）

**持续动画**：
- `float`：6s ease-in-out infinite，元素上下浮动 10-20px，用于装饰元素
- `glow`：box-shadow 在 20px-40px 间脉冲，用于 CTA 辉光
- `pulse-soft`：透明度 0.5-1 脉冲，用于状态指示器

**关键帧动画**：
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes glow {
  0% { box-shadow: rgba(37, 99, 235, 0.3) 0px 0px 20px; }
  100% { box-shadow: rgba(37, 99, 235, 0.6) 0px 0px 40px; }
}

@keyframes shimmer {
  0% { background-position: -200% 0px; }
  100% { background-position: 200% 0px; }
}
```

---

## 响应式策略

**断点哲学**：移动端优先，从单列堆叠到多列网格渐进增强。

- **Hero**：移动端单列（文案在上、UI 模型在下），桌面端双栏 55:45
- **Features**：移动端单列，平板 2 列，桌面 3 列
- **Chains 网格**：移动端 2 列，桌面 4 列
- **Footer**：移动端单列堆叠，桌面 5 列

**关键适配**：
- 标题尺寸：移动端 `clamp(2rem, 8vw, 4rem)`
- 间距缩减：移动端区块间距 48px，桌面 96px
- 装饰元素：移动端隐藏浮动装饰和辉光效果

---

## 可访问性与最佳实践

**色彩对比**：白色文字在 #0A0E17 背景上对比度 > 15:1，满足 WCAG AAA。渐变文字需确保最小字号 18px 或字重 700+。

**聚焦状态**：所有交互元素使用 2px solid 青色 (#00D4FF) 聚焦环，offset 2px。

**触控目标**：按钮最小高度 44px，卡片点击区域充足。

**运动**：`prefers-reduced-motion: reduce` 时禁用所有动画和过渡，仅保留必要状态变化。

---

## 实现说明

- **组件结构**：单文件 HTML，零构建依赖。使用 CSS 自定义属性实现主题化。
- **CSS 自定义属性**：所有颜色、间距、圆角、阴影均定义为 `:root` 变量，支持暗色主题翻转。
- **字体加载**：Google Fonts CDN 加载 Space Grotesk (400-700) 和 DM Sans (400-700)。
- **动画库**：纯 CSS 动画 + IntersectionObserver 入场，无需外部库。
