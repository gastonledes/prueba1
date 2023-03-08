from archivo_entrega import Factura
from modulo2 import *
cliente1 = Factura(input('Nombre: ').capitalize(),input('Apellido: ').capitalize(), int(input('Edad: ')), int(input('D.N.I: ')),input('Email: '))

cliente1.confirmar_email(None)

print(cliente1)

cliente1.catalogo()

cliente1.compra(int(input('Elija el numero de opcion que desea comprar: ')))

cliente1.tarjeta_nombre(input('Nombre del titular de la tarjeta: '))

cliente1.tarjeta_nro(None)

cliente1.tarjeta_vencimiento(None, 5)

cliente1.tarjeta_seguridad(None,3)

cliente1.datos_facturacion(int(input('Elegir el numnero de opcion correspondiente: ')))

cliente1.envio(input('Ciudad: '), input('Direccion: '))

cliente1.numero_factura(0)