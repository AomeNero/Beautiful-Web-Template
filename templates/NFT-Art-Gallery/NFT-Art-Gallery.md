# NFT-Art-Gallery

> 来源：https://www.uupm.cc/demo/nft-art-gallery

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `nft-art-gallery` |
| 显示名称 | NFT Art Gallery |
| 模式 | Light（支持 Dark 切换） |
| 字体类型 | serif + sans-serif |
| 描述 | 极简画廊风格 NFT 艺术展示页面，衬线标题与无衬线正文的经典搭配，黑白灰主调，突出艺术品本身 |

## 布局创意 (Layout Ideas)

### Header

固定顶部导航栏，毛玻璃背景（`backdrop-filter: blur(10px)` + 半透明白底），底部 1px 浅色边框分隔。左侧衬线 Logo（GALERIE），中间大写间距导航链接（Exhibitions / Artists / Collections / About），右侧描边 Connect 按钮。

### Hero

全宽居中大标题区块，顶部 uppercase 小标签（"Current Exhibition"），超大衬线标题（72px，"Digital *Renaissance*"，斜体强调关键词），副标题灰色正文（max-width 672px 居中），底部双按钮（实心黑 + 描边）。

### Featured Artwork

全宽大图展示区，图片底部左侧叠加半透明白色毛玻璃卡片（backdrop-filter: blur(8px)），内含 uppercase 标签 + 衬线标题 + 灰色描述文字。

### Artists

浅灰背景（#FAFAFA）区块，居中 uppercase 标签 + 衬线大标题（"Curated *Creators*"），4 列网格艺术家卡片。每张卡片：圆形灰度头像（filter: grayscale(1)）+ 衬线姓名 + 灰色作品数。卡片有 1px 浅色边框，hover 时边框加深。

### Collection / Works

白色背景区块，左侧标签 + 标题，右侧"View All"描边按钮。4 列网格作品卡片：顶部图片 + 衬线标题 + 灰色艺术家名 + 1px 分隔线 + 价格行（uppercase "PRICE" 标签 + 粗体 ETH 价格）。

### Footer

顶部 1px 边框分隔，4 列网格：品牌列（Logo + 描述）+ 3 列链接列（Gallery / Information / Support）。底部版权行，居中灰色小字。

---

## 完整提示词 (Full Prompt)

# 设计风格：NFT-Art-Gallery

## 设计哲学

### 核心原则

此设计追求"让艺术品说话"——页面本身是极简的画框，所有视觉注意力导向作品本身。通过克制的排版、充足的留白和中性的灰白底色，消除界面噪音，让数字艺术成为唯一焦点。设计语言根植于传统画廊美学：衬线标题传递文化厚重感，无衬线正文保证可读性，uppercase 标签提供策展式的分类秩序。

### 视觉气质

**情感关键词**：
- *策展感* — 每个区块像画廊的一面墙，精心排列、留白充足
- *学术优雅* — 衬线字体 + 大写标签 + 灰度头像，传递专业与品位
- *克制现代* — 无装饰、无渐变、无阴影，纯粹的排版与网格

**此设计不是什么**：
- 不是 Web3 炫技风（无霓虹、无粒子、无 3D）
- 不是电商促销风（无红色价格标签、无倒计时、无紧迫感）
- 不是社交娱乐风（无圆角气泡、无渐变按钮、无 emoji）

### 此风格的 DNA

#### 1. 衬线 + 斜体标题
所有区块标题使用 Playfair Display 衬线字体，关键词用斜体（em）强调，形成画廊展览标题的学术感。

#### 2. Uppercase 小标签系统
每个区块顶部都有 12px、letter-spacing: 1.4px 的大写标签（"CURRENT EXHIBITION"、"FEATURED ARTISTS"、"COLLECTION"），提供策展式的分类导航。

#### 3. 灰度艺术家头像
所有艺术家头像应用 `filter: grayscale(1)`，统一为黑白肖像，消除色彩干扰，强化"人物作为创作者"而非"网红"的定位。

#### 4. 毛玻璃叠加卡片
Featured 区块的图片上叠加半透明白色毛玻璃卡片（`rgba(250,250,250,0.95)` + `backdrop-filter: blur(8px)`），在不遮挡艺术品的前提下承载文字信息。

#### 5. 1px 边框卡片系统
所有卡片（艺术家、作品）使用 1px 浅色边框（#E2E8F0），无阴影、无圆角，hover 时边框加深为 #1A1A1A，传递"画框"隐喻。

#### 6. ETH 价格行
作品卡片底部以分隔线 + 价格行展示 ETH 价格，左侧 uppercase "PRICE" 标签，右侧粗体数值，简洁而专业。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：以纯白和近白为基底，黑色文字为焦点，灰色为辅助。零彩色点缀——所有色彩来自艺术品图片本身。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `--bg` | `#FFFFFF` | 主背景色 |
| `--bg-alt` | `#FAFAFA` | 交替区块背景（Artists 区） |
| `--bg-overlay` | `rgba(250, 250, 250, 0.95)` | 毛玻璃叠加层背景 |
| `--foreground` | `#0F172A` | 主文字色、主按钮背景 |
| `--foreground-secondary` | `#1A1A1A` | 次要文字、hover 边框 |
| `--muted` | `#666666` | 副标题、描述文字、链接 |
| `--muted-light` | `#999999` | 禁用态文字 |
| `--border` | `#E2E8F0` | 卡片边框、分隔线 |
| `--border-strong` | `#1A1A1A` | hover 边框、按钮边框 |

**签名渐变**：无——此风格刻意避免渐变，保持中性画布。

### 字体系统

**字体配对**：
- **展示字体**：`Playfair Display` — 衬线 serif，用于所有标题和 Logo，传递画廊的学术与经典气质
- **UI/正文字体**：`DM Sans` — 几何无衬线，用于正文、导航、标签、按钮，保证现代可读性

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 72px | Playfair Display | 600 | normal | 关键词用斜体 |
| 区块标题 | 36px | Playfair Display | 600 | normal | 关键词用斜体 |
| 卡片标题 | 24px | Playfair Display | 600 | normal | — |
| 艺术家名 | 18px | Playfair Display | 600 | normal | — |
| 正文/副标题 | 16-18px | DM Sans | 400 | normal | 行高 1.6 |
| 导航链接 | 14px | DM Sans | 500 | 1px | uppercase |
| 标签 | 12px | DM Sans | 500 | 1.4px | uppercase |
| 价格标签 | 12px | DM Sans | 400 | 1px | uppercase |
| 价格数值 | 18px | DM Sans | 600 | normal | 粗体 |

### 间距与布局

- **区块间距**：垂直内边距 80px-128px，Hero 顶部 128px，其余区块 80px
- **容器宽度**：max-width 1280px，水平 padding 32px
- **网格间隙**：24px-32px（卡片网格 32px gap）
- **非对称模式**：无——严格对称居中布局

**常见间距值**：4px / 8px / 12px / 16px / 24px / 32px / 48px / 64px / 80px / 128px

### 边框、表面与阴影

**圆角策略**：零圆角——所有元素使用直角（0px），仅头像使用全圆（9999px）。传递"画框"的硬边美学。

**边框**：统一 1px solid，默认 #E2E8F0，hover 加深为 #1A1A1A。按钮边框与背景同色。

**阴影系统**：无阴影——所有层级通过边框和背景色区分，保持平面感。

**纹理与图案**：无——纯色彩表面。

---

## 组件样式与交互

### 按钮

**主按钮**：
- 背景：#0F172A（黑色）
- 文字：白色
- 边框：1px solid #0F172A
- 圆角：0px
- padding：14px 28px
- 字体：DM Sans 14px 600，uppercase，letter-spacing 1px
- 悬停：背景变为 #1A1A1A

**描边按钮**：
- 背景：透明
- 文字：#0F172A
- 边框：1px solid #1A1A1A
- 悬停：背景变黑、文字变白

**禁用按钮**：
- 背景：#E2E8F0，文字 #999999，opacity 0.5，cursor not-allowed

### 卡片

- 背景：白色（或 --bg）
- 边框：1px solid #E2E8F0
- 圆角：0px
- 悬停：边框变为 #1A1A1A
- 无阴影、无过渡动画（仅边框颜色过渡 0.25s）

### 导航

- Logo：Playfair Display 20px 700，letter-spacing 1px
- 链接：DM Sans 14px 500，uppercase，letter-spacing 1px，颜色 #666666
- 悬停：颜色变为 #0F172A
- 毛玻璃背景：rgba(250,250,250,0.95) + backdrop-filter blur(10px)

### 标签/徽章

- 字体：DM Sans 12px 500，uppercase，letter-spacing 1.4px
- 颜色：#666666
- 无背景、无边框，纯文字标签

### 输入框

（此页面未展示输入框组件，参考风格应为：1px #E2E8F0 边框，0px 圆角，聚焦时边框变 #1A1A1A）

---

## "大胆要素"（签名元素）

1. **零圆角画框美学**：所有卡片、按钮、图片容器均使用 0px 圆角，仅头像为圆形。这种"硬边"设计传递传统画框的仪式感，与常见 Web3 模板的大圆角形成鲜明对比。

2. **灰度头像统一**：所有艺术家头像强制 `filter: grayscale(1)`，消除个人照片的色彩差异，统一为黑白肖像画风格，强化"创作者"而非"网红"的定位。

3. **斜体关键词强调**：标题中的关键词使用斜体（`<em>`）而非加粗或变色，如 "Digital *Renaissance*"、"Curated *Creators*"、"Available *Works*"，传递学术出版物的排版品味。

4. **毛玻璃信息叠加**：Featured 区块在艺术品图片上叠加半透明白色毛玻璃卡片，而非传统的底部文字条或侧边栏，在不遮挡作品的前提下优雅地承载策展信息。

5. **ETH 价格行设计**：作品卡片底部以 1px 分隔线 + "PRICE" uppercase 标签 + 粗体 ETH 数值的组合展示价格，简洁专业，避免电商式的红色价格标签。

6. **纯黑白灰色彩纪律**：整个页面无任何彩色点缀（按钮、边框、文字均为黑白灰），所有色彩来自艺术品图片本身。页面是画布，作品是色彩。

---

## 效果与动画

**运动哲学**：极简克制——仅使用入场淡入上移（8px 位移，0.6s ease），无持续动画、无悬停缩放、无粒子效果。

**过渡默认**：
- 标准：`0.25s ease`（边框颜色、背景色）
- 入场：`0.6s ease`（opacity 0→1 + translateY 8px→0）
- 悬停：边框颜色过渡 0.25s

**关键帧动画**：无——此风格完全静态，依靠排版和布局传递美感。

**毛玻璃效果**：
```css
background: rgba(250, 250, 250, 0.95);
backdrop-filter: blur(8px);
-webkit-backdrop-filter: blur(8px);
```

---

## 响应式策略

**断点哲学**：从 4 列网格逐步降级为 2 列（1024px）和 1 列（768px），标题字号同步缩小。

- **导航栏**：768px 以下隐藏导航链接，仅保留 Logo 和 Connect 按钮
- **艺术家网格**：4 列 → 2 列（1024px）→ 1 列（768px）
- **作品网格**：4 列 → 2 列（1024px）→ 1 列（768px）
- **Footer 网格**：4 列 → 2 列（1024px）→ 1 列（768px）
- **Hero 标题**：72px → 48px（1024px）→ 36px（768px）
- **Featured 叠加卡片**：桌面端绝对定位在图片左下角，移动端改为相对定位在图片下方

**关键适配**：
- 标题尺寸：72px → 48px → 36px
- 区块间距：128px/80px → 64px/48px
- Collection 头部：flex 行布局 → 列布局（768px）

---

## 可访问性与最佳实践

**色彩对比**：主文字 #0F172A on #FFFFFF 对比度 > 15:1（AAA），副文字 #666666 on #FFFFFF 对比度 ~5.7:1（AA）。

**聚焦状态**：按钮和链接使用浏览器默认焦点环，建议自定义为 2px outline。

**触控目标**：按钮最小 44px 高度，导航链接有充足 padding。

**运动**：`prefers-reduced-motion: reduce` 时禁用所有过渡和动画，直接显示最终状态。

---

## 实现说明

- **组件结构**：单文件 HTML，零构建依赖，纯 CSS + 少量 JS（主题切换 + IntersectionObserver 入场动画）
- **CSS 自定义属性**：完整 Token 系统在 `:root` 中定义，Dark 模式通过 `html[data-theme="dark"]` 覆盖
- **字体加载**：Google Fonts CDN，Playfair Display（400-700 + italic）+ DM Sans（400-700）
- **图片资源**：Unsplash CDN，艺术家头像加 `filter: grayscale(1)`
- **动画库**：无——仅使用 CSS transitions + IntersectionObserver
