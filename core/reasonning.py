#from core.rules import RULES
#from core.processor import Precessor


class Reasonning:
    def __init__(self, memory, agent):
        self.memory = memory
      #  self.processor = Precessor()
        self.agent = agent
    
    def think(self, text: str) ->str:
     memory_texts = [m["text"] for m in self.memory.get_all()]
     
     decision = self.agent.score(text, memory_texts)
     
     self.memory.add(text, decision["intent"])
     
     # Sélection basée sur SCORE 
     if decision["score"] > 0.6:
       return f"Je reconnais une intention similaire ({decision['intent']})."
     
     else:
       return "Nouveau sujet détecté."