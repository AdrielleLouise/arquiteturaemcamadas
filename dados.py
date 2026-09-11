manutencoes = []
def salvar_manutencao(manutencao):
  manutencoes.append(manutencao)
def listar_todas():
  return manutencoes
def buscar_manutencao(nome, tipo):
  for manutencao in manutencoes:
    if manutencao["nome"] == nome and manutencao["tipo"] == tipo:
      return manutencao
  return None
def buscar_manutencoes(nome):
  resultados = []
  for manutencao in manutencoes:
    if manutencao["nome"] == nome:
      resultados.append(manutencao)
  return resultados
def remover_equipamento(nome):
  manutencoes_encontradas = buscar_manutencoes(nome)
  if not manutencoes_encontradas:
    return False
  for manutencao in manutencoes_encontradas:
    manutencoes.remove(manutencao)
  return True
def remover_manutencao(nome, tipo):
  manutencao = buscar_manutencao(nome, tipo)
  if manutencao:
    manutencoes.remove(manutencao)
    return True
  return False
def remover_equipamento(nome):
  manutencoes_encontradas = buscar_manutencoes(nome)
  if not manutencoes_encontradas:
    return False
  for manutencao in manutencoes_encontradas:
    manutencoes.remove(manutencao)
  return True