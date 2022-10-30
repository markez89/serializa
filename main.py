from Vehiculo.vehiculo import Vehiculo
import pickle

def main():
    serializa("text.txt")
    deserializa("text.txt")  
        

def serializa(fichero): 
        #Cargamos la clase en el fichero
        coche = Vehiculo(4,4,"verde","Focus")
        f = open(fichero, 'wb')
        pickle.dump(coche,f)
        f.close()    

def deserializa(fichero):
         #Leemos la clase del fichero
        f = open(fichero, 'rb')
        coche = pickle.load(f)
        f.close()
        print(str(coche))
       

if __name__ == '__main__':
    main()