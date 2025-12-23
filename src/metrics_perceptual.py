import numpy as np
import cv2

class PerceptualMetrics:
    def __init__(self):
        pass
    
    def _prepare_image(self, img):
        """
        Prepara a imagem NORMALIZADA (0.0 a 1.0)
        Isso evita explosão numérica nos cálculos de variância.
        """
        # 1. Garantir array float
        img = np.array(img, dtype=np.float32)
        
        # 2. Normalizar para range [0.0, 1.0] se estiver em [0, 255]
        if img.max() > 1.0:
            img = img / 255.0
            
        # 3. Clip de segurança
        img = np.clip(img, 0.0, 1.0)
        
        # 4. Conversão Grayscale Matemática (R=0.299, G=0.587, B=0.114)
        if img.ndim == 3:
            if img.shape[2] == 3: # RGB/BGR
                # Assumindo que o OpenCV leu como BGR, mas vamos usar uma média simples 
                # ponderada que funciona para ambos em métricas estruturais
                img = np.dot(img[...,:3], [0.114, 0.587, 0.299])
            elif img.shape[2] == 4: # RGBA
                img = np.dot(img[...,:3], [0.114, 0.587, 0.299])
            elif img.shape[2] == 1:
                img = img.squeeze()
                
        return img

    def ssim_metric(self, ref, dist):
        """
        SSIM Manual Normalizado (0-1)
        Baseado em Wang et al. (2004)
        """
        try:
            # Imagens entram como float 0.0-1.0
            I1 = self._prepare_image(ref)
            I2 = self._prepare_image(dist)
            
            # Verificação de shape
            if I1.shape != I2.shape:
                if I1.size == I2.size:
                    I2 = I2.reshape(I1.shape)
                else:
                    return 0.0

            # Constantes para range 0-1 (L=1.0)
            C1 = (0.01 * 1.0)**2
            C2 = (0.03 * 1.0)**2
            
            # Kernel Gaussiano
            win_size = 11
            sigma = 1.5
            
            # Médias (mu)
            mu1 = cv2.GaussianBlur(I1, (win_size, win_size), sigma)
            mu2 = cv2.GaussianBlur(I2, (win_size, win_size), sigma)
            
            mu1_sq = mu1 ** 2
            mu2_sq = mu2 ** 2
            mu1_mu2 = mu1 * mu2
            
            # Variâncias (sigma)
            # sigma^2 = E[x^2] - (E[x])^2
            sigma1_sq = cv2.GaussianBlur(I1**2, (win_size, win_size), sigma) - mu1_sq
            sigma2_sq = cv2.GaussianBlur(I2**2, (win_size, win_size), sigma) - mu2_sq
            sigma12 = cv2.GaussianBlur(I1 * I2, (win_size, win_size), sigma) - mu1_mu2
            
            # Fórmula
            numerator = (2 * mu1_mu2 + C1) * (2 * sigma12 + C2)
            denominator = (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)
            
            ssim_map = numerator / denominator
            
            # Média e Clip final (segurança extra)
            mssim = np.clip(ssim_map.mean(), -1.0, 1.0)
            
            return float(mssim)
            
        except Exception as e:
            print(f"⚠️ Erro SSIM: {e}")
            return 0.0

    def uiq_metric(self, ref, dist):
        """Universal Image Quality Index (Normalizado)"""
        try:
            # Normalizar para 0-1
            ref = self._prepare_image(ref)
            dist = self._prepare_image(dist)
            
            ref_flat = ref.flatten()
            dist_flat = dist.flatten()
            
            mean_r = np.mean(ref_flat)
            mean_d = np.mean(dist_flat)
            var_r = np.var(ref_flat)
            var_d = np.var(dist_flat)
            
            cov_mx = np.cov(ref_flat, dist_flat)
            cov_rd = cov_mx[0][1]

            numerator = 4 * cov_rd * mean_r * mean_d
            denominator = (var_r + var_d) * (mean_r**2 + mean_d**2)
            
            if denominator == 0:
                return 1.0 if np.array_equal(ref, dist) else 0.0
                
            return float(np.clip(numerator / denominator, -1.0, 1.0))
        except: return 0.0

    def fsim_metric(self, ref, dist):
        """FSIM Simplificado (Normalizado)"""
        try:
            ref = self._prepare_image(ref)
            dist = self._prepare_image(dist)
            
            if ref.shape != dist.shape:
                if ref.size == dist.size: dist = dist.reshape(ref.shape)
                else: return 0.0
            
            # Gradientes (Scharr é mais estável que Sobel para floats)
            gx_r = cv2.Sobel(ref, cv2.CV_32F, 1, 0, ksize=3)
            gy_r = cv2.Sobel(ref, cv2.CV_32F, 0, 1, ksize=3)
            mag_r = cv2.sqrt(gx_r**2 + gy_r**2)
            
            gx_d = cv2.Sobel(dist, cv2.CV_32F, 1, 0, ksize=3)
            gy_d = cv2.Sobel(dist, cv2.CV_32F, 0, 1, ksize=3)
            mag_d = cv2.sqrt(gx_d**2 + gy_d**2)
            
            # Constante perceptiva
            C = 0.85  # Ajustado para range 0-1
            
            gms = (2 * mag_r * mag_d + C) / (mag_r**2 + mag_d**2 + C)
            return float(np.mean(gms))
        except: return 0.0