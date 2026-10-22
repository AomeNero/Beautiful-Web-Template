# Gaming Platform

> 来源：[uupm.cc - Gaming Platform Demo](https://www.uupm.cc/demo/gaming-platform)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `gaming-platform` |
| 显示名称 | Gaming Platform |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | display / sans-serif |
| 描述 | 3D 超写实 + 复古未来主义游戏美学。深色虚空背景配霓虹绿/品红/青色点缀，网格纹理，粗体块状标题字体，发光按钮与卡片。 |

## 布局创意 (Layout Ideas)

### Header / Nav

固定顶部导航栏，半透明深色背景 + 毛玻璃模糊效果。左侧 Logo（霓虹粉方块图标 + 粗体品牌名），中间导航链接（GAMES / STORE / COMMUNITY / SUPPORT），右侧 SIGN IN 文字链接 + 霓虹绿 CTA 按钮。底部 1px 边框分隔。

### Hero

全幅深色画布，网格背景纹理。左侧大标题 "ENTER THE NEXUS"（白色粗体 + 青色霓虹发光 "NEXUS"），副标题描述文字。两个 CTA 按钮：实心霓虹绿 "PLAY NOW FREE" + 描边青色 "WATCH TRAILER"。底部统计数据（50M+ PLAYERS / 4.8 RATING / 24/7 SERVERS）。右侧游戏截图配浮动徽章（ONLINE NOW 1.2M / NEW UPDATE v4.2.0）。

### Games Grid

四列游戏卡片网格。每张卡片：顶部游戏封面图（带渐变遮罩），底部深色卡片区域含游戏名（粗体白色）、玩家数图标 + 数量、星标评分。卡片悬停上浮效果。

### Features

居中区块标题 "BUILT FOR GAMERS"（白色 + 霓虹粉 "GAMERS"）。四列特性卡片：图标置于发光方块中（品红/青色/绿色/品红），下方粗体标题 + 描述文字。

### Community / Leaderboard

社区板块，左侧 "JOIN THE SQUAD" 标题 + 描述，右侧 Discord 风格社区卡片展示。

### Download CTA

全幅渐变背景（品红到青色）。居中 "READY TO PLAY?" 标题（白色 + 霓虹粉 "PLAY?"）。三个平台下载按钮（Windows 实心绿 / macOS 描边 / Linux 描边）。底部特性列表（Free to Play / No Credit Card / 2GB Download）。

### Footer

深色卡片背景。左侧品牌 Logo + 描述 + 社交图标（X / Discord / Twitch / YouTube）。右侧四列链接（GAMES / COMMUNITY / SUPPORT / COMPANY）。底部版权 + 法律链接。

---

## 完整提示词 (Full Prompt)

# Gaming Platform / Retro-Futurism 设计系统

## 1. 设计哲学

**核心原则**："进入未来竞技场。"美学是 3D 超写实渲染与 80 年代复古未来主义的碰撞。它捕捉电子竞技的肾上腺素与街机黄金时代的怀旧感——霓虹浸透的游戏大厅、全息 HUD 界面与脉动的数字能量。这不是极简主义；它是最大化的感官冲击。每个像素都应感觉在顶级电竞舞台的巨型 LED 屏幕上渲染，或在次世代游戏主机的启动界面上。

**气质**：激烈、电气、竞技、未来复古。大量汲取赛博朋克游戏（赛博朋克 2077、守望先锋）与街机文化（Tron、Ready Player One）的视觉语言。界面应感觉*活的*且充满能量——嗡嗡作响的霓虹灯、脉动的发光元素、动态的网格背景。它不只是网站；它是通往游戏宇宙的入口、竞技场的数字门面。

**触感体验**：
- **深色虚空**：背景不只是暗，而是深邃的宇宙黑（#0d0d1a）。在这个虚空之上，霓虹光不只是为元素上色——它*定义*它们。光源应感觉物理，投射辉光与阴影。
- **网格宇宙**：含蓄的网格线背景暗示数字空间/虚拟现实，创造深度与科技感。
- **霓虹能量**：三种霓虹色（绿 #39ff14、粉 #ff006e、青 #00ffff）不只是装饰——它们是交互的视觉反馈，引导用户注意力。

**令此难忘的视觉签名**：
- **霓虹辉光**：强烈的 box-shadow 堆叠创造发光效果，按钮与图标仿佛自身在发光。
- **网格背景**：含蓄的网格线纹理，暗示 VR 空间或数字竞技场。
- **粗体块状标题**：Russo One 字体的超大标题，字母间距紧凑，视觉冲击力极强。
- **渐变遮罩**：图片上的渐变遮罩创造深度与戏剧性。
- **浮动徽章**：悬浮在内容上的小徽章/标签，增加信息层次与科技感。
- **三色霓虹系统**：绿（主 CTA / 成功）、粉（强调 / 品牌）、青（次要 CTA / 信息）。

---

## 2. 设计 Token 系统（DNA）

### 色彩（深色模式 — 强制）

```
background:          #0d0d1a      // 深虚空黑，略带紫底
background-card:     #1a1a2e      // 卡片/区块背景，稍浅
background-muted:    #2d2d4a      // 边框/分隔线
foreground:          #ffffff      // 主要文字，纯白
foreground-muted:    #a0a0b8      // 次要文字，降低对比
accent-green:        #39ff14      // 主霓虹 - 电光绿（CTA / 成功）
accent-pink:         #ff006e      // 次霓虹 - 热品红（品牌 / 强调）
accent-cyan:         #00ffff      // 三级霓虹 - 青（次要 CTA / 信息）
border:              #2d2d4a      // 边框色
input:               #1a1a2e      // 输入框背景
ring:                #39ff14      // 聚焦环匹配点缀色
destructive:         #ff3366      // 错误/危险
```

### 字体

**字体栈**：
- **标题**：`"Russo One", sans-serif` — 粗体、块状、未来感
- **副标题/标签**：`"Chakra Petch", sans-serif` — 科技感、几何
- **正文**：`"Space Grotesk", sans-serif` — 现代、清晰、易读

**字号与样式**：
- H1：`4rem` 至 `5rem`，`font-weight: 400`（Russo One 本身很粗），`uppercase`
- H2：`2.5rem` 至 `3rem`，`font-weight: 700`
- H3：`1.25rem` 至 `1.5rem`，`font-weight: 700`，`uppercase`
- 正文：`1rem`，`font-weight: 400`，`line-height: 1.6`
- 标签/徽章：`0.75rem` 至 `0.875rem`，`font-weight: 600`，`uppercase`，`letter-spacing: 0.05em`

### 圆角与边框

```
radius.sm:       4px        // 小元素
radius.base:     8px        // 卡片默认
radius.md:       12px       // 大卡片/按钮
radius.full:     9999px     // 圆形/胶囊
```

**边框宽度**：默认 `1px`，强调用 `2px`

### 阴影与效果

**霓虹辉光（CSS 变量 Token）**：
```css
/* 绿色霓虹辉光 - 主 CTA */
--glow-green: 0 0 20px rgba(57, 255, 20, 0.4);
--glow-green-lg: 0 0 30px rgba(57, 255, 20, 0.3);

/* 粉色霓虹辉光 - 品牌强调 */
--glow-pink: 0 0 30px rgba(255, 0, 110, 0.3);

/* 青色霓虹辉光 - 次要 CTA */
--glow-cyan: 0 0 30px rgba(0, 255, 255, 0.3);

/* 绿色图标辉光 */
--glow-green-icon: 0 0 30px rgba(57, 255, 20, 0.3);
```

### 纹理与图案

1. **网格背景**（CSS 伪元素）：
```css
background-image:
  linear-gradient(rgba(45, 45, 74, 0.3) 1px, transparent 1px),
  linear-gradient(90deg, rgba(45, 45, 74, 0.3) 1px, transparent 1px);
background-size: 40px 40px;
```

2. **渐变遮罩**（图片覆盖）：
```css
background: linear-gradient(to top, #0d0d1a 0%, transparent 50%, transparent 100%);
```

3. **毛玻璃效果**（导航栏）：
```css
backdrop-filter: blur(12px);
background: rgba(13, 13, 26, 0.9);
```

---

## 3. 组件样式

### 按钮

**主 CTA（实心绿）**：
```
- 背景：accent-green (#39ff14)
- 文字：background (#0d0d1a) 深色
- 圆角：8px
- 字重：700，大写
- 悬停：glow-green 辉光阴影
- 过渡：all 200ms
```

**次要 CTA（描边青）**：
```
- 背景：透明
- 边框：2px solid accent-cyan (#00ffff)
- 文字：accent-cyan
- 圆角：8px
- 字重：700，大写
- 悬停：背景 accent-cyan/10，glow-cyan 辉光
```

**描边变体**：
```
- 边框：1px solid border (#2d2d4a)
- 背景：透明
- 文字：foreground-muted
- 悬停：边框变 accent-green，文字变 accent-green
```

### 卡片/容器

**游戏卡片**：
```
- 背景：background-card (#1a1a2e)
- 边框：1px solid border (#2d2d4a)
- 圆角：12px
- 顶部：游戏封面图（带底部渐变遮罩）
- 底部：游戏名（粗体白）、玩家数、星标评分
- 悬停：translateY(-4px)，边框变 accent-cyan
```

**特性卡片**：
```
- 背景：透明
- 图标：置于 64x64 方块中，带霓虹辉光背景
- 标题：粗体白色，大写
- 描述：foreground-muted
```

### 导航栏

```
- 位置：fixed top-0，z-index: 50
- 背景：rgba(13, 13, 26, 0.9) + backdrop-filter: blur(12px)
- 底部边框：1px solid border
- Logo：霓虹粉方块 + 粗体品牌名（白色 + 粉色 "PLAY"）
- 链接：foreground-muted，悬停变白色
- CTA 按钮：实心绿
```

### 徽章/标签

```
- 背景：background-card
- 边框：1px solid border
- 圆角：8px
- 文字：小字号，大写，accent-green 或 accent-cyan
- 内含小圆点指示器（accent-green）
```

### 统计数字

```
- 数字：2rem+，粗体，白色
- 标签：小字号，大写，foreground-muted
- 图标：accent-cyan 星标
```

---

## 4. 动画与交互

### 关键帧动画

```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes glow {
  0% { box-shadow: rgba(37, 99, 235, 0.3) 0px 0px 20px; }
  100% { box-shadow: rgba(37, 99, 235, 0.6) 0px 0px 40px; }
}

@keyframes shimmer {
  100% { transform: translate(100%); }
}
```

### 过渡效果

- 按钮悬停：`all 200ms cubic-bezier(0.4, 0, 0.2, 1)`
- 卡片悬停：`all 300ms cubic-bezier(0.4, 0, 0.2, 1)`
- 链接悬停：`color 200ms`

### 交互模式

- 按钮悬停：辉光阴影出现
- 卡片悬停：上浮 + 边框变色
- 导航链接：颜色渐变
- 徽章圆点：脉冲动画

---

## 5. 响应式断点

```
Desktop:  >= 1024px  // 四列网格，完整布局
Tablet:   >= 768px   // 两列网格，压缩间距
Mobile:   < 768px    // 单列堆叠，汉堡菜单
```

---

## 6. 签名特征总结

1. **三色霓虹系统**：绿/粉/青三色霓虹，各有明确语义
2. **网格虚空背景**：深色背景 + 含蓄网格线，创造 VR 空间感
3. **粗体块状标题**：Russo One 字体，超大尺寸，视觉冲击
4. **发光按钮**：实心绿 CTA 配霓虹辉光，悬停增强
5. **浮动徽章**：悬浮信息标签，增加科技层次
6. **渐变遮罩图片**：游戏封面配底部渐变，融入深色背景
7. **毛玻璃导航**：半透明 + 模糊，现代感
8. **特性图标辉光**：图标置于发光方块中，三种霓虹色轮换
