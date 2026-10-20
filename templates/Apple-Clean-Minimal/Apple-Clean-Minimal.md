# Apple Clean Minimal

> 来源：https://www.apple.com/

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `apple-clean-minimal` |
| 显示名称 | Apple Clean Minimal |
| 模式 | ️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 极致克制的极简主义，以产品为绝对主角。纯白画布、SF Pro 字体系统、负字距大标题、标志性蓝色 CTA 与磨砂玻璃导航，让每一像素都为产品叙事服务。 |

## 布局创意 (Layout Ideas)

### Hero

全宽单列居中布局。超大产品标题（SF Pro Display 600 字重，负字距 -0.374px）居顶，副标题与发布日期依次递减字号与字重，形成清晰的视觉层级。双 CTA 并排：实心蓝胶囊按钮 + 描边胶囊按钮。下方为全幅产品摄影图，无背景装饰，产品即视觉焦点。

### Promo Grid

全宽双列或三列网格，每格为独立产品推广卡片。卡片内采用"标题 + 副标题 + 双链接"的经典三段式结构，背景色交替使用纯白与浅灰（#f5f5f7）以区分层级。卡片间无可见边框，靠背景色差异自然分隔。

### Entertainment Gallery

全宽横向滚动画廊，展示 Apple 服务生态（Apple TV+、Apple Music 等）。采用点状导航指示器，支持自动轮播与手动切换。

### Footer

五列链接网格（Shop and Learn / Account / Apple Store / For Business / Apple Values），浅灰背景（#f5f5f7），链接为深灰（#1d1d1f），无下划线，悬停变蓝。底部为版权信息与法律链接行，极小字号（12px）。

---

## 完整提示词 (Full Prompt)

# 设计风格：Apple Clean Minimal

## 设计哲学

### 核心原则

**产品即内容，内容即设计。** Apple 的设计语言根植于一种近乎偏执的克制：页面上存在的每一个元素都必须为产品展示或用户转化服务。没有装饰性图形、没有纹理叠加、没有多余的视觉噪音。白色不是"背景色"，而是"无"——它让产品照片成为唯一的视觉主角。

这种设计的根基是**编辑式极简主义**：像一本高端产品目录那样排版，用字号、字重和间距建立层级，而非用颜色或图形。

### 视觉气质

**情感关键词**：
- *克制* — 每一处留白都是有意为之的沉默，让产品自己说话
- *精准* — 像素级的对齐、数学般的间距节奏、负字距带来的紧凑张力
- *自信* — 不需要花哨的装饰来证明价值，产品本身就是最好的广告

**此设计不是什么**：
- 不是"加了白色背景的普通网站"——留白的比例、字号的阶梯、负字距的精度共同构成了一套严密的设计系统
- 不是"冷淡"——蓝色 CTA（#0071e3）在纯白画布上形成强烈的行动召唤，克制中蕴含转化力
- 不是"简单"——看似简单的背后是 SF Pro 字体系统、cubic-bezier 缓动曲线、磨砂玻璃导航等精密工程

### 此风格的 DNA

#### 1. 负字距大标题
Hero 标题使用 SF Pro Display 600 字重，letter-spacing 为 -0.374px（约 -0.02em）。这种微妙的字距收紧让大标题显得紧凑有力，是 Apple 排印的签名特征。

#### 2. 磨砂玻璃导航栏
全局导航使用 `backdrop-filter: saturate(1.8) blur(20px)` 实现 iOS 风格的毛玻璃效果，滚动时内容在导航下方模糊透出，营造层次感而不遮挡内容。

#### 3. 蓝色胶囊 CTA
主行动按钮为 #0071e3 实心填充，圆角 11px（接近胶囊形），白色文字。次按钮为同色描边。这是整个页面唯一的强色彩，所有转化路径都指向它。

#### 4. 无阴影平面卡片
Promo 卡片不使用 box-shadow，仅靠背景色差异（#ffffff vs #f5f5f7）区分层级。这种"零深度"设计让页面保持绝对的平面感与清洁度。

#### 5. 产品摄影即视觉
Hero 区域的产品图占据约 60% 视口高度，无边框、无阴影、无背景装饰。产品本身就是设计元素。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：近乎单色的灰阶体系，仅用一抹蓝色（#0071e3）作为行动召唤。色彩的存在感被压到最低，让产品照片的色彩成为页面上唯一的"彩色"。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `background` | `#ffffff` | 主背景，Hero 与内容区 |
| `background-alt` | `#f5f5f7` | 次级背景，Promo 卡片、Footer |
| `background-elevated` | `#fafafc` | 导航栏半透明底色 |
| `foreground` | `#1d1d1f` | 主文字色，标题与正文 |
| `muted` | `#6e6e73` | 次要文字，副标题、日期、说明 |
| `muted-alt` | `#333336` | 三级文字，Footer 链接 |
| `accent` | `#0071e3` | 主 CTA 按钮、链接悬停 |
| `accent-link` | `#0066cc` | 文本链接色 |
| `border` | `rgba(0,0,0,0.04)` | 极淡分隔线 |
| `border-strong` | `#1d1d1f` | 描边按钮边框 |

### 字体系统

**字体配对**：
- **展示/标题字体**：`"SF Pro Display", "Helvetica Neue", Helvetica, Arial, sans-serif` — 大字号标题专用，字重 600，负字距
- **UI/正文字体**：`"SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif` — 正文与界面文字，字重 400
- **中文回退**：`"SF Pro SC", "PingFang SC", "Microsoft YaHei", sans-serif`

> SF Pro 为 Apple 私有字体，非 Apple 环境使用 Helvetica Neue / Inter 作为替代。

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 行高 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|:------|
| Hero 标题 | 48-56px | SF Pro Display | 600 | -0.02em | 1.1 | 负字距，紧凑有力 |
| 区块标题 | 40px | SF Pro Display | 600 | normal | 1.1 | Promo 卡片标题 |
| 副标题 | 24px | SF Pro Display | 400 | normal | 1.2 | Hero 副标题 |
| 正文 | 17px | SF Pro Text | 400 | normal | 1.47 | 默认正文 |
| 说明文字 | 14px | SF Pro Text | 400 | normal | 1.43 | 日期、标签 |
| 法律文字 | 12px | SF Pro Text | 400 | -0.01em | 1.33 | Footer、免责声明 |
| 导航链接 | 12px | SF Pro Text | 400 | normal | 1.33 | 全局导航 |

**字重分布**：
- 600（Semibold）：标题、CTA 按钮文字
- 400（Regular）：正文、导航、说明
- 300（Light）：极少使用，仅用于特殊展示

### 间距与布局

- **区块间距**：Hero 区 580px 内容高度；Promo 区间 12px 水平间距；Footer 顶部 37px 内边距
- **容器宽度**：内容区 max-width 980px；Hero 与 Promo 全宽（max-width 2560px）
- **垂直节奏**：区块内边距 40px 22px 84px（上-左右-下），营造呼吸感

**常见间距值**：
- 元素间距：8px、14px、22px
- 区块内边距：40px（上）、84px（下）
- 导航高度：44px

### 边框、表面与阴影

**圆角策略**：
- **按钮**：11px（接近胶囊形，高度约 22px 时接近完美胶囊）
- **卡片**：8px（Promo 卡片顶部/底部独立圆角）
- **输入框**：8px

**边框**：
- 默认：无可见边框（靠背景色区分）
- 描边按钮：1px solid #1d1d1f
- 分隔线：rgba(0,0,0,0.04) 极淡

**阴影系统**：
- **无阴影**。这是 Apple 风格的核心特征之一。所有层级通过背景色差异而非阴影实现。

**纹理与图案**：无。纯平面。

---

## 组件样式与交互

### 按钮

**主按钮（实心蓝）**：
- 背景：`#0071e3`
- 文字：白色，SF Pro Text 400，14-17px
- 圆角：11px
- 内边距：约 8px 16px
- 悬停：`#0077ed`（略亮）
- 按下：`#0068d4`（略暗）
- 过渡：`background-color 0.24s cubic-bezier(0.4, 0, 0.6, 1)`

**次按钮（描边）**：
- 背景：透明
- 边框：1px solid #1d1d1f（或 #0071e3 用于蓝色变体）
- 文字：#1d1d1f（或 #0071e3）
- 圆角：11px
- 悬停：背景变为 #1d1d1f，文字变白（或蓝色变体）

**文本链接**：
- 颜色：#0066cc
- 悬停：下划线
- 字重：400

### 导航

- 高度：44px
- 背景：`rgba(250, 250, 252, 0.8)` + `backdrop-filter: saturate(1.8) blur(20px)`
- 链接：12px，#1d1d1f，悬停变 #0071e3
- Logo：Apple 图标，16x16px
- 右侧：搜索图标 + 购物袋图标

### 卡片（Promo）

- 背景：#ffffff 或 #f5f5f7（交替）
- 圆角：8px（顶部卡片）或 0（底部卡片，与下一张衔接）
- 内边距：50px 20px 60px
- 无阴影、无边框
- 内容：标题（40px/600）+ 副标题（24px/400）+ 双链接（蓝色文本链接）

### 输入框

- 背景：#ffffff
- 边框：1px solid rgba(0,0,0,0.1)
- 圆角：8px
- 高度：约 36px
- 聚焦：边框变 #0071e3，outline 2px solid rgba(0,113,227,0.3)
- 文字：17px，#1d1d1f

---

## "大胆要素"（签名元素）

1. **负字距标题**：letter-spacing: -0.02em（约 -0.374px @ 48px），让大标题紧凑有力，这是 Apple 排印的 DNA。

2. **磨砂玻璃导航**：`backdrop-filter: saturate(1.8) blur(20px)`，iOS 标志性效果移植到 Web，滚动时内容在导航下方模糊透出。

3. **零阴影设计**：整个页面无 box-shadow，层级完全靠背景色差异（#fff vs #f5f5f7）实现，极致的平面美学。

4. **单一行动色**：全页仅 #0071e3 一处强色彩，所有转化路径（按钮、链接悬停）都指向它，形成强烈的视觉引导。

5. **产品摄影即视觉**：Hero 区产品图占 60%+ 视口，无边框无装饰，产品本身就是设计元素。

6. **cubic-bezier(0.4, 0, 0.6, 1) 缓动**：Apple 签名缓动曲线，用于所有过渡动画，自然减速，不弹跳不机械。

7. **44px 导航高度**：精确的导航栏高度，与 iOS 状态栏 + 导航栏的视觉比例一致，形成跨平台的设计连贯性。

---

## 效果与动画

**运动哲学**：克制、流畅、自然。动画服务于内容揭示而非装饰。所有过渡使用 Apple 签名缓动曲线 `cubic-bezier(0.4, 0, 0.6, 1)`。

**过渡默认**：
- 标准：`all 0.24s cubic-bezier(0.4, 0, 0.6, 1)`
- 颜色过渡：`color 0.32s cubic-bezier(0.4, 0, 0.6, 1)`
- 入场：`opacity 0.32s 0.08s, transform 0.32s 0.08s`（带延迟的淡入上移）

**关键帧动画**：

```css
/* 导航下拉菜单滑入 */
@keyframes flyout-slide-forward {
  0% { opacity: 0; transform: translate(8px); }
  100% { opacity: 1; transform: translate(0px); }
}

/* 淡入 */
@keyframes fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

/* 搜索框滑入 */
@keyframes search-fade-and-slide {
  0% { opacity: 0; transform: translateY(-20px); }
  100% { opacity: 1; transform: translateY(0px); }
}
```

**轮播指示器动画**：
- 点状指示器展开：`dotnav-timed-dot-expand`（8px → 32px 宽度变化）
- 切换滑动：`dotnav-shift-start/end`（8px/16px/24px 位移）

---

## 响应式策略

**断点哲学**：移动优先，内容堆叠。Apple 的响应式策略是"内容不变，布局重排"——所有信息在移动端完整保留，仅改变排列方式。

- **Hero**：桌面端标题 48-56px → 移动端 32-40px；产品图从全幅变为裁切适配
- **Promo Grid**：桌面端双列/三列 → 平板双列 → 移动端单列堆叠
- **Footer**：桌面端五列 → 移动端手风琴折叠或单列
- **导航**：桌面端水平链接 → 移动端汉堡菜单 + 全屏下拉

**关键适配**：
- 标题字号：桌面 48-56px → 移动 32px
- 区块内边距：桌面 84px → 移动 40px
- 容器宽度：桌面 980px → 移动 100%（16px 左右内边距）

---

## 可访问性与最佳实践

**色彩对比**：
- 主文字 #1d1d1f 对 #ffffff：15.4:1（远超 WCAG AAA）
- 次要文字 #6e6e73 对 #ffffff：4.6:1（达 WCAG AA）
- 蓝色 #0071e3 对 #ffffff：4.5:1（达 WCAG AA）

**聚焦状态**：
- `outline: 2px solid #0071e3; outline-offset: 1px;`
- 或使用 `box-shadow: 0 0 0 3px rgba(0,113,227,0.3);`

**触控目标**：
- 最小 44x44px（与导航高度一致）
- 按钮内边距充足，文字周围有足够点击区域

**运动**：
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 实现说明

- **字体**：SF Pro 为 Apple 私有字体。非 Apple 环境推荐 `Inter` 或 `Helvetica Neue` 作为替代。中文使用 `PingFang SC` / `Microsoft YaHei`。
- **CSS 自定义属性**：建议使用 `:root` 定义完整 Token 系统，支持主题切换。
- **磨砂玻璃导航**：需要 `backdrop-filter` 支持，Firefox 需开启布局支持。降级方案：半透明背景色 `rgba(250,250,252,0.95)`。
- **动画库**：无需外部库，纯 CSS 过渡 + 关键帧即可实现。滚动触发动画可用 IntersectionObserver。
- **图片**：产品图需高质量、透明背景或纯白背景，以融入页面。
