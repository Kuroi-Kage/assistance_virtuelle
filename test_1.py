from core.memory import Memory
from core.reasonning import Reasonning

#mem = Memory()
#mem.add("Hello")
#mem.add("")

#print("Dernier élement : ", mem.get_last())

mem = Memory()
brain = Reasonning(mem)

#print("___ Kuroi Kage ___")
#print("Tape 'exit' pour quitter")

#while True:
  #  user_input = input("Toi :")
   # if user_input.lower() == "exit":
     #   print("IA : À bientôt!")
      #  break
    
#    response = brain.think(user_input)
  #  print("IA : ", response)
   # print("Mémoire actuelle :", mem.data)
    
    
tests = [
    "Bonjour",
    "Comment ça va?",
    "Comment ça va?",
    "Ouvre la porte",
    "Bonjour"
]

for t in tests:
    result = brain.think(t)
    print(f"Message: '{t}' => IA: {result}")
    
print("Mémoire actuelle:", mem.get_all())