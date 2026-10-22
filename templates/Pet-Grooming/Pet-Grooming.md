# Pet-Grooming-Claymorphism

> 来源：https://www.uupm.cc/demo/pet-grooming

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `pet-grooming-claymorphism` |
| 显示名称 | Pet Grooming Claymorphism |
| 模式 | Light |
| 字体类型 | sans-serif |
| 描述 | 温暖活泼的宠物美容服务落地页，采用 Claymorphism 粘土拟态风格，橙色主调搭配圆润造型与硬阴影 |

## 布局创意 (Layout Ideas)

### Hero

单栏居中布局，左侧文字区 + 右侧图片区。主标题使用渐变色彩（橙→粉），副标题灰色。两个 CTA 按钮并排（主按钮实心橙色 + 次按钮描边橙色）。底部三列统计数据（5,000+ Happy Pets / 4.9 Rating / 10+ Years Exp.）。右侧展示宠物照片，配有浮动服务卡片（Full Spa / Styling），卡片带硬阴影。

### Services

三列网格布局展示服务卡片（Bath & Brush / Full Grooming / Nail Trim / Spa Package）。每张卡片包含图标、标题、描述、价格。卡片使用大圆角（24px）+ 硬阴影。

### Gallery

三列宠物照片网格，每张照片下方显示宠物名字和品种。底部有"Share Your Pet's Photo"CTA 按钮。

### Pricing

三列定价卡片（Basic / Premium / Deluxe），中间卡片突出显示（推荐标签 + 稍大尺寸）。每张卡片列出包含的服务项目。

### Booking

左右两栏布局：左侧列出服务优势（Same-day appointments / Free pickup / Easy payment / Real-time updates），右侧为预约表单（Service 下拉 / Date 输入 / Time 下拉 / Book Appointment 按钮）。

### Footer

四列布局：Logo + 简介 + 社交图标 | Services 链接 | Company 链接 | Support 链接。底部版权信息 + Privacy/Terms 链接。

---

## 完整提示词 (Full Prompt)

# 设计风格：Pet Grooming Claymorphism

## 设计哲学

### 核心原则

温暖、友好、可信赖的宠物服务品牌形象。通过圆润的造型、柔和的色彩和硬阴影创造"粘土玩具"般的质感，让用户感到亲切和安心。设计追求活泼但不幼稚，专业但不冷漠。

### 视觉气质

**情感关键词**：
- *温暖* — 橙色主调传递阳光和活力
- *友好* — 圆润造型和柔和色彩降低距离感
- *专业* — 清晰的布局和充足留白展现专业度

**此设计不是什么**：
- 不是冷峻的企业风格（避免深蓝/灰色调）
- 不是极简主义（保留装饰性元素和阴影）
- 不是扁平化设计（使用硬阴影创造深度）

### 此风格的 DNA

#### 1. 硬阴影（Hard Shadows）
所有交互元素（按钮、卡片）使用 3-8px 的硬偏移阴影，颜色为橙色的半透明版本（rgba(255, 140, 66, 0.1-0.3)），创造粘土般的立体感。

#### 2. 超大圆角（Oversized Border Radius）
按钮使用 50px 圆角（胶囊形），卡片使用 24px 圆角，输入框使用 16px 圆角。所有元素都呈现柔和的圆润感。

#### 3. 橙色主调（Orange Primary）
主色 #FF8C42 贯穿整个设计，用于按钮、图标背景、强调文字。辅以青色 #06D6A0 和粉色 #FF6B9D 作为点缀。

#### 4. 渐变标题（Gradient Headings）
主标题使用橙→粉渐变（#FF8C42 → #FF6B9D），增加视觉趣味性和品牌识别度。

#### 5. 浮动卡片（Floating Cards）
Hero 区域的图片上叠加服务卡片（Full Spa / Styling），卡片带硬阴影，创造层次感和信息密度。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：温暖的橙色主调，辅以青色和粉色点缀，背景使用极浅的橙白色（#FFF9F5）营造温馨氛围。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `primary` | `#FF8C42` | 主按钮、图标背景、强调元素 |
| `primary-hover` | `#E67A35` | 按钮悬停状态 |
| `primary-light` | `rgba(255, 140, 66, 0.1)` | 浅色背景、徽章底色 |
| `secondary` | `#06D6A0` | 成功状态、辅助图标 |
| `accent` | `#FF6B9D` | 渐变终点、装饰元素 |
| `background` | `#FFFFFF` | 主背景 |
| `background-alt` | `#FFF9F5` | 交替区块背景 |
| `foreground` | `#0F172A` | 主文字 |
| `muted` | `#636E72` | 次要文字、描述 |
| `border` | `#FFE4D6` | 卡片边框、分隔线 |
| `border-strong` | `#FF8C42` | 强调边框 |

**签名渐变**：
```css
background: linear-gradient(135deg, #FF8C42 0%, #FF6B9D 100%);
```

### 字体系统

**字体配对**：
- **展示字体**：`Space Grotesk` — 用于标题，现代几何感，字重 500-700
- **UI/正文字体**：`DM Sans` — 用于正文和 UI 元素，清晰易读，字重 400-500

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 64px | Space Grotesk | 700 | -0.02em | 渐变色彩 |
| 区块标题 | 40px | Space Grotesk | 700 | -0.01em | 单色或渐变 |
| 卡片标题 | 20px | Space Grotesk | 600 | 0 | 深色 |
| 正文 | 16px | DM Sans | 400 | 0 | 灰色 |
| 标签 | 14px | DM Sans | 500 | 0 | 彩色 |
| 小字 | 13px | DM Sans | 400 | 0 | 辅助信息 |

### 间距与布局

- **区块间距**：垂直内边距 80-96px，创造呼吸感
- **容器宽度**：最大宽度 1200px，居中布局
- **网格间隙**：24-32px
- **卡片内边距**：32px

**常见间距值**：8px / 16px / 24px / 32px / 48px / 64px / 80px / 96px

### 边框、表面与阴影

**圆角策略**：
- 按钮：50px（胶囊形）
- 卡片：24px
- 输入框：16px
- 徽章：50px（胶囊形）
- 图片：20px

**边框**：2px solid，颜色为 `#FFE4D6`（浅橙）或 `rgba(255, 140, 66, 0.2)`（半透明橙）

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `shadow-sm` | `rgba(255, 140, 66, 0.2) 4px 4px 0px 0px` | 小卡片、徽章 |
| `shadow-md` | `rgba(255, 140, 66, 0.3) 3px 3px 0px 0px` | 按钮、输入框 |
| `shadow-lg` | `rgba(255, 140, 66, 0.15) 8px 8px 0px 0px` | 大卡片、Hero 图片 |
| `shadow-inset` | `rgba(0, 0, 0, 0.05) 0px -3px 0px 0px inset` | 按钮底部内阴影 |

### 组件样式与交互

#### 按钮

**主按钮**：
- 背景：`#FF8C42`
- 文字：白色，16px，字重 600
- 圆角：50px
- 内边距：16px 32px
- 阴影：`rgba(255, 140, 66, 0.3) 4px 4px 0px 0px` + `rgba(0, 0, 0, 0.1) 0px -3px 0px 0px inset`
- 悬停：背景变深 `#E67A35`，阴影不变
- 激活：transform translateY(2px)，阴影减小

**次/描边按钮**：
- 背景：透明
- 边框：2px solid `#FF8C42`
- 文字：`#FF8C42`
- 圆角：50px
- 悬停：背景变为 `rgba(255, 140, 66, 0.1)`

#### 卡片
- 背景：白色
- 边框：2px solid `#FFE4D6`
- 圆角：24px
- 内边距：32px
- 阴影：`rgba(255, 140, 66, 0.1) 6px 6px 0px 0px`
- 悬停：阴影加深，transform translateY(-4px)

#### 输入框
- 背景：白色
- 边框：2px solid `#FFE4D6`
- 圆角：16px
- 内边距：16px
- 聚焦：边框变为 `#FF8C42`

#### 导航
- 背景：白色，固定顶部
- Logo：橙色圆形图标 + 品牌名
- 链接：深灰色，悬停变橙色
- CTA 按钮：橙色实心

#### 徽章/标签
- 背景：`rgba(255, 140, 66, 0.1)`
- 文字：`#FF8C42`
- 圆角：50px
- 内边距：8px 16px
- 字体：14px，字重 500

---

## "大胆要素"（签名元素）

1. **硬阴影粘土质感**：所有交互元素使用 3-8px 硬偏移阴影，颜色为橙色半透明版本，创造独特的"粘土玩具"立体感，区别于常见的柔和弥散阴影。

2. **超大胶囊按钮**：按钮使用 50px 圆角形成完美胶囊形，配合硬阴影和内阴影，呈现可按压的 tactile 质感。

3. **渐变标题文字**：主标题使用橙→粉对角渐变（`linear-gradient(135deg, #FF8C42, #FF6B9D)`），配合 `-webkit-background-clip: text` 实现，增加视觉冲击力。

4. **浮动服务卡片**：Hero 图片上叠加带硬阴影的服务卡片（Full Spa / Styling），卡片轻微旋转（transform: rotate(-2deg)），创造层次感和趣味性。

5. **橙色单色系阴影**：所有阴影都使用橙色（#FF8C42）的半透明版本，而非传统的黑色/灰色阴影，保持色彩一致性并强化品牌色。

6. **极浅橙白背景**：交替区块使用 `#FFF9F5`（极浅橙白）而非纯白或灰色，营造温暖氛围而不刺眼。

---

## 效果与动画

**运动哲学**：轻快、友好、有弹性。动画幅度小（2-8px 位移），时长短（200-300ms），使用 ease-out 缓动。

**过渡默认**：
- 标准：`all 0.2s ease-out`
- 入场：`transform 0.3s ease-out` + `opacity 0.3s ease-out`
- 悬停：`transform 0.2s ease-out` + `box-shadow 0.2s ease-out`

**持续动画**（如有）：
- `gradient`：背景位置动画，8s 循环，用于渐变文字
- `float`：Y 轴位移 ±10px，3s 循环，用于浮动卡片

**关键帧动画**：
```css
@keyframes gradient {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}
```

---

## 响应式策略

**断点哲学**：移动端单列堆叠，平板双列，桌面三列。标题字号随视口缩小。

- **Hero**：移动端单列（文字上/图片下），桌面双列（文字左/图片右）
- **Services/Pricing**：移动端单列，平板双列，桌面三列
- **Gallery**：移动端单列，平板双列，桌面三列
- **Booking**：移动端单列堆叠，桌面双列并排

**关键适配**：
- 标题尺寸：64px → 48px → 36px（桌面 → 平板 → 移动）
- 区块间距：96px → 64px → 48px
- 卡片内边距：32px → 24px → 16px
- 浮动卡片：桌面显示，移动端隐藏

---

## 可访问性与最佳实践

**色彩对比**：橙色 #FF8C42 在白色背景上对比度约 3.5:1，用于大文字和图形可接受；主文字使用 #0F172A（对比度 >15:1）确保可读性。

**聚焦状态**：输入框和按钮聚焦时边框变为 #FF8C42，添加 2px 外发光 `box-shadow: 0 0 0 3px rgba(255, 140, 66, 0.3)`。

**触控目标**：按钮最小高度 48px，内边距充足，适合触控操作。

**运动**：尊重 `prefers-reduced-motion`，禁用所有动画和过渡。

---

## 实现说明

- **组件结构**：单文件 HTML，零构建依赖，使用 CSS 自定义属性（`:root`）管理 Token
- **CSS 自定义属性**：所有颜色、圆角、阴影、字体都定义为 CSS 变量，支持主题切换
- **字体加载**：Google Fonts 加载 Space Grotesk（400/500/600/700）和 DM Sans（400/500）
- **动画库**：纯 CSS 动画 + IntersectionObserver 触发入场动画，无需外部库
- **图片资源**：使用 `https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size={size}` 生成宠物相关图片
