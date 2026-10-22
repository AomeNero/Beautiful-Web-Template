# DEX-Swap

> 来源：[uupm.cc/demo/dex-swap](https://www.uupm.cc/demo/dex-swap)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `dex-swap` |
| 显示名称 | DEX-Swap |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 去中心化交易所界面，深海军蓝背景配蓝绿渐变品牌色，Space Grotesk 几何标题与 DM Sans 正文，Swap 交易卡片与特性网格布局，紫色渐变 CTA 按钮。 |

## 布局创意 (Layout Ideas)

### Hero

全屏深色画布配径向渐变环境光晕。左侧大标题"Swap Tokens Instantly"配蓝绿渐变文字，副标题描述 DEX 价值主张。底部三列统计卡片（$12B+ Volume、500K+ Users、10+ Chains），配代币标签行（ETH、USDC、WBTC、DAI、UNI、LINK +500 more）。右侧 Swap 交易卡片，含 From/To 字段（ETH→USDC）、汇率显示与紫色渐变"Connect Wallet"CTA 按钮。

### Features

"Why SwapX?" 标题配蓝绿渐变文字，3x2 网格特性卡片。每张卡片含 emoji 图标、标题与描述：Instant Swaps、Best Rates、Multi-Chain、Non-Custodial、Liquidity Pools、Governance。卡片悬停时边框变亮并上移。

### Footer

四列网格布局（移动端堆叠）。品牌信息与描述、Protocol/Governance/Community 三组导航链接、版权信息。顶部边框分隔线。

---

## 完整提示词 (Full Prompt)

# DEX-Swap / 去中心化交易所设计系统

## 1. 设计哲学

**核心原则**："去中心化金融的即时交易界面。"美学是金融科技的专业性与 Web3 的开放精神的融合。界面传达信任、效率与技术精密感——像一个高性能交易终端，但保持简洁与可访问性。

**气质**：专业、现代、可信赖。深色画布营造专注感，蓝绿渐变暗示增长与活力，紫色 CTA 提供明确的行动焦点。界面不只是信息展示；它是通往去中心化金融世界的入口。

**触感体验**：
- **深海军蓝画布**：背景是 #0d111c，不是纯黑。深邃但不过于压抑，暗示数字金融空间的深度。
- **蓝绿渐变光源**：#627eea 到 #00d395 的渐变不只装饰——它照亮品牌标识、关键文字与视觉焦点。
- **紫色行动焦点**：#627eea 到 #7b68ee 的渐变 CTA 按钮是界面的行动中心，吸引用户连接钱包。

**令此难忘的视觉签名**：
- **蓝绿渐变品牌色**：贯穿 Logo、标题文字、徽章的统一渐变色系
- **Swap 交易卡片**：深色卡片内嵌交易字段，From/To 结构清晰
- **代币标签行**：圆角胶囊标签展示支持的代币生态
- **几何标题 + 圆润正文**：Space Grotesk 标题的几何感与 DM Sans 正文的圆润形成层次
- **环境光晕**：Hero 区域中心的径向渐变光晕增加空间深度

---

## 2. 设计 Token 系统（DNA）

### 色彩（深色模式 — 强制）

```
background:          #0d111c      // 深海军蓝画布
background-alt:      #111827      // 交替区块背景
card:                #131a2a      // 卡片背景
card-hover:          #1a2236      // 卡片悬停
foreground:          #ffffff      // 主要文字，纯白
muted:               #98a1c0      // 次要文字，降低对比
accent-blue:         #627eea      // 品牌蓝（主色）
accent-green:        #00d395      // 品牌绿（增长/成功）
accent-purple:       #7b68ee      // 品牌紫（CTA）
border:              rgba(152, 161, 192, 0.2)  // 半透明边框
```

### 字体

**字体栈**：
- **标题**：`"Space Grotesk", sans-serif` — 几何、现代、科技感
- **正文**：`"DM Sans", sans-serif` — 圆润、友好、高可读性

**字号与样式**：
- H1：`clamp(2.5rem, 6vw, 4.5rem)`，`font-weight: 700`
- H2：`clamp(2rem, 4vw, 3rem)`，`font-weight: 700`
- H3：`1.25rem`，`font-weight: 600`
- 正文：`0.9375rem` 至 `1.125rem`
- 标签/徽章：`0.875rem`
- 大数字（金额）：`1.5rem` 至 `1.75rem`，`font-weight: 700`

### 圆角与边框

```
radius:     12px       // 标准圆角
radius-lg:  20px       // 大圆角（卡片）
radius-full: 9999px    // 胶囊/圆形元素
```

**边框宽度**：默认 `1px`，颜色 `rgba(152, 161, 192, 0.2)`

### 阴影与效果

**卡片阴影**：
```css
--shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -2px rgba(0, 0, 0, 0.3);
--shadow-lg: 0 20px 40px -12px rgba(0, 0, 0, 0.5);
```

**渐变**：
```css
--gradient-brand: linear-gradient(135deg, #627eea 0%, #00d395 100%);
--gradient-btn: linear-gradient(135deg, #627eea 0%, #7b68ee 100%);
```

**环境光晕**：
```css
background: radial-gradient(circle, rgba(98, 126, 234, 0.12) 0%, transparent 70%);
```

### 纹理与图案

1. **径向光晕**（Hero 区域中心）：蓝紫色径向渐变，增加空间深度
2. **毛玻璃导航**：`backdrop-filter: blur(20px)` + 半透明背景

---

## 3. 组件样式

### 按钮

**渐变 CTA 按钮**（Connect Wallet）：
```
- 背景：linear-gradient(135deg, #627eea, #7b68ee)
- 文字：#ffffff
- 字体：Space Grotesk, 600, 1rem
- 圆角：12px
- 悬停：filter: brightness(1.1) + translateY(-1px) + 蓝色辉光阴影
```

**描边按钮**（导航 CTA）：
```
- 背景：透明
- 边框：1px solid rgba(152, 161, 192, 0.3)
- 文字：#ffffff
- 悬停：background: rgba(255,255,255,0.05) + 边框变亮
```

### 卡片/容器

**统计卡片**：
```
- 背景：#131a2a
- 边框：1px solid rgba(152, 161, 192, 0.2)
- 圆角：20px
- 内边距：24px
- 文字居中
```

**Swap 交易卡片**：
```
- 背景：#131a2a
- 边框：1px solid rgba(152, 161, 192, 0.2)
- 圆角：20px
- 内边距：32px
- 阴影：0 20px 40px -12px rgba(0,0,0,0.5)
```

**特性卡片**：
```
- 背景：#131a2a
- 边框：1px solid rgba(152, 161, 192, 0.2)
- 圆角：20px
- 内边距：32px
- 悬停：边框变亮 + 背景变浅 + translateY(-2px)
```

### 徽章/标签

**状态徽章**（Decentralized Exchange）：
```
- 边框：1px solid rgba(152, 161, 192, 0.3)
- 圆角：9999px（胶囊）
- 文字：#00d395（绿色）
- 含脉动绿点动画
```

**代币标签**：
```
- 背景：#131a2a
- 边框：1px solid rgba(152, 161, 192, 0.2)
- 圆角：9999px（胶囊）
- 含蓝色小圆点 + 代币名称
```

### 输入框（Swap 字段）

```
- 背景：#0d111c（比卡片更深）
- 圆角：12px
- 内边距：16px
- 金额文字：Space Grotesk, 1.75rem, 700, 白色
- 右侧代币选择器：深色背景 + 边框 + 圆角胶囊
```

---

## 4. 布局策略

**最大宽度**：`1280px`，两侧 `32px` 内边距

**网格模式**：
- Hero：`1.2fr 1fr` 桌面端双栏（文字 + Swap 卡片）
- Stats：`repeat(3, 1fr)` 三列
- Features：`repeat(3, 1fr)` 3x2 网格
- Footer：`2fr 1fr 1fr 1fr` 四列

**间距**：区块 `96px` 垂直内边距。 generous 组件间距（24px gap）。

---

## 5. 非通用性（大胆要素）

**强制标志性选择**：

1. **蓝绿渐变品牌色**：Logo、标题文字、徽章统一使用 #627eea → #00d395 渐变
2. **Swap 交易卡片**：深色卡片内嵌完整交易界面（From/To/Rate/CTA）
3. **代币标签行**：圆角胶囊标签展示代币生态（ETH、USDC 等）
4. **紫色渐变 CTA**：Connect Wallet 按钮使用 #627eea → #7b68ee 渐变
5. **环境光晕**：Hero 区域中心径向渐变增加空间深度
6. **脉动状态点**：Decentralized Exchange 徽章含 CSS 脉动动画
7. **毛玻璃导航**：固定导航配 backdrop-filter blur

---

## 6. 效果与动画

**运动质感**：平滑、专业、微妙。

**过渡**：
```css
transition: all 200ms ease;
```

**关键帧动画**：
```css
/* 脉动状态点 */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}
```

**悬停效果**：
- 特性卡片：translateY(-2px) + 边框变亮
- CTA 按钮：brightness(1.1) + translateY(-1px) + 辉光阴影
- 代币选择器：边框变亮

---

## 7. 图标

**风格**：emoji 图标用于特性卡片（⚡、、🔗、🔒、、📦）。SVG 图标用于导航（设置齿轮、切换箭头、下拉箭头）。品牌图标为菱形几何图形配蓝绿渐变背景。

---

## 8. 响应式策略

**移动端适配**（移动优先方法）：

**布局变化**：
- Hero：单栏堆叠（文字在上，Swap 卡片在下）
- Stats：单列堆叠
- Features：单列 → 2 列（md+）→ 3 列（lg+）
- Footer：单列堆叠 → 2 列（md+）→ 4 列（lg+）
- 导航：< lg 隐藏链接，显示汉堡菜单

**保持元素**：
- 深色配色方案
- 蓝绿渐变品牌色
- 渐变 CTA 按钮
- 毛玻璃导航
- 圆角卡片风格

---

## 9. 可访问性

**对比**：白色文字于深海军蓝背景确保高对比度。渐变文字因字号大（clamp 2.5rem+）可接受。

**聚焦状态**：
```css
focus-visible: outline: 2px solid #627eea; outline-offset: 3px;
```

**减少运动**：尊重 `prefers-reduced-motion` — 禁用脉动动画与悬停过渡。

---

## 10. 实现说明

- 单文件零构建，所有 CSS 内联
- 环境光晕用 CSS 伪元素径向渐变实现，非图片
- 渐变文字用 `-webkit-background-clip: text` 实现
- 毛玻璃导航用 `backdrop-filter: blur(20px)` 实现
- 字体从 Google Fonts 加载（Space Grotesk + DM Sans）
- emoji 图标直接使用 Unicode 字符，无需外部资源
