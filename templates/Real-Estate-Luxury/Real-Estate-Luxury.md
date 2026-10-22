# Real Estate Luxury

> 来源：[uupm.cc/demo/real-estate](https://www.uupm.cc/demo/real-estate)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `real-estate-luxury` |
| 显示名称 | Real Estate Luxury |
| 模式 | ️ 浅色模式 (Light) |
| 字体类型 | serif + sans-serif |
| 描述 | Glassmorphism + Minimalism 豪华房地产风格。Cinzel 衬线标题配 DM Sans 正文，金色点缀与深蓝主色。磨砂玻璃导航栏、全幅 Hero 背景图、悬浮搜索栏与统计数据。专业、高端、值得信赖的房地产品牌形象。 |

## 布局创意 (Layout Ideas)

### Header

固定顶部导航栏，白色半透明背景配 `backdrop-filter: blur(12px)` 毛玻璃效果。左侧 "LUXEESTATE" 品牌标识（LUXE 深海军蓝 + ESTATE 金色），中间导航链接（Properties, Services, Agents, About, Contact），右侧蓝色 CTA 按钮 "Schedule Viewing"。下边框 `1px solid #E2E8F0`。

### Hero

全幅背景图（现代豪华别墅 + 泳池），上方叠加暗色渐变遮罩 `linear-gradient(to right, rgba(0,0,0,0.7), rgba(0,0,0,0.5), transparent)`。左上角 "Premium Properties" 金色圆点徽章。H1 标题 "FIND YOUR"（白色）+ "DREAM HOME"（金色）使用 Cinzel 衬线字体。下方副标题白色半透明文字。底部悬浮搜索栏（白色圆角卡片，毛玻璃效果），含 Location/Property Type/Price Range 下拉选择器与蓝色搜索按钮。搜索栏下方三组统计数据（500+ Properties, $2B+ Sales Volume, 15+ Years Experience）。

### Features / Why Choose Us

白色背景区块，居中标题结构："WHY CHOOSE US"（蓝色小字大写）+ "The LuxeEstate Difference"（Cinzel 衬线标题）+ 灰色描述文字。四列特性卡片网格，每张卡片含浅蓝色圆角图标容器（`#E8F0FE`）+ 蓝色线框图标 + Cinzel 标题 + 灰色描述文字。特性：Virtual Tours, Expert Guidance, Secure Transactions, Market Insights。

### Properties Grid

浅灰背景（`#F8FAFC`）区块。居中标题 "Featured Properties" + 描述文字。三列属性卡片网格，每张卡片含属性图片（圆角顶部）、价格标签、标题、地址、卧室/浴室/面积信息。卡片白色背景、圆角、柔和阴影 `rgba(0,0,0,0.08) 0px 4px 20px`。

### Agents / Team

白色背景区块。居中标题 "Meet Our Expert Agents" + 描述文字。四列代理人卡片网格，每张卡片含圆形头像、姓名、职位、联系图标。

### Contact

双栏布局。左栏联系信息（电话、邮箱、地址）配蓝色圆角图标。右栏联系表单（姓名、邮箱、电话、消息）白色卡片配柔和阴影。蓝色 "Request Consultation" 全宽按钮。

### Footer

深海军蓝背景（`#1E293B`）。四列布局：左侧品牌标识 + 描述 + 社交图标（Facebook, Instagram, X, LinkedIn），右侧三列导航链接（Properties, Services, Company）。底部分隔线 + 版权信息 + 法律链接（Privacy Policy, Terms of Service, Cookie Policy）。

---

## 完整提示词 (Full Prompt)

# 设计风格：Real Estate Luxury / Glassmorphism Minimalism

## 设计哲学

**核心原则**：通过 Glassmorphism 毛玻璃效果与极简主义布局的融合，打造高端、专业、可信赖的豪华房地产品牌形象。设计平衡了视觉冲击力（全幅 Hero 背景图）与功能性（悬浮搜索栏、清晰的信息层级），让用户在第一眼就感受到品质与专业。

**气质**：高端、专业、可信赖、现代、精致、宽敞、明亮。

**秘诀**：使用 Cinzel 衬线字体营造奢华感，DM Sans 保证正文可读性。金色（`#FFD700`）作为点缀色用于品牌标识和关键标题，深蓝（`#0077B6`）作为主行动色。毛玻璃效果（`backdrop-filter: blur(12px)`）用于导航栏和搜索栏，创造现代感与层次感。大量留白与柔和阴影营造高端空间感。

## 设计 Token 系统（DNA）

### 色彩

**主调色板**：
- **Background**：`#FFFFFF`（纯白）— 干净、专业的基础
- **Background Alt**：`#F8FAFC`（极浅蓝灰）— 交替区块背景
- **Primary**：`#0077B6`（深蓝）— 主行动色、按钮、链接
- **Accent**：`#FFD700`（金色）— 品牌点缀、关键标题
- **Dark**：`#1E293B`（深海军蓝）— Footer 背景、深色文字
- **Text Primary**：`#0F172A`（近黑）— 主要文字
- **Text Secondary**：`#64748B`（蓝灰）— 次要文字、描述
- **Text Muted**：`#94A3B8`（浅蓝灰）— 弱化文字
- **Border**：`#E2E8F0`（浅灰蓝）— 边框、分隔线
- **Icon BG**：`#E8F0FE`（极浅蓝）— 图标背景容器
- **Glass**：`rgba(255, 255, 255, 0.9)` — 毛玻璃背景

**渐变**：
- Hero 遮罩：`linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.5) 50%, transparent 100%)`
- 金色渐变：`linear-gradient(135deg, #FFD700, #FFA500)`
- 底部遮罩：`linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 50%)`

### 字体

**字体栈**：
- **标题（Cinzel）**：`'Cinzel', serif` — 奢华衬线，用于 H1/H2 大标题
- **正文（DM Sans）**：`'DM Sans', sans-serif` — 现代无衬线，用于正文和小标题
- **辅助（Space Grotesk）**：`'Space Grotesk', sans-serif` — 几何无衬线，用于标签和数据

**字体层级**：
- **H1**：60px / 700 / 75px line-height / 1.2px letter-spacing — Cinzel
- **H2**：36px / 600 / 40px line-height / 0.72px letter-spacing — Cinzel
- **H3**：20px / 600 / 28px line-height / 0.4px letter-spacing — DM Sans
- **H4**：16px / 600 / 24px line-height / 0.32px letter-spacing — DM Sans
- **Body**：16px / 400 / 1.625 line-height — DM Sans
- **Small**：14px / 400 — DM Sans
- **Label**：12px / 500 / uppercase / 1px letter-spacing — Space Grotesk

### 间距

- **Section Padding**：`80px 0`（上下）
- **Container Max-Width**：`1280px`
- **Container Padding**：`0 24px`
- **Card Padding**：`24px`
- **Grid Gap**：`32px`
- **Element Gap**：`16px` / `24px`
- **Button Padding**：`16px 32px`

### 圆角

- **Small**：`8px` — 图标容器、小元素
- **Medium**：`12px` — 卡片、表单输入
- **Large**：`16px` — 搜索栏、大卡片
- **Full**：`9999px` — 徽章、按钮

### 阴影

- **Card Shadow**：`rgba(0, 0, 0, 0.08) 0px 4px 20px 0px`
- **Elevated Shadow**：`rgba(0, 0, 0, 0.08) 0px 8px 32px 0px`

### 毛玻璃效果

- **Nav Blur**：`backdrop-filter: blur(12px)`
- **Search Blur**：`backdrop-filter: blur(20px)`
- **Light Blur**：`backdrop-filter: blur(8px)`

### 动效

- **Transition**：`0.3s cubic-bezier(0.4, 0, 0.2, 1)` — 标准缓动
- **Hover Scale**：`transform: translateY(-4px)` — 卡片悬停上移
- **Hover Shadow**：阴影加深

## 组件样式

### 导航栏 (Header)

```
position: fixed; top: 0; width: 100%; z-index: 100;
background: rgba(255,255,255,0.9);
backdrop-filter: blur(12px);
border-bottom: 1px solid #E2E8F0;
height: 72px;
```

品牌标识：LUXE（`#0F172A`）+ ESTATE（`#FFD700`），Cinzel 字体，24px。
导航链接：`#64748B`，14px，hover 变 `#0F172A`。
CTA 按钮：`#0077B6` 背景，白色文字，圆角 8px，padding 12px 24px。

### Hero 搜索栏

```
background: rgba(255,255,255,0.95);
backdrop-filter: blur(20px);
border-radius: 16px;
box-shadow: rgba(0,0,0,0.08) 0px 8px 32px 0px;
padding: 16px 24px;
```

三列选择器 + 搜索按钮。选择器标签 12px 大写灰色，值 16px 深色。

### 属性卡片

```
background: #FFFFFF;
border-radius: 12px;
box-shadow: rgba(0,0,0,0.08) 0px 4px 20px 0px;
overflow: hidden;
transition: transform 0.3s, box-shadow 0.3s;
```

悬停：`transform: translateY(-4px)`，阴影加深。
图片区域：宽高比 4:3，圆角顶部。
内容区：padding 24px，价格（`#0077B6`，20px 粗体），标题（`#0F172A`，18px），地址（`#64748B`，14px）。

### 特性图标容器

```
width: 64px; height: 64px;
background: #E8F0FE;
border-radius: 16px;
display: flex; align-items: center; justify-content: center;
```

图标：`#0077B6`，24px 线框风格。

### Footer

```
background: #1E293B;
color: #94A3B8;
padding: 80px 24px 32px;
```

品牌标识：LUXE（白色）+ ESTATE（金色）。
链接：`#94A3B8`，hover 变白色。
社交图标：`#334155` 背景圆角方块，白色图标。

## 签名特征

1. **Cinzel 衬线标题** — 大写奢华字体，用于所有主要标题，营造高端房地产品牌形象
2. **金色点缀系统** — `#FFD700` 用于品牌标识、关键标题、徽章圆点，贯穿全站的奢华信号
3. **毛玻璃导航与搜索栏** — `backdrop-filter: blur()` 创造现代感层次，白色半透明叠加
4. **全幅 Hero 背景图** — 豪华建筑摄影配暗色渐变遮罩，最大化视觉冲击
5. **悬浮搜索栏** — 白色圆角卡片浮于 Hero 图上方，功能与美学的完美平衡
6. **柔和卡片阴影** — `rgba(0,0,0,0.08)` 极低透明度阴影，精致而不突兀
7. **深蓝行动色** — `#0077B6` 专业可信赖的蓝色，用于所有 CTA 和交互元素
8. **统计数据展示** — 大号数字 + 小写标签，建立品牌可信度
