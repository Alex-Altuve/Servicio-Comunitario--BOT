from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

def alerta(mensaje_notificacion):
    # Ejecutar JavaScript para mostrar una notificación
    script = f'alert("{mensaje_notificacion}");'
    driver.execute_script(script)
    time.sleep(10)

#------VENTANA 0
# Ruta al controlador de Microsoft Edge (descárgalo previamente desde https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
# No funciono asi que lo deje asi pero hay que verificar como hacer esto 

# Inicializa las opciones del navegador Edge
options = Options()
options.use_chromium = True
options.add_argument("--disable-features=EnableEphemeralFlashPermission")


# Crea el controlador del navegador Edge con las opciones configuradas
# Inicializa el navegador Microsoft Edge
driver = webdriver.Edge(options=options)
#Esto es para inicializarlo sin configuraciones 
#driver = webdriver.Edge()

# Abre la página de Google
driver.get('https://eu.kobotoolbox.org/accounts/login/')
#Se maximiza la pantalla
driver.maximize_window()


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

    time.sleep(10) 
    check_principal = driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper > div.mdl-layout__content.page-wrapper__content.page-wrapper__content--form-landing > div.form-view.form-view--table > div.ReactTable.-highlight > div.rt-table > div.rt-thead.-filters > div > div.rt-th.rt-sub-actions.is-frozen.is-last-frozen > div > div.checkbox > label > input")
    check_principal.click()

    time.sleep(6) 
    boton_ojo = driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper > div.mdl-layout__content.page-wrapper__content.page-wrapper__content--form-landing > div.form-view.form-view--table > div.ReactTable.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div.rt-td.rt-sub-actions.is-frozen.is-last-frozen > div > button:nth-child(2)")
    boton_ojo.click()

    time.sleep(8) 
    boton_ver_form= driver.find_element(By.CSS_SELECTOR,"#kpiapp > div.mdl-layout.mdl-layout--fixed-header.page-wrapper.page-wrapper--is-modal-visible.page-wrapper--is-modal-submission > div.modal__backdrop > div > div > div > div > div:nth-child(2) > div.submission-actions > a:nth-child(3)")
    boton_ver_form.click()

    #VENTANA 1 -------------------------------------------
    ventana_form = driver.window_handles

    # Cambia el enfoque a la nueva ventana abierta
    # Puedes ajustar el índice de la lista `windows` si hay múltiples ventanas abiertas
    driver.switch_to.window(ventana_form[1])

    # Espera unos segundos para asegurarse de que la nueva ventana se cargue completamente
    time.sleep(10)

    # Encuentra y hace clic en el botón de imprimir en la nueva ventana
    boton_imprimir = driver.find_element(By.CSS_SELECTOR, "body > div.main > article > header > button.form-header__button--print.btn-bg-icon-only")
    boton_imprimir.click()
else: 
     alerta("ERROR \n El bot no puede continuar con el proceso de automatizacion ya que no ha seleccionado correctamente ninguno de los formularios")



# #ver si Peña logra hacerlo controlando el mouse (DARLE AL BOTON IMPRIMIR EN LA VENTANA EMERGENTE DEL PDF)  

# # # Hacer clic en el botón "Imprimir" en la ventana emergente
# boton_imprimir_guardar= driver.find_element(By.CSS_SELECTOR, '#sidebar > div.c01147 > div > button.c01123.c01154.c01124')
# boton_imprimir_guardar.click()


# Espera unos segundos para que los resultados se carguen las dos lineas de codigo son formas 
#driver.implicitly_wait(1200)
time.sleep(30)

# Cierra el navegador (no se porque igual se cierra solo)
driver.quit()

