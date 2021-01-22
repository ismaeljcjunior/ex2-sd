import rpyc
import socket
from const import * 
from rpyc.utils.server import ThreadedServer
 
class teste(rpyc.Service):
  value = []

  def exposed_append(self, data):
    
    print(f"Concatenando valor: {data}")
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    print(f"Retornando valor")
    return self.value

if __name__ == "__main__":
  print(f"Criaando server teste") 
  server = ThreadedServer(teste, port = PORT)
  print(f"Conectando ao Server de diretório")  
  conn_serverDir = rpyc.connect(SERVERDIR,PORTDIR)
  print(f"Obtendo ipAdress da teste")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no Server de diretório") 
  conn_serverDir.root.exposed_registraServer('teste',ipAdress,PORT)
