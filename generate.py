from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# CONFIG
IMAGE_SIZE = 3000  # square cover art
FRAME_WIDTH = 100
FONT_PATH = "fonts/Anton-Regular.ttf"
OUTPUT_DIR = "out"

def create_cover(background_path, title, subtitle=None, palette="default"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load and resize background image
    bg = Image.open(background_path).convert("RGB")
    bg = bg.resize((IMAGE_SIZE, IMAGE_SIZE))

    # Apply optional filters (blur/brightness/etc)
    bg = bg.filter(ImageFilter.GaussianBlur(radius=2))

    # Create frame overlay
    frame = Image.new("RGBA", (IMAGE_SIZE, IMAGE_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)

    # Frame color
    colors = {
        "default": (255, 255, 255),
        "warm": (255, 110, 80),
        "cool": (100, 180, 255),
        "earth": (120, 90, 60)
    }
    frame_color = colors.get(palette, colors["default"])

    # Draw border (outer rectangle)
    draw.rectangle([0, 0, IMAGE_SIZE, IMAGE_SIZE], outline=frame_color, width=FRAME_WIDTH)

    # Merge background and frame
    final = Image.alpha_composite(bg.convert("RGBA"), frame)

    # Add text
    draw = ImageDraw.Draw(final)
    try:
        font_main = ImageFont.truetype(FONT_PATH, 120)
        font_sub = ImageFont.truetype(FONT_PATH, 80)
    except:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Title text (centered)
    text_x = IMAGE_SIZE // 2
    title_y = IMAGE_SIZE - 400
    bbox = font_main.getbbox(title)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    draw.text((text_x - w // 2, title_y), title, font=font_main, fill=frame_color)

    # Optional subtitle
    if subtitle:
        bbox_sub = font_sub.getbbox(subtitle)
        w2 = bbox_sub[2] - bbox_sub[0]
        h2 = bbox_sub[3] - bbox_sub[1]

        draw.text((text_x - w2 // 2, title_y + h + 20), subtitle, font=font_sub, fill=frame_color)

    # Save
    filename = f"{OUTPUT_DIR}/{title.replace(' ', '_')}.png"
    final.convert("RGB").save(filename)
    print(f"✅ Saved cover to {filename}")

# --- Example usage ---
create_cover(
    background_path="img/cat.jpg",
    title="Mystical Jungle",
    subtitle="May 2025",
    palette="earth"
)
