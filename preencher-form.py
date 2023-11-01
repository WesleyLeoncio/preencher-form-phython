from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui
import random

navegador = webdriver.Chrome()

url = 'https://forms.gle/kxWXNAP6JzRLDCe76'

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

arrayIdCanaisDeOferta = ['i15', 'i9', 'i12']

arrayIdOutroCanaisOferta = ['i49','i46','i55']

def aleatorioArrays(a,b):
    return random.randint(a,b)

def aleatorioBairro(a,b):
    bairro = random.randint(a,b)
    return bairros[bairro]

selectXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
selectOptionXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]/span'

canalOfertaID = arrayIdCanaisDeOferta[aleatorioArrays(0,2)]
outroCanalOfertaID = arrayIdOutroCanaisOferta[aleatorioArrays(0,2)]

bairroXPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
botao = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'


for i in range(200):
    navegador.get(url)

    pyautogui.sleep(2)
# CAMPO Select
    navegador.find_element(By.XPATH, selectXPATH).click()
    pyautogui.sleep(0.5)
    navegador.find_element(By.XPATH, selectOptionXPATH).click()
    pyautogui.sleep(0.5)

# CAMPO Canal oferta
    navegador.find_element(By.ID, canalOfertaID).click()
    
# CAMPO Outro Canal Oferta
    navegador.find_element(By.ID, outroCanalOfertaID).click()


# CAMPO Bairro
    navegador.find_element(By.XPATH, bairroXPATH).send_keys(aleatorioBairro(0,18))

# CAMPO Botao
    navegador.find_element(By.XPATH, botao).click()
    pyautogui.sleep(2)