from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, text):
    # Open the original image
    photo = Image.open(input_image_path).convert("RGBA")
    
    # Create a transparent layer for the watermark
    txt_layer = Image.new("RGBA", photo.size, (255, 255, 255, 0))
    
    # Initialize drawing context
    draw = ImageDraw.Draw(txt_layer)
    
    # Define font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
    except IOError:
        print("Warning: Arial font not found, falling back to default. Text size might be small.")
        font = ImageFont.load_default()
        
    # Calculate text size and position (bottom right with padding)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    width, height = photo.size
    x = width - text_width - 20  # 20px padding from right
    y = height - text_height - 20 # 20px padding from bottom

    # Draw the text with semi-opacity (255, 255, 255, 128) -> Last number is alpha
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

    # Combine the original image with the watermark layer
    watermarked = Image.alpha_composite(photo, txt_layer)

    # Convert back to RGB to save as JPEG (or keep RGBA for PNG)
    watermarked = watermarked.convert("RGB")
    watermarked.save(output_image_path)
    print(f"Saved to {output_image_path}")


# Enable batch processing
import os

images_dir = "images"
watermark_text = "© 2026 Omkara Parashakti Devi Kshethram"

# Supported extensions
valid_extensions = {".jpg", ".jpeg", ".png", ".webp"}

print(f"Processing images in {images_dir}...")

for filename in os.listdir(images_dir):
    # Check extension
    ext = os.path.splitext(filename)[1].lower()
    
    # Skip invalid files or already watermarked files
    if ext not in valid_extensions or "_watermarked" in filename:
        continue
        
    input_path = os.path.join(images_dir, filename)
    
    # Create output filename (insert _watermarked before extension)
    name_without_ext = os.path.splitext(filename)[0]
    output_filename = f"{name_without_ext}_watermarked{ext}" # Saving with same extension properly
    
    # If using JPEG output for PNG input, logic might need adjustment if transparency matters, 
    # but the original script converted to RGB. Let's stick to the script's logic of converting to RGB.
    # So we can save as .jpg even if input is png, or keep extension.
    # The original script forced to RGB. Let's just save as .jpg for consistency or keep original extension but force RGB (no transparency support for jpg).
    # actually the script does `watermarked.save(output_image_path)`. If output path is .png it saves as png.
    # The script calls `watermarked = watermarked.convert("RGB")`. This removes transparency.
    # So saving as PNG would result in no alpha channel.
    # Let's just append _watermarked and keep extension for simplicity, knowing alpha is lost.
    
    output_path = os.path.join(images_dir, output_filename)
    
    print(f"Watermarking {filename}...")
    try:
        add_watermark(input_path, output_path, watermark_text)
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

print("Batch processing complete.")