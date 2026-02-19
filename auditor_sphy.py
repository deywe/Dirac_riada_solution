import os
import hashlib
import csv
import sys
import numpy as np # Importante para garantir a formatação idêntica

# --- CONFIGURAÇÕES ---
CSV_PATH = "dirac_logs/engine_brilho_vibrante.csv"
csv.field_size_limit(sys.maxsize)

def auditar_dataset(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"❌ ERRO: Arquivo {caminho_arquivo} não encontrado.")
        return

    print(f"🔍 SINCRONIZANDO FORMATO NUMPY: {caminho_arquivo}")
    
    sucessos = 0
    falhas = 0
    
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                frame_id = row['Frame']
                media_raw = row['Media']
                hash_gravado = row['SHA256']

                # 1. Transformamos a string de volta em uma lista
                lista_temp = eval(media_raw)
                
                # 2. Convertemos para Numpy Array (como estava no Gerador)
                # O Gerador usou f"{i}{media[0:5]}" onde media era um np.array
                array_media = np.array(lista_temp)
                fatia_numpy = array_media[0:5]

                # 3. Recriamos a string EXATA que o Gerador criou
                # O f-string de um np.array não tem vírgulas, só espaços.
                check_data = f"{frame_id}{fatia_numpy}".encode()
                hash_calculado = hashlib.sha256(check_data).hexdigest()

                if hash_calculado == hash_gravado:
                    sucessos += 1
                else:
                    falhas += 1
                    if falhas <= 1:
                        print(f"🚨 DIVERGÊNCIA DE STRING NO FRAME {frame_id}")
                        print(f"   Input esperado pelo Hash: {frame_id}{fatia_numpy}")
                        print(f"   Hash Gravado:  {hash_gravado}")
                        print(f"   Hash Auditor: {hash_calculado}")

        print("-" * 60)
        print(f"📊 RESULTADO FINAL:")
        print(f"   Integridade: {sucessos} confirmados")
        print(f"   Falhas:      {falhas}")
        
        if falhas == 0:
            print("\n🏆 STATUS: VERIFICADO COM SUCESSO! A ponte de Dirac está íntegra.")
        else:
            print("\n⚠️  Dica: Se ainda falhar, use o Gerador que enviei abaixo para garantir sincronia total.")

    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == "__main__":
    auditar_dataset(CSV_PATH)