import math
def sorvete():
  a = input("Utilizando essa fórmula, o que você deseja obter? S, S0, V0 ou T?")
  if(a=="S"):
    V0=float(input("Digite o valor de V0: "))
    S0=float(input("Digite o valor de S0: "))
    T=float(input("Digite o valor de T:"))
    S=S0+V0*T
    print(S)
  elif(a=="S0"):
    V0=float(input("Digite o valor de V0: "))
    S=float(input("Digite o valor de S: "))
    T=float(input("Digite o valor de T:"))
    S0=S-(V0*T)
    print(S0)
  elif(a=="V0"):
    S=float(input("Digite o valor de S: "))
    S0=float(input("Digite o valor de S0: "))
    T=float(input("Digite o valor de T:"))
    V0=(S-S0)/T
    print(V0)
  elif(a=="T"):
    S=float(input("Digite o valor de S: "))
    S0=float(input("Digite o valor de S0: "))
    V0=float(input("Digite o valor de V0:"))
    T=(S-S0)/V0
    print(T)
  else:
    print("Você digitou um comando inválido.")


def sorvetão():
  a = input("Utilizando essa fórmula, o que você deseja obter? S, S0 ou V0?")
  if(a=="S"):
    V0=float(input("Digite o valor de V0: "))
    S0=float(input("Digite o valor de S0: "))
    T=float(input("Digite o valor de T:"))
    A=float(input("Digite o valor de A:"))
    S=S0+V0*T+(A*T*T/2)
    print(S)
  elif(a=="S0"):
    V0=float(input("Digite o valor de V0: "))
    S=float(input("Digite o valor de S: "))
    T=float(input("Digite o valor de T:"))
    A=float(input("Digite o valor de A:"))
    S0=S-(V0*T+(A*T*T/2))
    print(S0)
  elif(a=="V0"):
    S0=float(input("Digite o valor de S0: "))
    S=float(input("Digite o valor de S: "))
    T=float(input("Digite o valor de T:"))
    A=float(input("Digite o valor de A:"))
    V0=S-(S0+(A*T*T/2))
    print(V0)
  else:
    print("Você digitou um comando inválido.")
    
  

def vovoateu():
  a = input("Utilizando essa fórmula, o que você deseja obter? V, V0, A ou T?")
  if(a=="V"):
    V0=float(input("Digite o valor de V0: "))
    A=float(input("Digite o valor de A: "))
    T=float(input("Digite o valor de T:"))
    V=V0+A*T
    print(V)
  elif(a=="V0"):
    V=float(input("Digite o valor de V: "))
    A=float(input("Digite o valor de A: "))
    T=float(input("Digite o valor de T:"))
    V0=V-A*T
    print(V0)
  elif(a=="A"):
    V0=float(input("Digite o valor de V0: "))
    V=float(input("Digite o valor de V: "))
    T=float(input("Digite o valor de T:"))
    A=(V-V0)/T
    print(A)
  elif(a=="T"):
    V0=float(input("Digite o valor de V0: "))
    A=float(input("Digite o valor de A: "))
    V=float(input("Digite o valor de V:"))
    T=(V-V0)/A
    print(T)
  else:
    print("Você digitou um comando inválido.")
    
  
  
def velx():
  V0=float(input("Digite o valor de V0:"))
  ANG=math.cos(math.radians(float(input("Digite o angulo"))))
  V0X=V0*(ANG)
  print(V0X)
  
def vely():
  V0=float(input("Digite o valor de V0:"))
  ANG=math.sin(math.radians(float(input("Digite o angulo"))))
  V0Y=V0*(ANG)
  print(V0Y)

def torricelli():
  a = input("Utilizando essa fórmula, o que você deseja obter? V, V0, A ou DS?")
  if(a=="V"):
    V0=float(input("Digite o valor de V0: "))
    A=float(input("Digite o valor de A: "))
    DS=float(input("Digite o valor de DS:"))
    V=((V0*2)+(2*A*DS))*0.5
    print(V)
  elif(a=="V0"):
    V=float(input("Digite o valor de V: "))
    A=float(input("Digite o valor de A: "))
    DS=float(input("Digite o valor de DS:"))
    V0=((V*2)-(2*A*DS))*0.5
    print(V0)
  elif(a=="A"):
    V=float(input("Digite o valor de V: "))
    V0=float(input("Digite o valor de A: "))
    DS=float(input("Digite o valor de DS:"))
    A=((V**2)-(V0**2)/(DS))*0.5
    print(A)
  elif(a=="DS"):
    V=float(input("Digite o valor de V: "))
    V0=float(input("Digite o valor de V0: "))
    A=float(input("Digite o valor de A:"))
    DS1=((V**2)-(V0**2))/(2*A)
    print(DS1)
  else:
    print("Você digitou um comando inválido.")
    
  

def main():
  
  print("O que você deseja calcular?")
  print("1 - sorvete")
  print("2 - sorvetão")
  print("3 - vovo ateu")
  print("4 - velx ")
  print("5 - vely ")
  print("6 - torricelli ")
  print()
  print("Obs: as fórmulas que 2,3 e 6 são utilizadas no eixo y, enquanto a fórmula 1 no eixo x.")
  print()
  count = input('qual formula? ')
  
  if count == '1':
    sorvete()
  elif count == '2':
    sorvetão() 
  elif count == '3':
    vovoateu()
  elif count == '4':
    velx()
  elif count == '5':
    vely()
  elif count == '6':
    torricelli()
  else:
    print("Você digitou um comando inválido.")

main()