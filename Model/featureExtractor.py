

import torch
import torchvision.transforms as transforms
import torchvision.models as models


class FeatureExtractor():
  def __init__(self):
      resnet18 = models.resnet18(pretrained=True)
      resnet18.eval()

      transform = transforms.Compose([
      transforms.ToPILImage(),
      transforms.Resize(256),
      transforms.CenterCrop(224),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
      ])

      self.resnet18 = resnet18
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
  
  
