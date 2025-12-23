# Análise Objetiva da Qualidade de Imagens (IQA)

> **Projeto Final - Impact-Lab (UFAM)**

> Aluno: Rômulo Fernandes Torres

Este repositório contém o sistema desenvolvido para a disciplina de **Análise da Qualidade de Imagens**. O projeto implementa uma arquitetura modular em Python capaz de aplicar distorções controladas em imagens e avaliar a degradação resultante, demonstrando as limitações das métricas de erro simples frente à percepção humana.

---

## Funcionalidades

O sistema executa um pipeline automatizado que:
1.  **Gera Distorções:** Aplica 5 tipos de degradação (Ruído Gaussiano, Sal e Pimenta, Desfoque, JPEG e Brilho).
2.  **Calcula Métricas:**
    * **Clássicas:** MSE, PSNR, RMSE, MAE.
    * **Perceptuais:** SSIM (Implementação Manual), UIQ, FSIM.
3.  **Gera Relatórios:** Cria gráficos comparativos (`.png`), tabelas de dados (`.csv`) e um relatório final em Markdown.

---

## Pré-requisitos e Instalação

O projeto foi desenvolvido em **Python 3.8+**. Siga os passos abaixo para preparar o ambiente.

### 1. Instalar Dependências
As bibliotecas necessárias são padrões para processamento de imagens e dados. Execute no terminal:

```bash
pip install numpy opencv-python matplotlib pandas scipy
```

### 2. Verificar a Imagem de Teste

Certifique-se de que a imagem de referência padrão esteja na raiz do projeto com o nome exato:
* Arquivo: (`final_test_image.png`)
* Local: Raiz do projeto (mesma pasta do README).

## Rodar o código

Para executar todos os experimentos e gerar os relatórios automaticamente, rode o script principal a partir da raiz do projeto:

```bash
python3 src/run_final.py
```

## Estrutura do Projeto e Saídas

Após a execução, o sistema criará automaticamente uma pasta resultados/ com os artefatos da análise.

```plaintext
/impact-lab
│
├── src/                      # Código-Fonte Modular
│   ├── run_final.py          # Script Principal (Execute este!)
│   ├── main_pipeline.py      # Lógica de orquestração dos testes
│   ├── distortions.py        # Gerador de distorções (Ruído, Blur, etc)
│   ├── metrics_classic.py    # Implementação vetorizada (PSNR, MSE)
│   ├── metrics_perceptual.py # Implementação MANUAL do SSIM (Wang et al.)
│   └── visualizations.py     # Gerador dos gráficos
│
├── resultados/               # (Gerado Automaticamente)
│   ├── gaussian_noise_analysis.png  # Gráficos comparativos
│   ├── brightness_analysis.png      # Gráfico do teste de brilho
│   ├── relatorio_final_corrigido.md # Resumo estatístico
│   └── *.csv                        # Dados brutos
│
└── final_test_image.png      # Imagem Ground-Truth
``` 

## Destaques da Implementação

1. **SSIM Manual**

Ao invés de usar bibliotecas prontas, o algoritmo SSIM foi implementado manualmente (src/metrics_perceptual.py) seguindo o paper original de Wang et al. (2004). O código força a normalização para float [0.0, 1.0], corrigindo instabilidades numéricas comuns em cálculos de variância com inteiros.

2. **A Falha do PSNR**

O projeto inclui um teste de Variação de Brilho projetado para expor a falha do PSNR.

* Resultado: O PSNR cai para ~10dB (indicando erro grave), enquanto o SSIM permanece estável (>0.33), provando sua robustez a mudanças de iluminação.
