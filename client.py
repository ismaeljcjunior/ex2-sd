import rpyc
from const import *

class Client:
  print(f"Iniciando conexão com servidor de diretorios de ip: {SERVERDIR} na porta: {PORTDIR}")
  
  conn = rpyc.connect(SERVERDIR, PORTDIR)
  
  print(f"Fazendo busca de test")
  
  nomeDir  =  conn.root.exposed_buscaServer('teste')
  
  print(f"Busca finalizada, resultado: ")
  print(nomeDir)