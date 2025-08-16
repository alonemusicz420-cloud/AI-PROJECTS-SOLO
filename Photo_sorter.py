import os
import shutil
from PIL import Image
import numpy as np
from collections import Counter
import argparse

def get_dominant_color_percentage(image_path):
    """
    Analyze an image and return the percentage of each primary color (Red, Green, Blue)
    """
    try:
        # Open and convert image to RGB
        img = Image.open(image_path).convert('RGB')
        
        # Convert to numpy array for easier processing
        img_array = np.array(img)
        
        # Reshape to get all pixels as a flat list of RGB values
        pixels = img_array.reshape(-1, 3)
        
        # Calculate total number of pixels
        total_pixels = len(pixels)
        
        # Sum up all red, green, and blue values
        red_sum = np.sum(pixels[:, 0])
        green_sum = np.sum(pixels[:, 1])
        blue_sum = np.sum(pixels[:, 2])
        
        # Calculate total sum of all color values
        total_color_sum = red_sum + green_sum + blue_sum
        
        # Calculate percentages (avoid division by zero)
        if total_color_sum == 0:
            return {'red': 0, 'green': 0, 'blue': 0}
        
        red_percentage = (red_sum / total_color_sum) * 100
        green_percentage = (green_sum / total_color_sum) * 100
        blue_percentage = (blue_sum / total_color_sum) * 100
        
        return {
            'red': round(red_percentage, 2),
            'green': round(green_percentage, 2),
            'blue': round(blue_percentage, 2)
        }
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def get_dominant_color(color_percentages):
    """
    Return the color with the highest percentage
    """
    if not color_percentages:
        return None
    
    return max(color_percentages, key=color_percentages.get)

def create_color_folders(base_path):
    """
    Create folders for each color if they don't exist
    """
    colors = ['red', 'green', 'blue']
    for color in colors:
        folder_path = os.path.join(base_path, f"{color}_photos")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

def sort_photos(source_folder, destination_folder=None):
    """
    Sort photos from source folder into color-based subfolders
    """
    if destination_folder is None:
        destination_folder = source_folder
    
    # Create color folders
    create_color_folders(destination_folder)
    
    # Supported image extensions
    supported_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    
    # Process each file in the source folder
    processed_count = 0
    error_count = 0
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip if it's not a file or not an image
        if not os.path.isfile(file_path):
            continue
            
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in supported_extensions:
            continue
        
        print(f"Processing: {filename}")
        
        # Get color percentages
        color_percentages = get_dominant_color_percentage(file_path)
        
        if color_percentages is None:
            error_count += 1
            continue
        
        # Get dominant color
        dominant_color = get_dominant_color(color_percentages)
        
        # Print analysis results
        print(f"  Red: {color_percentages['red']}%, Green: {color_percentages['green']}%, Blue: {color_percentages['blue']}%")
        print(f"  Dominant color: {dominant_color}")
        
        # Move file to appropriate folder
        destination_path = os.path.join(destination_folder, f"{dominant_color}_photos", filename)
        
        try:
            # If source and destination are the same, move the file
            if source_folder == destination_folder:
                shutil.move(file_path, destination_path)
            else:
                # Otherwise, copy the file
                shutil.copy2(file_path, destination_path)
            
            print(f"  Moved to: {dominant_color}_photos/")
            processed_count += 1
            
        except Exception as e:
            print(f"  Error moving file: {e}")
            error_count += 1
        
        print()  # Empty line for readability
    
    print(f"Processing complete!")
    print(f"Successfully processed: {processed_count} images")
    print(f"Errors encountered: {error_count} images")

def main():
    parser = argparse.ArgumentParser(description='Sort photos by dominant color')
    parser.add_argument('source', help='Source folder containing images')
    parser.add_argument('--destination', '-d', help='Destination folder (default: same as source)')
    parser.add_argument('--preview', '-p', action='store_true', help='Preview mode - analyze without moving files')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.source):
        print(f"Error: Source folder '{args.source}' does not exist")
        return
    
    if args.preview:
        print("=== PREVIEW MODE - No files will be moved ===")
        # Just analyze files without moving them
        supported_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        
        for filename in os.listdir(args.source):
            file_path = os.path.join(args.source, filename)
            
            if not os.path.isfile(file_path):
                continue
                
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in supported_extensions:
                continue
            
            print(f"Analyzing: {filename}")
            color_percentages = get_dominant_color_percentage(file_path)
            
            if color_percentages:
                dominant_color = get_dominant_color(color_percentages)
                print(f"  Red: {color_percentages['red']}%, Green: {color_percentages['green']}%, Blue: {color_percentages['blue']}%")
                print(f"  Would go to: {dominant_color}_photos/")
            else:
                print("  Error analyzing image")
            print()
    else:
        destination = args.destination if args.destination else args.source
        sort_photos(args.source, destination)

if __name__ == "__main__":
    main()

# Example usage (if running as a script):
# python photo_sorter.py /path/to/your/photos
# python photo_sorter.py /path/to/your/photos --destination /path/to/sorted/photos
# python photo_sorter.py /path/to/your/photos --preview