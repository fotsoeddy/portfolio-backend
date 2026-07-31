"""Shared helper for seed commands — not a management command itself
(leading underscore keeps Django's command loader from registering it).
"""

import textwrap
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont


def generate_placeholder(label: str, filename: str, size=(1200, 675), bg=(11, 11, 12), fg=(47, 219, 166)) -> ContentFile:
    """Simple typographic placeholder cover (no stock photography), matching
    the site's minimal dark/neutral aesthetic — used for seeded blog posts
    and projects until real artwork is uploaded."""
    image = Image.new("RGB", size, color=bg)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 54)
    except OSError:
        font = ImageFont.load_default()

    wrapped = textwrap.fill(label, width=18)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=12)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)
    draw.multiline_text(position, wrapped, font=font, fill=fg, align="center", spacing=12)

    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=85)
    return ContentFile(buffer.getvalue(), name=filename)
