from pathlib import Path
from output_capture import render_output_to_image


def capture_program_output(program, output_dir="Generated_Outputs"):
    Path(output_dir).mkdir(exist_ok=True)

    image_path = Path(output_dir) / f"{program['name']}_output.png"

    output_text = program["stdout"] or program["stderr"] or "No output"

    render_output_to_image(output_text, image_path)

    program["output_images"] = [image_path]
