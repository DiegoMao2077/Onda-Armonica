from sys import stdin
from turtle import *
from math import *
shape("circle")
def con(w,m):
    if(w<=0 or m<=0):
        print("ERROR: la frecuencia angular o la masa son menores 0")
        exit()

def posicion(a,w,p,t):
    x=float(a*cos((w*t)+p))
    return x

def velocidad(a,w,p,t):
    v=float((-1)*a*w*sin(((w)*t)+p))
    return v

def aceleracion(a,w,p,t):
    a=float((-1)*a*(w*w)*cos(((w)*t)+p))
    return a
def plano():
    speed(10)
    goto(500,0)
    home()
    goto(0,500)
    home()
    goto(0,-500)
    home()
    goto(-500,0)
    home()
    
def gx(lx,lt):
    for i in range(len(lt)):
        goto((lt[i]*300),(lx[i]*30))
    penup()
    home()
    pendown()
    
def gv(lv,lt):
    for i in range(8):
        goto((lt[i]*100),((lv[i]/10)*30))
    penup()
    home()
    pendown()
def ga(la,lt):
    speed(2)
    for i in range(8):
        goto((lt[i]*1),((la[i]/100)*50))
    penup()
    home()
    pendown()
def gf1(la,lt):
    for i in range(8):
        goto((lt[i]*100),((la[i]/1000)*10))
    penup()
    home()
    pendown()
def gf2(la,lt):
    for i in range(8):
        goto((lt[i]*20),((la[i]/1000)*10))
    penup()
    home()
    pendown()
def gec(la,lt):
    for i in range(8):
        goto((lt[i]*100),((la[i]/10)*10))
    penup()
    home()
    pendown()
def gep(la,lt):
    color("red")
    for i in range(8):
        goto((lt[i]*100),((la[i]/10)*10))
    penup()
    home()
    pendown()
def gecx(la,lt):
    for i in range(8):
        goto((lt[i]*100),((la[i]/10)*10))
    penup()
    home()
    pendown()
def gepx(la,lt):
    color("red")
    for i in range(8):
        goto((lt[i]*100),((la[i]/10)*10))
    penup()
    home()
    pendown()
def main():
    print("Amplitud(m):")
    am=float(stdin.readline())
    print("frecuencia angular(rad/s):")
    w=float(stdin.readline())*pi
    p=pi
    print("fase inicial(rad):",p)
    print("masa(Kg):")
    m=float(stdin.readline())
    print("Constante K(N/m):")
    k=float(stdin.readline())
    con(w,m)
    lt=[0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.3, 1.31, 1.32, 1.33]
    T=(2*pi)/w
    f=1/T
    print("T=",T,"s")
    print("F=",f,"Hz")
    lx=[]
    lv=[]
    la=[]
    lf1=[]
    lf2=[]
    lec=[]
    lep=[]
    let=[]
    for i in range(len(lt)):
        x=round(posicion(am,w,p,lt[i]),1)
        lx.append(x)
        v=round(velocidad(am,w,p,lt[i]),2)
        lv.append(v)
        a=round(aceleracion(am,w,p,lt[i]),2)
        la.append(a)
        f1=round(m*(a),3)
        lf1.append(f1)
        f2=round((-1)*(k)*(x),3)
        lf2.append(f2)
        ec=round((0.5)*(m)*(v**2),3)
        lec.append(ec)
        ep=round((0.5)*(k)*(x**2),3)
        lep.append(ep)
        et=ec+ep
        let.append(et)
    plano()
    gx(lx,lt)
main()


