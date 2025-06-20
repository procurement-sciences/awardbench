# AwardBench - Enhanced with Apple/OpenAI Design

This is the enhanced version of AwardBench with:

1. **Academic Paper Generation**: Dynamically generates LaTeX papers with figures and citations
2. **Apple/OpenAI Design Aesthetic**: Clean, minimalist interface inspired by the BrowseComp design

## Features

### 1. Academic Paper Generation

- **LaTeX Source**: Professional academic paper format with proper citations
- **PDF Export**: Compiled PDF version (requires LaTeX installation)
- **Bundle Download**: Complete package with all source files

### 2. New Design System

Based on the OpenAI BrowseComp design analysis:

- **Color Palette**:

  - Background: `#101010` (dark charcoal)
  - Text: `#EAEAEA` (off-white)
  - Accent: `#00A67E` (vibrant green)
  - Components: `#1C1C1C` (lighter gray)

- **Typography**:

  - Font: Inter (similar to SF Pro/Söhne)
  - Large headings: 72px, tight line height
  - Clean hierarchy with consistent spacing

- **Interactive Elements**:

  - Tabbed examples section with smooth transitions
  - Hover effects on all interactive elements
  - Active tab indicators with accent color
  - Subtle animations (0.2s transitions)

- **Layout**:
  - Single column, max-width 1100px
  - Generous vertical spacing (96-128px sections)
  - Minimalist card components
  - Flat design with functional focus

## Setup

### Frontend

1. Open `index-new.html` in a browser
2. The dashboard loads with sample data

### Backend (for paper generation)

```bash
pip install -r requirements.txt
python paper_api.py
```

### LaTeX Requirements

For PDF generation, install:

- TeX distribution (MacTeX, TeX Live, or MiKTeX)
- `pdflatex` command available in PATH

## API Endpoints

- `GET /api/paper/generate` - Generate paper files
- `GET /api/paper/download/<format>` - Download paper (tex/pdf/bundle)
- `GET /api/paper/status` - Check generation status

## Design Principles

Following Apple/OpenAI aesthetics:

1. **Minimalism**: Every element serves a purpose
2. **Typography First**: Strong type hierarchy drives the design
3. **Generous Space**: Dark space creates focus and premium feel
4. **Subtle Interactions**: Smooth, purposeful animations
5. **High Contrast**: Clear readability with limited color palette

## Files

- `index-new.html` - New UI with Apple/OpenAI design
- `dashboard-new.js` - Interactive functionality
- `generate_latex_paper.py` - LaTeX paper generator
- `paper_api.py` - Flask API for paper generation
- `index.html` - Original dashboard (preserved)
- `dashboard.js` - Original functionality (preserved)
