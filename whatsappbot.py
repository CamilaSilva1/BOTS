#Criado por Camila Silva
#Este script é responsavel pela criação completa do bot para WhatsApp

#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegar ate o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.whatsapp.com')
time.sleep(30)

#definir contatos e grupos e mensagens a serem enviadas
contatos = ['Grupo eu']
mensagem = 'Olá?'

#buscar contatos ou grupos
def buscar_contato(contato):
   campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
   time.sleep(3)
   campo_pesquisa.click()
   campo_pesquisa.send_keys(contato)
   campo_pesquisa.send_keys(Keys.ENTER)

#enviar mensagens pra eles
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(4)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(4)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

#campo de pesquisa  'copyable-text selectable-text'
#campo de mensagem privada  'copyable-text selectable-text'

