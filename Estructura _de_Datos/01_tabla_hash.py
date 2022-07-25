# https://www.youtube.com/watch?v=so1wDKYbJfQ
#Tabla hash
#Funciones Hash 
#Insertar(Tabla T, elemento k)
#T[h(clave(k))] <----- k
#Buscar(Tabla T, clave x)
#T[h(X)]
#Eliminar(Tabla T, clave x)
#T[h(X)]<----- Libre

class hash_table:
    def __init__(self):
        self.table = [None] * 127
    
    # Función hash
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value): # Metodo para ingresar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value): # Metodo para buscar elementos
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
    def Remove(self,value): # Metodo para eliminar elementos
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[hash] is None;
        
        
H = hash_table()
H.Insert("A")
H.Insert("B")
H.Insert("C")

print(H.Search("B"))
print(H.Search("A"))
