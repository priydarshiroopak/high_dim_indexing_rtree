import tkinter as tk
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import torch
import torchvision.transforms as transforms
import torchvision.models as models

class FeatureExtractor():
  def __init__():
      resnet18 = models.resnet18(pretrained=True)
      resnet18.eval()

      transform = transforms.Compose([
      transforms.ToPILImage(),
      transforms.Resize(256),
      transforms.CenterCrop(224),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
      ])

      self.resenet18 = resnet18
      self.transform = transform

  def extract_features(self,img):
      '''
      image --> (h,w,3) ndarray
      '''
      img_tensor = self.transform(img).unsqueeze(0)   
      with torch.no_grad():
          features = self.resnet18(img_tensor)
      # print(features.shape)
      feature_vector = features.flatten().numpy()

      return feature_vector

class ImageSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Image search")
        self.master.geometry("500x900")
        
        
        # Create a button to select an image
        self.select_button = tk.Button(self.master, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)
        
    
    def select_image(self):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename()
        
        if file_path:
            # Destroy all labels before creating new ones
            for widget in self.master.winfo_children():
                if widget != self.select_button:
                    widget.destroy()
            
            # Display the selected image
            img = Image.open(file_path)
            img.thumbnail((250, 250))
            img_tk = ImageTk.PhotoImage(img)
            # img_features = FeatureExtractor.extract_features(np.array(img))
            
            # Create a label to display the "Query image" heading
            self.query_label = tk.Label(self.master, text="Query image", font=("Helvetica", 16))
            self.query_label.pack()
            
            # Create a label to display the selected image
            self.image_label = tk.Label(self.master)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk
            self.image_label.pack(pady=10)
            
            # Create a label to display the "Similar images" heading
            self.similar_images_label = tk.Label(self.master, text="Similar images", font=("Helvetica", 16))
            self.similar_images_label.pack(pady=20)
            
            # Create a frame to hold similar images
            self.similar_images_frame = tk.Frame(self.master)
            self.similar_images_frame.pack()
            
            # Display similar images
            similar_images_dir = "./"
            similar_images = ["sample.jpeg", "sample.jpeg", "sample.jpeg", "sample.jpeg"]
            
            for i in range(4):
                img_path = os.path.join(similar_images_dir, similar_images[i])
                img = Image.open(file_path)
                img.thumbnail((250*4/5, 250*4/5))
                img_tk = ImageTk.PhotoImage(img)
                label = tk.Label(self.similar_images_frame, image=img_tk)
                label.image = img_tk
                label.grid(row=i//2, column=i%2, padx=10, pady=10)

# feature = FeatureExtractor()
root = tk.Tk()
app = ImageSelector(root)
root.mainloop()