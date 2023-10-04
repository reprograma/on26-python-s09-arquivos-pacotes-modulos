from pacote_aline import modulo1
from soma import soma_casa
from soma.moto import soma_moto

info = modulo1.main()
print(info)


soma = modulo1.soma(2,3)
print(soma)

soma_casa_maria = soma_casa.soma_casa(4)
print (soma_casa_maria)

soma_moto_daniela = soma_moto.soma_moto(1)
print (f'A daniela tem: {soma_moto_daniela} de motos')

