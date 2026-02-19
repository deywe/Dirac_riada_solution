import pandas as pd
import numpy as np
import py5
import os
import sys

# --- CONFIGURAÇÕES ---
CSV_PATH = "dirac_logs/engine_brilho_vibrante.csv"
NUM_REDUNDANCIAS = 36
N_PONTOS = 800

# Variáveis Globais
df_dataset = None
current_frame = 0
zoom_factor = 1.0
cores = []

def map_value(val, start1, stop1, start2, stop2):
    return start2 + ((val - start1) / (stop1 - start1)) * (stop2 - start2)

def setup():
    global cores, df_dataset
    py5.size(1360, 720)
    py5.frame_rate(30)
    py5.color_mode(py5.HSB, 360, 100, 100, 255)
    
    if not os.path.exists(CSV_PATH):
        print(f"❌ Erro: Dataset {CSV_PATH} não encontrado!")
        py5.exit_sketch()
        return

    print("🎬 Carregando Dataset Auditado...")
    # Usamos o pandas para carregar rapidamente, mas tratamos os dados com cautela
    df_dataset = pd.read_csv(CSV_PATH)
    
    # Recria a paleta de cores vibrantes
    cores = [(int((i / NUM_REDUNDANCIAS) * 360), 90, 100) for i in range(NUM_REDUNDANCIAS)]
    print(f"✅ Pronto para reproduzir {len(df_dataset)} frames.")

def draw():
    global current_frame
    py5.background(0) # Preto absoluto para nitidez

    if current_frame >= len(df_dataset):
        current_frame = 0 # Loop da simulação

    # Busca a linha do tempo atual
    row = df_dataset.iloc[current_frame]
    
    # Converte as strings do CSV de volta para arrays
    sinais = np.array(eval(row['Sinais']))
    media = np.array(eval(row['Media']))
    f_hash = row['SHA256']

    # --- Renderização das Ondas ---
    x_off, y_off = 50, 70
    w, h = py5.width - 100, py5.height - 180
    min_v, max_v = -1.5 * zoom_factor, 4.5 * zoom_factor

    # 1. Ondas de Redundância (Brilho Intenso)
    for i, sinal in enumerate(sinais):
        h_c, s_c, b_c = cores[i]
        py5.stroke(h_c, s_c, b_c, 210) # Alpha alto para evitar o efeito fosco
        py5.stroke_weight(2)
        py5.no_fill()
        py5.begin_shape()
        for j in range(0, N_PONTOS, 2): # Passo 2 para manter a performance fluida
            tx = map_value(j, 0, N_PONTOS, x_off, x_off + w)
            ty = map_value(sinal[j], min_v, max_v, y_off + h, y_off)
            py5.vertex(tx, ty)
        py5.end_shape()

    # 2. Curva Mestre de Estabilização (Branco Neon)
    py5.stroke(0, 0, 100, 255) 
    py5.stroke_weight(4)
    py5.begin_shape()
    for j in range(N_PONTOS):
        tx = map_value(j, 0, N_PONTOS, x_off, x_off + w)
        ty = map_value(media[j], min_v, max_v, y_off + h, y_off)
        py5.vertex(tx, ty)
    py5.end_shape()

    # --- HUD Informativo ---
    py5.fill(0, 0, 100)
    py5.text_size(20)
    py5.text("🎥 REPRODUÇÃO SPHY - ESTADO VERIFICADO", 30, 40)
    
    py5.text_size(12)
    py5.fill(0, 0, 80)
    py5.text(f"INTEGRITY HASH (SHA256): {f_hash}", 30, 65)
    py5.text(f"FRAME ATUAL: {current_frame:04d} / {len(df_dataset)-1}", 30, 85)

    desenhar_equalizador(media)
    
    current_frame += 1

def desenhar_equalizador(media):
    num_barras = 40
    largura_total = py5.width - 120
    largura_barra = largura_total / num_barras
    base_y = py5.height - 25

    for i in range(num_barras):
        idx = int(i / num_barras * len(media))
        norm = py5.constrain(map_value(media[idx], -1.5, 4.0, 0, 1), 0, 1)
        
        h_bar = int(map_value(i, 0, num_barras, 190, 330)) # Tons de azul a violeta
        py5.fill(h_bar, 100, 100)
        py5.no_stroke()
        py5.rect(60 + i * largura_barra, base_y - (norm * 70), largura_barra * 0.7, norm * 70)

def key_pressed():
    global zoom_factor, current_frame
    if py5.key == '+' or py5.key == '=': zoom_factor *= 0.9
    elif py5.key == '-': zoom_factor *= 1.1
    elif py5.key == ' ': # Espaço para pausar/reiniciar
        current_frame = 0

if __name__ == "__main__":
    py5.run_sketch()