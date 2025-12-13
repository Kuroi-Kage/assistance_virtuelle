from core.memory import Memory
from core.reasonning import Reasonning


mem = Memory()
brain = Reasonning(mem)

#while True:
  #  msg = input("Toi : ")
  #  if msg.lower() == "exit":
    #    break
for msg in ["Bonjour", "Comment ça va?", "Bonjour", "Ouvre la porte", "Bonjour"]:
    rep = brain.think(msg)
    print("Toi :", msg)
    print("IA :", rep)
    print("Mémoire courte :", mem.short_memory)
    print("Mémoire longue :", mem.data)
   # print("IA :", brain.think(msg))
   # print("Mémoire actuelle :", mem.get_all())
