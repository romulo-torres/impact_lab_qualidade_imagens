import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, results_dir='results'):
        self.results_dir = Path(results_dir)
        self.results_dir.mkdir(exist_ok=True)
        
    def load_all_results(self):
        """Carrega todos os resultados dos experimentos"""
        results = {}
        for file in self.results_dir.glob('*_results.csv'):
            dist_type = file.stem.replace('_results', '')
            results[dist_type] = pd.read_csv(file)
        return results
    
    def create_summary_table(self, results):
        """Cria tabela comparativa de todas as métricas por distorção"""
        summary_data = []
        
        for dist_type, df in results.items():
            # Calcular médias para cada métrica
            row = {'Distorção': dist_type.replace('_', ' ').title()}
            
            for metric in ['MSE', 'PSNR', 'SSIM', 'UIQ', 'FSIM', 'NCC', 'Fidelity']:
                if metric in df.columns:
                    row[metric] = f"{df[metric].mean():.4f}"
            
            summary_data.append(row)
        
        summary_df = pd.DataFrame(summary_data)
        return summary_df
    
    def create_variation_table(self, results):
        """Tabela de variação das métricas por nível de ruído"""
        variation_data = []
        
        for dist_type, df in results.items():
            for _, row in df.iterrows():
                level = row['Nível']
                variation_data.append({
                    'Distorção': dist_type,
                    'Nível': level,
                    'MSE': row['MSE'],
                    'PSNR': row['PSNR'],
                    'SSIM': row['SSIM']
                })
        
        variation_df = pd.DataFrame(variation_data)
        return variation_df
    
    def create_ranking_table(self, results):
        """Ranking das métricas que melhor detectaram a degradação"""
        sensitivity_scores = {}
        
        for dist_type, df in results.items():
            # Calcular sensibilidade como variação relativa
            for metric in df.columns:
                if metric not in ['Nível']:
                    if metric not in sensitivity_scores:
                        sensitivity_scores[metric] = []
                    
                    # Quanto maior a variação, mais sensível a métrica
                    if len(df[metric]) > 1:
                        variation = df[metric].std() / df[metric].mean()
                        sensitivity_scores[metric].append(variation)
        
        # Calcular score médio para cada métrica
        ranking_data = []
        for metric, scores in sensitivity_scores.items():
            if scores:  # Se tem scores
                avg_score = np.mean(scores)
                ranking_data.append({
                    'Métrica': metric,
                    'Score de Sensibilidade': f"{avg_score:.4f}"
                })
        
        ranking_df = pd.DataFrame(ranking_data)
        ranking_df = ranking_df.sort_values('Score de Sensibilidade', ascending=False)
        
        return ranking_df
    
    def generate_all_tables(self, results):
        """Gera todas as tabelas obrigatórias"""
        print("📊 Gerando tabelas obrigatórias...")
        
        # Tabela 1: Comparação de métricas por distorção
        summary_table = self.create_summary_table(results)
        summary_path = self.results_dir / 'tabela_comparativa_metricas.csv'
        summary_table.to_csv(summary_path, index=False)
        print(f"✅ Tabela 1 salva em: {summary_path}")
        
        # Tabela 2: Variação por nível
        variation_table = self.create_variation_table(results)
        variation_path = self.results_dir / 'tabela_variacao_niveis.csv'
        variation_table.to_csv(variation_path, index=False)
        print(f"✅ Tabela 2 salva em: {variation_path}")
        
        # Tabela 3: Ranking de sensibilidade
        ranking_table = self.create_ranking_table(results)
        ranking_path = self.results_dir / 'tabela_ranking_sensibilidade.csv'
        ranking_table.to_csv(ranking_path, index=False)
        print(f"✅ Tabela 3 salva em: {ranking_path}")
        
        # Gerar versões em Markdown para o relatório
        self.generate_markdown_tables(summary_table, variation_table, ranking_table)
        
        return summary_table, variation_table, ranking_table
    
    def generate_markdown_tables(self, summary_table, variation_table, ranking_table):
        """Gera tabelas formatadas em Markdown"""
        md_path = self.results_dir / 'tabelas_relatorio.md'
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write("# Tabelas de Resultados\n\n")
            
            f.write("## Tabela 1: Comparação de Métricas por Distorção\n\n")
            f.write(summary_table.to_markdown(index=False))
            f.write("\n\n")
            
            f.write("## Tabela 2: Variação das Métricas por Nível\n\n")
            f.write(variation_table.head(20).to_markdown(index=False))
            f.write("\n\n")
            
            f.write("## Tabela 3: Ranking de Sensibilidade das Métricas\n\n")
            f.write(ranking_table.to_markdown(index=False))
            f.write("\n\n")
        
        print(f"📄 Tabelas em Markdown salvas em: {md_path}")
    
        def generate_required_plots(self, results):
        """Gera todos os gráficos obrigatórios"""
        print("📈 Gerando gráficos obrigatórios...")
        
        # Configurar estilo
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
        # Gráfico 1: PSNR × nível de ruído
        self.plot_psnr_vs_noise(results)
        
        # Gráfico 2: SSIM × nível de desfoque
        self.plot_ssim_vs_blur(results)
        
        # Gráfico 3: Correlação entre métricas
        self.plot_metrics_correlation(results)
        
        # Gráfico 4: Sensibilidade das métricas
        self.plot_metrics_sensitivity(results)
        
        # Gráfico 5: Comportamento de todas as métricas
        self.plot_all_metrics_behavior(results)
    
    def plot_psnr_vs_noise(self, results):
        """Gráfico PSNR × nível de ruído"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Ruído Gaussiano
        if 'gaussian_noise' in results:
            df = results['gaussian_noise']
            axes[0].plot(df['Nível'], df['PSNR'], 'bo-', linewidth=2, markersize=8)
            axes[0].set_title('PSNR vs Ruído Gaussiano', fontsize=14, fontweight='bold')
            axes[0].set_xlabel('Sigma (Nível de Ruído)', fontsize=12)
            axes[0].set_ylabel('PSNR (dB)', fontsize=12)
            axes[0].grid(True, alpha=0.3)
            axes[0].set_ylim(0, 80)
        
        # Ruído Sal e Pimenta
        if 'salt_pepper' in results:
            df = results['salt_pepper']
            axes[1].plot(df['Nível'], df['PSNR'], 'ro-', linewidth=2, markersize=8)
            axes[1].set_title('PSNR vs Ruído Sal e Pimenta', fontsize=14, fontweight='bold')
            axes[1].set_xlabel('Probabilidade', fontsize=12)
            axes[1].set_ylabel('PSNR (dB)', fontsize=12)
            axes[1].grid(True, alpha=0.3)
            axes[1].set_ylim(0, 80)
        
        plt.tight_layout()
        plt.savefig(self.results_dir / 'psnr_vs_ruido.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Gráfico 1: PSNR vs Ruído gerado")
    
    def plot_ssim_vs_blur(self, results):
        """Gráfico SSIM × nível de desfoque"""
        if 'gaussian_blur' in results:
            df = results['gaussian_blur']
            
            plt.figure(figsize=(8, 6))
            plt.plot(df['Nível'], df['SSIM'], 'go-', linewidth=2, markersize=8)
            plt.title('SSIM vs Desfoque Gaussiano', fontsize=16, fontweight='bold')
            plt.xlabel('Sigma do Kernel', fontsize=12)
            plt.ylabel('SSIM', fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.ylim(0, 1)
            
            # Adicionar linha de referência para qualidade "aceitável"
            plt.axhline(y=0.9, color='r', linestyle='--', alpha=0.5, label='Boa qualidade (SSIM > 0.9)')
            plt.axhline(y=0.7, color='y', linestyle='--', alpha=0.5, label='Qualidade média (SSIM > 0.7)')
            plt.legend()
            
            plt.tight_layout()
            plt.savefig(self.results_dir / 'ssim_vs_desfoque.png', dpi=300, bbox_inches='tight')
            plt.close()
            print("✅ Gráfico 2: SSIM vs Desfoque gerado")
    
    def plot_metrics_correlation(self, results):
        """Gráfico de correlação entre métricas"""
        # Combinar todos os resultados
        all_data = []
        for dist_type, df in results.items():
            for metric in ['MSE', 'PSNR', 'SSIM', 'UIQ', 'FSIM', 'NCC', 'Fidelity', 'Accuracy']:
                if metric in df.columns:
                    for value in df[metric]:
                        all_data.append({'Métrica': metric, 'Valor': value})
        
        if all_data:
            corr_df = pd.concat([df.drop(columns=['Nível']) for df in results.values()], ignore_index=True)
            
            # Calcular matriz de correlação
            corr_matrix = corr_df.corr()
            
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                       center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
            plt.title('Correlação entre Métricas de Qualidade', fontsize=16, fontweight='bold')
            plt.tight_layout()
            plt.savefig(self.results_dir / 'correlacao_metricas.png', dpi=300, bbox_inches='tight')
            plt.close()
            print("✅ Gráfico 3: Correlação entre métricas gerado")
    
    def plot_metrics_sensitivity(self, results):
        """Gráfico de sensibilidade das métricas"""
        sensitivity = {}
        
        for metric in ['MSE', 'PSNR', 'SSIM', 'UIQ', 'FSIM']:
            scores = []
            for df in results.values():
                if metric in df.columns and len(df[metric]) > 1:
                    # Coeficiente de variação
                    cv = df[metric].std() / df[metric].mean()
                    scores.append(abs(cv))
            
            if scores:
                sensitivity[metric] = np.mean(scores)
        
        if sensitivity:
            metrics = list(sensitivity.keys())
            scores = list(sensitivity.values())
            
            # Ordenar por sensibilidade
            sorted_idx = np.argsort(scores)[::-1]
            metrics = [metrics[i] for i in sorted_idx]
            scores = [scores[i] for i in sorted_idx]
            
            plt.figure(figsize=(10, 6))
            bars = plt.bar(metrics, scores, color=sns.color_palette("husl", len(metrics)))
            
            # Adicionar valores nas barras
            for bar, score in zip(bars, scores):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
                        f'{score:.4f}', ha='center', va='bottom', fontweight='bold')
            
            plt.title('Sensibilidade das Métricas a Diferentes Distorções', 
                     fontsize=16, fontweight='bold')
            plt.xlabel('Métrica', fontsize=12)
            plt.ylabel('Coeficiente de Variação (Média)', fontsize=12)
            plt.grid(True, alpha=0.3, axis='y')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(self.results_dir / 'sensibilidade_metricas.png', dpi=300, bbox_inches='tight')
            plt.close()
            print("✅ Gráfico 4: Sensibilidade das métricas gerado")
    
    def plot_all_metrics_behavior(self, results):
        """Gráfico do comportamento de todas as métricas"""
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        dist_types = list(results.keys())[:6]  # Mostrar até 6 distorções
        
        for idx, dist_type in enumerate(dist_types):
            if idx < len(axes):
                df = results[dist_type]
                
                # Plotar múltiplas métricas normalizadas
                for metric in ['MSE', 'PSNR', 'SSIM']:
                    if metric in df.columns:
                        # Normalizar entre 0 e 1 para comparação
                        values = df[metric].values
                        if len(values) > 0:
                            norm_values = (values - values.min()) / (values.max() - values.min() + 1e-10)
                            axes[idx].plot(df['Nível'], norm_values, 'o-', label=metric)
                
                axes[idx].set_title(dist_type.replace('_', ' ').title(), fontsize=12, fontweight='bold')
                axes[idx].set_xlabel('Nível')
                axes[idx].set_ylabel('Valor Normalizado')
                axes[idx].legend(loc='best', fontsize=8)
                axes[idx].grid(True, alpha=0.3)
        
        # Remover eixos extras
        for idx in range(len(dist_types), len(axes)):
            fig.delaxes(axes[idx])
        
        plt.suptitle('Comportamento das Métricas em Diferentes Distorções', 
                    fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.savefig(self.results_dir / 'comportamento_metricas.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Gráfico 5: Comportamento das métricas gerado")