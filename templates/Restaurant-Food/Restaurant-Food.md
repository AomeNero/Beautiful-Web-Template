# Restaurant-Food

> 来源：https://www.uupm.cc/demo/restaurant-food

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `restaurant-food` |
| 显示名称 | Restaurant & Food |
| 模式 | Light |
| 字体类型 | serif + sans-serif |
| 描述 | 高端餐厅落地页，暖白背景搭配深棕硬阴影与珊瑚橙主色，Playfair Display SC 衬线标题 + DM Sans 正文，块状布局与运动驱动风格 |

## 布局创意 (Layout Ideas)

### Header

固定顶部导航栏，带 2px 深棕边框，圆角 12px，毛玻璃背景（rgba(255,255,255,0.95) + backdrop-blur）。左侧品牌名 "La Maison"，中间导航链接（Menu / Our Story / Reservation / Contact），右侧珊瑚橙 CTA 按钮 "Book a Table"，带 6px 深棕硬阴影。

### Hero

双栏布局：左侧文字区 + 右侧图片拼贴。顶部有 "Award-Winning Cuisine" 徽章（带星形图标 + 深棕边框）。主标题使用 Playfair Display SC 衬线字体，"EXPERIENCE" 为深棕色，"CULINARY ART" 为珊瑚橙色。副标题灰色正文。两个 CTA 按钮并排（主按钮珊瑚橙实心 + 次按钮深棕描边）。底部显示营业时间和地址信息。右侧为 4 张美食照片拼贴网格，带深棕硬阴影，底部叠加 "15+ YEARS OF EXCELLENCE" 橙色徽章。

### Menu

居中布局，顶部有书本图标分隔线。标题 "OUR MENU" 使用衬线字体。三列网格展示菜品卡片（Starters / Mains / Desserts / Wine / Cocktails），每张卡片包含菜品图片、名称、描述和价格。卡片带深棕边框和硬阴影。

### Our Story

双栏布局：左侧厨师照片 + 右侧文字。顶部有菱形图标分隔线。标题 "OUR STORY" 使用衬线字体。文字描述餐厅历史和理念。照片下方叠加引用卡片（带橙色引号图标 + 厨师名言）。底部三列统计数据（15+ YEARS / 50K+ HAPPY GUESTS / 3 MICHELIN STARS），带深棕边框。

### Reservation

深色背景（#2C1810）区块，白色文字。双栏布局：左侧文字 + 右侧预约表单。表单包含日期、时间、人数选择器和 "Reserve Now" 按钮。

### Testimonials

三列评价卡片网格，每张卡片包含五星评分、评价文字、评价人姓名和身份。卡片带深棕边框和硬阴影。

### Footer

深色背景（#2C1810）四列布局：Logo + 简介 + 社交图标 | Menu 链接 | Visit 链接 | About 链接。底部版权信息 + Privacy/Terms 链接。

---

## 完整提示词 (Full Prompt)

# 设计风格：Restaurant & Food

## 设计哲学

### 核心原则

高端餐厅品牌形象，通过深棕硬阴影、珊瑚橙点缀和衬线字体传递精致与温暖。设计追求"手工质感"与"现代优雅"的平衡——硬阴影创造 tactile 的物理存在感，衬线字体传递经典与品味，珊瑚橙注入活力与食欲。

### 视觉气质

**情感关键词**：
- *精致* — Playfair Display SC 衬线字体和考究间距传递高端感
- *温暖* — 暖白背景（#FFFAF0）和珊瑚橙（#FF6B35）营造舒适氛围
- *手工质感* — 深棕硬阴影（4-6px 偏移）创造物理存在感，仿佛印刷品

**此设计不是什么**：
- 不是冷峻的极简主义（保留装饰性边框和阴影）
- 不是扁平化设计（使用硬阴影创造深度）
- 不是科技感（避免蓝色调和几何图形）

### 此风格的 DNA

#### 1. 深棕硬阴影（Dark Brown Hard Shadows）
所有交互元素使用 4-6px 的硬偏移阴影，颜色为深棕色（#2C1810），创造印刷品般的物理质感。这是此风格最显著的视觉特征。

#### 2. 珊瑚橙点缀（Coral Orange Accent）
主色 #FF6B35 用于 CTA 按钮、强调文字、图标和徽章，在暖白背景上形成温暖而醒目的对比。

#### 3. 衬线展示字体（Serif Display Typography）
Playfair Display SC 用于所有标题，传递经典、优雅和文学感。DM Sans 用于正文和 UI 元素，保持清晰易读。

#### 4. 块状边框布局（Block-based Borders）
所有卡片、按钮和容器使用 2px 深棕实线边框，配合硬阴影，创造"块状"视觉语言。

#### 5. 图片拼贴（Photo Collage）
Hero 区域使用多张图片拼贴网格，每张图片带独立硬阴影，创造丰富的视觉层次。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：暖白背景搭配深棕文字和边框，珊瑚橙作为活力点缀，深色区块（#2C1810）用于对比。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `primary` | `#FF6B35` | CTA 按钮、强调文字、图标、徽章 |
| `primary-hover` | `#E55A25` | 按钮悬停状态 |
| `primary-light` | `rgba(255, 107, 53, 0.1)` | 浅色背景、徽章底色 |
| `background` | `#FFFFFF` | 主背景 |
| `background-warm` | `#FFFAF0` | 交替区块暖白背景 |
| `background-dark` | `#2C1810` | 深色区块背景（Reservation / Footer） |
| `foreground` | `#2C1810` | 主文字、边框 |
| `muted` | `#6B5344` | 次要文字、描述 |
| `border` | `#2C1810` | 卡片边框、分隔线 |
| `border-light` | `#E8DDD4` | 浅色分隔线 |

**签名渐变**：
```css
/* 无渐变，使用纯色对比 */
background: #FF6B35; /* 珊瑚橙实心 */
```

### 字体系统

**字体配对**：
- **展示字体**：`Playfair Display SC` — 用于标题，经典衬线感，字重 400-700
- **UI/正文字体**：`DM Sans` — 用于正文和 UI 元素，清晰易读，字重 400-500-700

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 72px | Playfair Display SC | 700 | 0.02em | 深棕/珊瑚橙双色 |
| 区块标题 | 48px | Playfair Display SC | 700 | 0.02em | 深棕色 |
| 卡片标题 | 20px | Playfair Display SC | 700 | 0 | 深棕色 |
| 正文 | 16px | DM Sans | 400 | 0 | 灰色 |
| 导航链接 | 15px | DM Sans | 500 | 0 | 深棕色 |
| 标签 | 14px | DM Sans | 500 | 0.05em | 彩色 |
| 小字 | 13px | DM Sans | 400 | 0 | 辅助信息 |

### 间距与布局

- **区块间距**：垂直内边距 80-128px，创造呼吸感
- **容器宽度**：最大宽度 1152px，居中布局
- **网格间隙**：24-32px
- **卡片内边距**：24-32px

**常见间距值**：8px / 16px / 24px / 32px / 48px / 64px / 80px / 128px

### 边框、表面与阴影

**圆角策略**：
- 按钮：12px
- 卡片：12px
- 输入框：8px
- 导航栏：12px
- 图片：8px

**边框**：2px solid `#2C1810`（深棕）

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `shadow-sm` | `4px 4px 0px 0px #2C1810` | 小按钮、徽章 |
| `shadow-md` | `6px 6px 0px 0px #2C1810` | 按钮、卡片 |
| `shadow-soft` | `0px 4px 16px 0px rgba(44, 24, 16, 0.06)` | 柔和阴影 |

### 组件样式与交互

#### 按钮

**主按钮**：
- 背景：`#FF6B35`
- 文字：白色，16px，字重 600
- 圆角：12px
- 内边距：16px 32px
- 阴影：`6px 6px 0px 0px #2C1810`
- 悬停：背景变深 `#E55A25`
- 激活：transform translateY(2px)，阴影减小为 `4px 4px 0px 0px`

**次/描边按钮**：
- 背景：透明
- 边框：2px solid `#2C1810`
- 文字：`#2C1810`
- 圆角：12px
- 悬停：背景变为 `rgba(44, 24, 16, 0.05)`

#### 卡片
- 背景：白色或暖白
- 边框：2px solid `#2C1810`
- 圆角：12px
- 内边距：24-32px
- 阴影：`6px 6px 0px 0px #2C1810`
- 悬停：transform translateY(-4px)

#### 输入框
- 背景：白色
- 边框：2px solid `#2C1810`
- 圆角：8px
- 内边距：16px
- 聚焦：边框变为 `#FF6B35`

#### 导航
- 背景：白色/95 透明度 + backdrop-blur
- 边框：2px solid `#2C1810`
- 圆角：12px
- Logo：深棕色衬线字体
- 链接：深棕色，悬停变珊瑚橙
- CTA 按钮：珊瑚橙实心 + 硬阴影

#### 徽章/标签
- 背景：白色或珊瑚橙
- 边框：2px solid `#2C1810`（白色徽章）或无（橙色徽章）
- 圆角：8px
- 内边距：8px 16px
- 字体：14px，字重 500

---

## "大胆要素"（签名元素）

1. **深棕硬阴影**：所有交互元素使用 4-6px 硬偏移阴影，颜色为深棕色（#2C1810），创造独特的"印刷品"立体感，区别于常见的柔和弥散阴影或彩色阴影。

2. **衬线展示标题**：Playfair Display SC 用于所有标题，配合 0.02em 字距，传递经典、优雅和文学感，与无衬线正文形成鲜明对比。

3. **珊瑚橙双色标题**：Hero 标题使用深棕 + 珊瑚橙双色设计（"EXPERIENCE" 深棕 + "CULINARY ART" 珊瑚橙），创造视觉节奏和品牌识别度。

4. **图片拼贴网格**：Hero 区域使用 4 张图片拼贴，每张图片带独立硬阴影，底部叠加橙色统计徽章，创造丰富的视觉层次和信息密度。

5. **块状边框语言**：所有元素使用 2px 深棕实线边框，配合硬阴影，创造统一的"块状"视觉语言，仿佛手工印刷品。

6. **暖白背景系统**：主背景使用纯白（#FFFFFF），交替区块使用暖白（#FFFAF0），深色区块使用深棕（#2C1810），三色背景系统创造节奏感。

---

## 效果与动画

**运动哲学**：优雅、克制、有质感。动画幅度小（2-6px 位移），时长适中（300ms），使用 ease-out 缓动。

**过渡默认**：
- 标准：`all 0.3s ease-out`
- 入场：`transform 0.6s ease-out` + `opacity 0.6s ease-out`
- 悬停：`transform 0.3s ease-out` + `box-shadow 0.3s ease-out`

**持续动画**（如有）：
- `float`：Y 轴位移 ±10px，4s 循环，用于浮动元素
- `fadeInUp`：从下方淡入，用于入场动画

**关键帧动画**：
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}
```

---

## 响应式策略

**断点哲学**：移动端单列堆叠，平板双列，桌面多列。标题字号随视口缩小。

- **Hero**：移动端单列（文字上/图片下），桌面双列（文字左/图片右）
- **Menu**：移动端单列，平板双列，桌面三列
- **Our Story**：移动端单列堆叠，桌面双列并排
- **Testimonials**：移动端单列，平板双列，桌面三列
- **Reservation**：移动端单列堆叠，桌面双列并排

**关键适配**：
- 标题尺寸：72px → 48px → 36px（桌面 → 平板 → 移动）
- 区块间距：128px → 80px → 64px
- 卡片内边距：32px → 24px → 16px
- 图片拼贴：桌面 4 张网格，移动端 2 张或单张

---

## 可访问性与最佳实践

**色彩对比**：珊瑚橙 #FF6B35 在白色背景上对比度约 3.2:1，用于大文字和图形可接受；主文字使用 #2C1810（对比度 >12:1）确保可读性。

**聚焦状态**：输入框和按钮聚焦时边框变为 #FF6B35，添加 2px 外发光 `box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.3)`。

**触控目标**：按钮最小高度 48px，内边距充足，适合触控操作。

**运动**：尊重 `prefers-reduced-motion`，禁用所有动画和过渡。

---

## 实现说明

- **组件结构**：单文件 HTML，零构建依赖，使用 CSS 自定义属性（`:root`）管理 Token
- **CSS 自定义属性**：所有颜色、圆角、阴影、字体都定义为 CSS 变量，支持主题切换
- **字体加载**：Google Fonts 加载 Playfair Display SC（400/700）和 DM Sans（400/500/700）
- **动画库**：纯 CSS 动画 + IntersectionObserver 触发入场动画，无需外部库
- **图片资源**：使用 Unsplash 餐厅/美食相关图片
