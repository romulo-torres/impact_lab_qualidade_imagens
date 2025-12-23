# src/visualizations.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import Rectangle

class ImageVisualizer:
    def __init__(self, output_dir='results/visualizations'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def create_absolute_difference_map(self, ref_img, dist_img, title="Mapa de Diferença Absoluta"):
        """Cria heatmap da diferença absoluta"""
        # Converter para escala de cinza se necessário
        if len(ref_img.shape) == 3:
            ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_RGB2GRAY)
            dist_gray = cv2.cvtColor(dist_img, cv2.COLOR_RGB2GRAY)
        else:
            ref_gray = ref_img
            dist_gray = dist_img
        
        # Calcular diferença absoluta
        diff = cv2.absdiff(ref_gray.astype(np.float32), dist_gray.astype(np.float32))
        
        # Normalizar para 0-255
        diff_norm = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
        
        # Criar figura
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Imagem original
        axes[0].imshow(ref_img if ref_img.ndim == 3 else ref_gray, cmap='gray' if ref_img.ndim == 2 else None)
        axes[0].set_title('Imagem Original', fontsize=12, fontweight='bold')
        axes[0].axis('off')
        
        # Imagem distorcida
        axes[1].imshow(dist_img if dist_img.ndim == 3 else dist_gray, cmap='gray' if dist_img.ndim == 2 else None)
        axes[1].set_title('Imagem Distorcida', fontsize=12, fontweight='bold')
        axes[1].axis('off')
        
        # Heatmap da diferença
        im = axes[2].imshow(diff_norm, cmap='hot')
        axes[2].set_title(title, fontsize=12, fontweight='bold')
        axes[2].axis('off')
        
        # Adicionar barra de cores
        plt.colorbar(im, ax=axes[2], fraction=0.046, pad=0.04)
        
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / f'difference_map_{title.replace(" ", "_").lower()}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Mapa de diferença salvo: {filename}")
        return diff_norm
    
    def create_side_by_side_comparison(self, ref_img, dist_img, metrics_dict, dist_type, level):
        """Cria visualização lado a lado com métricas"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        
        # Imagem original
        axes[0].imshow(ref_img if ref_img.ndim == 3 else cv2.cvtColor(ref_img, cv2.COLOR_GRAY2RGB))
        axes[0].set_title('Original', fontsize=14, fontweight='bold')
        axes[0].axis('off')
        
        # Imagem distorcida
        axes[1].imshow(dist_img if dist_img.ndim == 3 else cv2.cvtColor(dist_img, cv2.COLOR_GRAY2RGB))
        axes[1].set_title(f'Distorcida: {dist_type} (Nível: {level})', 
                         fontsize=14, fontweight='bold', color='red')
        axes[1].axis('off')
        
        # Adicionar texto com métricas
        metrics_text = "\n".join([f"{k}: {v:.4f}" for k, v in metrics_dict.items()])
        plt.figtext(0.5, 0.02, metrics_text, 
                   ha='center', fontsize=10, 
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.suptitle(f'Comparação: {dist_type.replace("_", " ").title()}', 
                    fontsize=16, fontweight='bold', y=0.98)
        plt.tight_layout(rect=[0, 0.1, 1, 0.95])
        
        # Salvar
        filename = self.output_dir / f'comparison_{dist_type}_level{level}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Comparação lado a lado salva: {filename}")
    
    def create_distortion_series(self, ref_img, distorted_imgs, dist_type, levels):
        """Cria série de imagens com diferentes níveis de distorção"""
        n_levels = len(levels)
        
        fig, axes = plt.subplots(1, n_levels + 1, figsize=(15, 4))
        
        # Imagem original
        axes[0].imshow(ref_img if ref_img.ndim == 3 else cv2.cvtColor(ref_img, cv2.COLOR_GRAY2RGB))
        axes[0].set_title('Original', fontsize=10, fontweight='bold')
        axes[0].axis('off')
        
        # Imagens distorcidas
        for i in range(n_levels):
            axes[i+1].imshow(distorted_imgs[i] if distorted_imgs[i].ndim == 3 else 
                           cv2.cvtColor(distorted_imgs[i], cv2.COLOR_GRAY2RGB))
            axes[i+1].set_title(f'Nível: {levels[i]}', fontsize=10, fontweight='bold')
            axes[i+1].axis('off')
        
        plt.suptitle(f'Série de Distorção: {dist_type.replace("_", " ").title()}', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / f'distortion_series_{dist_type}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Série de distorção salva: {filename}")
    
    def create_roi_analysis(self, ref_img, dist_img, roi_coords):
        """Análise de Região de Interesse (ROI)"""
        x, y, w, h = roi_coords
        
        # Extrair ROIs
        ref_roi = ref_img[y:y+h, x:x+w]
        dist_roi = dist_img[y:y+h, x:x+w]
        
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        
        # Imagem completa com ROI destacada
        axes[0, 0].imshow(ref_img if ref_img.ndim == 3 else cv2.cvtColor(ref_img, cv2.COLOR_GRAY2RGB))
        axes[0, 0].add_patch(Rectangle((x, y), w, h, linewidth=2, edgecolor='r', facecolor='none'))
        axes[0, 0].set_title('Original com ROI', fontsize=12, fontweight='bold')
        axes[0, 0].axis('off')
        
        axes[0, 1].imshow(dist_img if dist_img.ndim == 3 else cv2.cvtColor(dist_img, cv2.COLOR_GRAY2RGB))
        axes[0, 1].add_patch(Rectangle((x, y), w, h, linewidth=2, edgecolor='r', facecolor='none'))
        axes[0, 1].set_title('Distorcida com ROI', fontsize=12, fontweight='bold')
        axes[0, 1].axis('off')
        
        # ROIs ampliadas
        axes[1, 0].imshow(ref_roi if ref_roi.ndim == 3 else cv2.cvtColor(ref_roi, cv2.COLOR_GRAY2RGB))
        axes[1, 0].set_title('ROI Original', fontsize=12, fontweight='bold')
        axes[1, 0].axis('off')
        
        axes[1, 1].imshow(dist_roi if dist_roi.ndim == 3 else cv2.cvtColor(dist_roi, cv2.COLOR_GRAY2RGB))
        axes[1, 1].set_title('ROI Distorcida', fontsize=12, fontweight='bold')
        axes[1, 1].axis('off')
        
        plt.suptitle('Análise de Região de Interesse (ROI)', fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / 'roi_analysis.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Análise de ROI salva: {filename}")
        
        return ref_roi, dist_roi