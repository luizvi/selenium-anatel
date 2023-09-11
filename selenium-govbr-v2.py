import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select
import time

user_agent = UserAgent()
random_user_agent = user_agent.random

navegador = uc.Chrome()

#Login Anatel
navegador.get("https://apps.anatel.gov.br/acesso/")
navegador.find_element('xpath', '/html/body/form/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/a').click()
navegador.find_element('xpath', '/html/body/div[1]/main/form/div/div[2]/input').send_keys('xxx')
navegador.find_element('xpath', '/html/body/div[1]/main/form/div/div[2]/div/button').click()
navegador.find_element('xpath', '/html/body/div[1]/main/form/div[1]/div[1]/input').send_keys('xxx')
navegador.find_element('xpath', '/html/body/div[1]/main/form/div[1]/div[2]/button[2]').click()
time.sleep(3)

# Area de coleta
navegador.find_element('xpath', '/html/body/form/div[4]/div/div/main/div[3]/div[2]/div[1]/span/div[3]/div/div[2]/div[2]/div/input').click()
time.sleep(3)
 #Entidade CNPJ
navegador.find_element('xpath', '/html/body/form/div[4]/div/div/main/div[3]/div/div[1]/div[1]/div/div[1]/div[2]/input').send_keys('123123000199')
 # Situação Envio - Caixa de seleção
dropdown_element = navegador.find_element('xpath', '/html/body/form/div[4]/div/div/main/div[3]/div/div[1]/div[1]/div/div[2]/select')
dropdown = Select(dropdown_element)
dropdown.select_by_value('1')
 # Data de Envio
navegador.find_element('xpath', '/html/body/form/div[4]/div/div/main/div[3]/div/div[1]/div[1]/div/div[3]/div/input').send_keys('11/09/2023')
 # Até... (Data de envio)
navegador.find_element('xpath', '/html/body/form/div[4]/div/div/main/div[3]/div/div[1]/div[1]/div/div[4]/input').send_keys('11/09/2023')
 # Pesquisar
navegador.find_element('xpath', '/html/body/form/div[4]/div/div/main/div[3]/div/div[1]/div[2]/input[1]').click()

input("Pressione Enter para fechar o navegador...")
navegador.quit()