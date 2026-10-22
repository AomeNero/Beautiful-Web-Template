# Fitness-Gym

> 来源：[uupm.cc/demo/fitness-gym](https://www.uupm.cc/demo/fitness-gym)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `fitness-gym` |
| 显示名称 | Fitness & Gym |
| 模式 |  深色模式 (Dark) |
| 字体类型 | condensed / sans-serif |
| 描述 | 活力块面式健身应用落地页，OLED 深黑背景搭配亮橙/绿色点缀，Barlow Condensed 粗体标题传递力量感，DM Sans 正文保证可读性。 |

## 设计哲学

**Vibrant & Block-based + Dark Mode (OLED)**：以近乎纯黑的 OLED 背景为画布，用高饱和亮橙色（#FF6B35）作为主行动色，绿色（#22C55E）作为成功/完成状态色。块面式布局通过大圆角卡片和明确的区块分隔组织内容，传递力量、能量与专业感。

## Token 系统

### 色彩

| Token | 值 | 用途 |
|-------|-----|------|
| `--bg` | `#0A0A0A` | 页面主背景（近黑 OLED） |
| `--bg-card` | `#141414` | 卡片/区块背景 |
| `--bg-elevated` | `#1A1A1A` | 悬浮/高亮卡片背景 |
| `--bg-feature` | `#1E1E1E` | 特性区块背景 |
| `--accent` | `#FF6B35` | 主行动色（按钮、高亮文字、图标） |
| `--accent-hover` | `#E85D2A` | 按钮悬停色 |
| `--success` | `#22C55E` | 完成/勾选状态 |
| `--text` | `#FFFFFF` | 主文字 |
| `--text-muted` | `#9CA3AF` | 次要文字/描述 |
| `--text-subtle` | `#6B7280` | 更淡的辅助文字 |
| `--border` | `#262626` | 卡片/区块边框 |
| `--border-light` | `#383838` | 高亮边框 |

### 字体

| Token | 值 | 用途 |
|-------|-----|------|
| `--font-display` | `Barlow Condensed`, sans-serif | 大标题、区块标题 |
| `--font-body` | `DM Sans`, sans-serif | 正文、导航、按钮 |
| `--font-heading` | `Space Grotesk`, sans-serif | 统计数字、特性标题 |

### 圆角

| Token | 值 |
|-------|-----|
| `--radius-sm` | `8px` |
| `--radius-base` | `12px` |
| `--radius-lg` | `16px` |
| `--radius-xl` | `20px` |
| `--radius-full` | `9999px` |

### 间距

| Token | 值 |
|-------|-----|
| `--space-xs` | `8px` |
| `--space-sm` | `16px` |
| `--space-md` | `24px` |
| `--space-lg` | `32px` |
| `--space-xl` | `48px` |
| `--space-2xl` | `64px` |
| `--space-3xl` | `80px` |

## 布局创意

### Header

固定顶部导航，半透明黑色背景 + backdrop-blur。左侧闪电 Logo + PULSEFIT 品牌名（白色+橙色），中间导航链接（大写、字间距），右侧 LOG IN 文字链接 + 橙色胶囊 CTA 按钮。

### Hero

全屏 Hero，深色健身房背景图 + 渐变遮罩。左上角"NEW: AI-POWERED TRAINING"胶囊徽章（橙色描边+绿色圆点）。超大 Barlow Condensed 标题"TRANSFORM YOUR BODY / YOUR LIFE"，"YOUR LIFE"用橙色高亮。副标题灰色。两个 CTA：橙色填充按钮 + 描边按钮。底部三列统计数据（500K+ / 1000+ / 50+）。右侧浮动"Today's Workout"卡片（深色卡片+进度条）。

### Features

"FEATURED"橙色标签 + "EVERYTHING YOU NEED"标题。4 列网格，每列：深色圆角图标容器（橙色图标）+ 粗体标题 + 灰色描述。

### Trainers

"OUR TEAM"橙色标签 + "EXPERT TRAINERS"标题。4 列训练师卡片网格，圆角图片 + 名字 + 专长标签。

### Workouts

"OUR PROGRAMS"标签 + "POPULAR WORKOUTS"标题。分类标签栏 + 3 列训练卡片网格，每张卡片含图片、分类标签、标题、时长/难度/卡路里信息。

### Pricing

"PRICING PLANS"标签 + "CHOOSE YOUR PLAN"标题。3 列定价卡片，中间"Pro"卡片橙色背景高亮，含功能列表（绿色勾选）+ CTA 按钮。

### Footer

深色背景，4 列布局：品牌+描述+社交图标 | WORKOUTS 链接 | COMPANY 链接 | SUPPORT 链接。底部版权行 + 隐私/条款链接。

## 组件样式

### 按钮

- **Primary**：橙色填充 `#FF6B35`，白色文字，`border-radius: 12px`，大写加粗，hover 变暗
- **Outline**：透明背景，白色描边，白色文字，hover 填充白色
- **Ghost**：透明背景，灰色文字，hover 变亮

### 卡片

- 深色背景 `#141414` 或 `#1A1A1A`
- `border-radius: 16px`
- 边框 `1px solid #262626`
- 悬停时边框变亮

### 标签/徽章

- 小写或大写，橙色文字
- 胶囊形 `border-radius: 9999px`
- 可选描边或填充

### 图标容器

- 圆角方形 `border-radius: 12px`
- 深色背景 + 橙色图标描边

## 签名特征

1. **OLED 纯黑背景**：`#0A0A0A` 近乎纯黑，最大化对比度
2. **亮橙主色**：`#FF6B35` 高能量感，用于所有关键行动点
3. **Barlow Condensed 标题**：压缩粗体字体传递力量与运动感
4. **块面式布局**：明确的区块分隔，大圆角卡片
5. **绿色成功指示**：`#22C55E` 用于勾选、完成状态
6. **浮动 UI 卡片**：Hero 右侧的 Workout 进度卡片增加层次感
7. **大写导航**：导航链接全部大写 + 字间距，专业运动品牌感
