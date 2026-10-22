# Travel-Tourism

> Source: https://www.uupm.cc/demo/travel-tourism

## Basic Info

| Attribute | Value |
|-----------|-------|
| Style ID | `travel-tourism` |
| Display Name | Travel-Tourism |
| Mode | Light |
| Font Type | Geometric Sans-serif |
| Description | A vibrant travel agency landing page with lavender backdrop, orange CTA accents, blue highlight text, and a photo collage hero. Clean, adventurous, and conversion-focused. |

## Layout Ideas

### Hero

Two-column asymmetric layout: left side carries headline, subtitle, search bar, and stats; right side features a 2x2 image collage with rounded corners and a floating "Next Trip" card overlapping the bottom-left image. The navbar floats as a white pill with shadow above the lavender canvas.

### Destinations

Horizontal card row with destination photos, titles, prices, and duration. Cards have rounded corners, subtle shadows, and a dropdown arrow indicator.

### Why Choose Us (Features)

Four-column icon-feature grid on white background. Each feature has a light-blue rounded-square icon container, bold title, and muted description. Section label "WHY CHOOSE US" in orange uppercase tracking.

### Testimonials

Centered heading with "TESTIMONIALS" orange label. Card-based testimonial layout with user avatars and quotes.

### CTA

Full-width lavender section with centered heading "Ready for Your Next Adventure?", dual buttons (orange primary + outlined secondary), and three trust badges with icons below.

### Footer

Dark navy (#0F172A) full-width footer with 4-column layout: brand + description + social icons on the left, three link columns (Destinations, Company, Support) on the right. Bottom bar with copyright and legal links.

---

## Full Prompt

# Design Style: Travel-Tourism

## Design Philosophy

### Core Principles

This design pursues an adventurous yet trustworthy travel brand identity. It balances vibrant energy (orange CTAs, blue accents) with calm professionalism (lavender canvas, clean typography). The layout prioritizes conversion through prominent search functionality, social proof stats, and clear CTA hierarchy. Photography is the emotional anchor -- real destination images evoke wanderlust.

### Visual Mood and Personality

**Emotional Keywords**:
- *Adventurous* -- bold orange buttons and dynamic image collage spark the desire to explore
- *Trustworthy* -- clean layout, verified stats (500+ destinations, 4.9 rating), and professional navy footer
- *Welcoming* -- soft lavender background creates a warm, approachable atmosphere

**This design is NOT**:
- Dark or moody -- it stays light and optimistic throughout
- Minimalist to the point of austerity -- it uses color, imagery, and decorative elements generously
- Corporate or sterile -- the photo collage and floating card add personality and warmth

### This Style's DNA

#### 1. Lavender Canvas
A soft purple-lavender background (#EDE9FE or similar) serves as the primary page canvas, differentiating from the typical white travel site. This creates a dreamy, aspirational mood.

#### 2. Dual Accent System
Orange (#FF7F00) for primary CTAs and action elements; Blue (#0080FF) for text highlights and icon backgrounds. The two-color accent system creates visual hierarchy without competing.

#### 3. Floating Pill Navbar
The navigation bar is a white rounded rectangle floating with shadow above the lavender background, not a full-width bar. This creates a modern, app-like feel.

#### 4. Photo Collage Hero
Instead of a single hero image, a 2x2 grid of destination photos with rounded corners creates visual richness. A floating "Next Trip" card overlaps the collage, adding depth.

#### 5. Two-Tone Headlines
Section headings split into dark text + blue accent word (e.g., "Travel with **Confidence**", "What Travelers **Say**"). This creates rhythm and draws the eye to key emotional words.

---

## Design Token System (DNA)

### Color Strategy

**Color Focus**: Light, optimistic palette with lavender as the emotional canvas. Orange drives action; blue highlights key words and icons. Dark navy grounds the footer.

| Token | Value | Usage & Context |
|:------|:------|:----------------|
| `background` | `#EDE9FE` | Primary page canvas (lavender) |
| `background-white` | `#FFFFFF` | Cards, navbar, feature sections |
| `foreground` | `#0F172A` | Primary headings, footer background |
| `foreground-body` | `#64748B` | Body text, subtitles |
| `accent-orange` | `#FF7F00` | Primary CTA buttons, section labels, logo icon |
| `accent-blue` | `#0080FF` | Highlighted headline words, icon backgrounds |
| `accent-blue-soft` | `#DBEAFE` | Icon container backgrounds |
| `muted` | `#94A3B8` | Secondary text, labels |
| `border` | `#E2E8F0` | Card borders, dividers |
| `footer-bg` | `#0F172A` | Footer background |
| `footer-text` | `#94A3B8` | Footer link text |

**Signature Gradient**:
```css
background: linear-gradient(135deg, #EDE9FE 0%, #E0D4F5 100%);
```

### Typography System

**Font Pairing**:
- **Display Font**: `Space Grotesk` -- geometric, modern, used for headlines with strong presence
- **UI/Body Font**: `DM Sans` -- clean, readable, used for body text and navigation
- **Alternative**: `Manrope` -- used for some headings, slightly more rounded geometric feel

**Type Scale & Usage**:

| Element | Size | Font | Weight | Tracking | Notes |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero Title | 56-64px | Space Grotesk | 700 | -0.02em | Two-tone: dark + blue |
| Section Title | 36-42px | Space Grotesk | 700 | -0.01em | Two-tone pattern |
| Card Title | 18-20px | Space Grotesk | 600 | 0 | Destination names |
| Body | 16px | DM Sans | 400 | 0 | Standard reading text |
| Label | 12-13px | DM Sans | 500 | 0.08em | Uppercase section labels |
| Nav Link | 15px | DM Sans | 500 | 0 | Navigation items |
| Button | 15-16px | DM Sans | 600 | 0 | CTA text |
| Stat Number | 28-32px | Space Grotesk | 700 | 0 | Hero stats |

### Spacing & Layout

- **Section Spacing**: 80-100px vertical padding between major sections
- **Container Width**: max-width 1200px, centered
- **Grid Gap**: 24-32px between cards and grid items
- **Asymmetric Pattern**: Hero uses 50/50 split with image collage taking slightly more visual weight

**Common Spacing Values**: 8px, 16px, 24px, 32px, 48px, 64px, 80px, 96px

### Borders, Surfaces & Shadows

**Border Radius Strategy**:
- Cards: 16px rounded corners
- Buttons: 12px (primary) / 999px (pill outline)
- Icon containers: 12px rounded squares
- Navbar: 16px floating pill
- Images: 16px rounded corners

**Borders**: 1px solid #E2E8F0 for subtle card separation; no borders on primary elements

**Shadow System**:

| Token | Value | Usage |
|:------|:------|:------|
| `shadow-sm` | `0 1px 3px rgba(0,0,0,0.08)` | Small cards, icons |
| `shadow-md` | `0 4px 12px rgba(0,0,0,0.1)` | Destination cards, feature cards |
| `shadow-lg` | `0 8px 30px rgba(0,0,0,0.12)` | Navbar, floating elements |

**Texture & Patterns**: None -- clean, flat surfaces with photography providing visual texture.

---

## Component Styles & Interaction

### Buttons

**Primary Button**:
- Background: #FF7F00 (orange)
- Text: #FFFFFF, 600 weight
- Border-radius: 12px
- Hover: Slight brightness increase, subtle scale-up
- Active: Slight press-down effect

**Outline Button**:
- Background: transparent
- Border: 1.5px solid #CBD5E1
- Text: #0F172A, 600 weight
- Border-radius: 12px
- Hover: Border darkens, background tints slightly

### Cards

- White background, 16px border-radius
- Subtle shadow (0 4px 12px rgba(0,0,0,0.1))
- Image on top with 16px top-radius matching card
- Content padding: 20-24px
- Hover: Slight lift (translateY -4px) with enhanced shadow

### Input Fields (Search Bar)

- Integrated into a white rounded container (16px radius)
- Fields separated by subtle dividers
- Placeholder text in #94A3B8
- Focus: Blue underline or border highlight
- Search button embedded on the right with orange background

### Navigation

- Floating white pill with shadow, 16px border-radius
- Logo: Orange tent icon + "Wanderlust" text (bold, dark)
- Links: DM Sans 500, #64748B, hover to #0F172A
- CTA button on the right end of the navbar
- Sticky on scroll

### Badges/Labels

- Section labels: uppercase, 12-13px, letter-spacing 0.08em, orange color
- Rating badge: light blue background, star icon, rounded pill
- Trust badges: icon + text, inline layout

---

## "Bold Elements" (Signature Elements)

1. **Floating Pill Navbar**: The navbar is not full-width but a floating white rounded rectangle with shadow, creating a modern app-like feel above the lavender canvas.

2. **Two-Tone Headline Pattern**: Every major heading splits into dark text + blue accent word ("Next **Adventure**", "Travel with **Confidence**", "What Travelers **Say**"), creating visual rhythm and emotional emphasis.

3. **Photo Collage with Floating Card**: The hero uses a 2x2 image grid with a floating "Next Trip" card overlapping the bottom-left, creating depth and a sense of curated discovery.

4. **Orange-Blue Dual Accent**: Orange exclusively drives action (buttons, labels), while blue exclusively highlights meaning (key words, icons). This strict separation creates clear visual hierarchy.

5. **Integrated Search Bar**: The search functionality is embedded as a prominent white rounded container within the hero, with multiple fields and an orange search button -- making trip planning feel immediate and accessible.

---

## Effects & Animations

**Motion Philosophy**: Smooth, gentle transitions that feel premium but not flashy. Elements fade and slide up on scroll entry.

**Transition Defaults**:
- Standard: `all 0.3s ease`
- Entry: Fade-in + translateY(20px) to translateY(0), staggered by 100ms
- Hover: translateY(-4px) on cards, brightness(1.05) on buttons

**Keyframe Animations**:
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## Responsive Strategy

**Breakpoint Philosophy**: Three-tier responsive design maintaining the adventurous feel at all sizes.

- **Hero**: Desktop 2-column -> Tablet stacked -> Mobile single column with image collage below text
- **Features**: 4-column -> 2-column -> 1-column
- **Destinations**: 4-card row -> 2-card row -> horizontal scroll
- **Footer**: 4-column -> 2-column -> 1-column stacked

**Key Adaptations**:
- Hero title scales from 64px -> 42px -> 32px
- Section spacing reduces from 96px -> 64px -> 48px
- Photo collage collapses to single image on mobile
- Floating navbar becomes full-width with hamburger menu

---

## Accessibility & Best Practices

**Color Contrast**: Orange (#FF7F00) on white passes AA for large text; Blue (#0080FF) on white passes AA for all text sizes. Dark navy (#0F172A) on lavender passes AAA.

**Focus States**: Visible focus ring (2px solid #0080FF with 2px offset) on all interactive elements.

**Touch Targets**: Minimum 44x44px for all buttons and interactive elements.

**Motion**: All animations respect `prefers-reduced-motion: reduce` by disabling transitions and using instant visibility changes.

---

## Implementation Notes

- **Component Structure**: Single-file HTML with inline CSS and minimal JS. No build tools required.
- **CSS Custom Properties**: Full token system in `:root` for easy theming.
- **Font Loading**: Google Fonts CDN for Space Grotesk (300-700) and DM Sans (400-700).
- **Animation Library**: Native CSS transitions + IntersectionObserver for scroll-triggered entry animations. No external animation library needed.
- **Images**: Use Unsplash or similar for travel photography placeholders.
