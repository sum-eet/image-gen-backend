from PIL import Image, ImageDraw, ImageFont
import textwrap
from string import ascii_letters

# Open image
img = Image.open(fp='GajbImage.png', mode='r')

# Load custom font
font = ImageFont.truetype(font='Inter.ttf', size=72)

# Create DrawText object
draw = ImageDraw.Draw(im=img)

# Define our text
text = """Simplicity"""

# Calculate the average length of a single character of our font.
# Note: this takes into account the specific font and font size.
avg_char_width = sum(font.getsize(char)[0]
                     for char in ascii_letters) / len(ascii_letters)

# Translate this average length into a character count
max_char_count = int(img.size[0] * .618 / avg_char_width)

# Create a wrapped text object using scaled character count
text = textwrap.fill(text=text, width=max_char_count)

# Add text to the image
draw.text(xy=(img.size[0]/2, img.size[1] / 2), text=text,
          font=font, fill='#000000', anchor='mm')

# view the result
img.show()
