class Cliente: 
    def __init__(self, nombre,apellido, edad, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.email = email
    def confirmar_email(self,confirmacion):
      while True:
        confirmacion = input('Repetir email: ')
        if confirmacion == self.email :
          break
        else:
          print('La confirmacion del email no es correcta')

    def __str__(self,):
      return  self.nombre + ' ' + self.apellido + ', tu usuario fue creado correctamente. '+'\n'



    def catalogo(self):
      print('A continuacion te mostraremos el catalogo',
       '\n', '1 : Notebook Lenovo: $150000', 
       '\n', '2 : Noteboook HP $125000', 
       '\n', '3 : Televisor smart "32 RCA: $70000'
       '\n', '4 : Televisor smart "32 Philco: $80000')

    def compra(self, producto):
          if producto == 1:
            producto = 'Notebook Lenovo'
          elif producto == 2:
            producto = 'Noteboook HP'
          elif producto == 3:
            producto = 'Televisor smart "32 RCA'
          elif producto == 4:
            producto = 'Televisor smart "32 Philco'
          self.producto = producto
          producto = self.producto
          print('  ')
        
class Factura(Cliente):

    def tarjeta_nombre(self, nombre_titular):
        self.nombre_titular = nombre_titular

    def tarjeta_nro(self, nro_tarjeta,):
      while True:
        nro_tarjeta = input('Numero de tarjeta: ')
        if len(nro_tarjeta) == 16:
          self.nro_tarjeta = nro_tarjeta
          break
        else:
          print('Numero invalido, intente nuevamente (Recordá que son 16 numeros). ')

    def tarjeta_vencimiento(self, vencimiento, limite):
      vencimiento =input('Vencimiento (seprara mes y año con un espacio): ')[:limite].replace(' ', '/')
      self.vencimiento = vencimiento

    def tarjeta_seguridad(self, nro_seguridad, limitante):
      nro_seguridad = input('Numero de seguridad (esta en el dorso): ')[:limitante]
      self.nro_seguridad = nro_seguridad
      print('\n','Nombre del titular: ', self.nombre_titular,'\n',
            'Numero de tarjeta', self.nro_tarjeta, '\n',
            'Vencimiento: ', self.vencimiento, '\n',
            'Numero de seguridad: ', self.nro_seguridad, '\n',
            'Si los datos son correctos escriba 1', '\n',
            'Si tienen algun error escriba 2')

    def datos_facturacion(self, confirmacion_datos):
      self.confrmacion_datos = confirmacion_datos
      if confirmacion_datos == 1:
        print('Pasaremos a realizar el envio.')
      else:
        quit()
   
    def envio(self, ciudad, direccion):
      self.ciudad = ciudad
      self.direccion = direccion
      print('Ya se hizo efectiva la compra de ' + self.producto)
      print('Los avances del envio se le informaran mediante email a ' + self.email )

    def numero_factura(self, numero):
      self.numero = numero
      numero +=1
      print('Tu numero de facturacion es ' + str(numero) , '\n', 'Muchas gracias por su compra. ' )

   