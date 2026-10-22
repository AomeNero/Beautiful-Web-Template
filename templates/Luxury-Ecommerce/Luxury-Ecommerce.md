# Luxury-Ecommerce

> 来源：[uupm.cc/demo/luxury-ecommerce](https://www.uupm.cc/demo/luxury-ecommerce)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `luxury-ecommerce` |
| 显示名称 | Luxury E-commerce |
| 模式 | ️ 浅色模式 (Light) |
| 字体类型 | serif + sans-serif |
| 描述 | Liquid Glass + Glassmorphism 奢华电商风格。磨砂玻璃导航栏、奶油白背景、Playfair Display 衬线标题、深色海军蓝主文字与金色点缀。产品卡片悬浮阴影、毛玻璃徽章、优雅的电商落地页。 |

## 布局创意 (Layout Ideas)

### Header

固定顶部导航栏，磨砂玻璃背景 `backdrop-filter: blur(20px)` + 半透明白底。左侧 MAISON 品牌名（Playfair Display 粗体），中间导航链接（大写、宽字距），右侧搜索/账户/购物车图标。底部 1px 淡色边框。

### Hero

全视口高度 Hero 区，背景为精品店室内摄影图。左上角 "AUTUMN/WINTER 2024" 标签配金色短横线装饰。巨型衬线标题 "The Art of Timeless Elegance"（"Timeless" 为斜体）。副标题描述文字。两个 CTA 按钮：黑色实心胶囊按钮 "EXPLORE COLLECTION" + 线框按钮 "BOOK APPOINTMENT"。底部三组统计数据（150+ / 48 / 1892）配微型大写标签。

### Our Story

左右双栏布局。左侧工匠特写摄影图，右下角叠加毛玻璃卡片 "130+ YEARS OF EXCELLENCE"。右侧品牌故事文字 + 三列价值图标（Quality / Passion / Timeless）+ "DISCOVER OUR STORY" 线框按钮。

### Collections

奶油色背景区块。"EXPLORE" 标签 + "Our Collections" 衬线大标题。产品卡片网格（3 列），每张卡片含产品图、名称、价格。卡片悬停有微妙上浮与阴影加深效果。

### Features / Banner

深色（近黑）全宽横幅区块，白色文字。大标题 + 描述文字 + CTA 按钮，形成强烈对比。

### Newsletter

简洁的邮件订阅区。"Stay in Touch" 衬线标题 + 描述文字。邮箱输入框与黑色 "SUBSCRIBE" 按钮并排。

### Footer

奶油色背景。五列布局：品牌介绍 + SHOP / SERVICES / COMPANY / SUPPORT 导航列。底栏含版权信息与社交媒体图标（Instagram / Facebook / Pinterest / YouTube）。

---

## 完整提示词 (Full Prompt)

# 设计风格：Luxury E-commerce / Liquid Glass

## 设计哲学

**核心原则**：将高端时尚电商的精致感与现代 Liquid Glass 毛玻璃效果融合。设计效仿 MAISON、Hermès、Dior 等奢侈品牌的线上体验，通过磨砂玻璃导航、奶油白画布、衬线排版与金色点缀营造尊贵感。关键特征是**半透明磨砂层**叠加在摄影背景之上，创造深度与层次。

**气质**：精致、现代、奢华、通透、优雅、高端、 curated、呼吸感。

**秘诀**：磨砂玻璃效果是此风格的灵魂——导航栏、浮动徽章、卡片叠加层都使用 `backdrop-filter: blur()` + 半透明白底。背景摄影图选择精品店室内或工匠工作场景，色调偏暖。排版上 Playfair Display 衬线字体用于标题（斜体变体增加优雅感），Inter / DM Sans 用于正文。金色（#FFD700）仅用于装饰性短线、图标和强调，绝不滥用。

## 设计 Token 系统（DNA）

### 色彩（奶油白 + 深海军 + 金色点缀）

**主调色板**：
- **Background**：`#FFFFFF`（纯白）/ `#FAF9F6`（暖白/奶油色）— 区块交替使用
- **Primary Text**：`#0F172A`（深海军蓝，近黑）
- **Secondary Text**：`#6B6B6B`（中灰）
- **Accent / Gold**：`#FFD700`（金色，用于装饰线与图标）
- **Border**：`#E2E8F0` / `#E5E5E5`（极淡灰）
- **Dark Section**：`#000000`（纯黑，用于横幅区块）
- **Glass**：`rgba(255, 255, 255, 0.7)` ~ `rgba(255, 255, 255, 0.8)`（毛玻璃层）

### 字体（衬线标题 + 无衬线正文）

- **Display / Headings**：`"Playfair Display", serif` — 用于品牌名、大标题、区块标题
- **Body / UI**：`"DM Sans", "Inter", sans-serif` — 用于导航、正文、按钮、标签
- **字重**：标题 400-700，正文 400-500，标签 500-600

### 间距与布局

- **Section Padding**：`96px 0`（桌面），`64px 0`（平板）
- **Container Max-Width**：`1280px`，居中
- **Grid Gap**：`24px` ~ `40px`
- **Hero Min-Height**：`100vh`

### 圆角

- **Buttons**：`12px`（胶囊形）
- **Cards**：`12px`
- **Inputs**：`12px`

### 阴影

- **Card Hover**：`0 8px 32px rgba(0, 0, 0, 0.08)`
- **Glass Badge**：`0 4px 24px rgba(0, 0, 0, 0.06)`

### 特效

- **Backdrop Filter**：`blur(12px)` / `blur(20px)`（毛玻璃核心）
- **Gradient Overlay**：Hero 图上的白色渐变遮罩（左到右，从实白到透明）
- **Image Gradient**：产品图底部黑色渐变遮罩（用于文字叠加）

### 动效

- **Transition**：`0.3s cubic-bezier(0.4, 0, 0.2, 1)`（标准缓动）
- **Hover**：卡片上浮 `translateY(-4px)` + 阴影加深
- **Link**：颜色渐变过渡

---

## 签名特征 (Signature Features)

1. **磨砂玻璃导航栏** — `backdrop-filter: blur(20px)` + `rgba(255,255,255,0.8)` 半透明白底，滚动时始终固定在顶部
2. **Hero 白色渐变遮罩** — 左侧从纯白渐变到透明，让衬线标题在摄影背景上清晰可读
3. **金色装饰短线** — 标签文字前的短横线（`width: 32px, height: 2px, background: #FFD700`）
4. **毛玻璃浮动徽章** — "130+ YEARS OF EXCELLENCE" 等数据卡片使用磨砂玻璃效果悬浮在图片上
5. **衬线斜体强调** — 标题中的关键词使用斜体（如 "Timeless"）增加优雅感
6. **深色对比横幅** — 纯黑背景区块与奶油白页面形成强烈视觉节奏
7. **极简图标系统** — 细线描边图标（搜索、账户、购物车、社交），保持克制
8. **购物车角标** — 金色圆形角标显示数量，是页面中唯一的鲜艳色彩点
