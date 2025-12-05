from PIL import Image, ImageDraw, ImageFont
import os

def merge_images_professional(image1_path, image2_path, output_path="figure_merged.tiff"):
    """
    Professional image merging for scientific publications
    with proper scaling, alignment and labeling
    """
    
    # Open images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    print(f"Original sizes: {img1.size} and {img2.size}")
    
    # Standardize to same height (maintain aspect ratio)
    target_height = max(img1.height, img2.height)
    
    # Calculate new widths maintaining aspect ratio
    ratio1 = target_height / img1.height
    new_width1 = int(img1.width * ratio1)
    
    ratio2 = target_height / img2.height
    new_width2 = int(img2.width * ratio2)
    
    # Resize images
    img1_resized = img1.resize((new_width1, target_height), Image.Resampling.LANCZOS)
    img2_resized = img2.resize((new_width2, target_height), Image.Resampling.LANCZOS)
    
    # Create canvas with spacing
    spacing = 80  # Professional spacing between panels
    total_width = new_width1 + spacing + new_width2
    background_color = (255, 255, 255)  # White background
    
    merged = Image.new('RGB', (total_width, target_height), background_color)
    
    # Paste images (centered vertically since heights are same now)
    merged.paste(img1_resized, (0, 0))
    merged.paste(img2_resized, (new_width1 + spacing, 0))
    
    # Add professional labels
    draw = ImageDraw.Draw(merged)
    
    # Calculate font size based on image height
    base_font_size = int(target_height * 0.08)  # 8% of image height
    font_size = max(60, min(120, base_font_size))  # Min 60, Max 120
    
    try:
        # Try professional fonts (Arial Bold)
        font_paths = [
            "C:/Windows/Fonts/arialbd.ttf",  # Windows
            "/Library/Fonts/Arial Bold.ttf",  # Mac
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
            "arialbd.ttf"
        ]
        
        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    font = ImageFont.truetype(font_path, font_size)
                    print(f"Using font: {font_path}")
                    break
                except:
                    continue
        
        if font is None:
            # Fallback to default
            font = ImageFont.load_default()
            font = ImageFont.load_default().font_variant(size=font_size)
            print("Using default font")
            
    except Exception as e:
        print(f"Font loading error: {e}")
        font = ImageFont.load_default()
        font = ImageFont.load_default().font_variant(size=font_size)
    
    # Label positions (top-left corner with margin)
    margin = int(font_size * 0.8)
    
    # Draw labels with shadow/border for better visibility
    label_color = (0, 0, 0)  # Black
    shadow_color = (255, 255, 255)  # White shadow
    shadow_offset = int(font_size * 0.15)
    
    # Panel A label
    text_position_a = (margin, margin)
    
    # White shadow/outline
    for dx in [-shadow_offset, 0, shadow_offset]:
        for dy in [-shadow_offset, 0, shadow_offset]:
            if dx != 0 or dy != 0:
                draw.text((text_position_a[0] + dx, text_position_a[1] + dy), 
                         "A", fill=shadow_color, font=font)
    
    # Main black text
    draw.text(text_position_a, "A", fill=label_color, font=font)
    
    # Panel B label
    text_position_b = (new_width1 + spacing + margin, margin)
    
    # White shadow/outline
    for dx in [-shadow_offset, 0, shadow_offset]:
        for dy in [-shadow_offset, 0, shadow_offset]:
            if dx != 0 or dy != 0:
                draw.text((text_position_b[0] + dx, text_position_b[1] + dy), 
                         "B", fill=shadow_color, font=font)
    
    # Main black text
    draw.text(text_position_b, "B", fill=label_color, font=font)
    
    # Save with publication quality settings
    merged.save(
        output_path,
        'TIFF',
        compression='tiff_lzw',
        dpi=(600, 600),  # High DPI for publications
        quality=100
    )
    
    print(f"\n✅ MERGED IMAGE SAVED: {output_path}")
    print(f"📐 Final dimensions: {total_width} × {target_height} pixels")
    print(f"📏 Panel spacing: {spacing} pixels")
    print(f"🔤 Label font size: {font_size} pixels")
    print(f"💾 File size: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    # Cleanup
    img1.close()
    img2.close()
    
    return output_path

# Alternative: Simple version with fixed parameters
def merge_images_simple_fixed(image1_path, image2_path, output_path="merged_figure.tiff"):
    """
    Simple version with fixed height and larger labels
    """
    
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    # Set fixed height (choose based on your needs)
    target_height = 2000  # or max(img1.height, img2.height)
    
    # Resize maintaining aspect ratio
    w1 = int(img1.width * (target_height / img1.height))
    img1 = img1.resize((w1, target_height), Image.Resampling.LANCZOS)
    
    w2 = int(img2.width * (target_height / img2.height))
    img2 = img2.resize((w2, target_height), Image.Resampling.LANCZOS)
    
    # Create merged image
    spacing = 100
    total_width = w1 + spacing + w2
    
    merged = Image.new('RGB', (total_width, target_height), (255, 255, 255))
    merged.paste(img1, (0, 0))
    merged.paste(img2, (w1 + spacing, 0))
    
    # Add LARGE labels
    draw = ImageDraw.Draw(merged)
    
    # Very large font
    font_size = 150  # Much larger
    
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("arialbd.ttf", font_size)
        except:
            # Create large default font
            from PIL import ImageFont
            font = ImageFont.load_default()
            # Increase size
            for i in range(5):
                font = font.font_variant(size=font_size)
    
    # Draw labels with black border and white fill for maximum visibility
    label_positions = [
        (50, 50),  # A
        (w1 + spacing + 50, 50)  # B
    ]
    
    for i, (x, y) in enumerate(label_positions):
        label = "A" if i == 0 else "B"
        
        # White background box for label
        bbox = draw.textbbox((x, y), label, font=font)
        padding = 20
        draw.rectangle(
            [bbox[0]-padding, bbox[1]-padding, bbox[2]+padding, bbox[3]+padding],
            fill=(255, 255, 255)
        )
        
        # Black border around box
        draw.rectangle(
            [bbox[0]-padding, bbox[1]-padding, bbox[2]+padding, bbox[3]+padding],
            outline=(0, 0, 0),
            width=5
        )
        
        # Black text
        draw.text((x, y), label, fill=(0, 0, 0), font=font)
    
    # Save
    merged.save(output_path, 'TIFF', compression='tiff_lzw', dpi=(600, 600))
    
    print(f"\n✅ SIMPLE MERGE COMPLETE")
    print(f"📐 Size: {total_width} × {target_height}")
    print(f"🔤 Label size: VERY LARGE ({font_size}px)")
    
    return output_path

# Usage examples
if __name__ == "__main__":
    # Method 1: Professional (auto-adjusts)
    # merge_images_professional("image1.jpg", "image2.jpg", "figure_professional.tiff")
    
    # Method 2: Simple with large labels
    merge_images_simple_fixed("photo1.jpeg", "photo2.jpg", "figure_large_labels.tiff")
