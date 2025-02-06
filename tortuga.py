import turtle
import random
from tkinter import messagebox
#Configurar la ventana
window = turtle.Screen()
window.title("Carrera de tortugas")
window.bgcolor("lightblue")
window.setup(500,500)
window.setworldcoordinates(0,500,500,0) #para que empiecen arriba a la izquierda

#Crear a todas las tortugas
tortugas = []
colores = ["green","orange", "pink", "white","black","yellow","purple","red","blue","grey"]

for index, color in enumerate(colores):
    tortuga = turtle.Turtle() #crear instancia de tortuga
    tortuga.shape("turtle") #para que tenga forma de tortuga
    tortuga.color(color) #cada tortuga se identifica po el color
    tortuga.pensize(2)
    tortuga.speed(4) #velocidad a la que se mueven
    tortuga.penup() #para moverlas al inicio sin generar lineas
    tortuga.goto(10,index*40+50)
    tortuga.pendown()
    tortugas.append(tortuga) #añadir las tortugas a la lista de tortugas


#Hacer que se muevan una distancia random, la primera que llegue hasta el limite de la ventana gana
run = True
while run:
    for tortuga in tortugas:
        distancia = random.randint(0,25) #distancia aleatoria
        tortuga.forward(distancia) #para que cada tortuga avance esa distancia
        if tortuga.xcor() >= 480: #si la tortuga llega al final (hay que tener en cuenta el tamaño de la tortuga)
            messagebox.showinfo(title="Fin de la carrera", message=f"Ha ganado la tortuga {tortuga.color()[0].capitalize()}")
            print(f"Ha ganado la tortuga {tortuga.color()[0].capitalize()}")
            run = False
            break





turtle.mainloop()