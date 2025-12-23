# image_loader.py
import cv2
import numpy as np
from pathlib import Path

class ImageLoader:
    def __init__(self):
        self.supported_formats = ['.png', '.jpg', '.jpeg', '.bmp']
    
    def load_image(self, path):
        """Carrega imagem em escala de cinza ou colorida"""
        img = cv2.imread(str(path))
        if img is None:
            raise ValueError(f"Não foi possível carregar a imagem: {path}")
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    def load_image_pair(self, ref_path, dist_path):
        """Carrega par de imagens (referência e distorcida)"""
        ref = self.load_image(ref_path)
        dist = self.load_image(dist_path)
        return ref, dist