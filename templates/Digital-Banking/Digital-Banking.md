# Digital-Banking（数字银行应用）

> 来源：https://www.uupm.cc/demo/digital-banking

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `Digital-Banking` |
| 显示名称 | Digital Banking |
| 模式 | Dark（深空蓝暗色模式） |
| 字体类型 | sans-serif（Space Grotesk 展示 + DM Sans 正文） |
| 描述 | 深蓝金融科技美学，手机模型展示银行 App UI，蓝紫渐变点缀，信任徽章与 APY 利率卡片，传递安全、现代、专业的数字银行形象。 |

## 布局创意 (Layout Ideas)

### Hero（深蓝首屏 + 手机模型）
- 双栏布局：左侧文字栈（安全徽章 → 大标题 "Banking Made Simple" → 描述 → 双 CTA 按钮 → 信任图标行），右侧浮起手机模型展示银行 App 界面。
- 手机模型含余额卡片（蓝紫渐变）、操作按钮（Send/Receive/Cards/Invest）、最近交易列表，右上角浮动 "+12.5% This month" 徽章。
- 背景为深海军蓝纯色，无渐变装饰，干净利落。

### Features（功能特性网格）
- 居中标题 + 描述，下方 3 列等宽特性卡片网格。
- 每张卡：图标 + 标题 + 描述，深色表面配微妙边框。

### Accounts（账户类型定价卡）
- 居中标题 "Choose Your Account" + 副标题。
- 3 列等宽定价卡：Everyday Checking (0.50% APY)、High-Yield Savings (4.50% APY, "Most Popular" 徽章)、Investment Account (Variable APY)。
- 每张卡含利率大字、特性列表（绿色勾选）、"Open Account" 按钮。
- 中间卡片为推荐款，按钮为实心蓝色，其余为描边样式。

### Security（安全特性）
- 居中标题 + 描述，下方安全特性展示。

### Download（应用下载）
- 双栏：左侧 App Store / Google Play 下载按钮 + 统计数据（4.9 评分、2M+ 下载、$50B+ 转账），右侧手机模型 + QR 码。

### Footer（深色多栏页脚）
- 5 列布局：品牌 + 标语 + 社交图标 | Products | Company | Resources | Legal。
- 底部 FDIC Insured 横幅 + 版权行 + SOC 2 / PCI DSS 认证徽章。

---

## 完整提示词 (Full Prompt)

# 设计风格：Digital-Banking（数字银行应用）

## 设计哲学

### 核心原则

以"信任与简洁"为信条：用深海军蓝的沉稳包裹清晰的金融信息层级，让数据（余额、利率、交易）成为视觉焦点。拒绝花哨装饰与多余动效，一切设计服务于"安全、专业、易用"的数字银行气质。设计语言的根基是**深蓝暗面 × 蓝紫渐变点缀 × 手机模型实景展示**。

### 视觉气质

金融科技的冷静与可信赖感。深空蓝画布传递安全与稳定，蓝紫渐变注入现代科技感，绿色点缀（勾选、收益）传递正向与增长。手机模型将抽象的"数字银行"具象化，让用户一眼看到产品实际体验。

**情感关键词**：
- *Trustworthy* — 深蓝底色与 FDIC/SOC 2 认证徽章建立金融级信任
- *Modern* — 蓝紫渐变、圆角卡片、手机模型传递前沿科技感
- *Clean* — 信息层级清晰，数据可视化直观，无视觉噪音

**此设计不是什么**：
- 不是消费级社交应用的活泼多彩
- 不是企业级 SaaS 的冷峻灰白
- 不是加密 Web3 的霓虹赛博朋克

### 此风格的 DNA

#### 1. 深蓝暗面画布
全页面使用 #0B1121 深海军蓝作为主背景，营造金融级的沉稳与安全感，区别于普通深色模式的纯黑或深灰。

#### 2. 手机模型实景展示
Hero 与 Download 区块均使用手机模型展示真实 App UI（余额卡片、交易列表、操作按钮），将产品体验前置为视觉主角。

#### 3. 蓝紫渐变强调
余额卡片、"Simple" 标题文字、推荐账户按钮使用 #2563EB → #7C3AED 蓝紫渐变，在深蓝画布上形成克制的视觉焦点。

#### 4. 利率大字展示
APY 利率以超大字号（0.50%、4.50%、Variable）配合彩色数字展示，成为账户卡片的核心视觉锚点。

#### 5. 信任徽章系统
FDIC Insured、256-bit Encryption、No Hidden Fees、SOC 2 Certified、PCI DSS Compliant 等认证徽章贯穿页面，持续强化信任感。

#### 6. 绿色正向信号
所有收益数字（+$4,500.00）、勾选图标、增长百分比（+12.5%）统一使用 #36B37E 绿色，建立"增长=绿色"的视觉语义。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：深海军蓝画布上，蓝紫渐变作为主强调色，绿色作为正向信号色，白色/灰白作为文字色。整体色彩克制、专业、金融感强。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `background` | `#0B1121` | 页面主背景，深海军蓝 |
| `surface` | `#1E293B` | 卡片/面板表面色 |
| `surface-elevated` | `#263347` | 浮起元素（手机模型、弹窗） |
| `foreground` | `#FFFFFF` | 主文字色 |
| `text-muted` | `#A3B3C9` | 次要文字、描述 |
| `accent` | `#2563EB` | 主按钮、链接、CTA |
| `accent-gradient` | `linear-gradient(135deg, #2563EB, #7C3AED)` | 余额卡片、标题渐变、推荐按钮 |
| `success` | `#36B37E` | 收益数字、勾选图标、增长指示 |
| `warning` | `#FFAB00` | 注意/警告色 |
| `purple` | `#6554C0` | 辅助强调、投资账户标题 |
| `border` | `rgba(255,255,255,0.1)` | 卡片边框、分隔线 |
| `border-strong` | `rgba(255,255,255,0.2)` | 强调边框 |

**签名渐变**：
```css
background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
```

### 字体系统

**字体配对**：
- **展示字体**：`Space Grotesk` — 几何感强，用于 Hero 标题、区块标题、利率数字，传递现代科技感
- **UI/正文字体**：`DM Sans` — 圆润友好，用于正文、按钮、导航、卡片描述
- **等宽字体**（如有）：`Inter` — 用于数据展示、金额数字

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 48-64px | Space Grotesk | 700 | normal | "Banking Made Simple" |
| 区块标题 | 36-42px | Space Grotesk | 700 | normal | "Choose Your Account" |
| 卡片标题 | 20-22px | Space Grotesk | 600 | normal | 账户名称、特性标题 |
| 利率数字 | 36-42px | Space Grotesk | 700 | normal | 0.50%、4.50% |
| 正文 | 16px | DM Sans | 400 | normal | 描述文字 |
| 导航/按钮 | 15-16px | DM Sans | 500 | normal | 导航链接、按钮文字 |
| 标签/徽章 | 12-13px | DM Sans | 500 | normal | "Most Popular"、"Primary" |
| 辅助文字 | 14px | DM Sans | 400 | normal | 页脚链接、副标题 |

### 间距与布局

- **区块间距**：每区块垂直内边距 96px（py-24），区块间节奏统一
- **容器宽度**：max-width 1280px，两侧 padding 32px
- **网格间隙**：卡片网格 gap 32px
- **非对称模式**：Hero 与 Download 为双栏非对称布局（文字 50% + 手机模型 50%）

**常见间距值**：4px / 8px / 12px / 16px / 24px / 32px / 48px / 64px / 96px

### 边框、表面与阴影

**圆角策略**：
- 卡片：20-24px（大圆角，柔和现代）
- 按钮：12px（中等圆角）
- 徽章/胶囊：50px（全圆角）
- 手机模型：24px

**边框**：1px solid rgba(255,255,255,0.1)，卡片使用微妙半透明白边框

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `shadow-sm` | `0 4px 6px rgba(0,0,0,0.3)` | 小元素、图标按钮 |
| `shadow-md` | `0 4px 14px rgba(0,82,204,0.4)` | 卡片、手机模型 |
| `shadow-lg` | `0 0 60px rgba(0,82,204,0.3)` | 蓝色辉光（推荐卡片、CTA） |
| `shadow-glow-purple` | `0 0 60px rgba(101,84,192,0.3)` | 紫色辉光（投资卡片） |

**纹理与图案**：无纹理，纯色背景保持干净专业。

---

## 组件样式与交互

### 按钮

**主按钮**（Open Account / Open Free Account）：
- 背景：#2563EB 实心蓝
- 文字：白色，DM Sans 500
- 圆角：12px
- 悬停：亮度提升 + 微上移（translateY -1px）
- 激活：轻微缩放

**次/描边按钮**（See How It Works）：
- 背景：透明
- 边框：1px solid rgba(255,255,255,0.2)
- 文字：白色
- 悬停：边框变亮，背景微亮

**下载按钮**（App Store / Google Play）：
- 背景：rgba(255,255,255,0.08)
- 边框：1px solid rgba(255,255,255,0.15)
- 含平台图标 + 文字

### 卡片
- 背景：#1E293B 深色表面
- 边框：1px solid rgba(255,255,255,0.1)
- 圆角：20-24px
- 内边距：32px
- 悬停：边框微亮 + 微上移
- 推荐卡片：底部蓝色辉光阴影

### 输入框
- 背景：rgba(255,255,255,0.05)
- 边框：1px solid rgba(255,255,255,0.15)
- 圆角：12px
- 聚焦：边框变为蓝色 #2563EB

### 导航
- 固定顶部，背景透明或微透深蓝
- Logo：美元符号图标 + "NexBank" 文字
- 链接：白色/灰白文字，悬停变亮
- CTA 按钮：右侧 "Open Account" 实心蓝按钮

### 徽章/标签
- "Bank-Grade Security"：描边胶囊，蓝色边框 + 蓝色文字
- "Most Popular"：实心蓝紫渐变胶囊，白色文字
- "Primary"：半透明白色胶囊，小字号
- "+12.5%"：绿色文字 + 箭头图标，浮动徽章

### 手机模型
- 圆角矩形框架，深色边框
- 内部展示 App UI：余额卡片（蓝紫渐变）、操作按钮行、交易列表
- 带柔和投影，浮于页面右侧

---

## "大胆要素"（签名元素）

1. **手机模型实景嵌入**：Hero 与 Download 区块直接使用手机模型展示真实 App 界面（余额 $24,562.80、交易记录 Netflix -$15.99 / Salary +$4,500），将产品体验作为核心视觉说服手段，而非抽象插画。

2. **APY 利率大字视觉锚**：账户卡片中利率数字（0.50%、4.50%、Variable）以 36-42px 超大字号 + 彩色（蓝/绿/紫）展示，成为每张卡片的视觉中心，一眼传达核心价值。

3. **蓝紫渐变余额卡片**：手机模型内的余额卡片使用 #2563EB → #7C3AED 蓝紫渐变背景，白色大字显示金额，模拟真实银行 App 的视觉体验。

4. **信任徽章贯穿系统**：从 Hero 的 "Bank-Grade Security" 胶囊、FDIC/256-bit/No Fees 信任行，到页脚的 SOC 2 / PCI DSS 认证，信任信号贯穿全页面。

5. **绿色正向语义统一**：所有收益（+$4,500.00）、增长（+12.5%）、勾选图标统一使用 #36B37E 绿色，建立直观的"绿色=正向/安全"视觉语义。

---

## 效果与动画

**运动哲学**：克制、平滑、专业。动画服务于信息层级揭示，不喧宾夺主。

**过渡默认**：
- 标准：all 0.2s cubic-bezier(0.4, 0, 0.2, 1)
- 入场：opacity 0 → 1 + translateY 20px → 0 + filter blur 6px → 0
- 悬停：translateY -2px + 边框/阴影微增强

**持续动画**：
- `float`：3s ease-in-out infinite，手机模型上下浮动（translateY 0 → -20px → 0）
- `gradient`：8s ease infinite，渐变背景位置移动（background-position 0% → 100% → 0%）
- `glow`：2s ease-in-out infinite alternate，蓝色辉光强度脉动

**关键帧动画**：
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
@keyframes gradient {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}
@keyframes glow {
  0% { box-shadow: 0 0 20px rgba(37,99,235,0.3); }
  100% { box-shadow: 0 0 40px rgba(37,99,235,0.6); }
}
```

---

## 响应式策略

**断点哲学**：移动端单列堆叠，平板双列，桌面三列/双栏。

- **Hero**：移动端文字全宽 + 手机模型下移/缩小；桌面双栏并排
- **Features/Accounts**：移动端单列 → 平板双列 → 桌面三列
- **Download**：移动端单列堆叠 → 桌面双栏
- **Footer**：移动端 2 列 → 桌面 5 列

**关键适配**：
- 标题尺寸：Hero 标题 48px → 32px（移动端）
- 间距缩减：区块内边距 96px → 48px（移动端）
- 手机模型：桌面 100% → 移动端 70% 宽度
- 装饰元素：浮动徽章在小屏下缩小或隐藏

---

## 可访问性与最佳实践

**色彩对比**：白色文字在深蓝背景上对比度 > 7:1（AAA），灰白文字 #A3B3C9 对比度 > 4.5:1（AA）。绿色 #36B37E 在深色背景上对比度充足。

**聚焦状态**：focus-visible 使用 2px solid #2563EB 蓝色聚焦环，offset 2px。

**触控目标**：按钮最小 44×44px，卡片点击区域充足。

**运动**：prefers-reduced-motion 下禁用所有动画（float、gradient、glow），入场动画改为即时显示。

---

## 实现说明

- **组件结构**：纯 HTML + CSS，零构建依赖。使用 CSS 自定义属性（:root）管理设计 Token。
- **CSS 自定义属性**：所有颜色、字体、间距、圆角、阴影均通过 --var 定义，支持主题切换。
- **字体加载**：Google Fonts 加载 Space Grotesk（300-700）+ DM Sans（400-700）。
- **动画库**：纯 CSS 动画 + IntersectionObserver 触发入场动画，无外部依赖。
- **手机模型**：纯 CSS 绘制（圆角矩形 + 内部 UI 组件），无需图片资源。
- **图标**：使用内联 SVG 图标（美元符号、箭头、勾选、平台图标等）。
