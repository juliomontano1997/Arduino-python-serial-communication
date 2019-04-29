from tkinter import *
import time
import serial
try:
    arduino = serial.Serial("COM4", 9600)
    time.sleep(1) 
except: 
    print("Verifica que el arduino este conectado")
    x = input("Ok")
    exit()

def enviar_dato():    
    if var.get()==1:  
        mensajes.config(text = "La luz esta encendida")
        arduino.write(b'1')            
    else:
        mensajes.config(text = "La luz esta apagada")
        arduino.write(b'0')                        


ventana  = Tk()
ventana.title("Control de luz")
ventana.resizable(width=True, height=False)
ventana.geometry("300x200")


var = IntVar()
R2 = Radiobutton(ventana, text="OFF", variable=var, value=0, command=enviar_dato)
R1 = Radiobutton(ventana, text="ON", variable=var, value=1, command=enviar_dato)
R2.place(x="130", y="60")
R1.place(x="80", y="60")

mensajes = Label(ventana,text="La luz esta apagada")
mensajes.place(x="100", y="100")
mensajes.place()

ventana.mainloop()
arduino.close()