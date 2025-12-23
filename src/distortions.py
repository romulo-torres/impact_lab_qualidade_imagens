import cv2
import numpy as np
from scipy import ndimage
from PIL import Image
import io

class ImageDistorter:
    def __init__(self):
        pass
    
    def add_gaussian_noise(self, image, sigma=0.01):
        """Adiciona ruído Gaussiano"""
        noise = np.random.normal(0, sigma, image.shape)
        noisy = image.astype(np.float32) / 255.0 + noise
        return np.clip(noisy * 255, 0, 255).astype(np.uint8)
    
    def add_salt_pepper_noise(self, image, prob=0.01):
        """Adiciona ruído sal e pimenta"""
        noisy = np.copy(image)
        
        # Salt noise
        salt_mask = np.random.rand(*image.shape[:2]) < prob/2
        noisy[salt_mask] = 255
        
        # Pepper noise
        pepper_mask = np.random.rand(*image.shape[:2]) < prob/2
        noisy[pepper_mask] = 0
        
        return noisy
    
    def apply_gaussian_blur(self, image, kernel_size=5, sigma=1.0):
        """Aplica desfoque Gaussiano"""
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    
    def apply_jpeg_compression(self, image, quality=50):
        """Aplica compressão JPEG"""
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, encimg = cv2.imencode('.jpg', image, encode_param)
        decimg = cv2.imdecode(encimg, 1)
        return decimg
    
    def adjust_brightness_contrast(self, image, alpha=1.0, beta=0):
        """Ajusta brilho e contraste"""
        # alpha: contraste (1.0 = original)
        # beta: brilho (0 = original)
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        