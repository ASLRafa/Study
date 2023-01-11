from cpf import Doc,DocCnpj,DocCpf
# cpf_um = CpfCnpj(47516902802,"cpf")
# print(cpf_um)

# exemplo_cnpj = CpfCnpj(35379838000112,"cnpj")
# print(exemplo_cnpj)

cnpj_um = '35379838000112'
cpf_um = '47516902802'

documento = Doc.cria_documento(cnpj_um)
print(documento)

documento1 = Doc.cria_documento(cpf_um)
print(documento1)