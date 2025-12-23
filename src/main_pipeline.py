import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import json
import seaborn as sns
from datetime import datetime

# Importar outros módulos
from imagem_loader import ImageLoader
from distortions import ImageDistorter
from metrics_classic import ClassicMetrics
from metrics_perceptual import PerceptualMetrics

class QualityAssessmentPipeline:
    def __init__(self):
        self.loader = ImageLoader()
        self.distorter = ImageDistorter()
        self.classic_metrics = ClassicMetrics()
        self.perceptual_metrics = PerceptualMetrics()
        self.results = {}
    
    def run_experiment(self, ref_path, dist_type, levels, output_dir='results'):
        """Executa experimento completo"""
        Path(output_dir).mkdir(exist_ok=True)
        
        # Carregar imagem de referência
        ref_img = self.loader.load_image(ref_path)
        
        results_table = []
        
        for level in levels:
            # Aplicar distorção
            if dist_type == 'gaussian_noise':
                dist_img = self.distorter.add_gaussian_noise(ref_img, sigma=level)
            elif dist_type == 'salt_pepper':
                dist_img = self.distorter.add_salt_pepper_noise(ref_img, prob=level)
            elif dist_type == 'gaussian_blur':
                dist_img = self.distorter.apply_gaussian_blur(ref_img, sigma=level)
            elif dist_type == 'jpeg':
                dist_img = self.distorter.apply_jpeg_compression(ref_img, quality=level)
            elif dist_type == 'brightness':
                dist_img = self.distorter.adjust_brightness_contrast(ref_img, alpha=1.0, beta=level)
            else:
                raise ValueError(f"Tipo de distorção desconhecido: {dist_type}")
            
            # Calcular todas as métricas
            try:
                metrics = {
                    'Nível': level,
                    'MSE': self.classic_metrics.mse(ref_img, dist_img),
                    'RMSE': self.classic_metrics.rmse(ref_img, dist_img),
                    'PSNR': self.classic_metrics.psnr(ref_img, dist_img),
                    'MAE': self.classic_metrics.mae(ref_img, dist_img),
                    'NAE': self.classic_metrics.nae(ref_img, dist_img),
                    'Fidelity': self.classic_metrics.fidelity(ref_img, dist_img),
                    'Accuracy': self.classic_metrics.accuracy(ref_img, dist_img),
                    'NCC': self.classic_metrics.ncc(ref_img, dist_img),
                }
                
                # Métricas perceptuais com fallback
                try:
                    metrics['SSIM'] = self.perceptual_metrics.ssim_metric(ref_img, dist_img)
                except:
                    metrics['SSIM'] = 0.0
                
                try:
                    metrics['UIQ'] = self.perceptual_metrics.uiq_metric(ref_img, dist_img)
                except:
                    metrics['UIQ'] = 0.0
                
                try:
                    metrics['FSIM'] = self.perceptual_metrics.fsim_metric(ref_img, dist_img)
                except:
                    metrics['FSIM'] = 0.0
                    
            except Exception as e:
                print(f"⚠️  Erro ao calcular métricas para nível {level}: {e}")
                continue
            
            results_table.append(metrics)
            
            # Salvar imagem distorcida (mesmo código)
        
        # Criar DataFrame
        df = pd.DataFrame(results_table)
        
        # Salvar resultados (mesmo código)
        
        return df
    
    def visualize_results(self, df, dist_type, output_dir='results'):
        """Cria visualizações dos resultados"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # PSNR vs Nível
        axes[0, 0].plot(df['Nível'], df['PSNR'], 'bo-')
        axes[0, 0].set_title(f'PSNR vs {dist_type}')
        axes[0, 0].set_xlabel('Nível')
        axes[0, 0].set_ylabel('PSNR (dB)')
        axes[0, 0].grid(True)
        
        # SSIM vs Nível
        axes[0, 1].plot(df['Nível'], df['SSIM'], 'ro-')
        axes[0, 1].set_title(f'SSIM vs {dist_type}')
        axes[0, 1].set_xlabel('Nível')
        axes[0, 1].set_ylabel('SSIM')
        axes[0, 1].grid(True)
        
        # MSE vs Nível
        axes[1, 0].plot(df['Nível'], df['MSE'], 'go-')
        axes[1, 0].set_title(f'MSE vs {dist_type}')
        axes[1, 0].set_xlabel('Nível')
        axes[1, 0].set_ylabel('MSE')
        axes[1, 0].grid(True)
        
        # Correlação entre métricas
        corr_matrix = df[['MSE', 'PSNR', 'SSIM', 'UIQ']].corr()
        sns.heatmap(corr_matrix, annot=True, ax=axes[1, 1])
        axes[1, 1].set_title('Correlação entre Métricas')
        
        plt.tight_layout()
        plt.savefig(Path(output_dir) / f'{dist_type}_analysis.png', dpi=300)
        plt.close()
        
        print(f"✅ Gráficos salvos em: {output_dir}/{dist_type}_analysis.png")
    
    def generate_report(self, results, output_dir='results'):
        """Gera relatório completo"""
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report_path = Path(output_dir) / 'relatorio_final.md'
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Relatório de Análise - {data_atual}\n\n")
            
            for dist_type, df in results.items():
                f.write(f"## {dist_type.replace('_', ' ').title()}\n\n")
                f.write(df.to_markdown(index=False))
                f.write("\n\n")
        
        print(f"✅ Relatório salvo em: {report_path}")