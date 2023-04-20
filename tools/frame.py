from PIL import Image, ImageDraw
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont


def add_frame_to_image(input_image, output_iamge):
    # def add_frame_to_image(image, frame_width, frame_height, radius, shadow_width, title_bar_height, button_radius, button_spacing):

    # Load the screenshot image
    screenshot = Image.open(input_image)

    # Define the dimensions of the custom frame
    frame_thickness_horizontal = 10  # add 20 pixels for the thicker top frame
    frame_thickness_vertical = frame_thickness_horizontal + 40  # add 60 pixels for the title bar and buttons
    frame_width = screenshot.width + frame_thickness_horizontal  # add 20 pixels for the thicker top frame
    frame_height = screenshot.height + frame_thickness_vertical  # add 60 pixels for the title bar and buttons
    radius = 13  # define the radius for the rounded corners

    # Create the custom frame image
    frame_color = (255, 255, 255, 0)  # use RGBA to support transparency
    frame = Image.new("RGBA", (frame_width, frame_height),
                      frame_color)  # use RGBA to support transparency
    draw = ImageDraw.Draw(frame)

    # Draw the rounded rectangle for the frame
    rectangle_width = 0
    rectangle_outline = (
    128, 128, 128, 255)  # use RGBA to support transparency
    rectangle_a = 70
    # gray = (128, 128, 128, 255)
    # rectangle_fill = (255, 255, 255, rectangle_a)  # use RGBA to support transparency
    rectangle_fill = (
    128, 128, 128, rectangle_a)  # use RGBA to support transparency
    # rectangle_fill = rectangle_outline
    draw.rounded_rectangle((0, 0, frame_width, frame_height), radius,
                           fill=rectangle_fill, outline=rectangle_outline,
                           width=rectangle_width)

    # Draw the title bar and buttons
    title_bar_height = 40
    # draw.rectangle((0, 0, frame_width, title_bar_height), fill=(128, 128, 128, 255))
    # draw.text((10, 10), "Window Title", fill=(255, 255, 255, 255), font=ImageFont.truetype("arial.ttf", 20))

    # Draw the close, minimize, and maximize buttons
    button_radius = 8
    button_spacing = 20
    button_center_y = int(title_bar_height / 2) + 3
    button_center_x = (button_radius * 3 + button_spacing * 2) - 40

    color_red = (244, 67, 54, 255)
    color_yellow = (255, 193, 7, 255)
    color_green = (76, 175, 80, 255)

    # Draw the close button
    draw.ellipse((button_center_x, button_center_y - button_radius,
                  button_center_x + button_radius * 2,
                  button_center_y + button_radius), fill=color_red,
                 width=2)
    button_center_x += button_radius + button_spacing

    # Draw the minimize button
    draw.ellipse((button_center_x, button_center_y - button_radius,
                  button_center_x + button_radius * 2,
                  button_center_y + button_radius), fill=color_yellow,
                 width=2)
    button_center_x += button_radius + button_spacing

    # Draw the maximize/restore button
    draw.ellipse((button_center_x, button_center_y - button_radius,
                  button_center_x + button_radius * 2,
                  button_center_y + button_radius), fill=color_green,
                 width=2)

    # Add rounded corners to the screenshot
    screenshot_radius = 5
    screenshot_mask = Image.new("L", screenshot.size, 0)
    screenshot_draw = ImageDraw.Draw(screenshot_mask)
    screenshot_draw.rounded_rectangle(
        (0, 0, screenshot.width, screenshot.height), screenshot_radius,
        fill=255)
    screenshot.putalpha(screenshot_mask)

    # # apply anti-aliasing to the entire result
    # frame = frame.filter(ImageFilter.SMOOTH)

    # Overlay the screenshot on top of the custom frame
    frame.paste(screenshot, (frame_thickness_horizontal // 2,
                             title_bar_height + frame_thickness_horizontal // 2))

    # Save the result
    frame.save(output_iamge)

from subprocess import run
from subprocess import run
import os
def add_shadow_to_image(input_image, output_iamge):
    cmd = f'convert "{input_image}" \( +clone -background black -shadow 55x10+0+2 \) +swap -background none -layers merge +repage "{output_iamge}"'
    run(cmd, shell=True)


if __name__ == "__main__":
    import glob

    for basepath in ["../docs/assets/screenshots"]:

        for filename in glob.glob(os.path.join(basepath, "*.jpeg")):
            base_filename = os.path.basename(filename)
            output_filepath = os.path.join(basepath, base_filename.replace(".jpeg", ".png"))
            add_frame_to_image(filename, output_filepath)
            add_shadow_to_image(output_filepath, output_filepath)


