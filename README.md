# Image Viewer Application

A simple and user-friendly Image Viewer application built using Python and Tkinter. This app allows users to open and view various image formats in a resizable window.

## Features

- Open image files in formats like JPG, PNG, GIF, and BMP.
- Simple and intuitive graphical user interface (GUI).
- Displays the loaded image with a status bar indicating the image name.

## Requirements

- Python 3.x
- Pillow library (for image processing)
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nelzouki22/Image-Viewer.git
   cd Image-Viewer
Install the required dependencies:

bash
Copy code
pip install Pillow
Usage
Run the application:

bash
Copy code
python image_viewer.py
Click the Open Image button to select an image file from your computer.

The selected image will be displayed in the window.

Screenshot
<!-- Replace with your actual screenshot path -->

Contributing
Contributions are welcome! If you have suggestions for improvements or want to report a bug, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thanks to the Pillow library for providing powerful image processing capabilities.
Thanks to Tkinter for making GUI development easy and accessible.
Author
Nadir Elzouki
GitHub : https://github.com/Nelzouki22
LinkedIn : https://www.linkedin.com/in/nadir-elzouki-40679a1a9/

markdown
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.configure(bg='lightgrey')  # Set background color

        # Create a frame for better layout
        frame = tk.Frame(self.root, bg='lightgrey')
        frame.pack(padx=10, pady=10)

        # Create a label to display images
        self.image_label = tk.Label(frame, bg='white', bd=2, relief='groove')
        self.image_label.pack(padx=10, pady=10)

        # Create a button to open images
        self.open_button = tk.Button(frame, text="Open Image", command=self.open_image,
                                      bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.open_button.pack(pady=10)

        # Status label
        self.status = tk.Label(self.root, text="No image loaded", bd=1, relief='sunken', anchor='w', bg='lightgrey')
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

    def open_image(self):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(title="Select an Image",
                                                filetypes=(("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"),
                                                           ("All Files", "*.*")))
        if file_path:  # Check if a file was selected
            self.display_image(file_path)

    def display_image(self, file_path):
        try:
            # Open and display the image
            img = Image.open(file_path)
            img = img.resize((600, 400), Image.LANCZOS)  # Resize the image
            self.img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.img_tk)
            self.image_label.image = self.img_tk  # Keep a reference to avoid garbage collection
            
            # Update status label with the loaded image name
            self.status.config(text=f"Loaded: {file_path.split('/')[-1]}")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")

if __name__ == "__main__":
    root = tk.Tk()  # Initialize Tkinter
    viewer = ImageViewer(root)
    root.mainloop()  # Start the main loop

### Instructions for Customization:

- **Screenshot**: Replace `path/to/screenshot.png` with the actual path of a screenshot of your application. You can take a screenshot of your app in action and save it in your repository.
- **Repository Link**: Ensure that the GitHub clone link reflects the correct repository URL.
- **License**: If you have a specific license file, ensure it’s included in your repository and link to it correctly.

### Adding the README.md to Your Repository:

1. Create a new file named `README.md` in the root of your project directory.
2. Copy and paste the above markdown text into the `README.md` file.
3. Save the file.
4. Commit the changes to your GitHub repository:

   ```bash
   git add README.md
   git commit -m "Add README.md"
   git push
