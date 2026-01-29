from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap


def render_output_to_image(
    text: str,
    output_path: Path,
    width=900,
    padding=20,
    bg_color=(30, 30, 30),
    text_color=(230, 230, 230)
):
    font = ImageFont.load_default()

    # Wrap text for readability
    wrapped_lines = []
    for line in text.splitlines():
        wrapped_lines.extend(textwrap.wrap(line, width=90) or [""])

    line_height = font.getbbox("A")[3] + 4
    img_height = padding * 2 + line_height * len(wrapped_lines)

    img = Image.new("RGB", (width, img_height), bg_color)
    draw = ImageDraw.Draw(img)

    y = padding
    for line in wrapped_lines:
        draw.text((padding, y), line, fill=text_color, font=font)
        y += line_height

    img.save(output_path)
