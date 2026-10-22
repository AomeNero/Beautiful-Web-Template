# DeFi-Yield

> 来源：[uupm.cc/demo/defi-yield](https://www.uupm.cc/demo/defi-yield)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `defi-yield` |
| 显示名称 | DeFi-Yield |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 赛博朋克风 DeFi 收益平台，近黑背景配青色网格纹理，霓虹青/绿/品红多色点缀，Space Grotesk 几何标题与 Space Mono 等宽标签，渐变 CTA 按钮与发光数据卡片。 |

## 布局创意 (Layout Ideas)

### Hero

全屏深色画布配青色网格背景。左侧大标题"MAXIMIZE YOUR YIELD"配霓虹青色辉光文字，副标题描述协议价值主张。双 CTA 按钮——渐变主按钮（青到品红）与描边次按钮。底部三列统计卡片（TVL、Users、Max APY），配霓虹青色数字与发光效果。右侧 APY Calculator 面板，含存款金额输入、锁仓期限选择器（4 档）、预估收益展示与连接钱包 CTA。

### Pools

2x2 网格布局的收益池卡片。每张卡片含代币图标对、池名称、奖励代币说明与风险等级徽章（低/中/高风险用绿/橙/品红区分）。APY 数值以霓虹绿色大号字体展示，TVL 以白色展示。底部全宽 Deposit 按钮配青色描边。

### Tokenomics

左右分栏布局。左侧为环形图（conic-gradient 实现）配图例列表，展示代币分配比例（流动性挖矿 40%、团队 15%、国库 20%、公募 15%、生态 10%）。右侧为代币说明文字、权益列表、价格卡片（当前价格与市场市值）与购买 CTA 按钮。

### Footer

四列网格布局（移动端堆叠）。品牌信息、Protocol/Governance/Resources 三组导航链接、版权信息与社交图标（X、Discord、Telegram）。顶部青色分隔线。

---

## 完整提示词 (Full Prompt)

# DeFi-Yield / 赛博 DeFi 设计系统

## 1. 设计哲学

**核心原则**："去中心化金融的未来界面。"美学是赛博朋克与金融科技的专业碰撞。它捕捉了区块链世界的技术精密感与去中心化金融的激进创新精神。界面应感觉像一台高性能交易终端——数据密集、实时刷新、充满能量。

**气质**：技术感、未来感、高能量。大量汲取赛博朋克视觉语言（霓虹辉光、网格背景、等宽字体）与 DeFi 产品的数据展示需求（大数字、百分比、金融指标）。界面不只是信息展示；它是通往去中心化金融世界的控制面板。

**触感体验**：
- **深色虚空**：背景是近黑色（#0a0a0f），不是纯黑。青色网格纹理暗示数字空间的无限延伸。
- **霓虹光源**：青色（#00ffff）、绿色（#39ff14）、品红（#ff00ff）不只是装饰色——它们是功能性光源，照亮关键数据点。
- **数据优先**：APY、TVL、价格等金融指标以最大字号、最强色彩呈现。数字是界面的主角。

**令此难忘的视觉签名**：
- **青色网格背景**：全页固定网格纹理，暗示数字空间/赛博空间
- **霓虹辉光文字**：关键数字与标题配多层 text-shadow 创造真实发光效果
- **渐变 CTA 按钮**：青色到品红的线性渐变，高能量视觉焦点
- **等宽标签 + 几何标题**：Space Mono 用于标签/数据，Space Grotesk 用于标题，形成技术感字体层次
- **风险等级色彩编码**：绿/橙/品红三色区分低/中/高风险

---

## 2. 设计 Token 系统（DNA）

### 色彩（深色模式 — 强制）

```
background:          #0a0a0f      // 近黑虚空，略带蓝底
background-alt:      #0d0d15      // 交替区块背景
card:                #0d0d15      // 卡片背景
foreground:          #ffffff      // 主要文字，纯白
muted:               #8b8b9a      // 次要文字，降低对比
accent-cyan:         #00ffff      // 主霓虹 - 青色（品牌色）
accent-green:        #39ff14      // 收益色 - 霓虹绿（APY/增长）
accent-magenta:      #ff00ff      // 次霓虹 - 品红
accent-pink:         #ff1493      // 三级霓虹 - 热粉
accent-orange:       #ff6600      // 风险色 - 橙色（中风险）
border:              rgba(0,255,255,0.3)  // 青色半透明边框
```

### 字体

**字体栈**：
- **标题**：`"Space Grotesk", sans-serif` — 几何、未来、科技感
- **正文/标签**：`"Space Mono", monospace` — 等宽、终端感、数据展示
- **辅助**：`"DM Sans", sans-serif` — 用于长段落正文

**字号与样式**：
- H1：`clamp(2.5rem, 7vw, 5rem)`，`font-weight: 700`，`uppercase`
- H2：`clamp(2rem, 4vw, 3rem)`，`font-weight: 700`，`uppercase`
- H3：`1.25rem` 至 `1.5rem`，`font-weight: 600-700`，`uppercase`
- 正文：`0.875rem` 至 `0.9375rem`，`font-family: "Space Mono"`
- 标签/徽章：`0.6875rem` 至 `0.75rem`，`uppercase`，`letter-spacing: 0.1em+`
- 大数字（APY/TVL）：`1.5rem` 至 `1.75rem`，`font-weight: 700`

### 圆角与边框

```
radius:     4px        // 小圆角，技术感
radius-full: 9999px    // 胶囊/圆形元素
```

**边框宽度**：默认 `1px`，强调用青色半透明 `rgba(0,255,255,0.3)`

### 阴影与效果

**霓虹辉光（CSS 变量 Token）**：
```css
--glow-cyan:    0 0 10px rgba(0, 255, 255, 0.5);
--glow-green:   0 0 10px rgba(57, 255, 20, 0.5);
--glow-magenta: 0 0 10px rgba(255, 0, 255, 0.5);
--glow-pink:    0 0 10px rgba(255, 20, 147, 0.5);
--glow-orange:  0 0 10px rgba(255, 102, 0, 0.5);
```

**渐变**：
```css
--gradient-primary: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
```

**背景纹理**：
```css
/* 青色网格 */
background-image:
  linear-gradient(rgba(0, 255, 255, 0.06) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0, 255, 255, 0.06) 1px, transparent 1px);
background-size: 60px 60px;
```

### 纹理与图案

1. **网格背景**（固定定位，全页）：青色极淡网格线，暗示赛博空间
2. **毛玻璃导航**：`backdrop-filter: blur(20px)` + 半透明背景
3. **发光数字**：APY/TVL 等关键数据配 text-shadow 辉光

---

## 3. 组件样式

### 按钮

**渐变主按钮**（CTA）：
```
- 背景：linear-gradient(135deg, #00ffff, #ff00ff)
- 文字：#0a0a0f（深色，高对比）
- 字体：Space Grotesk, 600-700, uppercase
- 圆角：4px
- 悬停：filter: brightness(1.15) + 双层辉光阴影
```

**描边按钮**（次级）：
```
- 背景：透明
- 边框：1px solid #00ffff
- 文字：#00ffff
- 悬停：background: rgba(0,255,255,0.1) + 青色辉光
```

**白色描边按钮**（ tertiary）：
```
- 边框：1px solid rgba(255,255,255,0.3)
- 文字：#ffffff
- 悬停：border-color: #ffffff
```

### 卡片/容器

**数据卡片**（统计/池/价格）：
```
- 背景：#0d0d15
- 边框：1px solid rgba(0,255,255,0.3)
- 圆角：4px
- 悬停：边框变亮 + 含蓄辉光
```

**计算器面板**：
```
- 背景：#0d0d15
- 边框：1px solid rgba(0,255,255,0.3)
- 圆角：4px
- 内边距：32px
```

### 徽章/标签

**风险徽章**：
```
- 低风险：background: rgba(57,255,20,0.15), color: #39ff14
- 中风险：background: rgba(255,102,0,0.15), color: #ff6600
- 高风险：background: rgba(255,0,255,0.15), color: #ff00ff
- 字体：Space Mono, 0.6875rem, uppercase
- 圆角：4px
```

**状态徽章**（Live on Mainnet）：
```
- 边框：1px solid rgba(0,255,255,0.3)
- 文字：#00ffff
- 含脉动绿点动画
```

### 输入框

```
- 背景：#0a0a0f（比卡片更深）
- 边框：1px solid rgba(0,255,255,0.3)
- 圆角：4px
- 文字：Space Mono, 1.25rem, 700, 白色
- 右侧货币标签：青色
```

### 锁仓期限选择器

```
- 4 列网格按钮
- 默认：透明背景，青色边框，灰色文字
- 激活态：rgba(0,255,255,0.1) 背景，青色边框与文字
- 悬停：边框变亮
```

---

## 4. 布局策略

**最大宽度**：`1280px`，两侧 `32px` 内边距

**网格模式**：
- Hero：`1.2fr 1fr` 桌面端双栏（文字 + 计算器）
- Pools：`repeat(2, 1fr)` 2x2 网格
- Tokenomics：`1fr 1fr` 双栏（图表 + 信息）
- Footer：`2fr 1fr 1fr 1fr` 四列
- Stats：`repeat(3, 1fr)` 三列

**间距**：区块 `96px` 垂直内边距。 generous 组件间距。

---

## 5. 非通用性（大胆要素）

**强制标志性选择**：

1. **青色网格背景**：全页固定网格纹理，定义赛博空间感
2. **霓虹辉光数字**：APY/TVL 等关键金融指标必须配 text-shadow 发光效果
3. **渐变 CTA**：主行动按钮必须使用青到品红渐变
4. **等宽字体层次**：标签/数据用 Space Mono，标题用 Space Grotesk
5. **风险色彩编码**：绿/橙/品红三色直观区分风险等级
6. **脉动状态点**：Live 状态徽章含 CSS 脉动动画
7. **毛玻璃导航**：固定导航配 backdrop-filter blur

---

## 6. 效果与动画

**运动质感**：快速、数字感、平滑缓动。

**过渡**：
```css
transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
```

**关键帧动画**：
```css
/* 脉动状态点 */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}
```

---

## 7. 图标

**风格**：简洁几何图标，用于社交链接与品牌标识。品牌图标为六边形/菱形几何图形配青色边框与辉光。

---

## 8. 响应式策略

**移动端适配**（移动优先方法）：

**布局变化**：
- Hero：单栏堆叠（文字在上，计算器在下）
- Pools：单列 → 2 列（md+）
- Tokenomics：单栏堆叠 → 双栏（md+）
- Footer：单列堆叠 → 4 列网格（md+）
- Stats：保持 3 列（缩小字号）
- 导航：< lg 隐藏链接，显示汉堡菜单

**保持元素**：
- 网格背景（全页）
- 霓虹辉光效果
- 渐变 CTA 按钮
- 等宽字体
- 深色配色方案
- 风险色彩编码

---

## 9. 可访问性

**对比**：霓虹青色文字于深色背景需确保足够对比度。大数字（APY）因字号大（1.5rem+）可接受略低对比度。

**聚焦状态**：
```css
focus-visible: outline: 2px solid #00ffff; outline-offset: 3px;
```

**减少运动**：尊重 `prefers-reduced-motion` — 禁用脉动动画。

---

## 10. 实现说明

- 单文件零构建，所有 CSS 内联
- 网格背景用 CSS 伪元素实现，非图片
- 环形图用 conic-gradient 实现，非 SVG/Canvas
- 霓虹辉光用多层 text-shadow/box-shadow 堆叠
- 渐变按钮用 linear-gradient + hover brightness 滤镜
- 字体从 Google Fonts 加载（Space Grotesk + Space Mono + DM Sans）
