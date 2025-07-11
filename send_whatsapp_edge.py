import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configurações
NUMBER = "+5511947419444"
CSV_PATH = os.path.join(BASE_DIR, "messages.csv")
EDGE_DRIVER_PATH = os.path.join(BASE_DIR, "edgedriver_win64", "msedgedriver.exe")
EDGE_PROFILE_PATH = os.path.join(BASE_DIR, "edge_profile")

def enviar_mensagem(numero, mensagem):
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    driver.get(url)
    
    try:
        # Espera a caixa de mensagem carregar e enviar a mensagem
        send_box = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        time.sleep(2)  # esperar carregar direito
        
        # Pressiona ENTER para enviar
        send_box.send_keys("\n")
        print(f"Mensagem enviada: {mensagem}")
        
        time.sleep(5)  # tempo para enviar e evitar problemas
    except Exception as e:
        print(f"Erro ao enviar mensagem: {mensagem}. Erro: {e}")

if __name__ == "__main__":
    # Configurar o driver Edge
    options = Options()
    options.add_argument(f"user-data-dir={EDGE_PROFILE_PATH}")  # perfil para evitar QR code toda hora
    options.add_argument("--profile-directory=Default")
    service = EdgeService(EDGE_DRIVER_PATH)
    
    driver = webdriver.Edge(service=service, options=options)
    
    driver.get("https://web.whatsapp.com")
    print("Aguardando login no WhatsApp Web, se necessário...")
    
    # Espera o usuário logar manualmente, ou se já estiver logado pelo perfil, espera carregar
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "app"))
    )
    print("WhatsApp Web carregado.")
    
    # Ler CSV
    df = pd.read_csv(CSV_PATH)
    
    for idx, row in df.iterrows():
        projeto = row['Projeto']
        mensagem = row['Mensagem']
        texto = f"{projeto} - Mensagem: {mensagem}"
        enviar_mensagem(NUMBER, texto)
    
    print("Todas as mensagens enviadas.")
    driver.quit()
