from tkinter import *    
from tkinter import scrolledtext
import matplotlib
import matplotlib.pyplot as plt

ventana = Tk()
x1 = IntVar()
y1 = IntVar()
x2 = IntVar()
y2 = IntVar()
seleccionAlg=IntVar()
seleccionFig=IntVar()

ventana.configure(bg = 'orange')
ventana.title('Representación y trazo de líneas y polígonos')
ventana.geometry("500x500")

txtTitulo=Label(ventana,text="Trazo de figuras por Algoritmo DDA y Brensenhams",bg = 'orange', fg='black',font=("Arial", 14)).place(x=30,y=20)

lbResult=Label(ventana,text="Resultados de X, Y:",bg = 'orange',font=("Arial", 11)).place(x=250, y=60)
txtResultado = scrolledtext.ScrolledText(ventana,width=25,height=23,bg = '#333333',fg='#FFFFFF',font=("Arial", 11))
txtResultado.grid(column=0,row=0)
txtResultado.place(x=250, y=90)

 
def calcularAlgoritmos():
    
    if seleccionAlg.get() == 1:
        f1 = plt.figure(1).add_subplot(1,1,1)
        plt.title("Algoritmo DDA")
        plt.grid()

        if seleccionAlg.get() == 1 and seleccionFig.get() == 1 or seleccionFig.get() == 2:
            X1=3
            Y1=2
            X2=3
            Y2=6

        if seleccionAlg.get() == 1 and seleccionFig.get() == 3 :
            X1=0
            Y1=1
            X2=5
            Y2=6
        
        if seleccionAlg.get() == 1 and seleccionFig.get() == 4 :
            X1=1
            Y1=1
            X2=10
            Y2=6
        
        plt.xlim([X1-2, X2+10])
        plt.ylim([Y1-2, Y2+4])

        dx = abs(X2 - X1)
        dy = abs(Y2 - Y1)
        steps = 0
    
        if (dx) > (dy):
            steps = (dx)
        else:
            steps = (dy)
          
        xInc = float(dx / steps)
        yInc = float(dy / steps)

        xInc = round(xInc,1)
        yInc = round(yInc,1)

        x_g = X1
        y_g = Y1

        if seleccionFig.get() == 1:

            txtResultado.insert(INSERT,'Cuadrado DDA\n')
            txtResultado.insert(INSERT,'X   Y\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g += xInc
                y_g += yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')
            
            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g += 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                y_g -= yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g -= 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            plt.show()
            txtResultado.insert(INSERT,'\n')

        if seleccionFig.get() == 2:

            txtResultado.insert(INSERT,'Rectangulo DDA\n')
            txtResultado.insert(INSERT,'X   Y\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g += xInc
                y_g += yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')
            
            for i in range(0, int(steps + 3)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g += 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                y_g -= yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps + 3)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g -= 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            plt.show()
            txtResultado.insert(INSERT,'\n')
            
        if seleccionFig.get() == 3:

            txtResultado.insert(INSERT,'Triangulo DDA\n')
            txtResultado.insert(INSERT,'X   Y\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g += xInc
                y_g += yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')
            
            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                y_g -= 1
                x_g += 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps+5)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g -= 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            plt.show()
            txtResultado.insert(INSERT,'\n')

        if seleccionFig.get() == 4:

            txtResultado.insert(INSERT,'Triangulo Recatangulo DDA\n')
            txtResultado.insert(INSERT,'X   Y\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g += xInc
                y_g += yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                y_g -= yInc
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            for i in range(0, int(steps+1)):
                g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f1.add_patch(g1)
                x_g -= 1
                x_r = round(x_g)
                y_r = round(y_g)
                txtResultado.insert(INSERT,str(x_r) + "   " + str(y_r)+ '\n')

            plt.show()
            txtResultado.insert(INSERT,'\n')

            

    if seleccionAlg.get() == 2:
        f2 = plt.figure(2).add_subplot(1,1,1)
        plt.title("Algoritmo Bresenhams")
        plt.grid()

        if seleccionAlg.get() == 2 and seleccionFig.get() == 1 or seleccionFig.get() == 2:
            X1=4
            Y1=2
            X2=8
            Y2=2

        if seleccionAlg.get() == 2 and seleccionFig.get() == 3 :
            X1=0
            Y1=1
            X2=5
            Y2=6
        
        if seleccionAlg.get() == 2 and seleccionFig.get() == 4 :
            X1=1
            Y1=1
            X2=10
            Y2=6

        plt.xlim([X1-2, X2+12])
        plt.ylim([Y1-2, Y2+12])

        dx = abs(X2 - X1)
        dy = abs(Y2 - Y1)
        p = 2*dy - dx

        X = X1
        Y = Y1

        if seleccionFig.get() == 1:

            txtResultado.insert(INSERT,'Cuadrado Bresenhams\n')
            txtResultado.insert(INSERT,'X   Y\n')
    
            while (X <= X2):
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                if(dx < 0):
                    X-=1
                else:
                    X+=1

                if (dy <0):
                    if p < 0:
                        p = p + 2 * dy
                        Y-=1
                    else:
                        p = p + (2*dy) -(2*dx)
                else:
                    if(p < 0):
                        p = p + 2 * dy
                    else:
                        p = p + (2*dy) -(2*dx)
                        Y+=1

            for i in range(Y+1, X2):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                Y+=1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+'\n')

            for i in range(X2-X1, X):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                X-=1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+'\n')

            for i in range(Y-Y+2, X2):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                Y-=1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+'\n')

            plt.show()
            txtResultado.insert(INSERT,'\n')
        
        if seleccionFig.get() == 2:

            txtResultado.insert(INSERT,'Rectangulo Bresenhams\n')
            txtResultado.insert(INSERT,'X   Y\n')
    
            while (X <= X2):
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                if(dx < 0):
                    X-=1
                else:
                    X+=1

                if (dy <0):
                    if p < 0:
                        p = p + 2 * dy
                        Y-=1
                    else:
                        p = p + (2*dy) -(2*dx)
                else:
                    if(p < 0):
                        p = p + 2 * dy
                    else:
                        p = p + (2*dy) -(2*dx)
                        Y+=1

            for i in range(Y+1, X2+5):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)     
                Y+=1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+'\n')

            for i in range(X2-X1, X):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                X-=1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+'\n')

            for i in range(Y-Y+2, X2+5):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                Y-=1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+'\n')

            plt.show()
            txtResultado.insert(INSERT,'\n')

        if seleccionFig.get() == 3:

            txtResultado.insert(INSERT,'Triangulo Bresenhams\n')
            txtResultado.insert(INSERT,'X   Y\n')
    
            while (X <= X2):
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                if(dx < 0):
                    X-=1
                else:
                    X+=1

                if (dy <0):
                    if p < 0:
                        p = p + 2 * dy
                        Y-=1
                    else:
                        p = p + (2*dy) -(2*dx)
                else:
                    if(p < 0):
                        p = p + 2 * dy
                    else:
                        p = p + (2*dy) -(2*dx)
                        Y+=1
                
            for i in range(X, X2+8):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                X += 1
                Y -= 1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')

            for i in range(X, X2+23):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                X -= 1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')
                
            plt.show()
            txtResultado.insert(INSERT,'\n')
        
        if seleccionFig.get() == 4:

            txtResultado.insert(INSERT,'Triangulo Rectangulo Bresenhams\n')
            txtResultado.insert(INSERT,'X   Y\n')
    
            while (X <= X2):
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                if(dx < 0):
                    X-=1
                else:
                    X+=1

                if (dy <0):
                    if p < 0:
                        p = p + 2 * dy
                        Y-=1
                    else:
                        p = p + (2*dy) -(2*dx)
                else:
                    if(p < 0):
                        p = p + 2 * dy
                    else:
                        p = p + (2*dy) -(2*dx)
                        Y+=1
            
            for i in range(X, X2+7):
                g2= matplotlib.patches.Rectangle((X, Y-1),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                Y -= 1
                
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')

            for i in range(X, X2+12):
                g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                f2.add_patch(g2)
                X -= 1
                txtResultado.insert(INSERT,str(X) + "   " + str(Y)+ '\n')
                
            plt.show()
            txtResultado.insert(INSERT,'\n')

def nuevo():
    seleccionAlg.set(None)
    seleccionFig.set(None)
    txtResultado.delete(1.0,END)
    plt.close()  

def salir(): 
    ventana.destroy()
    plt.close()

lblAlg=Label(ventana,text="Selecciona el algoritmo:",bg = 'orange', font=("Arial", 11)).place(x=35, y=60)
rBDDA=Radiobutton(ventana,text="DDA",bg = 'orange', variable=seleccionAlg, value=1,font=("Arial", 11)).place(x=35, y=90)
rBBS=Radiobutton(ventana,text="Bresenhams",bg = 'orange', variable=seleccionAlg, value=2,font=("Arial", 11)).place(x=35, y=120)

lblFig=Label(ventana,text="Selecciona la figura:",bg = 'orange', font=("Arial", 11)).place(x=35, y=160)
rBCuadrado=Radiobutton(ventana,text="Cuadrado",bg = 'orange',variable=seleccionFig, value=1,font=("Arial", 11)).place(x=35, y=190)
rBRectangulo=Radiobutton(ventana,text="Rectangulo",bg = 'orange',variable=seleccionFig, value=2,font=("Arial", 10)).place(x=35, y=220)
rBTriangulo=Radiobutton(ventana,text="Triangulo",bg = 'orange', variable=seleccionFig, value=3,font=("Arial", 11)).place(x=35, y=250)
rBTrianguloRec=Radiobutton(ventana,text="Triangulo Rectangulo",bg = 'orange', variable=seleccionFig, value=4,font=("Arial", 11)).place(x=35, y=280)

btnCalcularBS=Button(ventana, text="Graficar", command=calcularAlgoritmos,bg = '#333333',fg='#FFFFFF',font=("Arial", 11)).place(x=20, y=350)
btnNuevo=Button(ventana, text="Nuevo", command=nuevo,bg = '#333333',fg='#FFFFFF',font=("Arial", 11)).place(x=100, y=350)
btnSalir=Button(ventana, text="Salir", command=salir,bg = '#333333',fg='#FFFFFF',font=("Arial", 11)).place(x=180, y=350)

ventana.mainloop()

