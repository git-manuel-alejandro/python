from tkinter import *
from tkinter import messagebox
import csv
import os
import pandas as pd

def inicio_sesion():        
    columnas = ['Usuario', 'Password']
    count = 0
    count_letra = 0
    cont = 0
    path = "usuarios.csv"
    usuario= entry_nom.get()
    passs= entry_pass.get()
    
    if usuario == "" or passs == "" :
        messagebox.showinfo('Alerta!!', 'Todos los campos obligatorios')
        return
    
    for i in range(0, len(usuario)):       
               
        if usuario[i] == " ": 
            count += 1
        else:
            count_letra += 1
    
    if count > 0:
        messagebox.showinfo('Alerta!!', 'No debe contener espacios en blanco' )
        return
    
    if count_letra <= 3:
        messagebox.showinfo('Alerta!!', 'Largo usuario mayor o igual a tres carácteres')
        return
  
    try:  
        with open('usuarios.csv', 'r') as csvfile:
            csv_dict = [row for row in csv.DictReader(csvfile)]
            if len(csv_dict) == 0:
                cont = 1
            else:
                cont = 0
    except FileNotFoundError:       
        open("usuarios.csv", "w").close()
        data1 = [['', '']]
        df1 = pd.DataFrame(data1, columns=columnas)    
        df1.to_csv(path, index=None, mode="a", header=not os.path.isfile(path)) 
        messagebox.showinfo('Success', 'Archivo usuario creado exitosamente') 
        exit()
        
   
    if cont == 1:  
        messagebox.showinfo('Alerta!!', 'Usuario no existe, debe ser creado')         
    else:
        contusu = 0
        #con = 0
        mycsv = csv.reader(open('usuarios.csv'))

        for row2 in mycsv: 
            if row2:
                if usuario == row2[0]:
                    contusu = 1
                    if usuario == row2[0] and  passs == row2[1]:
                        messagebox.showinfo('Success', 'Bienvenido!!')
                        break
                    else:
                        messagebox.showinfo('Titulo', 'Credenciales inválidas')
                        break                    
                              
        
        if (contusu == 0):
              messagebox.showinfo('Alerta!!', 'Usuario no registrado, favor crear cuenta')   
    
           
def valida_campo():
    count = 0
    count_letra = 0
    usuario= entry_nom.get()
    passs= entry_pass.get()
    if usuario == "" or passs == "" :
        messagebox.showinfo('Alerta!!', 'Todos los campos son obligatorios')
        return
    for i in range(0, len(usuario)):       
               
        if usuario[i] == " ": 
            count += 1
        else:
            count_letra += 1
     
    if count > 0:
        messagebox.showinfo('Alerta!!', 'No debe ingresar espacios en blanco' )
        return
    
    if count_letra <= 3:
        messagebox.showinfo('Alerta!!', 'Largo mayor o igual a tres')
        return
    
    columnas = ['Usuario', 'Password']
    path = "usuarios.csv"
    cont = 0
    contusu=0 
    try:  
        with open('usuarios.csv', 'r') as csvfile:
            csv_dict = [row for row in csv.DictReader(csvfile)]
            if len(csv_dict) == 0:
                cont = 1
            else:
                cont = 0
    except FileNotFoundError:       
        open("usuarios.csv", "w").close()
        data1 = [['', '']]
        df1 = pd.DataFrame(data1, columns=columnas)    
        df1.to_csv(path, index=None, mode="a", header=not os.path.isfile(path)) 
        messagebox.showinfo('Mensaje', 'Archivo usuarios creado') 
        exit()
        
    with open('usuarios.csv', 'r') as csvfile:
            csv_dict = [row for row in csv.DictReader(csvfile)]
            if len(csv_dict) == 0:
                cont = 1
            else:
                cont = 0
    if cont == 1:  
        data1 = [[usuario, passs]]
        df1 = pd.DataFrame(data1, columns=columnas)    
        df1.to_csv(path, index=None, mode="a", header=not os.path.isfile(path))
        messagebox.showinfo('Mensaje', 'Enhorabuena!! Usuario registrado')
        return
    else:
          with open("usuarios.csv",'r') as file:
            data=file.readlines()
            i = 0
            lista = []
            repeticiones = {}
            for i, c in  enumerate(data):
                text = c.split(",")
                l1 = []
                for elem in text:
                    l1.extend(elem.strip().split(','))  
                    texto = l1[0:]
                    if usuario == texto[0]: 
                        contusu = 1  
                        break                                         
                      

    if (contusu == 1):
         messagebox.showinfo('Alerta!!', 'Usuario, ya existe')
    else:        
        data1 = [[usuario, passs]]
        df1 = pd.DataFrame(data1, columns=columnas)    
        df1.to_csv(path, index=None, mode="a", header=not os.path.isfile(path)) 
        messagebox.showinfo('Mensaje', 'Enhorabuena!! Usuario registrado')
        

#Desarrollo interfaz    
root = Tk()
root.geometry("900x720")
root.title("Login")

titulo_principal = Label(root, text="Registro usuarios", font="Arial 20 bold")
titulo_principal.pack(pady=40)

texto_inicio = Label(root, text="Nombre Usuario", font="Arial 15 bold")
texto_inicio.pack()

entry_nom = Entry(root, width=40, font="Courier 16", bg="White")
entry_nom.pack()


texto_pass = Label(root, text="Contraseña", font="Arial 15 bold", anchor="e")
texto_pass.pack()

entry_pass = Entry(root, width=40, font="Courier 16", bg="White", show="*")
entry_pass.pack()

btn = Button(root, text="Inicio Sesión", font="Arial 14", width=20, height=2, 
             relief="solid", borderwidth=4, bg="white", command=inicio_sesion)
btn.pack(pady=20)

btn_2 = Button(root, text="Crear Cuenta", font="Arial 14", width=20, height=2, 
             relief="solid", borderwidth=4, bg="white", command=valida_campo)
btn_2.pack(pady=20)

root.mainloop()