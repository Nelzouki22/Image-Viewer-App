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
