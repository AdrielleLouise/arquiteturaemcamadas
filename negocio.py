from dados import *
from datetime import datetime, timedelta

def cadastrar_manutencao(nome, tipo, periodicidade, ultima_manutencao):
  if periodicidade <= 0:
    return False, "Erro! Periodicidade está com valor inválido."
  manutencao_existente = buscar_manutencao(nome, tipo)
  if manutencao_existente:
    return False, "Erro! Essa manutenção já está cadastrada para o equipamento."

  nova_manutencao = {
      "nome": nome,
      "tipo": tipo,
      "periodicidade": periodicidade,
      "ultima_manutencao": ultima_manutencao
  }
  salvar_manutencao(nova_manutencao)
  return True, "Manutenção salva com sucesso! :)"
def consultar_manutencao(nome):
  manutencoes_encontradas = buscar_manutencoes(nome)
  if not manutencoes_encontradas:
    return False, "Manutenção não encontrada."
  resultados = []
  for manutencao in manutencoes_encontradas:
    ultima = datetime.strptime(
        manutencao["ultima_manutencao"],
        "%d/%m/%Y"
    )
    proxima = ultima + timedelta(
        days=manutencao["periodicidade"]
    )
    hoje = datetime.today()
    if hoje.date() > proxima.date():
      status = "Manutenção VENCIDA."
    else:
      status = "Manutenção em dia."
    resultado = {
        "nome": manutencao["nome"],
        "tipo": manutencao["tipo"],
        "ultima_manutencao": manutencao["ultima_manutencao"],
        "proxima_manutencao": proxima.strftime("%d/%m/%Y"),
        "status": status
    }
    resultados.append(resultado)
  return True, resultados
def realizar_manutencao(nome, tipo, data_realizada):
  manutencao = buscar_manutencao(nome, tipo)
  if not manutencao:
    return False, "Manutenção não encontrada no histórico."
  manutencao["ultima_manutencao"] = data_realizada
  return True, "Manutenção realizada com sucesso!"
def listar_manutencoes():
  manutencoes = listar_todas()
  if not manutencoes:
    return False, "Nenhuma manutenção cadastrada."
  resultados = []
  for manutencao in manutencoes:
    ultima = datetime.strptime(
      manutencao["ultima_manutencao"],
      "%d/%m/%Y"
    )
    proxima = ultima + timedelta(
      days=manutencao["periodicidade"]
    )
    hoje = datetime.today()
    if hoje.date() > proxima.date():
      status = "Manutenção VENCIDA."
    else:
      status = "Manutenção em dia."
    resultado = {
      "nome": manutencao["nome"],
      "tipo": manutencao["tipo"],
      "ultima_manutencao":  manutencao["ultima_manutencao"],
      "proxima_manutencao": proxima.strftime("%d/%m/%Y"),
      "status": status 
    }
    resultados.append(resultado)
  return True, resultados
def remover_manutencao_cadastrada(nome, tipo):
  removida = remover_manutencao(nome, tipo)
  if not removida:
    return False, "Manutenção não encontrada no histórico."
  return True, "Manutenção removida com sucesso!"
def remover_equipamento_cadastrado(nome):
  removido = remover_equipamento(nome)
  if not removido:
    return False, "Equipamento não encontrado no histórico."
  return True, "Equipamento removido com sucesso!"