from PIL import Image, ImageDraw, ImageFont


# Function to get the appropriate font size for the text
def get_font_size(draw, text, max_width, font_path, initial_size):
    font_size = initial_size
    font = ImageFont.truetype(font_path, font_size)
    while draw.textbbox((0, 0), text, font=font)[2] > max_width:
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
    return font

# Function to create the logo
def create_logo(title, subtitle, title_color, subtitle_color, background_color):
    # Create a new image
    img = Image.new('RGB', (600, 200), color=background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Specify font path
    font_path = "arial.ttf"

    # Get appropriate font sizes
    title_font = get_font_size(draw, title, img.width - 20, font_path, 50)
    subtitle_font = get_font_size(draw, subtitle, img.width - 20, font_path, 25)

    # Calculate text size
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width, title_height = title_bbox[2] - title_bbox[0], title_bbox[3] - title_bbox[1]
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width, subtitle_height = subtitle_bbox[2] - subtitle_bbox[0], subtitle_bbox[3] - subtitle_bbox[1]

    # Calculate positions
    title_x = (img.width - title_width) // 2
    title_y = (img.height - title_height) // 2 - subtitle_height // 2
    subtitle_x = (img.width - subtitle_width) // 2
    subtitle_y = (title_y + title_height)

    # Add some spacing between title and subtitle
    title_y -= 10
    subtitle_y += 10

    # Draw title
    draw.text((title_x, title_y), title, fill=title_color, font=title_font)
    # Draw subtitle
    draw.text((subtitle_x, subtitle_y), subtitle, fill=subtitle_color, font=subtitle_font)

    # Save the image
    img.save("./assets/logo.png")

create_logo("Auto_Repo_Readme", "Automatically generate a README for any repository blah blah blah", (0, 0, 0), (65, 105, 225), (255, 255, 255))