import stepic
from PIL import Image

def extract_text(image_path):
    img = Image.open(image_path)  # Open the encoded image
    secret_text = stepic.decode(img)  # Decode hidden message
    print(f"🔓 Hidden Message: {secret_text}")

# Example Usage
extract_text("output_image.png")
