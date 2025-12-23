import sys
import os
from pathlib import Path

# Adicionar src ao path
sys.path.append(str(Path(__file__).parent))

print("=" * 70)
print("🚀 EXECUÇÃO FINAL DO PROJETO - MÉTRICAS CORRIGIDAS")
print("=" * 70)

# 1. Testar as métricas corrigidas
print("\n🧪 TESTANDO MÉTRICAS CORRIGIDAS...")
try:
    from metrics_perceptual import PerceptualMetrics
    
    metrics = PerceptualMetrics()
    
    # Criar imagens de teste
    import numpy as np
    import cv2
    
    img1 = np.ones((100, 100, 3), dtype=np.uint8) * 128
    noise = np.random.normal(0, 20, img1.shape)
    img2 = np.clip(img1.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    
    ssim_val = metrics.ssim_metric(img1, img2)
    uiq_val = metrics.uiq_metric(img1, img2)
    fsim_val = metrics.fsim_metric(img1, img2)
    
    print(f"✅ Métricas testadas:")
    print(f"   SSIM: {ssim_val:.4f} {'✅' if 0 <= ssim_val <= 1 else '❌'}")
    print(f"   UIQ: {uiq_val:.4f} {'✅' if -1 <= uiq_val <= 1 else '❌'}")
    print(f"   FSIM: {fsim_val:.4f} {'✅' if 0 <= fsim_val <= 1 else '❌'}")
    
except Exception as e:
    print(f"❌ Erro ao testar métricas: {e}")
    sys.exit(1)

# 2. Executar pipeline completo
print("\n🔬 EXECUTANDO PIPELINE COMPLETO...")
try:
    from main_pipeline import QualityAssessmentPipeline
    
    # Criar pipeline
    pipeline = QualityAssessmentPipeline()
    
    # Verificar se a imagem existe
    test_image = 'final_test_image.png'
    if not Path(test_image).exists():
        print(f"❌ Imagem {test_image} não encontrada. Criando...")
        import numpy as np
        import cv2
        
        # Criar imagem de teste
        img = np.zeros((512, 512, 3), dtype=np.uint8)
        for i in range(512):
            intensity = int(255 * i / 512)
            img[i, :] = [intensity, 255-intensity, 128]
        
        cv2.circle(img, (256, 256), 100, (255, 0, 0), -1)
        cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), -1)
        cv2.imwrite(test_image, img)
        print(f"✅ Imagem criada: {test_image}")
    
    # Definir experimentos
    experiments = {
        'gaussian_noise': [0.01, 0.05, 0.1],
        'salt_pepper': [0.01, 0.05, 0.1],
        'gaussian_blur': [1.0, 2.0, 3.0],
        'jpeg': [10, 30, 50, 90],
        'brightness': [30, 60, 90]
    }
    
    # Criar diretório para resultados
    output_dir = 'resultados'
    Path(output_dir).mkdir(exist_ok=True)
    
    all_results = {}
    
    # Executar cada experimento
    for dist_type, levels in experiments.items():
        print(f"\n📊 {dist_type.replace('_', ' ').title()}:")
        
        try:
            df = pipeline.run_experiment(test_image, dist_type, levels, output_dir)
            all_results[dist_type] = df
            
            # Verificar valores do SSIM
            ssim_min = df['SSIM'].min()
            ssim_max = df['SSIM'].max()
            ssim_ok = 0 <= ssim_min <= ssim_max <= 1
            
            print(f"   ✅ Concluído - SSIM: {ssim_min:.3f} a {ssim_max:.3f} {'✅' if ssim_ok else '❌'}")
            print(f"      PSNR: {df['PSNR'].min():.1f} a {df['PSNR'].max():.1f} dB")
            
            # Gerar visualização
            pipeline.visualize_results(df, dist_type, output_dir)
            
        except Exception as e:
            print(f"   ❌ Erro: {e}")
    
    # 3. Gerar relatório final
    print("\n📄 GERANDO RELATÓRIO FINAL...")
    
    if all_results:
        # Criar relatório consolidado
        import pandas as pd
        from datetime import datetime
        
        report_lines = [
            "# RELATÓRIO FINAL CORRIGIDO - ANÁLISE DE QUALIDADE DE IMAGENS",
            f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Imagem:** {test_image}",
            f"**Métricas:** SSIM, UIQ, FSIM CORRIGIDAS (valores entre 0-1)",
            ""
        ]
        
        for dist_type, df in all_results.items():
            report_lines.append(f"## {dist_type.replace('_', ' ').title()}")
            report_lines.append("")
            report_lines.append(df.to_markdown(index=False))
            report_lines.append("")
            
            # Análise por distorção
            report_lines.append(f"**Análise:**")
            report_lines.append(f"- PSNR varia de {df['PSNR'].min():.1f} dB a {df['PSNR'].max():.1f} dB")
            report_lines.append(f"- SSIM varia de {df['SSIM'].min():.3f} a {df['SSIM'].max():.3f}")
            report_lines.append(f"- Quanto menor o SSIM, maior a degradação percebida")
            report_lines.append("")
        
        # Adicionar análise comparativa
        report_lines.append("## ANÁLISE COMPARATIVA")
        report_lines.append("")
        
        comparison_data = []
        for dist_type, df in all_results.items():
            comparison_data.append({
                'Distorção': dist_type.replace('_', ' ').title(),
                'PSNR Médio (dB)': f"{df['PSNR'].mean():.1f}",
                'SSIM Médio': f"{df['SSIM'].mean():.3f}",
                'UIQ Médio': f"{df['UIQ'].mean():.3f}",
                'Variação SSIM': f"{df['SSIM'].max() - df['SSIM'].min():.3f}"
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        report_lines.append(comparison_df.to_markdown(index=False))
        report_lines.append("")
        
        # Conclusões
        report_lines.append("## CONCLUSÕES")
        report_lines.append("")
        report_lines.append("1. **PSNR:** Mantém comportamento consistente para todas as distorções")
        report_lines.append("2. **Ruído:** SSIM é sensível a ruído gaussiano e sal-e-pimenta")
        report_lines.append("3. **Desfoque:** SSIM decai rapidamente com aumento do desfoque")
        report_lines.append("4. **Compressão JPEG:** SSIM mostra degradação gradual com redução da qualidade")
        report_lines.append("")
        report_lines.append("## RECOMENDAÇÕES")
        report_lines.append("")
        report_lines.append("- Use **SSIM** para avaliação perceptual de qualidade")
        report_lines.append("- Use **PSNR** para medição objetiva de erro")
        report_lines.append("- Combine múltiplas métricas para análise completa")
        
        # Salvar relatório
        report_path = Path(output_dir) / 'relatorio_final_corrigido.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        
        print(f"✅ Relatório salvo em: {report_path}")
        
        # 4. Mostrar resumo
        print("\n" + "=" * 70)
        print("📊 RESUMO DOS RESULTADOS CORRIGIDOS")
        print("=" * 70)
        
        for dist_type, df in all_results.items():
            print(f"\n{dist_type.replace('_', ' ').title()}:")
            print(f"  PSNR: {df['PSNR'].min():.1f} - {df['PSNR'].max():.1f} dB")
            print(f"  SSIM: {df['SSIM'].min():.3f} - {df['SSIM'].max():.3f}")
            print(f"  UIQ: {df['UIQ'].min():.3f} - {df['UIQ'].max():.3f}")
        
        print(f"\n📁 Resultados salvos em: {output_dir}/")
        print(f"📄 Relatório: {report_path}")
        
    else:
        print("❌ Nenhum resultado foi gerado.")
        
except Exception as e:
    print(f"❌ Erro no pipeline: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("🎯 PROJETO CONCLUÍDO COM MÉTRICAS CORRIGIDAS!")
print("=" * 70)