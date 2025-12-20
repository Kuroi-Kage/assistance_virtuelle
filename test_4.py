from core.memory import Memory
from core.reasonning import Reasonning
from core.agents import AgentIntent
from core.processor import Precessor


mem = Memory()
agent = AgentIntent()
processor = Precessor()
brain = Reasonning(mem, agent)

#while True:
  #  msg = input("Toi : ")
  #  if msg.lower() == "exit":
    #    break
#for msg in ["Bonjour", "Comment ça va?", "Bonjour", "Ouvre la porte", "Bonjour"]:
   # rep = brain.think(msg)
   # print("Toi :", msg)
   # print("IA :", rep)
  #  print("Mémoire courte :", mem.short_memory)
  #  print("Mémoire longue :", mem.data)
   # print("IA :", brain.think(msg))
   # print("Mémoire actuelle :", mem.get_all())
def send(msg):
  rep = brain.think(msg)
  print(f"Toi : {msg}")
  print(f"IA : {rep}")
  #print("Mémoire: ", mem.data)
  
msg = input("Toi : ")
send(msg)