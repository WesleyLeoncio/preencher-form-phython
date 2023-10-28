from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui
import random

navegador = webdriver.Chrome()

url = 'https://forms.gle/edAQca2c1QT3vPsM7'

bairros = [
 'Centro',
 'Santa lucia',
 'Santa Rosa' ,
 'Santos Dumont',
 'Catalão ',
 'São José ',
 'Porto velho ',
 'Maria Peçanha',
 'Niterói ',
 'Maria Helena',
 'Ferrador ',
 'Bom pastor ',
 'Halim souki ',
 'Sidil',
 'Interlagos',
 'Paraíso ',
 'Padre Eustáquio',
 'Davanuze ',
 'Nova holanda ',
 'Santa Tereza ',
 'Jardinópolis ',
 'Esplanada',
]
selectXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
selectOptionXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]/span'
sabendoID = 'i15'
canalXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
bairroXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
botao = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

canalTextInput = 'email'
def aleatorioLojas(a,b):
    return '{}'.format(random.randint(a,b))

def aleatorioBairro(a,b):
    bairro = random.randint(a,b)
    return bairros[bairro]

for i in range(200):
    navegador.get(url)

    pyautogui.sleep(2)
# CAMPO Select
    navegador.find_element(By.XPATH, selectXPATH).click()
    pyautogui.sleep(0.5)
    navegador.find_element(By.XPATH, selectOptionXPATH).click()
    pyautogui.sleep(0.5)

# CAMPO Sabendo
    navegador.find_element(By.ID, sabendoID).click()

# CAMPO Canal
    navegador.find_element(By.XPATH, canalXPATH).send_keys(canalTextInput)

# CAMPO Bairro
    navegador.find_element(By.XPATH, ).send_keys(aleatorioBairro(0,20))

# CAMPO Botao
    navegador.find_element(By.XPATH, botao).click()
    pyautogui.sleep(2)