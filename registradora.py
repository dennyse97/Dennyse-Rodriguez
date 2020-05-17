#class registradora:
 #   arituclos={}
  #  cambio=0

def ingresar_productos():
   caja=True
    while caja ==True:
        opcion =raw_input("Desea ingresar productos si o no")
        try:
            if opcion==True:
                if opcion.lower()=="si":
                    producto=raw_input("ingrese el producto")
                    precio =int(raw_input("ingrese el precio: "))
                    arituclos[producto]=precio
                elif opcion.lower()=="no":
                        caja=False
                else:
                    print ("no se reconoce")
            else:       
                print ("no se reconoce el movimiento")
        except:
            caja=True
    print ( "productos registrados:" )
                        


c
#    def costos():
 #       sumadecostos = 0
  #      for i in range(1,21):
  #         costo =float(input("Ingresar costos de producto"))
  #         sumadecostos= sumadecostos + costos
        
#  def pago(:)
 #       pago -float(input("ingresar monto de pago"))
    
  #  def cambio():
   #     if(pago>=sumadecostos):
    #        devolver=pago-sumadecostos
                


