from tkinter import *
from tkinter import ttk

def login():
    username = entry_username.get()
    password = entry_password.get()
    print(username)
    print(password)
    

root = Tk()
root.title("AVESSOC - Login Bot")
root.resizable(0,0)
root.iconbitmap("logo.ico")
root.configure(bg="darkslategray")

#---------------------PARA CENTRAR LA VENTANA
# Obtener la resolución de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (screen_width - 500) // 2
y = (screen_height - 500) // 2

# Establecer las coordenadas de la ventana
root.geometry(f"{500}x{500}+{x}+{y}")

# Crear estilo para los campos de entrada
style = ttk.Style()
style.configure("Custom.TEntry", padding=4, relief=SOLID, borderwidth=2)

#Imagen de avessoc
imagen= PhotoImage(file="1.png")
Label(root, image=imagen, bd=0).pack()

#----LABELS Y BOTON DE INICIAR SESION
label_username = Label(root, text="Usuario", bg="white", fg="black")
label_username.pack(pady=10)  # Añadir espacio arriba

entry_username = ttk.Entry(root, width=30, style="Custom.TEntry")  # Establecer ancho a 30 caracteres y aplicar estilo personalizado
entry_username.pack(pady=5)  # Añadir espacio arriba

label_password = Label(root, text="Contraseña", bg="white", fg="black")
label_password.pack(pady=10)  # Añadir espacio arriba

entry_password = ttk.Entry(root, show="*", width=30, style="Custom.TEntry")  # Establecer ancho a 30 caracteres y aplicar estilo personalizado
entry_password.pack(pady=5)  # Añadir espacio arriba

button_login = Button(root, text="Login", command=login)
button_login.pack(pady=10)  # Añadir espacio arriba


# Centrar horizontalmente y verticalmente los componentes
for widget in root.winfo_children():
    widget.pack_configure(anchor='center', side='top', padx=10)

root.mainloop()