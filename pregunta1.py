
m = [[5,4,7],[6,7,8],[1,2,3]]
n = [[1,2,3,4,],[4,5,6,7],[7,8,9,4]]
p = [[1.2],[5,4]]
suma =0
def matriz():
     o= int(input("Ingrese las fila de una matriz cuadrada"))
     m = input("Ingrese el nombre de la matriz")
     for i in range(o):    
         suma = suma + m[i][i]
     if suma %2==0:
        print("la suma es par")
     else:
        print("la suma no es par")
     print(suma)