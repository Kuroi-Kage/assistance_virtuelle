from core.memory import Memory
from core.reasonning import Reasonning

mem = Memory()
brain = Reasonning(mem)


#tests = [
 #   "Bonjour",
   # "Comment ça va?",
  #  "ouvre la porte",
   # "Montre-moi les fichiers",
  #  "Quoi de neuf?",
   # "Simple message"
#]
def send(msg):
  rep = brain.think(msg)
  #print(f"Toi : {msg}")
  print(f"IA : {rep}")
  print("Mémoire: ", mem.data)
  
msg = input("Toi : ")
send(msg)

