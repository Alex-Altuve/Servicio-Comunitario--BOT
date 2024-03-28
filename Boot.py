from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui  as pa
import time
from datetime import datetime, timedelta
import re
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select

def alerta(mensaje_notificacion): 

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
    #CODIGO UNICO 
    contenedor_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper.page-wrapper--is-modal-visible.page-wrapper--is-modal-submission > div.modal__backdrop > div > div > div > div > div.submission-data-table > div.submission-data-table__row.submission-data-table__row--group.submission-data-table__row--type-group_root > div.submission-data-table__row.submission-data-table__row--group-children > div:nth-child(2)'))
    )

    # Obtener todos los elementos dentro del contenedor div
    elementos = contenedor_div.find_elements(By.TAG_NAME, 'div')

    # Recorrer los elementos y verificar si contienen el texto deseado
    for i, elemento in enumerate(elementos):
        texto = elemento.text
        if'¿A qué proyecto se reportan las actividades que se van a realizar?' in texto:
        # Verificar si existe un elemento siguiente
            if i + 1 < len(elementos):
                elementoSiguiente = elementos[i + 1]
                nombre_proyecto = elementoSiguiente.text


        if 'Fecha en la que se realiza la atención' in texto:
            if i + 1 < len(elementos):
                elementoSiguiente = elementos[i + 1]
                fecha = elementoSiguiente.text

        # Verificar si el texto cumple con la condición deseada
        if 'Código único asignado a la PERSONA REGISTRADA' in texto:
            if i + 1 < len(elementos):
                elementoSiguiente = elementos[i + 1]
                codigo_unico = elementoSiguiente.text

    
    #Validamos el formato del codigo unico 
    #patron = r'^[A-Za-z]{4}\d{4}[A-Za-z]{3}$'
    patron = r'^[A-Z]{4}\d{8}[A-Z]{3}$'
    es_valido = re.match(patron, codigo_unico)

    if es_valido is None:
        alerta("El nombre unico no cumple el formato, este problema seguramente esta ocurriendo porque no cumple con el formato o el formulario no es compatible con el programa, porfavor, contactar con el desarrollador")
        time.sleep(10)
        driver.quit()

    # Guardar el valor de Fecha y validamos el formato de la fecha 
    patro = r'^\d{1,2} de (ene\.?|feb\.?|mar\.?|abr\.?|may\.?|jun\.?|jul\.?|ago\.?|sep\.?|oct\.?|nov\.?|dic\.?) de \d{4}$'

    valida = re.match(patro, fecha)
    if valida is None:
        alerta("La fecha no cumple el formato, este problema seguramente esta ocurriendo porque no cumple con el formato o el formulario no es compatible con el programa, porfavor, contactar con el desarrollador")
        time.sleep(10)
        driver.quit()

    fecha_nueva = modificar_fecha(fecha)
    # Guardar el valor del Nombre del Proyecto
    nom = codigo_unico + fecha_nueva + nombre_proyecto.upper()
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
    if  (siguiente.text == "ANTERIOR") or (siguiente.text=="BACK"):
        alerta("Ingreso un numero el cual no esta entre los permitidos se alcanzo el limite por lo tanto se cerrara el programa")
        time.sleep(10)
        driver.quit()
    else:
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
    time.sleep(6)
    imprimir= driver.find_element(By.XPATH, '/html/body/div[1]/article/header/button[1]')

    # Obtiene las coordenadas absolutas del botón en la pantalla
    x_absoluto = imprimir.location['x']
    y_absoluto = imprimir.location['y']

    #Click al boton de la impresora 
    pa.moveTo(x_absoluto, y_absoluto+123, duration=3)
    pa.click(x_absoluto,y_absoluto+123)
    time.sleep(4)
    #enter para presioanr el boton de guardar/imprimir  
    pa.press('enter')
    time.sleep(4)
    #Se escribe el nombre del PDF
    pa.typewrite(nom)
    #Guardar  el archivo con el nombre 
    pa.press('enter')
    time.sleep(4)
    driver.close()
    driver.switch_to.window(ventana_form[0])

def calcular_diferencia(numero):
    veces_resta = 0

    while numero > 500:
        numero -= 500
        veces_resta += 1

    return numero, veces_resta

#INICIO DEL CODIGO 
#------VENTANA 0
# Ruta al controlador de Microsoft Edge (descárgalo previamente desde https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
print(pa.size())
print(pa.position()) 

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


#usuario=driver.find_element(By.NAME, "login")
#usuario.send_keys('pasante_monitoreo')
#contrasena=driver.find_element(By.NAME,'password')
#contrasena.send_keys('1/fyV2g(H1h')
#contrasena.submit()

alerta("Debe ingresar su usuario y contraseña para que el bot pueda continuar")
#Pausa para que el usuario ingrese su usuario y contraseña
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

    #Se seleeciona para que se muestren 500 filas, para asi buscar mas eficientemente
    seleccionar_cant_filas= driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper > div.mdl-layout__content.page-wrapper__content.page-wrapper__content--form-landing > div.form-view.form-view--table > div.ReactTable.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select")
    select= Select(seleccionar_cant_filas)
    select.select_by_value("500")
    
    #Se espera a que cargue
    time.sleep(5) 

    
    #Se piden de donde a donde al usuario
    # Solicitar un número al usuario
    numero_inicio = pa.prompt(text='Por favor, ingrese un número desde donde iniciar')
    if(re.match("^[0-9]+$", numero_inicio)):
        numero_inicio=int(numero_inicio)
        posicion_ojito, veces_next = calcular_diferencia(numero_inicio)
        numero_pdf = pa.prompt(text='Por favor, ingrese la cantidad de PDFs a descargar')
        if (re.match("^[0-9]+$", numero_pdf)):
            numero_pdf=int(numero_pdf)
            alerta("Porfavor, no tocar ni el mouse ni el teclado hasta terminar con el proceso")
            time.sleep(6)
            sig= driver.find_element(By.XPATH, '//*[@id="kpiapp"]/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[3]/button')
            #le damos tantas veces a siguiente para llegar al archivo que queramos, con esto me refiero a la pagina 
            for i in  range(1,veces_next+1):
                sig.click()
                time.sleep(5)    
            #seleccionamos el ojito donde queremos descargar el pdf
            ojitos = driver.find_elements(By.CSS_SELECTOR,'button[data-tip="Abrir"]')
            ojitos[posicion_ojito-1].click() 
            time.sleep(6)
            
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

# Espera unos segundos para que los resultados se carguen 
time.sleep(10)

# Cierra el navegador 
driver.quit()

