from core.memory import Memory

class DummyAgent:
  def score(self, text, memory_texts, n_last=3):
    recent = memory_texts[-n_last:]
    if text in recent:
      return {"intent": "repetition", "score": 0.9}
    else:
      return {"intent": "nouveau", "score": 0.3}
    
  
from core.reasonning import Reasonning
  
mem = Memory()
agent = DummyAgent()
brain = Reasonning(mem, agent)

messages = [
  "Salut",
  "est ce que ça va?",
  "rebonjour",
  "Ouvre la porte",
  "Comment ça va?"
]

for msg in messages:
  print(f"Toi : {msg}")
  rep = brain.think(msg)
  print(f"IA : {rep}")
  #print(f"Mémoire actuelle : {mem.get_all()}")
  
  