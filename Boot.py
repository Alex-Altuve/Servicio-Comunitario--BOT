from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import pyautogui  as pa
import time
from datetime import datetime, timedelta
import re


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
    copiando_fecha=driver.find_element(By.CSS_SELECTOR, '#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper.page-wrapper--is-modal-visible.page-wrapper--is-modal-submission > div.modal__backdrop > div > div > div > div > div.submission-data-table > div.submission-data-table__row.submission-data-table__row--group.submission-data-table__row--type-group_root > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(2) > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(8) > div.submission-data-table__column.submission-data-table__column--data > div')
    texto2=copiando_fecha.text
    texto2=modificar_fecha(texto2)
    print(texto+texto2)

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


#------VENTANA 0
# Ruta al controlador de Microsoft Edge (descárgalo previamente desde https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

print(pa.size())#en la mia es 1920x1080
print(pa.position())#(x=143, y=961) esto para darle al boton imprimir, (x=170, y=435)Para escribir el nombre, (x=793, y=504)para guardarlo con el nombre 

# Inicializa las opciones del navegador Chrome
options = Options()
options.add_argument("--disable-features=EnableEphemeralFlashPermission")

# Crea el controlador del navegador Chrome con las opciones configuradas
# Inicializa el navegador Microsoft chrome
driver = webdriver.Chrome(options=options)


# Abre la página de Google
driver.get('https://eu.kobotoolbox.org/accounts/login/')
#Se maximiza la pantalla
driver.maximize_window()
time.sleep(6)

#PARA PROBAR 
# usuario=driver.find_element(By.NAME, "login")
# usuario.send_keys('pasante_monitoreo')
# contrasena=driver.find_element(By.NAME,'password')
# contrasena.send_keys('1/fyV2g(H1h')
# contrasena.submit()

alerta("Debe ingresar su usuario y contraseña para que el bot pueda continuar")
# Pausa para que el usuario ingrese su usuario y contraseña
while True:
    if driver.current_url != 'https://eu.kobotoolbox.org/accounts/login/':
        break
    time.sleep(0.1)

# Esperar a que la página se cargue completamente
driver.implicitly_wait(15)

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
    time.sleep(6) 
    enlace_datos_form= driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper > div.mdl-layout__content.page-wrapper__content.page-wrapper__content--form-landing > nav > ul > li:nth-child(3)")
    enlace_datos_form.click()
    #Se espera a que cargue
    time.sleep(6) 
    ojitos = driver.find_elements(By.CSS_SELECTOR,'button[data-tip="Abrir"]')
  
   
    numero_ingresado = pa.prompt(text='Por favor, ingrese un número desde donde iniciar')

    if(re.match("^[0-9]+$", numero_ingresado)):
        numero= int(numero_ingresado)
        print("Número convertido:", numero)
        ojitos[0].click() 
        time.sleep(6)
        #le damos tantas veces a siguiente para llegar al archivo que queramos 
        for i in  range(1,numero):
            pasar_siguiente()
        
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
        #print(len(ventana_form))
        # Espera unos segundos para asegurarse de que la nueva ventana se cargue completamente
        time.sleep(10)

        # Encuentra y hace clic en el botón de imprimir en la nueva ventana
        boton_imprimir = driver.find_element(By.CSS_SELECTOR, "body > div.main > article > header > button.form-header__button--print.btn-bg-icon-only")
        boton_imprimir.click()
    
        time.sleep(10)
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

