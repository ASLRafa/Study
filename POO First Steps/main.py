from cliente import Cliente
from replit import db
from conta import Conta


conta1 = Conta(1155,"rafael",2000)
conta1.deposita(50)
conta2 = Conta(1156,"raquel")
conta1.transfere(50,conta2)
conta1.extrato()
conta1.saca(2100)
conta1.extrato()

cliente = Cliente('rafael')
print(cliente.nome)

