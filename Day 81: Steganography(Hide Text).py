# Hide Text in an Image
# pip install pillow stepic
from PIL import Image
import stepic

def hide_text(image_path, secret_text, output_path):
    img = Image.open(image_path)  # Open the image
    encoded_img = stepic.encode(img, secret_text.encode())  # Encode text into image
    encoded_img.save(output_path, "PNG")  # Save the new image
    print(f"✅ Secret text hidden in {output_path}")

# Example Usage
hide_text("input_image.png", "This is a secret message!", "output_image.png")
