import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Make a pixel logo.')
parser.add_argument('source', type=str, help='Source PNG logo file')
parser.add_argument('target', type=str, help='Target PNG logo file')
parser.add_argument('--background-r', type=int, default=0, help='Red component of the background')
parser.add_argument('--background-g', type=int, default=0, help='Green component of the background')
parser.add_argument('--background-b', type=int, default=0, help='Blue component of the background')
parser.add_argument('--background-a', type=int, default=0, help='Alpha component of the background')
parser.add_argument('--pixel-size', type=int, default=10, help='Size of the pixels')
parser.add_argument('--margin-size', type=int, default=1, help='Size of the margin between the pixels')

args = parser.parse_args()
background_color = (args.background_r, args.background_g, args.background_b, args.background_a)
margin_size = args.margin_size
pixel_size = args.pixel_size
source = Image.open(args.source)
width, height = source.size
offset = pixel_size + margin_size
target_width = width * offset + margin_size
target_height = height * offset + margin_size
target = Image.new('RGBA', (target_width, target_height), color=background_color)
for px in range(0, width):
    for py in range(0, height):
        pixel = source.getpixel((px, py))
        for x in range(margin_size + px * offset, margin_size + px * offset + pixel_size):
            for y in range(margin_size + py * offset, margin_size + py * offset + pixel_size):
                target.putpixel((x, y), pixel)
target.save(args.target)

