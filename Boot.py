from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import pyautogui  as pa
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import re
from selenium.common.exceptions import NoAlertPresentException

def alerta(mensaje_notificacion): ## PROBAR
    # Ejecutar JavaScript para mostrar una notificación
    script = f'alert("{mensaje_notificacion}");'
    driver.execute_script(script)
  # Esperar hasta que aparezca la alerta
    wait = WebDriverWait(driver, 10)
    while True:
        try:
            alert = wait.until(EC.alert_is_present())

            # Verificar si el usuario ha interactuado con la notificación
            if alert.text == mensaje_notificacion:
                # Esperar a que el usuario interactúe manualmente
                while True:
                    time.sleep(5)  # Pausa de 1 segundo
                    try:
                        alert.accept()
                        break
                    except NoAlertPresentException:
                        break

                break

        except NoAlertPresentException:
            break
def nombrepdf():
    copiando_nombre=driver.find_element(By.CSS_SELECTOR, '#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper.page-wrapper--is-modal-visible.page-wrapper--is-modal-submission > div.modal__backdrop > div > div > div > div > div.submission-data-table > div.submission-data-table__row.submission-data-table__row--group.submission-data-table__row--type-group_root > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(2) > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(16) > div.submission-data-table__column.submission-data-table__column--data > div')
    texto=copiando_nombre.text
    print(texto)
    copiando_fecha=driver.find_element(By.CSS_SELECTOR, '#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper.page-wrapper--is-modal-visible.page-wrapper--is-modal-submission > div.modal__backdrop > div > div > div > div > div.submission-data-table > div.submission-data-table__row.submission-data-table__row--group.submission-data-table__row--type-group_root > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(2) > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(8) > div.submission-data-table__column.submission-data-table__column--data > div')
    texto2=copiando_fecha.text
    print(texto2)
    texto2=modificar_fecha(texto2)
    print(texto+texto2)
    nom=texto+texto2
    return nom


def modificar_fecha(fecha):
    # Definir mapeo de nombres de meses en español a números de mes
    meses = {
        'ene': '01',
        'feb': '02',
        'mar': '03',
        'abr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'ago': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dic': '12'
    }

    # Convertir el string de entrada a minúsculas
    fecha = fecha.lower()

    # Obtener día, mes y año de la fecha
    partes = fecha.split()
    dia = partes[0]
    mes = partes[2].rstrip('.')  # Eliminar el punto al final del nombre del mes
    anio = partes[4]

    # Convertir la fecha al formato AAAAMMDD
    fecha_modificada = anio + meses[mes] + dia

    # Restar un día a la fecha
    fecha_dt = datetime.strptime(fecha_modificada, '%Y%m%d')
    fecha_modificada = (fecha_dt + timedelta(days=1)).strftime('%Y%m%d')

    return fecha_modificada

def pasar_siguiente():

    siguiente=driver.find_element(By.CLASS_NAME, 'submission-pager')
    siguiente.click()
    time.sleep(6)
    pass

def descargar_pdf():
    nom=nombrepdf()
    time.sleep(6)
    boton_ver_form= driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper.page-wrapper--is-modal-visible.page-wrapper--is-modal-submission > div.modal__backdrop > div > div > div > div > div:nth-child(2) > div.submission-actions > a:nth-child(3)")
    boton_ver_form.click()
    time.sleep(6)
    
    #VENTANA 1 -------------------------------------------
    ventana_form = driver.window_handles

    # Cambia el enfoque a la nueva ventana abierta
    # Puedes ajustar el índice de la lista `windows` si hay múltiples ventanas abiertas
    driver.switch_to.window(ventana_form[1])

    # Esperar hasta que el elemento de destino esté presente en la página
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/article/header/button[1]')))
    pa.moveTo(x=1284, y=178, duration=3)
    pa.click(x=1284, y=178)
    pa.tripleClick()
    time.sleep(4)
    pa.moveTo(x=1456, y=902, duration=3)
    pa.click(x=1456, y=902)
    pa.tripleClick()
    time.sleep(4)
    pa.typewrite(nom)
    pa.press('enter')
    time.sleep(4)
    driver.close()
    driver.switch_to.window(ventana_form[0])
#------VENTANA 0
# Ruta al controlador de Microsoft Edge (descárgalo previamente desde https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
# No funciono asi que lo deje asi pero hay que verificar como hacer esto 
print(pa.size())#en la mia es 1920x1080
print(pa.position())#(x=143, y=961) esto para darle al boton imprimir, (x=170, y=435)Para escribir el nombre, (x=793, y=504)para guardarlo con el nombre 
# Inicializa las opciones del navegador Chrome
options = Options()
options.add_argument("--disable-features=EnableEphemeralFlashPermission")


# Crea el controlador del navegador Chrome con las opciones configuradas
# Inicializa el navegador Microsoft chrome
driver = webdriver.Chrome(options=options)
#Esto es para inicializarlo sin configuraciones 
#driver = webdriver.Edge()

# Abre la página de Google
driver.get('https://eu.kobotoolbox.org/accounts/login/')
#Se maximiza la pantalla
driver.maximize_window()

time.sleep(6)
#usuario=driver.find_element(By.NAME, "login")
#usuario.send_keys('pasante_monitoreo')
#contrasena=driver.find_element(By.NAME,'password')
#contrasena.send_keys('1/fyV2g(H1h')
#contrasena.submit()
alerta("Debe ingresar su usuario y contraseña para que el bot pueda continuar")
# Pausa para que el usuario ingrese su usuario y contraseña
while True:
    if driver.current_url != 'https://eu.kobotoolbox.org/accounts/login/':
        break
    time.sleep(0.1)
# Esperar a que la página se cargue completamente
driver.implicitly_wait(10)

#Variable necesarias para validacion
enlaces_url = []
validacion=False

enlaces = driver.find_elements(By.XPATH, '//a[not(@class) and contains(@href, "summary")]')
if( len(enlaces)!=0):
    for elemento in enlaces:
        url_enlace = elemento.get_attribute("href")
        enlaces_url.append(url_enlace)
else: 
     alerta("Ha ocurrido un error al continuar con el proceso con el bot, por favor, apague el bot e intente de nuevo")
     time.sleep(8)
     driver.quit()

alerta("Debe seleccionar un formulario para que el bot pueda continuar con el proceso de automatización")

#Pausa para que el usuario seleccione el formulario
while True:
    if driver.current_url != 'https://eu.kobotoolbox.org/#/projects/home':
        break
    time.sleep(0.1)

for url_enlace in enlaces_url:
    if driver.current_url == url_enlace :
        validacion=True
        break

#Valida si verdaderamente selecciono un formulario (Esta automatizacion aplica para todos los formularios que seleccione)
if validacion == True:

    time.sleep(5) 
    enlace_datos_form= driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper > div.mdl-layout__content.page-wrapper__content.page-wrapper__content--form-landing > nav > ul > li:nth-child(3)")
    enlace_datos_form.click()
    #Se espera a que cargue

    time.sleep(5) 
    ojitos = driver.find_elements(By.CSS_SELECTOR,'button[data-tip="Abrir"]')
    #Se piden de donde a donde al usuario
    # Solicitar un número al usuario
    numero_inicio = pa.prompt(text='Por favor, ingrese un número desde donde iniciar')
    #numero_inicio = int(input("Por favor, ingrese el numero desde donde iniciar: "))
    if(re.match("^[0-9]+$", numero_inicio)):
        numero_inicio=int(numero_inicio)
        numero_pdf = pa.prompt(text='Por favor, ingrese la cantidad de PDFs a descargar')
        #numero_pdf=int(input("Por favor, ingrese la cantidad de archivos a descargar: "))
        if (re.match("^[0-9]+$", numero_pdf)):
            numero_pdf=int(numero_pdf)
            #seleccionamos el primer ojito para llegar al que queremos esto por ahora
            ojitos[0].click() 
            time.sleep(6)
            #le damos tantas veces a siguiente para llegar al archivo que queramos 
            for i in  range(1,numero_inicio):
                pasar_siguiente()

            #Se abre ventana 1 para la descarga de archivos
            for i in range(1,numero_pdf+1):
                descargar_pdf()
                if(i!=numero_pdf):
                    pasar_siguiente()
        else:
            alerta("ERROR Solo se aceptan numeros en el campo solicitado anteriormente")
            time.sleep(8)
            driver.quit()
    else:
        alerta("ERROR Solo se aceptan numeros en el campo solicitado anteriormente")
        time.sleep(8)
        driver.quit()  
else: 
    alerta("ERROR El bot no puede continuar con el proceso de automatizacion ya que no ha seleccionado correctamente ninguno de los formularios")
    time.sleep(8)
    driver.quit()

# Espera unos segundos para que los resultados se carguen las dos lineas de codigo son formas 
#driver.implicitly_wait(1200)
time.sleep(10)

# Cierra el navegador (no se porque igual se cierra solo)
driver.quit()

