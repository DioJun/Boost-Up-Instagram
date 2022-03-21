import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import time

# Abrindo o navegador
driver = webdriver.Edge()
driver.get("https://www.instagram.com/accounts/login/?hl=pt-br")

# Inserindo Login e Senha
time.sleep(10)
login = input("Digite seu Login: ")
senha = input("Digite sua Senha: ")

# Inserindo as 'hashtags' em uma lista para uso posterior
ht1 = input("Primeira hashtag: ")
ht2 = input("Segunda hashtag: ")
ht3 = input("Terceira hashtag: ")
ht4 = input("Quarta hashtag: ")
ht5 = input("Quinta hashtag: ")

hashtags = [ht1, ht2, ht3, ht4, ht5]


# Localizando e guardando em uma lista as primeiras 9 imagens para uso posterior
def like_posts():

    time.sleep(10)
    imglink = driver.find_elements_by_tag_name('a')
    imglink = [a.get_attribute('href') for a in imglink]
    imglink = [a for a in imglink if str(a).startswith("https://www.instagram.com/p/")]
    imglink[:8]

    # Utilizando O BeautifulSoup para curtir a publicação
    for like in imglink:
        time.sleep(5)
        lk = driver.get(like)
        time.sleep(10)
        lk = driver.find_element_by_class_name('fr66n')
        soup = bs(lk.get_attribute('innerHTML'),'html.parser')
        if(soup.find('svg')['aria-label'] == 'Curtir'):
            lk.click()
        time.sleep(5)
        print(like, " foi curtido!")
        time.sleep(20)

def hashtag():
    for catg in hashtags:
            # Selecionando ferramenta de Busca e deixando-a em branco para inserir algo
            searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pesquisar']")))
            searchbox.clear()

            # Utilização da ferramenta de Busca com a Hastag
            searchbox.send_keys(catg)
            time.sleep(3)
            searchbox.send_keys(Keys.ARROW_DOWN)
            time.sleep(3)
            searchbox.send_keys(Keys.ENTER)

            like_posts()

def run_auto_insta():
    
    # Localizando entradas de 'Usuário' e 'Senha'
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    # Deixando entradas em branco para utilização das informações inseridas 
    username.clear()
    username.send_keys(login)
    password.clear()
    password.send_keys(senha)

    # Fazendo Login
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Espera de 5 segundos para negar questões desnecessárias
    time.sleep(5)
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()
    alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()

    hashtag()

    print('## Boost Up Instagram ## Finalizou com SUCESSO!! ')

run_auto_insta()