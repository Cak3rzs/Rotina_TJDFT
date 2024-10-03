import os
import requests
import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


navegador = webdriver.Chrome()
navegador.get("https://pesquisadje.tjdft.jus.br")


try:
    fechar_aviso = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div/span'))
    )
    fechar_aviso.click()
    print("Aviso fechado com sucesso")
except Exception as e:
    print("Aviso não apareceu ou não foi possível fechar.")

try:
    abrir_diario = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ultimasEdicoes"]/ul/li[1]/a[1]'))
    )
    diario_numero = abrir_diario.get_attribute("href").split('/')[-1]  
    print(f"Número do diário mais recente: {diario_numero}")

   
    pdf_url = f"https://pesquisadje-api.tjdft.jus.br/v1/diarios/pdf/2024/{diario_numero.split('.')[0]}.pdf"
    print(f"URL do PDF: {pdf_url}")

    response = requests.get(pdf_url)

    
    script_dir = os.getcwd()  
    nome_pdf = f'diario_{diario_numero.split(".")[0]}.pdf'  

    if response.status_code == 200:
       
        caminho_pdf = os.path.join(script_dir, nome_pdf)
        with open(caminho_pdf, 'wb') as file:
            file.write(response.content)
        print(f"PDF baixado com sucesso! Nome do arquivo: {caminho_pdf}")
    else:
        print(f"Falha ao baixar o PDF: Status Code {response.status_code}")

except Exception as e:
    print(f"Não foi possível abrir o PDF ou capturar a URL: {e}")


def ler_pdf(pdf_path):
    
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_paginas = len(pdf_reader.pages)
            print(f"Número de páginas: {num_paginas}")

            
            for pagina in range(num_paginas):
                pagina_conteudo = pdf_reader.pages[pagina].extract_text()
                print(f"\nConteúdo da Página {pagina + 1}:\n{pagina_conteudo}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {pdf_path}")


pdf_path = f'diario_{diario_numero}.pdf'


ler_pdf(pdf_path)
