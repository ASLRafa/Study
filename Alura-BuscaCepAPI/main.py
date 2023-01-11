from acesso_cep import BuscaEndereço
import requests

cep = "11706210"

obj_cep=BuscaEndereço(cep)
print(obj_cep)

bairro,cidade,uf = obj_cep.API_CEP()
print(bairro, cidade, uf)

