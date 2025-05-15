# soundcloud art generator (sc-art-gen)

project where i'm trying to generate visual cover art for soundcloud mixes

## template design elements

1. frame/border (fixed element)

   - shape: square (soundcloud recommends 1:1 aspect ration, 3000x3000px)
   - style: thin or bold frame, or a layered visual (e.g., "inner window" effect)
   - elements:

     - top/bottom text brands
     - corner embellishments or symbols (e.g., logo, date, series title)
     - optional texture (grain, paper, glitch, metallic, etc.)

2. inner image area (variable)

   - this is where different photos or abstract visuals will be swapped for different arts.
   - it could be centered, blurred, or under a semi-transparent overlay to blend it with the frame.
   - consistent visual treatments can be applied (e.g., monochrome or duotone filters).

3. typography (semi-fixed)

    - piece title (dynamic)
    - series name / dj name (static)
    - consider these to be placed in the same spot each time (e.g., bottom left corner).

4. optional accents

    - bpm range, genre icon, date stamp, emoji or symbol to hint at piece's vibe.
    - color tints that match the mood (e.g., warm reds for energetic, cold blues for hypnotic, earthy greens for jungle themes).

## aesthetic options

- minimalist: thin border, mono font, clean contrast
- retro: tape texture, serif fonts, muted palette
- clubby/high-energy: neon, grids, bold fonts
- mystical/natural: organic textures, earthy tones, hand-drawn symbols

## build process

option a: canva or photoshop (reusable layer template)

- a 3000x3000px psd or canva project
- the border, text boxes, and overlays in fixed layers
- a central placeholder layer for each piece's unique image

option b: an automation with python

- `pillow` or `opencv` in python
- definition of the frame layout in code, then images and text to be added programmatically
