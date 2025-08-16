Analyzes images pixel-by-pixel to find dominant colors
Creates folders and sorts photos automatically
Preview mode to test before moving files
Supports JPG, PNG, BMP, TIFF, WebP formats

Installation

Make sure you have Python 3.6+ installed
Install required dependencies:

bashpip install Pillow numpy

Download photo_sorter.py from this repository

Usage
Basic Usage
Sort photos in a folder (creates color folders within the same directory):
bashpython photo_sorter.py "/path/to/your/photos"
Preview Mode (Recommended First)
See what would happen without actually moving files:
bashpython photo_sorter.py "/path/to/your/photos" --preview
Sort to Different Destination
Copy sorted photos to a new location:
bashpython photo_sorter.py "/path/to/source" --destination "/path/to/sorted"
Example Output
Processing: sunset.jpg
  Red: 45.2%, Green: 32.1%, Blue: 22.7%
  Dominant color: red
  Moved to: red_photos/

Processing: ocean_view.jpg
  Red: 15.3%, Green: 28.9%, Blue: 55.8%
  Dominant color: blue
  Moved to: blue_photos/

Processing: forest.png
  Red: 20.1%, Green: 65.4%, Blue: 14.5%
  Dominant color: green
  Moved to: green_photos/

Processing complete!
Successfully processed: 3 images
Errors encountered: 0 images
How It Works
Analyzes each image to calculate red, green, and blue percentages, then moves the image to the folder for whichever color is highest.
Example: Image with Red 25%, Green 30%, Blue 45% → goes to blue_photos folder
Command Line Options
OptionShortDescription--destination-dSpecify destination folder for sorted photos--preview-pPreview mode - analyze without moving files--help-hShow help message
Folder Structure
After running the script, your folder structure will look like this:
your_photos/
├── red_photos/
│   ├── sunset.jpg
│   └── roses.png
├── green_photos/
│   ├── forest.jpg
│   └── leaves.png
└── blue_photos/
    ├── ocean.jpg
    └── sky.png
Tips

Always test first: Use --preview mode before sorting your entire collection
Backup important photos: Make copies before running the script on irreplaceable images
Start small: Test with a few images to understand how the color analysis works
Check results: Some images might not sort as expected due to mixed colors or lighting

Supported Image Formats

JPEG/JPG
PNG
BMP
TIFF
WebP

Requirements

Python 3.6 or higher
Pillow (PIL) library
NumPy library

Contributing
Found a bug or have an idea for improvement? Feel free to:

Open an issue describing the problem or suggestion
Fork the repository and submit a pull request
Share examples of images that don't sort correctly

Possible Enhancements
Some ideas for future development:

 Add more color categories (yellow, purple, orange, pink, black, white)
 Implement HSV color space analysis for better color detection
 GUI interface for drag-and-drop functionality
 Undo functionality to reverse sorting
 Support for RAW image formats
 Color palette extraction for multi-color sorting

License
This project is open source and available under the MIT License.
Example Use Cases

📸 Photography Organization: Sort photos by color themes for easy browsing
🎨 Design Assets: Organize stock photos and graphics by dominant colors
🖼️ Art Collections: Categorize artwork and illustrations by color palette
🤖 Machine Learning: Pre-sort image datasets for computer vision projects
🌈 Creative Projects: Find all your blue-toned or warm-toned images quickly


Created with ❤️ for photographers and digital organizers everywhere!
