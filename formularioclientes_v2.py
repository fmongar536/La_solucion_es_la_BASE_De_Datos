import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import clientes


class FormularioClientes:
    def __init__(self):
        self.cliente1=clientes.Clientes()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de clientes")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_clientes()                           #Llamamos a las diferentes funciones que "pintan" el contenido de la ventana.
        self.consulta_de_cliente()                      
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_clientes(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de Clientes")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Cliente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

    # Nombre
        self.label1 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrecarga = tk.StringVar()
        self.entrynombre = ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)

    # Apellidos
        self.label2 = ttk.Label(self.labelframe1, text="Apellidos:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.apellidoscarga = tk.StringVar()
        self.entryapellidos = ttk.Entry(self.labelframe1, textvariable=self.apellidoscarga)
        self.entryapellidos.grid(column=1, row=1, padx=4, pady=4)

    # DNI
        self.label3 = ttk.Label(self.labelframe1, text="DNI:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.dnicarga = tk.StringVar()
        self.entrydni = ttk.Entry(self.labelframe1, textvariable=self.dnicarga)
        self.entrydni.grid(column=1, row=2, padx=4, pady=4)

    # Fecha nacimiento
        self.label4 = ttk.Label(self.labelframe1, text="Fecha nacimiento:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.nacimientocarga = tk.StringVar()
        self.entrynacimiento = ttk.Entry(self.labelframe1, textvariable=self.nacimientocarga)
        self.entrynacimiento.grid(column=1, row=3, padx=4, pady=4)

    # Teléfono
        self.label5 = ttk.Label(self.labelframe1, text="Teléfono:")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.telefonocarga = tk.StringVar()
        self.entrytelefono = ttk.Entry(self.labelframe1, textvariable=self.telefonocarga)
        self.entrytelefono.grid(column=1, row=4, padx=4, pady=4)

    # Correo
        self.label6 = ttk.Label(self.labelframe1, text="Correo:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.correocarga = tk.StringVar()
        self.entrycorreo = ttk.Entry(self.labelframe1, textvariable=self.correocarga)
        self.entrycorreo.grid(column=1, row=5, padx=4, pady=4)

    # Dirección
        self.label7 = ttk.Label(self.labelframe1, text="Dirección:")
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.direccioncarga = tk.StringVar()
        self.entrydireccion = ttk.Entry(self.labelframe1, textvariable=self.direccioncarga)
        self.entrydireccion.grid(column=1, row=6, padx=4, pady=4)

    # Botón Confirmar
        self.boton1 = ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    def agregar(self):
        datos = (
            self.nombrecarga.get(),
            self.apellidoscarga.get(),
            self.dnicarga.get(),
            self.nacimientocarga.get(),
            self.telefonocarga.get(),
            self.correocarga.get(),
            self.direccioncarga.get()
        )
        self.cliente1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados.")

    # Limpiar campos
            self.nombrecarga.set("")
            self.apellidoscarga.set("")
            self.dnicarga.set("")
            self.nacimientocarga.set("")
            self.telefonocarga.set("")
            self.correocarga.set("")
            self.direccioncarga.set("")


    def consulta_de_cliente(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta de cliente")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Cliente")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Apellidos:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.apellidos=tk.StringVar()
        self.entryapellidos=ttk.Entry(self.labelframe2, textvariable=self.apellidos, state="readonly")
        self.entryapellidos.grid(column=1, row=1, padx=4, pady=4)

        [...]

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)

    def consultar(self):
        datos=(self.dni.get(), )
        respuesta=self.cliente1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][0])
            [...]
        else:
            self.nombre.set('')
            [...]
            mb.showinfo("Información", "No existe un cliente con dicho DNI.")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Clientes")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.cliente1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Nombre:"+fila[0]+"\nApellidos:"+fila[1]+ [...] +"\n\n")
            


aplicacion1=FormularioClientes()
