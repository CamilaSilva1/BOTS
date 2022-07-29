#Criado por Camila Silva
#Este script é responsavel pela criação completa do bot para Instagram

#importando as bibliotecas
from selenium import webdriver
import time
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#setando username e senha para acessar a conta no Instagram
class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    #bot realizando o login com o preenchimento dos fieldsets
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')  
        time.sleep(2)     
        campo_login = driver.find_element_by_xpath("//input[@name='username']")
        campo_login.send_keys(self.username)

        campo_login = driver.find_element_by_xpath("//input[@name='password']")
        campo_login.send_keys(self.password)
        time.sleep(2)
        campo_login.send_keys(Keys.RETURN)
        time.sleep(4)

        salvar_info = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        salvar_info.click()
        time.sleep(4)

        salvar_info = driver.find_element_by_xpath(" /html/body/div[4]/div/div/div/div[3]/button[2]")
        salvar_info.click()
        self.procurar_perfil('camila_da_silva_assis')
        
    #bot procurando pelo perfil pesquisado
    def procurar_perfil(self, nome):
        driver = self.driver
        driver.get('https://www.instagram.com/' + nome + '/')
        
        
       
#setando email e senha ao bot (email e senha ficticios)
camilaBot = instagramBot('camila1234@gmail.com', '123')
#chamando função login
camilaBot.login()





   
   
  







