# metrics_classic.py
import numpy as np
from scipy import signal
from skimage.metrics import structural_similarity as ssim

class ClassicMetrics:
    def __init__(self):
        self.MAX_VAL = 255.0
    
    def mse(self, ref, dist):
        """Mean Squared Error"""
        return np.mean((ref.astype(np.float32) - dist.astype(np.float32)) ** 2)
    
    def rmse(self, ref, dist):
        """Root Mean Squared Error"""
        return np.sqrt(self.mse(ref, dist))
    
    def psnr(self, ref, dist):
        """Peak Signal-to-Noise Ratio"""
        mse_val = self.mse(ref, dist)
        if mse_val == 0:
            return float('inf')
        return 10 * np.log10((self.MAX_VAL ** 2) / mse_val)
    
    def mae(self, ref, dist):
        """Mean Absolute Error"""
        return np.mean(np.abs(ref.astype(np.float32) - dist.astype(np.float32)))
    
    def nae(self, ref, dist):
        """Normalized Absolute Error"""
        numerator = np.sum(np.abs(ref.astype(np.float32) - dist.astype(np.float32)))
        denominator = np.sum(np.abs(ref.astype(np.float32)))
        return numerator / denominator if denominator != 0 else 0
    
    def fidelity(self, ref, dist):
        """Fidelity Metric"""
        return 1 - self.nae(ref, dist)
    
    def accuracy(self, ref, dist):
        """Accuracy Metric"""
        mae_val = self.mae(ref, dist)
        return 1 - (mae_val / self.MAX_VAL)
    
    def ncc(self, ref, dist):
        """Normalized Cross-Correlation"""
        ref_mean = np.mean(ref)
        dist_mean = np.mean(dist)
        
        numerator = np.sum((ref - ref_mean) * (dist - dist_mean))
        denominator = np.sqrt(np.sum((ref - ref_mean) ** 2) * np.sum((dist - dist_mean) ** 2))
        
        return numerator / denominator if denominator != 0 else 0