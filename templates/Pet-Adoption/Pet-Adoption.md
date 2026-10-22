# Pet-Adoption (FureverHome)

> Source: https://www.uupm.cc/demo/pet-adoption

## Basic Info

| Property | Value |
|----------|-------|
| Style ID | `pet-adoption` |
| Display Name | Pet-Adoption |
| Mode | Light |
| Font Type | Rounded sans-serif (Fredoka) + Clean sans-serif (DM Sans) |
| Description | Warm, friendly pet adoption platform with coral accents, rounded shapes, heart motifs, and playful Fredoka typography on a cream canvas. |

## Layout Ideas

### Navigation

Sticky top navbar with logo (heart icon + brand name) on the left, centered nav links (Find a Pet, Success Stories, Shelters, About), and right-aligned Sign In link + coral pill CTA button (Adopt Now with heart icon). Background uses semi-transparent warm cream with subtle bottom border.

### Hero

Asymmetric two-column layout. Left column: pill-shaped badge ("Find Your Perfect Companion" with paw icon), large Fredoka heading with coral-colored "Furever Home" accent, descriptive paragraph with heart emoji, search bar (rounded input + coral pill search button), category filter pills (Dogs, Cats, Rabbits, Birds with emoji icons), and statistics row (15,000+ Pets Adopted, 500+ Partner Shelters, 98% Happy Families). Right column: overlapping pet photo cards with rounded corners, heart favorite buttons, pet name/breed/age info, and a "Matched!" notification card.

### Featured Pets

Section with pill badge header, Fredoka heading with coral accent, subtitle text, and a 3-column grid of pet cards. Each card has a large rounded photo, pet name, breed, and heart icon. A "View All Pets" outline button centered below.

### Success Stories

Similar section structure with "Happy Tails" heading, 3-column testimonial/story cards with large pet photos, names, breeds, and heart icons.

### Shelters

Section showcasing partner shelters with card-based layout on alternate background color.

### Final CTA

Full-width dark navy (#3D405B) section with paw print decoration, large white Fredoka heading "Ready to Change a Life?", descriptive text, two CTA buttons (coral pill + outline), and checkmark feature list (Free adoption support, Verified shelters, Post-adoption resources).

### Footer

Multi-column footer with brand info (heart logo + description + social icons), and link columns (Adopt, Resources, Company, For Shelters). Bottom bar with copyright and legal links.

---

## Full Prompt

# Design Style: Pet-Adoption (FureverHome)

## Design Philosophy

### Core Principles

This design embodies warmth, approachability, and emotional connection. It rejects cold corporate minimalism in favor of a friendly, homey aesthetic that makes pet adoption feel inviting and joyful. The design language is rooted in rounded softness, warm earth tones, and playful touches that evoke the feeling of a loving home. Every element -- from the heart icons to the rounded cards -- reinforces the emotional bond between pets and their future families.

### Visual Mood and Personality

**Emotional Keywords**:
- *Warmth* -- The cream background and coral accents create a cozy, welcoming atmosphere like stepping into a sunlit living room.
- *Playfulness* -- Fredoka's rounded letterforms, emoji icons, and heart motifs inject joy and lightheartedness.
- *Trust* -- The sage green accents and clean layout convey reliability and care, essential for an adoption platform.

**This design is NOT**:
- Cold, corporate, or sterile
- Dark or moody
- Geometric or angular
- Minimalist to the point of austerity

### This Style's DNA

#### 1. Coral Heart Motif
Heart icons appear throughout -- in the logo, CTA buttons, pet cards, and statistics. They serve as the emotional anchor of the design, reinforcing the love-centered mission.

#### 2. Rounded Everything
Every UI element uses generous border-radius: cards at 16-24px, buttons as full pills (50px+), search inputs with soft curves. Nothing has sharp corners, creating a soft, approachable feel.

#### 3. Fredoka Rounded Display Typography
The Fredoka font family for headings gives the design its playful, friendly character. Its rounded terminals and generous proportions feel warm and approachable rather than corporate.

#### 4. Warm Cream Canvas
The background uses warm cream tones (#FDF8F4, #FFF5EE) rather than pure white, creating a cozy, paper-like warmth that feels like home.

#### 5. Pet Photography as Hero Content
Large, high-quality pet photos are the visual stars of the design, placed prominently in cards and the hero section with rounded corners and subtle shadows.

#### 6. Dual-Tone CTA Strategy
Coral (#E07A5F) for primary actions and sage green (#81B29A) for secondary/trust elements create a balanced, nature-inspired palette that feels both energetic and calming.

---

## Design Token System (DNA)

### Color Strategy

**Color Focus**: A warm, nature-inspired palette centered on coral as the primary action color, sage green as the trust/secondary color, and warm cream as the canvas. The dark navy section provides dramatic contrast for the final CTA.

| Token | Value | Usage & Context |
|:------|:------|:----------------|
| `background` | `#FDF8F4` | Primary page background, warm cream |
| `background-alt` | `#FFF5EE` | Secondary/section background, lighter cream |
| `background-dark` | `#3D405B` | CTA section background, deep navy |
| `foreground` | `#0F172A` | Primary text, headings |
| `foreground-secondary` | `#3D405B` | Secondary text, nav links |
| `muted` | `#6B6E8A` | Muted text, descriptions |
| `muted-light` | `#9A9CB8` | Light muted text |
| `accent` | `#E07A5F` | Primary accent, coral/salmon for CTAs and highlights |
| `accent-hover` | `#C96A50` | Coral hover state |
| `accent-soft` | `rgba(224, 122, 95, 0.1)` | Soft coral background for badges/pills |
| `accent-green` | `#81B29A` | Secondary accent, sage green for trust elements |
| `accent-green-soft` | `rgba(129, 178, 154, 0.1)` | Soft sage background |
| `accent-yellow` | `#F2CC8F` | Tertiary accent, warm yellow for highlights |
| `border` | `#E2E8F0` | Default border color |
| `border-warm` | `#F0E6DE` | Warm border for cards |
| `white` | `#FFFFFF` | Card backgrounds, overlays |

**Signature Gradient**:
```css
background: linear-gradient(135deg, #E07A5F 0%, #E8917A 100%);
background: linear-gradient(135deg, #E07A5F 0%, #F4A261 100%);
```

### Typography System

**Font Pairing**:
- **Display Font**: `Fredoka` -- Rounded, playful headings that convey warmth and friendliness. Used for all major headings and the brand name.
- **UI/Body Font**: `DM Sans` -- Clean, modern sans-serif for body text, navigation, and UI elements. Highly legible and professional.
- **Fallback**: `Nunito Sans` -- Similar rounded character as an alternative body font.

**Type Scale & Usage**:

| Element | Size | Font | Weight | Letter-spacing | Notes |
|:--------|:-----|:-----|:-------|:---------------|:------|
| Hero Title | 56-64px | Fredoka | 600 | -0.02em | Large, impactful, with coral accent words |
| Section Title | 36-42px | Fredoka | 600 | -0.01em | Centered, with coral accent |
| Card Title | 20-22px | DM Sans | 600 | 0 | Pet names, shelter names |
| Body | 16px | DM Sans | 400 | 0 | Standard body text |
| Subtitle | 18px | DM Sans | 400 | 0 | Descriptive text under headings |
| Label/Tag | 14px | DM Sans | 500 | 0 | Category pills, badges |
| Nav Link | 15px | DM Sans | 500 | 0 | Navigation items |
| Stat Number | 36-42px | Fredoka | 700 | -0.02em | Large statistics |
| Footer Link | 14px | DM Sans | 400 | 0 | Footer navigation |

### Spacing & Layout

- **Section Spacing**: 96px vertical padding (py-24) for major sections, 64px for footer
- **Container Width**: max-w-7xl (1280px) with responsive padding (px-4 sm:px-6 lg:px-8)
- **Grid Gap**: 24-32px for card grids
- **Element Gap**: 8-16px for inline elements

**Common Spacing Values**: 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px

### Borders, Surfaces & Shadows

**Border Radius Strategy**: Generous rounding throughout. Cards use 16-24px, buttons are full pills (50px+), inputs use 12-16px.

**Borders**: 1px solid for subtle dividers, 2px solid for active/focused states. Colors range from #E2E8F0 (neutral) to #F0E6DE (warm).

**Shadow System**:

| Token | Value | Usage |
|:------|:------|:------|
| `shadow-sm` | `0 4px 12px rgba(0, 0, 0, 0.1)` | Cards, subtle elevation |
| `shadow-accent` | `0 4px 14px rgba(224, 122, 95, 0.3)` | Primary CTA buttons, coral glow |

**Textures & Patterns**: No explicit textures. The warm cream background provides subtle visual warmth without patterns.

---

## Component Styles & Interactions

### Buttons

**Primary Button (Coral Pill)**:
- Background: Coral gradient (#E07A5F to #E8917A or #F4A261)
- Text: White, DM Sans 600
- Border-radius: 50px (full pill)
- Padding: 14px 28px
- Shadow: 0 4px 14px rgba(224, 122, 95, 0.3)
- Hover: Slight lift (translateY(-1px)), deeper shadow
- Icon: Heart emoji/icon on right side

**Outline Button**:
- Background: Transparent
- Border: 2px solid coral (#E07A5F)
- Text: Coral (#E07A5F), DM Sans 600
- Border-radius: 50px
- Hover: Coral background fill, white text

**Secondary/Link Button**:
- Text only, coral or navy color
- Underline on hover

### Cards

**Pet Cards**:
- Background: White (#FFFFFF)
- Border-radius: 16-24px
- Image: Full-width top, rounded top corners
- Content: Pet name (DM Sans 600), breed/age (muted text)
- Heart icon: Top-right corner, circular white background
- Hover: Slight lift, enhanced shadow
- Shadow: 0 4px 12px rgba(0, 0, 0, 0.1)

**Story/Testimonial Cards**:
- Similar structure to pet cards
- Larger image area
- Name and breed below image

### Input Fields

**Search Bar**:
- Background: White
- Border: 1px solid #E2E8F0
- Border-radius: 12-16px
- Padding: 14px 20px
- Placeholder: Muted gray text
- Focus: Border color changes to coral
- Adjacent pill button for search action

### Navigation

- Sticky, semi-transparent warm cream background
- Logo: Heart icon in coral circle + "FureverHome" text (Fredoka 600)
- Nav links: DM Sans 500, muted color, hover to dark
- CTA button: Coral pill with heart icon
- Mobile: Hamburger menu (not shown in screenshots)

### Badges/Pills

**Category Pills**:
- Background: White with border, or coral-tinted for active
- Border-radius: 50px
- Padding: 8px 16px
- Icon + text (emoji + label)
- Active state: Coral border or background

**Section Badge**:
- Small pill with icon + text
- Background: Soft coral or sage tint
- Border-radius: 50px
- Used above section headings

### Statistics

- Large Fredoka numbers (36-42px, weight 700) in coral
- Small DM Sans labels below in muted color
- Horizontal row layout with generous spacing

---

## "Bold Elements" (Signature Features)

1. **Heart Icon System**: Hearts appear in the logo, CTA buttons, pet cards, and as decorative elements. They unify the design around the theme of love and adoption, making every interaction feel emotionally connected.

2. **Overlapping Pet Photo Cards**: In the hero section, pet photos overlap slightly with rounded corners and heart buttons, creating a dynamic, collage-like feel that showcases the pets as the stars.

3. **Emoji-Enhanced Category Pills**: Category filters (Dogs, Cats, Rabbits, Birds) use emoji icons alongside text, adding playfulness and instant visual recognition.

4. **Dark Navy CTA Contrast Section**: The final CTA section breaks the warm cream palette with a deep navy background, creating dramatic visual contrast that draws attention to the conversion point.

5. **Coral Gradient Buttons**: Primary CTAs use a subtle coral-to-peach gradient rather than flat color, adding depth and visual interest to the most important interactive elements.

6. **Statistics with Fredoka Numbers**: Large, bold Fredoka numbers for statistics (15,000+, 500+, 98%) create visual impact and build trust through social proof.

---

## Effects & Animations

**Motion Philosophy**: Gentle, friendly animations that feel warm and inviting. Nothing too fast or aggressive -- movements should feel like a pet gently approaching you.

**Default Transitions**:
- Standard: `all 0.2s ease` or `all 0.3s ease`
- Hover: Slight translateY(-2px) lift on cards and buttons
- Focus: Border color transition to coral

**Keyframe Animations**:
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes gradient {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}
```

**Decorative Animations**: Floating elements (paw prints, hearts) use gentle float animation. Background gradient blobs use slow movement.

---

## Responsive Strategy

**Breakpoint Philosophy**: Mobile-first with two major breakpoints at 768px and 1024px. Content reflows from single column to multi-column grids.

- **Hero**: Stacks to single column on mobile, two-column on desktop. Pet cards become a horizontal scroll or stacked list.
- **Pet Grid**: 1 column on mobile, 2 on tablet, 3 on desktop.
- **Footer**: Single column on mobile, multi-column on desktop.
- **Navigation**: Full links on desktop, hamburger menu on mobile.

**Key Adaptations**:
- Title sizes scale down: 56px -> 36px on mobile
- Section padding reduces: 96px -> 64px on mobile
- Statistics row wraps on mobile
- Category pills scroll horizontally on small screens

---

## Accessibility & Best Practices

**Color Contrast**: Coral (#E07A5F) on white passes AA for large text. Dark navy (#0F172A) on cream provides excellent contrast for body text. The dark navy CTA section with white text exceeds AAA requirements.

**Focus States**: All interactive elements should have visible focus rings. Coral border or outline on focus for inputs and buttons.

**Touch Targets**: All buttons and interactive elements meet minimum 44x44px touch target size.

**Motion**: Respect `prefers-reduced-motion` by disabling float animations and reducing transition durations.

---

## Implementation Notes

- **Component Structure**: Single-file HTML with inline CSS. No build dependencies.
- **CSS Custom Properties**: Full token system in :root for easy theming.
- **Font Loading**: Google Fonts -- Fredoka (400-700) and DM Sans (400-700).
- **Animations**: CSS-only with IntersectionObserver for scroll-triggered entrance animations.
- **Images**: Use placeholder images from Unsplash or similar for pet photos.
- **Icons**: Use emoji or inline SVG for heart, paw, and category icons.
