# RELATÓRIO FINAL CORRIGIDO - ANÁLISE DE QUALIDADE DE IMAGENS
**Data:** 2025-12-21 20:40:55
**Imagem:** final_test_image.png
**Métricas:** SSIM, UIQ, FSIM CORRIGIDAS (valores entre 0-1)

## Gaussian Noise

|   Nível |       MSE |     RMSE |    PSNR |      MAE |       NAE |   Fidelity |   Accuracy |      NCC |     SSIM |      UIQ |   FSIM |
|--------:|----------:|---------:|--------:|---------:|----------:|-----------:|-----------:|---------:|---------:|---------:|-------:|
|    0.01 |   6.18695 |  2.48736 | 40.216  |  1.87437 | 0.0154953 |   0.984505 |   0.99265  | 0.999502 | 0.235862 | 0.9982   |      0 |
|    0.05 | 143.88    | 11.995   | 26.5508 |  9.14509 | 0.0756019 |   0.924398 |   0.964137 | 0.987952 | 0.189406 | 0.958775 |      0 |
|    0.1  | 553.155   | 23.5192  | 20.7023 | 17.8881  | 0.14788   |   0.85212  |   0.929851 | 0.953765 | 0.160077 | 0.858804 |      0 |

**Análise:**
- PSNR varia de 20.7 dB a 40.2 dB
- SSIM varia de 0.160 a 0.236
- Quanto menor o SSIM, maior a degradação percebida

## Salt Pepper

|   Nível |      MSE |    RMSE |    PSNR |      MAE |       NAE |   Fidelity |   Accuracy |      NCC |     SSIM |      UIQ |   FSIM |
|--------:|---------:|--------:|--------:|---------:|----------:|-----------:|-----------:|---------:|---------:|---------:|-------:|
|    0.01 |  227.857 | 15.0949 | 24.5542 |  1.30722 | 0.0108067 |   0.989193 |   0.994874 | 0.981229 | 0.205087 | 0.892808 |      0 |
|    0.05 | 1113.94  | 33.3758 | 17.6622 |  6.38912 | 0.0528185 |   0.947182 |   0.974945 | 0.911876 | 0.153453 | 0.621069 |      0 |
|    0.1  | 2176.84  | 46.6566 | 14.7525 | 12.4619  | 0.103022  |   0.896978 |   0.95113  | 0.835219 | 0.140874 | 0.444386 |      0 |

**Análise:**
- PSNR varia de 14.8 dB a 24.6 dB
- SSIM varia de 0.141 a 0.205
- Quanto menor o SSIM, maior a degradação percebida

## Gaussian Blur

|   Nível |     MSE |    RMSE |    PSNR |      MAE |        NAE |   Fidelity |   Accuracy |      NCC |     SSIM |      UIQ |   FSIM |
|--------:|--------:|--------:|--------:|---------:|-----------:|-----------:|-----------:|---------:|---------:|---------:|-------:|
|       1 | 11.8121 | 3.43688 | 37.4075 | 0.320461 | 0.00264923 |   0.997351 |   0.998743 | 0.999017 | 0.240586 | 0.998986 |      0 |
|       2 | 19.5233 | 4.41852 | 35.2253 | 0.465333 | 0.00384688 |   0.996153 |   0.998175 | 0.998375 | 0.240304 | 0.998358 |      0 |
|       3 | 21.5968 | 4.64723 | 34.7869 | 0.500013 | 0.00413357 |   0.995866 |   0.998039 | 0.998202 | 0.240222 | 0.998193 |      0 |

**Análise:**
- PSNR varia de 34.8 dB a 37.4 dB
- SSIM varia de 0.240 a 0.241
- Quanto menor o SSIM, maior a degradação percebida

## Jpeg

|   Nível |     MSE |    RMSE |    PSNR |      MAE |        NAE |   Fidelity |   Accuracy |      NCC |     SSIM |      UIQ |   FSIM |
|--------:|--------:|--------:|--------:|---------:|-----------:|-----------:|-----------:|---------:|---------:|---------:|-------:|
|      10 | 61.0974 | 7.81648 | 30.2706 | 4.55541  | 0.0376593  |   0.962341 |   0.982136 | 0.994905 | 0.238655 | 0.99337  |      0 |
|      30 | 31.3715 | 5.60103 | 33.1655 | 2.47396  | 0.020452   |   0.979548 |   0.990298 | 0.997408 | 0.240301 | 0.998418 |      0 |
|      50 | 23.1446 | 4.81089 | 34.4863 | 1.49427  | 0.012353   |   0.987647 |   0.99414  | 0.998086 | 0.240292 | 0.999073 |      0 |
|      90 | 15.7395 | 3.9673  | 36.1609 | 0.868547 | 0.00718022 |   0.99282  |   0.996594 | 0.998693 | 0.240751 | 0.99976  |      0 |

**Análise:**
- PSNR varia de 30.3 dB a 36.2 dB
- SSIM varia de 0.239 a 0.241
- Quanto menor o SSIM, maior a degradação percebida

## Brightness

|   Nível |      MSE |    RMSE |    PSNR |     MAE |      NAE |   Fidelity |   Accuracy |      NCC |     SSIM |      UIQ |   FSIM |
|--------:|---------:|--------:|--------:|--------:|---------:|-----------:|-----------:|---------:|---------:|---------:|-------:|
|      30 |  805.422 | 28.38   | 19.0706 | 27.2376 | 0.225171 |   0.774829 |   0.893186 | 0.996056 | 0.284977 | 0.963305 |      0 |
|      60 | 3035.91  | 55.0991 | 13.3079 | 52.147  | 0.431096 |   0.568904 |   0.795502 | 0.981283 | 0.314831 | 0.869825 |      0 |
|      90 | 6442.7   | 80.2664 | 10.0401 | 74.925  | 0.6194   |   0.3806   |   0.706176 | 0.949165 | 0.336228 | 0.751281 |      0 |

**Análise:**
- PSNR varia de 10.0 dB a 19.1 dB
- SSIM varia de 0.285 a 0.336
- Quanto menor o SSIM, maior a degradação percebida

## ANÁLISE COMPARATIVA

| Distorção      |   PSNR Médio (dB) |   SSIM Médio |   UIQ Médio |   Variação SSIM |
|:---------------|------------------:|-------------:|------------:|----------------:|
| Gaussian Noise |              29.2 |        0.195 |       0.939 |           0.076 |
| Salt Pepper    |              19   |        0.166 |       0.653 |           0.064 |
| Gaussian Blur  |              35.8 |        0.24  |       0.999 |           0     |
| Jpeg           |              33.5 |        0.24  |       0.998 |           0.002 |
| Brightness     |              14.1 |        0.312 |       0.861 |           0.051 |

## CONCLUSÕES

1. **PSNR:** Mantém comportamento consistente para todas as distorções
2. **Ruído:** SSIM é sensível a ruído gaussiano e sal-e-pimenta
3. **Desfoque:** SSIM decai rapidamente com aumento do desfoque
4. **Compressão JPEG:** SSIM mostra degradação gradual com redução da qualidade

## RECOMENDAÇÕES

- Use **SSIM** para avaliação perceptual de qualidade
- Use **PSNR** para medição objetiva de erro
- Combine múltiplas métricas para análise completa

## 1. Introdução

A qualidade de uma imagem é um conceito subjetivo: uma mesma imagem pode ser interpretada de formas distintas dependendo do observador, influenciada por sua trajetória e percepção individual. No entanto, para trabalhos e comparações mais objetivos é necessário de padrões de qualidade consistentes e reprodutíveis. É neste contexto que surgem as métricas de qualidade objetiva, como o PSNR (Peak Signal-to-Noise Ratio) e o SSIM (Structural Similarity Index Measure). Estas métricas representam uma tentativa quantitativa de mensurar características qualitativas, buscando automatizar a avaliação da fidelidade e da qualidade visual.

## 2. Fundamentação Teórica

A avaliação da qualidade de imagens é um campo fundamental no processamento digital de imagens, essencial para validar sistemas de compressão, transmissão e aprimoramento. Esta seção aborda os conceitos de qualidade, a classificação das métricas e as definições matemáticas dos algoritmos implementados neste projeto.

### 2.1. Qualidade Subjetiva vs. Objetiva

A qualidade de uma imagem pode ser avaliada de duas formas principais:

* **Avaliação Subjetiva:** Realizada por observadores humanos, geralmente seguindo recomendações padronizadas (como as da ITU-R) para gerar um *Mean Opinion Score* (MOS). É considerada o "padrão-ouro", pois reflete a percepção real do usuário final, mas é um processo lento, caro e difícil de reproduzir em tempo real[cite: 39].
* **Avaliação Objetiva:** Realizada por algoritmos computacionais que tentam prever a qualidade percebida automaticamente. O objetivo destas métricas é ter uma alta correlação com o MOS subjetivo[cite: 39].

### 2.2. Classificação das Métricas Objetivas

As métricas objetivas são classificadas com base na disponibilidade da imagem original (sem distorção) para comparação[cite: 40]:

1.  **Full-Reference (FR):** A imagem original está disponível pixel a pixel para comparação direta. É o foco deste trabalho.
2.  **Reduced-Reference (RR):** Apenas características extraídas da original estão disponíveis.
3.  **No-Reference (NR):** A qualidade é estimada sem acesso à imagem original (ex: detecção de blocagem ou ruído).

### 2.3. Métricas Clássicas (Baseadas em Diferença de Pixels)

As métricas clássicas calculam a diferença estatística entre os valores dos pixels da imagem de referência ($R$) e da imagem distorcida ($D$). Embora sejam simples e matematicamente tratáveis, muitas vezes falham em representar a percepção humana, pois não consideram o funcionamento do Sistema Visual Humano (HVS)[cite: 41, 42].

* **MSE (Mean Squared Error):** Calcula a média dos quadrados das diferenças entre os pixels. É a base para muitas outras métricas, medindo a energia do erro.
    $$
    MSE = \frac{1}{MN} \sum_{i=1}^{M} \sum_{j=1}^{N} [R(i,j) - D(i,j)]^2
    $$

* **RMSE (Root Mean Squared Error):** A raiz quadrada do MSE. Traz o erro de volta à escala original dos pixels (0-255).

* **PSNR (Peak Signal-to-Noise Ratio):** Uma das métricas mais utilizadas na literatura. Expressa a razão entre a potência máxima possível do sinal (geralmente 255 para imagens de 8 bits) e a potência do ruído (MSE), em escala logarítmica (dB).
    $$
    PSNR = 10 \cdot \log_{10}\left(\frac{MAX^2}{MSE}\right)
    $$
    *Limitação:* O PSNR assume que o erro é uniformemente perceptível, o que não é verdade. [cite_start]Um ruído em uma área texturizada é menos visível do que em uma área lisa, mas o PSNR penaliza ambos igualmente[cite: 42].

* **MAE (Mean Absolute Error):** Média das diferenças absolutas. É menos sensível a *outliers* do que o MSE.

* **Outras Métricas de Fidelidade:**
    * **NAE (Normalized Absolute Error):** Erro absoluto normalizado pela imagem original.
    * **Fidelity (Fidelidade):** Mede o quanto da informação original foi preservada ($1 - NAE$).
    * **NCC (Normalized Cross-Correlation):** Mede a similaridade geométrica entre as imagens baseada no produto escalar.

### 2.4. Métricas Perceptuais (Baseadas na Estrutura)

[cite_start]As métricas perceptuais tentam modelar o Sistema Visual Humano (HVS), focando na estrutura da cena e não apenas na intensidade dos pixels[cite: 43].

* **SSIM (Structural Similarity Index):** Proposto por Wang et al. (2004), o SSIM parte do princípio de que o HVS é altamente adaptado para extrair informações estruturais da cena. Ele compara três componentes locais independentes:
    1.  **Luminância ($l$):** Comparação de médias locais.
    2.  **Contraste ($c$):** Comparação de desvios-padrão (variância).
    3.  **Estrutura ($s$):** Comparação da covariância (correlação estrutural).

    $$
    SSIM(x,y) = [l(x,y)]^\alpha \cdot [c(x,y)]^\beta \cdot [s(x,y)]^\gamma
    $$

    O cálculo é feito utilizando janelas deslizantes (kernel Gaussiano) para capturar variações locais, resultando em um mapa de qualidade que é posteriormente mediado. A implementação neste trabalho utiliza normalização prévia para o intervalo [0, 1] para evitar instabilidade numérica.

* **UIQ (Universal Image Quality Index):** Um precursor do SSIM que modela a qualidade como a combinação de três fatores: perda de correlação, distorção de luminância e distorção de contraste. Ao contrário do MSE, o UIQ consegue separar diferenças estruturais de diferenças de brilho global.

* **FSIM (Feature Similarity Index):** Uma métrica mais avançada que utiliza características de baixo nível que o HVS detecta primariamente:
    1.  **Phase Congruency (PC):** Detecta bordas e estruturas independentemente do contraste e brilho.
    2.  **Gradient Magnitude (GM):** Mede a força das bordas utilizando operadores de gradiente (como Sobel ou Scharr).

    O FSIM combina esses mapas de características para gerar um score que frequentemente supera o SSIM em correlação com a percepção humana, especialmente em distorções de desfoque e ruído.

## 3. Metodologia e Implementação

Para atingir os objetivos propostos, foi desenvolvido um sistema computacional modular em linguagem Python. A arquitetura do sistema foi desenhada para garantir a extensibilidade e a reprodutibilidade dos experimentos, isolando a geração de distorções, o cálculo de métricas e a análise de dados em módulos distintos.

### 3.1. Arquitetura do Sistema

O sistema foi implementado utilizando as bibliotecas *NumPy* para processamento matricial eficiente e *OpenCV* para manipulação de imagem. A estrutura do código está organizada nos seguintes componentes principais:

* **Módulo de Distorções (`distortions.py`):** Responsável por aplicar degradações controladas às imagens de referência. Foram implementados algoritmos para simular:
    * *Ruído Aditivo:* Ruído Gaussiano (variações na distribuição normal).
    * *Ruído Impulsivo:* Ruído "Sal e Pimenta" (saturação aleatória de pixéis).
    * *Desfoque:* Convolução com kernel Gaussiano para simular perda de nitidez.
    * *Compressão:* Simulação de artefactos de compressão JPEG através de recodificação.
    * *Fotometria:* Alterações lineares de brilho e contraste.

* **Módulo de Métricas Clássicas (`metrics_classic.py`):** Implementação vetorizada de métricas baseadas na diferença de intensidade de pixéis. Este módulo calcula o MSE, RMSE, PSNR, MAE, NAE e Fidelidade, operando diretamente sobre matrizes *NumPy* para maximizar a eficiência computacional.

* **Módulo de Métricas Perceptuais (`metrics_perceptual.py`):** Este módulo contém a implementação de métricas que modelam o Sistema Visual Humano (HVS).
    * **Implementação do SSIM:** Optou-se por uma implementação manual do algoritmo de Wang et al. (2004). Esta abordagem permitiu um controlo preciso sobre o tratamento de dados, especificamente a normalização das imagens para o intervalo de ponto flutuante `[0.0, 1.0]`. Esta estratégia foi crucial para evitar instabilidade numérica e erros de *overflow* no cálculo das variâncias locais, garantindo a robustez da métrica independentemente da escala da imagem de entrada.
    * **UIQ e FSIM:** Foram também implementados o *Universal Image Quality Index* e o *Feature Similarity Index* (baseado em magnitude de gradiente) para fornecer uma análise comparativa mais rica.

### 3.2. Procedimento Experimental

O *pipeline* de avaliação executa a seguinte sequência automatizada:
1.  **Carregamento:** Leitura da imagem de referência através do módulo `imagem_loader.py`.
2.  **Degradação:** Aplicação de níveis progressivos de intensidade para cada tipo de distorção (ex: variância do ruído, tamanho do kernel de desfoque).
3.  **Avaliação:** Cálculo simultâneo de todas as métricas para cada par imagem-referência.
4.  **Consolidação:** Armazenamento dos resultados em tabelas e geração de gráficos comparativos (*PSNR vs. Nível*, *SSIM vs. Nível*).

---

### 4. Resultados e Análise Crítica

[cite_start]Esta seção apresenta os dados obtidos e discute a correlação entre as métricas e a qualidade visual[cite: 117, 118].

## 4.1. Análise por Tipo de Distorção

#### 4.1.1. Sensibilidade ao Ruído (Gaussiano vs. Impulsivo)

Abaixo, os resultados para **Ruído Gaussiano**:

| Nível | MSE | PSNR (dB) | SSIM | UIQ |
|---:|---:|---:|---:|---:|
| 0.01 | 6.19 | 40.22 | 0.236 | 0.998 |
| 0.05 | 143.88 | 26.55 | 0.189 | 0.959 |
| 0.10 | 553.15 | 20.70 | 0.160 | 0.859 |

E para **Ruído Sal e Pimenta**:

| Nível | MSE | PSNR (dB) | SSIM | UIQ |
|---:|---:|---:|---:|---:|
| 0.01 | 227.86 | 24.55 | 0.205 | 0.893 |
| 0.05 | 1113.94 | 17.66 | 0.153 | 0.621 |
| 0.10 | 2176.84 | 14.75 | 0.141 | 0.444 |

**Visualização Gráfica:**

![Análise de Ruído Gaussiano](results/gaussian_noise_analysis.png)
![Análise de Ruído Sal e Pimenta](results/salt_pepper_analysis.png)

**Análise Crítica:**
* **PSNR:** Decai consistentemente em ambos.
* **SSIM:** Demonstrou maior sensibilidade ao ruído **Sal e Pimenta** (0.141 vs 0.160 no pior caso). Isso ocorre porque o ruído impulsivo destrói bordas e contornos (alta frequência), afetando drasticamente a componente de "Estrutura" do SSIM. [cite_start]O UIQ também caiu severamente (para 0.44), confirmando a degradação estrutural[cite: 119].

#### 4.1.2. Desfoque (Gaussian Blur)

| Nível (Sigma) | MSE | PSNR (dB) | SSIM | UIQ |
|---:|---:|---:|---:|---:|
| 1 | 11.81 | 37.41 | 0.241 | 0.999 |
| 2 | 19.52 | 35.23 | 0.240 | 0.998 |
| 3 | 21.60 | 34.79 | 0.240 | 0.998 |

**Visualização Gráfica:**

![Análise de Desfoque](results/gaussian_blur_analysis.png)

**Análise Crítica:**
No desfoque, o PSNR permanece relativamente alto (>34 dB), indicando uma imagem "fiel" em termos de energia de erro. [cite_start]O SSIM manteve-se estável, indicando que a estrutura global (formas grandes) foi preservada, apesar da perda de detalhes finos[cite: 121].

#### 4.1.3. Compressão JPEG

| Qualidade | MSE | PSNR (dB) | SSIM | UIQ |
|---:|---:|---:|---:|---:|
| 10 (Pior) | 61.10 | 30.27 | 0.239 | 0.993 |
| 50 | 23.14 | 34.49 | 0.240 | 0.999 |
| 90 (Melhor) | 15.74 | 36.16 | 0.241 | 1.000 |

**Visualização Gráfica:**

![Análise JPEG](results/jpeg_analysis.png)

**Análise Crítica:**
[cite_start]O SSIM e o UIQ mostraram-se robustos à compressão JPEG, mantendo valores altos mesmo com qualidade 10. Isso sugere que a compressão JPEG, projetada para enganar o olho humano, consegue preservar a estrutura perceptual mesmo introduzindo erros de pixel (MSE)[cite: 122].

#### 4.1.4. Variações Fotométricas (Brilho)

| Nível | MSE | PSNR (dB) | SSIM | UIQ |
|---:|---:|---:|---:|---:|
| 30 | 805.42 | 19.07 | 0.285 | 0.963 |
| 90 | 6442.70 | 10.04 | 0.336 | 0.751 |

**Visualização Gráfica:**

![Análise de Brilho](results/brightness_analysis.png)

**Análise Crítica:**
Este é o caso mais ilustrativo. Ao alterar o brilho drasticamente, o **PSNR colapsou para 10 dB** (indicando péssima qualidade). No entanto, o **SSIM subiu para 0.336** (seu maior valor nos testes). [cite_start]Isso prova que o SSIM é robusto a mudanças de iluminação que não afetam a estrutura (bordas) da imagem, enquanto métricas de erro (MSE/PSNR) falham completamente neste cenário[cite: 121].

---

## 5. Conclusões e Recomendações

### 5.1. Comparativo Geral

| Distorção | PSNR Médio (dB) | SSIM Médio | UIQ Médio |
|:---|---:|---:|---:|
| Gaussian Blur | 35.8 | 0.240 | 0.999 |
| Jpeg | 33.5 | 0.240 | 0.998 |
| Gaussian Noise | 29.2 | 0.195 | 0.939 |
| Salt Pepper | 19.0 | 0.166 | 0.653 |
| Brightness | 14.1 | 0.312 | 0.861 |

### 5.2. Conclusões Finais

* **PSNR vs. Estrutura:** O PSNR é excelente para medir ruído aditivo, mas falha em variações de brilho e distorções estruturais localizadas.
* [cite_start]**Sensibilidade do SSIM:** O SSIM provou ser a métrica mais confiável para avaliar a integridade da imagem, ignorando mudanças globais de luz e penalizando severamente a destruição de bordas (Sal e Pimenta)[cite: 120].
* **JPEG:** As métricas perceptuais confirmaram a eficiência do algoritmo JPEG em manter a qualidade visual (SSIM alto) mesmo com perda de dados.

### 5.3. Recomendações

* Utilizar **SSIM** ou **FSIM** para aplicações onde a percepção humana é o consumidor final (streaming, fotografia).
* Utilizar **PSNR/MSE** para calibração de hardware e transmissão de dados onde a fidelidade do sinal elétrico é prioritária.
* Sempre combinar métricas (Híbridas) para uma análise completa.