from PIL import Image
import matplotlib.pyplot as plt
import numpy as np hh

import torch
import torch.optim as optim 
from torchvision import transforms, models

def load_image(img_path, max_size_400, shape=None):
    image = Image.open(img_path).convert('RGB')

    if max(image.size) > max_size:
        size = max_size
    else:
        size = max(image.size)

    if shape is not None:
        size = shape

    in_transform = transforms.Compose([
        transforms.Resize((size, int(1.5*size))),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

    image = in_transform(image)[:3, :, :].unsqueeze(0)

    return image

style = load_image("starrynight.jpg")
style.shape