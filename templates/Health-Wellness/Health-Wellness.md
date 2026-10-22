# Health & Wellness App (Serenity)

> 来源：[uupm.cc/demo/health-wellness](https://www.uupm.cc/demo/health-wellness)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `health-wellness` |
| 显示名称 | Health & Wellness |
| 模式 | ️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 新拟态软 UI 健康应用落地页，薄荷绿渐变主色，柔和双向阴影，Space Grotesk 几何标题，Manrope 正文，手机模型展示冥想界面。 |

## 布局创意 (Layout Ideas)

### Hero

左右非对称布局（60/40），左侧文案 + 下载按钮 + 统计数据，右侧手机模型展示冥想计时界面。顶部有 "#1 Wellness App 2024" 徽章，标题 "Find Your Inner Peace" 中 "Inner Peace" 使用渐变绿色。浮动徽章展示 "7 Day Streak!" 和 "Sleep Score: 92"。

### Features

三列卡片网格展示 Meditation / Sleep / Fitness，每张卡片使用新拟态凸出阴影，内含线性图标。下方 "One App for Complete Wellness" 分割布局，左侧卡片组，右侧特性列表配绿色勾选图标。

### Services

"Everything for Your Wellness" 标题居中，副标题说明冥想、健身、睡眠一体化工具。

### Testimonials

"Loved by Millions" 标题居中，副标题邀请加入 200 万用户社区。

### CTA

"Start Your Journey Today" 大卡片，渐变背景，iOS / Android 下载按钮，价格说明。

### Footer

五列布局：品牌 + 社交媒体图标（Instagram, X, Facebook），App / Resources / Company / Legal 链接列。底部版权行 + "Made with ❤ for your wellness"。

---

## 完整提示词 (Full Prompt)

# Health & Wellness App — Neumorphism Soft UI 设计系统

## 设计哲学

**核心原则**：将新拟态（Neumorphism）的柔软触感与健康/正念主题完美融合。使用极浅灰背景（#f5f5f5）作为"画布"，通过双向阴影（左上白色高光 + 右下灰蓝暗影）让元素仿佛从表面自然生长。薄荷绿（#22c55e）作为唯一的强色点缀，传递健康、活力与平静。天蓝到浅绿的渐变（#87CEEB → #90EE90）用于标题强调和 CTA 背景，营造清新自然的氛围。

**气质**：宁静、健康、可信赖、现代。UI 感觉如柔软的陶瓷或磨砂玻璃，让人联想到高端健康应用的精致感。设计在可访问性与美学之间取得平衡——足够的对比度确保可读性，同时保持柔和的新拟态美学。

**独特视觉签名**：
- **新拟态双向阴影**：`rgba(174,174,192,0.4) 8px 8px 16px` + `rgba(255,255,255,0.8) -8px -8px 16px`，创造柔和的凸起/凹陷效果。
- **薄荷绿主色**（#22c55e）：用于 CTA 按钮、勾选图标、进度环、徽章，传递健康活力。
- **天蓝→浅绿渐变**（#87CEEB → #90EE90）：用于标题强调文字和 CTA 卡片背景，清新自然。
- **Space Grotesk 几何标题**：现代、干净的几何无衬线字体作大标题，字重 600-700。
- **Manrope 正文**：高可读性无衬线字体，字重 300-700，传递专业感。
- **手机模型展示**：Hero 区域右侧放置手机模型，展示应用内冥想计时界面（进度环 75%、"Start Session" 按钮）。
- **浮动徽章**：新拟态小卡片悬浮于主内容周围（"7 Day Streak!"、"Sleep Score: 92"），增加层次感。
- **大圆角**：卡片 24px、按钮 16px、小元素 12px，强化柔和有机美学。

---

## 设计 Token 系统（DNA）

### 色彩（浅色模式 — 薄荷绿 + 天蓝）

- **Background**：`#f5f5f5` — 极浅灰作为基础画布，所有新拟态元素由此"生长"。
- **Surface**：`#ffffff` — 纯白用于卡片和手机模型背景。
- **Foreground**：`#0f172a` — 深蓝黑作主要标题文字。
- **Text Primary**：`#2d3748` — 深灰作正文文字。
- **Text Muted**：`#718096` — 中灰作次要文字和导航链接。
- **Accent**：`#22c55e` — 薄荷绿作主色调，用于 CTA、勾选、进度环。
- **Accent Gradient**：`linear-gradient(135deg, #87CEEB, #90EE90)` — 天蓝到浅绿渐变，用于标题强调和 CTA 背景。
- **Border**：`#e2e8f0` — 浅灰边框，极少使用（新拟态以阴影为主）。

**阴影色**（新拟态核心）：
- **Shadow Light**：`rgba(255,255,255,0.8)` — 纯白作左上光源阴影。
- **Shadow Dark**：`rgba(174,174,192,0.4)` — 灰蓝作右下暗影阴影。
- **Shadow Accent**：`rgba(34,197,94,0.3)` — 绿色发光阴影用于 CTA 按钮。
- **Shadow Soft**：`rgba(0,0,0,0.08)` — 柔和黑色阴影用于卡片悬浮。

### 字体

- **展示字体**：**"Space Grotesk"**（400, 500, 600, 700）— 现代几何无衬线作标题。
- **正文字体**：**"Manrope"**（300, 400, 500, 600, 700）— 干净高可读无衬线作正文与 UI。
- **字重**：
  - 标题：`font-weight: 600-700`
  - 正文：`font-weight: 400-500`
  - 次要：`font-weight: 300-400`
- **字号阶梯**：
  - H1：`60px / 75px line-height`
  - H2：`36px / 40px line-height`
  - H3：`18px / 28px line-height`
  - Body：`16px / 24px line-height`
  - Small：`14px / 20px line-height`

### 圆角

- **大卡片/容器**：`24px` — 柔和友好的大圆角。
- **按钮/中等元素**：`16px` — 标准圆角。
- **小元素/图标**：`12px` — 紧凑圆角。
- **药丸/徽章**：`9999px`（full）— 完全圆角。

### 阴影与效果

**凸出（标准新拟态）** — 卡片默认状态：
```css
box-shadow: 8px 8px 16px rgba(174,174,192,0.4), -8px -8px 16px rgba(255,255,255,0.8);
```

**凸出小** — 小元素：
```css
box-shadow: 4px 4px 8px rgba(174,174,192,0.4), -4px -4px 8px rgba(255,255,255,0.8);
```

**CTA 按钮** — 绿色发光：
```css
box-shadow: 0 4px 14px rgba(34,197,94,0.3);
```

**卡片悬浮** — 柔和深度：
```css
box-shadow: 0 4px 20px rgba(0,0,0,0.08);
```

**内嵌（凹陷）** — 输入框/进度环背景：
```css
box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
```

---

## 组件样式

### 按钮
- **主 CTA**：薄荷绿背景 `#22c55e`，白色文字，`border-radius: 16px`，`padding: 16px 32px`，绿色发光阴影。悬停时轻微上移 + 阴影增强。
- **次按钮**：白色背景，灰色边框 `#e2e8f0`，深色文字。悬停时背景变浅灰。
- **下载按钮**：App Store / Google Play 样式，含平台图标，大尺寸。

### 卡片
- **背景**：`#f5f5f5` 或 `#ffffff`。
- **圆角**：`24px`。
- **阴影**：新拟态凸出阴影。
- **内边距**：`24px-32px`。
- **悬停**：轻微上移 `translateY(-2px)` + 阴影增强。

### 徽章/标签
- **形状**：药丸形（`border-radius: 9999px`）。
- **背景**：浅绿 `rgba(34,197,94,0.1)` 或新拟态凸出。
- **文字**：绿色 `#22c55e` 或深色。
- **尺寸**：小尺寸，`padding: 6px 16px`。

### 手机模型
- **背景**：纯白 `#ffffff`。
- **圆角**：`24px`。
- **阴影**：新拟态凸出 + 柔和黑色阴影。
- **内容**：应用界面截图或 UI 组件展示。

### 进度环
- **背景环**：浅灰 `#e2e8f0`。
- **进度环**：渐变 `#87CEEB → #90EE90` 或纯绿 `#22c55e`。
- **中心文字**：百分比数字（大）+ 标签（小）。

### 勾选图标
- **形状**：圆形背景 `rgba(34,197,94,0.15)`。
- **图标**：绿色 `#22c55e` 勾选标记。
- **尺寸**：`24px` 圆形。

---

## 布局原则

- **间距**：开放通透。Hero 区 `padding: 128px 16px 80px`，Section 区 `padding: 80px 16px`。
- **容器**：`max-width: 1152px`，居中 `margin: 0 auto`。
- **网格**：三列特性卡片 `gap: 32px`，两列布局 `gap: 48px`。
- **背景**：页面背景 `#f5f5f5`，无渐变。CTA 卡片使用渐变背景。

## 动画与微交互

- **时长**：UI 元素 `300ms`，卡片悬浮 `300ms`。
- **缓动**：`ease-out` 或 `cubic-bezier(0.4, 0, 0.2, 1)`。
- **属性**：`transform`（translateY）、`box-shadow`（深度变化）、`opacity`。
- **悬停效果**：
  - 卡片：`translateY(-2px)` + 阴影增强。
  - 按钮：`translateY(-1px)` + 阴影增强。
  - 链接：颜色变化 + 下划线。

## 响应式断点

- **Desktop**：`>= 1024px` — 完整布局，左右分栏。
- **Tablet**：`768px - 1023px` — 单列布局，卡片堆叠。
- **Mobile**：`< 768px` — 紧凑布局，导航折叠为汉堡菜单。
