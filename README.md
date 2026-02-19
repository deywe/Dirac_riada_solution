🌌 SPHY Engine: Solução para a Riada de Dirac

O SPHY Engine é um framework de estabilização vibracional projetado para mitigar o fenômeno da Riada de Dirac (transbordamento de caminhos em campos de redundância quântica). Através de um sistema de 36 camadas de redundância e interpolação cúbica, o motor gera estados auditáveis que garantem a integridade da informação mesmo sob surtos de ruído de vácuo.
🧠 O Problema: Riada de Dirac

A Riada de Dirac ocorre quando a flutuação estocástica de múltiplos caminhos quânticos sobrecarrega a matriz de decisão, gerando instabilidades ruidosas que impedem a convergência do sinal mestre.
Formalismo Matemático

Para resolver a instabilidade, aplicamos a convergência ponderada sobre o campo de redundâncias:
ΨSPHY​=∑wr​∑r=1n​wr​⋅(I(Enum​,roll(r))+η)​=SPHY

Onde:

    I: Operador de Interpolação Cúbica.

    roll(r): Deslocamento cíclico do estado numérico r.

    η: Ruído vibracional dinâmico.

    wr​: Pesos lineares de decaimento para estabilização de borda.

🛠️ Funcionalidades Core

    Geração Auditada: Os frames são pré-calculados e assinados digitalmente com SHA256 em um dataset CSV.

    Player de Alta Fidelidade: Visualização em tempo real com modo HSB vibrante, otimizado para identificar surtos de ruído.

    Auditor Independente: Script de verificação que garante que nenhum bit do dataset foi alterado após a geração.

    Simulação de Surto: Injeção programável de instabilidades (Riada) para teste de resiliência da curva mestre.

🚀 Como Executar
Pré-requisitos

    Python 3.10+

    Pandas, Numpy, Scipy

    Py5 (Interface Visual)

Instalação
Bash

git clone https://github.com/seu-usuario/dirac-sphy.git
cd dirac-sphy
pip install pandas numpy scipy py5

Fluxo de Trabalho

    Gerar e Visualizar: Rode o script principal para criar o dataset e abrir o player.
    Bash

    python3 engine_sphy.py

    Auditar: Verifique a integridade matemática dos frames gerados.
    Bash

    python3 auditor_sphy.py

📥 Download e Recursos

Você pode baixar os binários e os datasets de exemplo nos links abaixo:

    Download SPHY Engine v1.0

    Documentação do Formalismo SPHY

📊 Visualização do Equalizador Vibracional

O Player inclui um HUD de monitoramento que exibe a energia por barra de frequência, permitindo visualizar a filtragem da Riada em tempo real.

    Nota Científica: Este projeto utiliza a constante de redundância N=36 para garantir que a média ponderada neutralize surtos de ruído superiores a 0.25σ sem perda de fase.
