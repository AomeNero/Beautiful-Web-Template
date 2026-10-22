# NFT-Web3 / NexusNFT

> 来源：https://www.uupm.cc/demo/nft-web3

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `nft-web3` |
| 显示名称 | NFT-Web3 |
| 模式 | Dark Mode |
| 字体类型 | Display + Sans-serif (Orbitron/Space Grotesk + DM Sans/Manrope) |
| 描述 | Web3/NFT 市场平台暗色美学，品红-青双色霓虹渐变，Orbitron 科幻标题，玻璃质感卡片与实时拍卖倒计时。 |

## 布局创意 (Layout Ideas)

### Hero

左右非对称双栏布局：左侧为超大标题 + 副文案 + 双按钮 CTA + 三组统计数据；右侧为一张 NFT 卡片预览（含实时出价浮动气泡 + LIVE 徽章 + 倒计时 + Place Bid 渐变按钮）。背景为深黑 #0D0D0D 叠加品红-青径向渐变光晕。

### NFT Card Grid

四列响应式网格，每张卡片含 NFT 图片、标题、创作者 @handle、价格（青色高亮 ETH 值）、心形收藏按钮。卡片背景 #1A1A1A，圆角 12px，边框 rgba(255,255,255,0.1)。

### How It Works

四步流程横向排列：Connect Wallet → Browse & Discover → Buy or Bid → Create & Sell。每步上方为圆角方形图标盒（深色背景 + 青色描边图标），下方为编号（品红）+ 标题（Orbitron 白色）+ 描述文案（灰色）。

### Featured Creators / Top Sellers

创作者头像 + 名称 + 作品数的横向滚动或网格展示，配合"Top Sellers"品红标签。

### CTA Section

全幅渐变背景（品红→青），居中"Ready to Start Your NFT Journey?"大标题（Orbitron 白色 + 品红高亮），副文案 + 双按钮（渐变 Connect Wallet + 描边 Learn More），底部 MetaMask / WalletConnect / Coinbase 钱包选项。

### Footer

深色背景，左侧 Logo + 描述 + 社交媒体图标（X/Discord/Instagram/YouTube），右侧三列链接（Marketplace / Resources / Company），底部版权行 + Privacy / Terms 链接。

---

## 完整提示词 (Full Prompt)

# 设计风格：NFT-Web3 / NexusNFT

## 设计哲学

### 核心原则

**Web3 原生视觉语言**：以深空黑为画布，品红 (#FF00FF) 与青 (#00FFFF) 双色霓虹作为核心信号色，构建去中心化、科技感、实时交易的平台气质。拒绝传统金融的保守蓝白，拥抱加密世界的霓虹脉冲。

**实时感与紧迫感**：通过 LIVE 徽章、倒计时、"New Bid +0.5 ETH" 浮动气泡等元素，营造拍卖市场的实时动态氛围。

**信息层级清晰**：在深色背景上，白色用于标题与核心信息，灰色 (#9CA3AF) 用于辅助文案，青色用于价格与数据，品红用于高亮与行动号召。

### 视觉气质

**情感关键词**：
- *霓虹脉冲* — 品红与青色的碰撞，如同加密市场的实时跳动
- *深空科技* — 近黑背景上的发光元素，暗示区块链的无垠可能
- *实时交易* — 倒计时、LIVE 徽章、出价气泡，营造市场紧迫感

**此设计不是什么**：
- 不是传统金融网站的保守蓝白配色
- 不是极简主义的克制留白
- 不是 Web2 社交平台的圆润友好

### 此风格的 DNA

#### 1. 品红-青双色霓虹渐变
出现在主按钮、标题高亮文字、CTA 背景、Logo 中。`linear-gradient(135deg, #FF00FF, #00FFFF)` 是该风格的视觉签名。

#### 2. Orbitron 科幻标题字体
用于所有大标题（Hero、区块标题、卡片标题），宽字距、全大写或首字母大写，传递未来科技感。

#### 3. 深色玻璃质感卡片
#1A1A1A 背景 + rgba(255,255,255,0.1) 边框 + 微妙阴影，在深黑画布上形成层次感。

#### 4. 实时数据徽章
LIVE 徽章（黄色圆角标签）、"New Bid" 浮动气泡、倒计时数字，强化市场实时性。

#### 5. ETH 价格青色高亮
所有加密货币价格统一使用 #00FFFF 青色，形成数据层的视觉一致性。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：深空黑画布上，品红与青双色霓虹构成核心信号系统。金色 (#FFD700) 用于紧急/限时徽章，灰色用于辅助文案层级。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `background` | `#0D0D0D` | 页面主背景，近纯黑深空 |
| `bg-card` | `#1A1A1A` | 卡片、导航栏、输入框背景 |
| `bg-elevated` | `#252525` | 悬浮层、模态框背景 |
| `foreground` | `#FFFFFF` | 主标题、正文、图标 |
| `muted` | `#9CA3AF` | 辅助文案、标签、描述 |
| `accent-magenta` | `#FF00FF` | 主强调色，标题高亮、渐变起点 |
| `accent-cyan` | `#00FFFF` | 次强调色，价格、数据、渐变终点 |
| `accent-gold` | `#FFD700` | 紧急徽章、LIVE 标签、限时提示 |
| `border` | `rgba(255,255,255,0.1)` | 卡片边框、分隔线 |
| `border-strong` | `rgba(255,255,255,0.2)` | 聚焦态、悬停态边框 |

**签名渐变**：
```css
background: linear-gradient(135deg, #FF00FF 0%, #00FFFF 100%);
/* CTA 背景渐变 */
background: linear-gradient(135deg, rgba(255,0,255,0.15) 0%, rgba(0,255,255,0.15) 100%);
```

### 字体系统

**字体配对**：
- **展示字体**：`Orbitron` — 科幻感宽字距标题，用于 Hero 大标题、区块标题、卡片标题，传递 Web3 未来感
- **UI/正文字体**：`DM Sans` / `Manrope` — 清晰易读的无衬线体，用于正文、标签、导航链接
- **等宽字体**（如有）：`Space Grotesk` — 用于价格数字、统计数据等需要等宽对齐的场景

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 64-72px | Orbitron | 700 | -0.02em | 白色主体 + 品红高亮词 |
| 区块标题 | 36-48px | Orbitron | 700 | -0.01em | 白色 + 品红高亮关键词 |
| 卡片标题 | 18-20px | Orbitron | 600 | 0 | 白色，NFT 名称 |
| 正文 | 16px | DM Sans | 400 | 0 | 灰色 #9CA3AF |
| 标签/小字 | 12-14px | DM Sans | 500 | 0.02em | 灰色或品红编号 |
| 统计数据 | 32-36px | Space Grotesk | 700 | 0 | 青色 #00FFFF |
| 价格 | 16-18px | Space Grotesk | 600 | 0 | 青色 #00FFFF |
| 导航链接 | 15px | DM Sans | 500 | 0 | 灰色，悬停变白 |

### 间距与布局

- **区块间距**：每区块垂直内边距 80px（`py-20`），区块间自然分隔
- **容器宽度**：`max-w-7xl`（1280px）居中，两侧 24px 内边距
- **网格间隙**：NFT 卡片网格 gap 24-32px，How It Works 四列 gap 48px
- **非对称模式**：Hero 区左文右图，文字区占约 55%，图片区占约 45%

**常见间距值**：8px、12px、16px、24px、32px、48px、64px、80px

### 边框、表面与阴影

**圆角策略**：
- 卡片/按钮：12px（`rounded-xl`）
- 图标盒/徽章：16px（`rounded-2xl`）
- 胶囊按钮/标签：999px（全圆角）

**边框**：1px solid rgba(255,255,255,0.1)，聚焦/悬停时 1px solid rgba(255,255,255,0.2)

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `shadow-sm` | `0 2px 4px rgba(0,0,0,0.3)` | 小卡片、徽章 |
| `shadow-md` | `0 4px 6px -1px rgba(0,0,0,0.4), 0 2px 4px -2px rgba(0,0,0,0.3)` | NFT 卡片、按钮 |
| `shadow-glow` | `0 0 20px rgba(255,0,255,0.3)` | 品红发光效果 |
| `shadow-glow-cyan` | `0 0 20px rgba(0,255,255,0.3)` | 青色发光效果 |

**纹理与图案**：Hero 背景叠加品红-青径向渐变光晕，营造深空氛围感。

---

## 组件样式与交互

### 按钮

**主按钮（渐变）**：
- 背景：`linear-gradient(135deg, #FF00FF, #00FFFF)`
- 文字：白色，DM Sans 600，15px
- 圆角：12px
- 内边距：16px 32px
- 悬停：亮度提升 + 轻微上移 translateY(-2px) + 发光阴影
- 激活：轻微下压 translateY(0)

**次/描边按钮**：
- 背景：透明
- 边框：1px solid rgba(255,255,255,0.2)
- 文字：白色
- 圆角：12px
- 悬停：边框变亮 + 背景 rgba(255,255,255,0.05)

### 卡片
- 背景：#1A1A1A
- 边框：1px solid rgba(255,255,255,0.1)
- 圆角：12px
- 内边距：16px
- 悬停：边框变亮 + 轻微上移 + 阴影加深
- NFT 图片区：圆角 8px，占卡片上部

### 输入框/搜索框
- 背景：#1A1A1A
- 边框：1px solid rgba(255,255,255,0.1)
- 圆角：12px
- 内边距：12px 16px
- 聚焦：边框变 rgba(255,255,255,0.3) + 青色外发光
- 占位符文字：#9CA3AF

### 导航
- 背景：rgba(13,13,13,0.9) + backdrop-blur-md（磨砂玻璃）
- 边框底部：1px solid rgba(255,255,255,0.1)
- Logo：渐变图标 + "NEXUS"白色 + "NFT"青色
- 链接：灰色 #9CA3AF，悬停变白
- 右侧：Search 按钮（描边）+ Connect Wallet 按钮（渐变）

### 徽章/标签
- LIVE 徽章：金色 #FFD700 背景，黑色文字，圆角 999px，小字重 600
- 限时徽章：金色文字 + 金色圆点，深色背景胶囊
- 编号标签：品红 #FF00FF，小字 12-14px

### 统计数据
- 数字：Space Grotesk 700，32-36px，青色 #00FFFF
- 标签：DM Sans 400，14px，灰色 #9CA3AF

---

## "大胆要素"（签名元素）

1. **品红-青双色霓虹渐变**：贯穿按钮、标题高亮、CTA 背景、Logo 的核心视觉签名，`linear-gradient(135deg, #FF00FF, #00FFFF)` 定义了整个平台的 Web3 身份。

2. **Orbitron 科幻标题**：所有大标题使用 Orbitron 字体，宽字距、强字重，在深色背景上形成强烈的科技感视觉冲击，与 DM Sans 正文形成鲜明对比。

3. **实时拍卖 UI 元素**：LIVE 金色徽章、"New Bid +0.5 ETH" 浮动气泡、倒计时 "05:23:45"，这些动态元素让静态页面充满市场交易的紧迫感。

4. **ETH 价格青色统一**：所有加密货币价格（1.2 ETH、0.8 ETH、2.5 ETH 等）统一使用 #00FFFF 青色，在深色卡片上形成清晰的数据层。

5. **磨砂玻璃导航栏**：`backdrop-blur-md` + 半透明背景，滚动时保持内容可见性的同时维持导航的视觉存在感。

6. **Hero 非对称布局 + NFT 卡片预览**：左侧文案 + 右侧实际 NFT 卡片（含图片、出价、倒计时、Place Bid 按钮），让访客一眼理解平台核心功能。

---

## 效果与动画

**运动哲学**：克制的微交互动画，强调实时感而非花哨效果。入场动画使用淡入 + 上移，悬停使用轻微位移 + 发光。

**过渡默认**：
- 标准：`all 0.2s cubic-bezier(0.4, 0, 0.2, 1)`
- 入场：`opacity 0.6s ease + translateY(20px) → 0`
- 悬停：`transform 0.2s ease + box-shadow 0.2s ease`

**持续动画**：
- `gradient`：背景位置 0% → 100% → 0%，8s 循环，用于渐变按钮/背景的流动效果
- `float`：translateY(0) → -20px → 0，3s 缓动，用于浮动气泡/装饰元素
- `glow`：box-shadow 强度变化，2s 循环，用于发光按钮/卡片
- `pulse`：opacity 1 → 0.5 → 1，用于 LIVE 徽章的脉冲效果

**关键帧动画**：
```css
@keyframes gradient {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
@keyframes glow {
  0% { box-shadow: 0 0 20px rgba(37, 99, 235, 0.3); }
  100% { box-shadow: 0 0 40px rgba(37, 99, 235, 0.6); }
}
@keyframes pulse {
  50% { opacity: 0.5; }
}
```

---

## 响应式策略

**断点哲学**：以内容优先级驱动的渐进式布局收缩。移动端优先保证核心信息（标题 + CTA）可见，逐步释放网格列数与装饰元素。

- **Hero**：桌面端左右双栏 → 平板端上下堆叠 → 移动端单栏居中
- **NFT 卡片网格**：4 列 → 2 列 → 1 列
- **How It Works**：4 列横排 → 2×2 网格 → 单列纵向
- **Footer**：4 列 → 2×2 → 单列堆叠

**关键适配**：
- 标题尺寸：72px → 48px → 36px
- 区块间距：80px → 64px → 48px
- 导航：完整链接 → 汉堡菜单
- 装饰光晕：保留 → 减弱 → 隐藏

---

## 可访问性与最佳实践

**色彩对比**：白色文字 (#FFFFFF) 在深黑背景 (#0D0D0D) 上对比度 > 18:1，远超 WCAG AAA 标准。青色 (#00FFFF) 在深色背景上对比度约 13:1，品红 (#FF00FF) 约 5.5:1（建议仅用于装饰/高亮，不用于正文）。

**聚焦状态**：输入框/按钮聚焦时显示青色外发光环 `box-shadow: 0 0 0 2px rgba(0,255,255,0.5)`。

**触控目标**：按钮最小 44×44px，导航链接间距充足。

**运动**：`prefers-reduced-motion: reduce` 时禁用所有动画，仅保留必要的过渡效果。

---

## 实现说明

- **组件结构**：纯 HTML + CSS，零构建依赖。使用 CSS 自定义属性实现主题化。
- **CSS 自定义属性**：所有颜色、字体、间距、圆角、阴影均定义为 `:root` 变量，便于主题切换。
- **字体加载**：Google Fonts CDN 加载 Orbitron (400-700)、DM Sans (400-700)、Space Grotesk (300-700)、Manrope (300-700)。
- **动画库**：纯 CSS 关键帧动画 + IntersectionObserver 入场动画，无需 JS 动画库。
- **图标**：内联 SVG 图标，零外部依赖。
