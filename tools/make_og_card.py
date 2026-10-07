"""Regenerate assets/img/og-card.png, the 1200x630 preview image shown when the
homepage link is shared (WeChat, Slack, X, LinkedIn, ...).

Edit the TEXT block below, then run from the repository root:

    pip install pillow
    python tools/make_og_card.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------------------------------------------------------------- TEXT
NAME = "Aocheng Luo"
LINES = [
    "Ph.D. Student, Peking University",
    "Navigation Algorithm Intern, Light Origins",
]
TAGS = ["Embodied Navigation", "VLA Models", "RL Post-training", "Legged Robots"]
URL = "luoac.github.io"
# ---------------------------------------------------------------------

OUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "og-card.png"
W, H = 1200, 630

BG = (240, 246, 252)
TEXT = (28, 41, 56)
MUTED = (85, 101, 121)
ACCENT = (45, 114, 184)
ACCENT_STRONG = (31, 92, 153)
CHIP_BORDER = (205, 220, 236)

# First font file that exists is used (Windows, macOS, Linux).
FONT_CANDIDATES = {
    "bold": ["C:/Windows/Fonts/segoeuib.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "semibold": ["C:/Windows/Fonts/seguisb.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "regular": ["C:/Windows/Fonts/segoeui.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
}


def font(weight, size):
    for path in FONT_CANDIDATES[weight]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    raise SystemExit(f"No {weight} font found; add a .ttf path to FONT_CANDIDATES.")


def blob(box, color, alpha, blur):
    layer = Image.new("RGBA", (W, H), color + (0,))
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).ellipse(box, fill=alpha)
    layer.putalpha(mask.filter(ImageFilter.GaussianBlur(blur)))
    return layer


def main():
    img = Image.new("RGBA", (W, H), BG + (255,))
    for box, color, alpha in [
        ((-250, -300, 700, 420), (143, 193, 234), 150),
        ((720, -240, 1450, 380), (186, 220, 247), 170),
        ((780, 400, 1450, 950), (205, 228, 248), 150),
    ]:
        img = Image.alpha_composite(img, blob(box, color, alpha, 110))
    img = img.convert("RGB")
    d = ImageDraw.Draw(img)

    d.rounded_rectangle((90, 178, 98, 256), radius=4, fill=ACCENT)
    d.text((124, 160), NAME, font=font("bold", 88), fill=TEXT)
    y = 282
    for line in LINES:
        d.text((128, y), line, font=font("regular", 40), fill=MUTED)
        y += 56

    chip_font = font("semibold", 26)
    x, chip_y = 128, y + 36
    for tag in TAGS:
        tw = d.textlength(tag, font=chip_font)
        d.rounded_rectangle((x, chip_y, x + tw + 36, chip_y + 48), radius=24,
                            fill=(255, 255, 255), outline=CHIP_BORDER, width=2)
        d.text((x + 18, chip_y + 24), tag, font=chip_font, fill=ACCENT_STRONG, anchor="lm")
        x += tw + 50
    if x > W - 40:
        print("Warning: tags run past the right edge; shorten or remove one.")

    d.text((128, 545), URL, font=font("semibold", 30), fill=ACCENT)
    img.save(OUT, optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
