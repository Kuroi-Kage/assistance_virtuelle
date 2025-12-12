from core.memory import Memory
from core.reasonneing import Reasonning


mem = Memory()
#mem.add('hello')
#print(mem.data)

brain = Reasonning(mem)

#resultat = brain.think("Bonjour")

#print(brain.think("test"))
#print('Resultat :', resultat)
#print('Memoire :', mem.data)
print(brain.think("Bonjour"))
print(brain.think("Comment ça va?"))
print(brain.think("Comment ça va?"))
print(brain.think("Peux-tu m'aider?"))
print("Memoire:", mem.data)
