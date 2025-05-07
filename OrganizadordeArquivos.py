import os
import shutil
import tkinter as tk
from tkinter import filedialog

DESTINATIONS = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Planilhas': ['.xls', '.xlsx', '.csv'],
    'Executáveis': ['.exe', '.msi'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Vídeos': ['.mp4', '.avi', '.mov'],
    'Outros': []  # Para o resto
}

def escolher_pasta():
    root = tk.Tk()
    root.withdraw() 
    pasta = filedialog.askdirectory(title="Selecione a pasta a ser organizada")
    return pasta

def organizar_arquivos(pasta_origem):
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

        if os.path.isfile(caminho_arquivo):
            _, ext = os.path.splitext(nome_arquivo)
            movido = False

            for pasta, extensoes in DESTINATIONS.items():
                if ext.lower() in extensoes:
                    pasta_destino = os.path.join(pasta_origem, pasta)
                    os.makedirs(pasta_destino, exist_ok=True)
                    shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
                    print(f'Movido: {nome_arquivo} → {pasta}/')
                    movido = True
                    break

            if not movido:
                pasta_outros = os.path.join(pasta_origem, 'Outros')
                os.makedirs(pasta_outros, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_outros, nome_arquivo))
                print(f'Movido: {nome_arquivo} → Outros/')

if __name__ == "__main__":
    pasta_selecionada = escolher_pasta()
    if pasta_selecionada:
        organizar_arquivos(pasta_selecionada)
    else:
        print("Nenhuma pasta foi selecionada.")
