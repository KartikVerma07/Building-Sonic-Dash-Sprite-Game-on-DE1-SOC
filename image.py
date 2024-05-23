from PIL import Image

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def write_hex_values(image_path):
    try:
        # Open the image
        image = Image.open(image_path)

        # Convert image to RGB mode (if it's not already)
        image = image.convert('RGB')

        # Get the dimensions of the image
        width, height = image.size

        # Create three files for R, G, and B values
        with open('red_values.txt', 'w') as red_file, \
             open('green_values.txt', 'w') as green_file, \
             open('blue_values.txt', 'w') as blue_file:
            print("here")
            # Iterate over each pixel in the image
            for y in range(height):
                for x in range(width):
                    # Get the RGB values of the pixel
                    r, g, b = image.getpixel((x, y))

                    # Convert RGB to hexadecimal
                    hex_color = rgb_to_hex((r, g, b))

                    # Write the hexadecimal value to the respective file
                    red_file.write(hex_color[1:3] + '\n')  # Exclude the '#' symbol
                    green_file.write(hex_color[3:5] + '\n')
                    blue_file.write(hex_color[5:] + '\n')

        print("Hexadecimal values for RGB components have been written to separate files.")

    except Exception as e:
        print("An error occurred:", e)

# Example usage:

write_hex_values("pixels.tif")

