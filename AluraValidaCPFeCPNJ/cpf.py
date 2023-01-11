from validate_docbr import CPF,CNPJ

class Doc:

  @staticmethod
  def cria_documento(documento):
    if len(documento) == 11:
      return DocCpf(documento)
    elif len(documento) == 14:
      return DocCnpj(documento)
    else:
      raise ValueError("Quantidade digitos incorreta")
    
class DocCpf:
  def __init__(self,documento):
    if self.valida(documento):
      self.cpf = documento
    else:
      raise ValueError("CPF Invalido")

  def __str__(self):
    return self.format()
    
  def valida(self,documento):
    validador = CPF()
    return validador.validate(documento)

  def format(self):
    mascara = CPF()
    return mascara.mask(self.cpf)

class DocCnpj:
  def __init__(self,documento):
    if self.valida(documento):
      self.cnpj = documento
    else:
      raise ValueError("CNPJ Invalido.")

  def valida(self,documento):
    validate_cnpj = CNPJ()
    return validate_cnpj.validate(documento)

  def format(self):
    mascara = CNPJ()
    return mascara.mask(self.cnpj)

  def __str__(self):
    return self.format()
    
# class CpfCnpj:

#     def __init__(self, documento,tipo_documento):
#         self.tipo_documento = tipo_documento
#         ndocumento = str(documento)
      
#         if tipo_documento == "cpf":
#           if self.valida_cpf(ndocumento):
#             self.cpf = ndocumento
#           else:
#             raise ValueError("CPF Inválido!!!")
            
#         elif tipo_documento == "cnpj":
#           if self.cnpj_e_valido(ndocumento):
#             self.cnpj = ndocumento
#           else:
#             raise ValueError("CPNJ Inválido!!!")
#         else:
#           raise ValueError("documento invalido")

#     def cnpj_e_valido(self,cnpj):
#       if len(cnpj) == 14:
        
#       else:
#         raise ValueError("Quantidade de digitos inválida")

#     def format_cnpj(self):
     
      
#     def format_cpf(self):
      

#     def __str__(self):
#       if self.tipo_documento == "cpf":
#         return self.format_cpf()
#       elif self.tipo_documento == 'cnpj':
#         return self.format_cnpj()
        