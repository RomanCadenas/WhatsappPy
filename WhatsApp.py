
#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Lista de Grupos de WhatsApp para enviar Mensaje de Texto
lista = ['contacto/Grupo']

print('APLICACIÓN PARA ENVIO A CHATS O GRUPOS DE WHATSAPP')
print('')
print('')
print('')
print('             ──▄▄█▀▀▀▀▀█▄▄──')
print('             ▄█▀░░▄▄░░░░░▀█▄')
print('             █░░░███░░░░░░░█')
print('             █░░░██▄░░░░░░░█')
print('             █░░░░▀██▄░██░░█')
print('             █░░░░░░▀███▀░░█')
print('             ▀█▄░░░░░░░░░▄█▀')
print('             ─▄█░░░▄▄▄▄█▀▀──')
print('             ─█░░▄█▀────────')
print('             ─▀▀▀▀──────────')
print('==========================================')
print('GRUPOS:')
print('')
for li in lista:
    print(li)

print('')

msg = input( "Introduce el Texto a enviar: ")

#Navegador a Usar
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#driver = webdriver.Ie()

#Funcion para buscar chat y enviar mensaje
def seleccionarChat(nombre: str, mensaje: str):
    time.sleep(5)
    print("Buscando grupo")
    grupo = driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    grupo.send_keys(nombre)
    grupo.send_keys('\ue007')

    g2 = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    g2.click()
    g2.send_keys(mensaje)
    g2.send_keys(' ')
    time.sleep(2)
    g2.send_keys('\ue007')

#Funcion para validar QR
def validaQr():
    try:
        element =  driver.find_elements(By.TAG_NAME,'canvas')
        if element== []:
            return False
    except:
        return False
    return True

#Función principal
def botWhatsapp(msg: str):
    #LLanzamos el sitio que deseamos automatizar
    driver.get("https://web.whatsapp.com/")
    time.sleep(2) #Esperamos 2 segundos para carga

    #Rutina para validar que se cargue el QR para Enlazar WhatsApp
    espera = True
    while espera:
        print("Estoy Esperando")
        espera = validaQr()
        time.sleep(5)
        if espera == False:
            print("SE AUTENTICO")
            break
    
    #Seleccionamos los grupos o Chats para enviar mensaje
    for item in lista:
        seleccionarChat(item, msg)
        print("MENSAJE ENVIADO A :" + item)
        time.sleep(3)


#Iniciar Bot de envio de mensajes
botWhatsapp(msg)

