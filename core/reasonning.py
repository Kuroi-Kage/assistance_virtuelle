#from core.rules import RULES
from core.precessor import Precessor

class Reasonning:
    def __init__(self, memory):
        self.memory = memory
        self.processor = Precessor()
    
    def think(self, text: str) ->str:
      
        msg_type = self.processor.detect(text)
         
        problem = {
          "text": text,
          "type": msg_type
        }
        
        analysis = {
          "linked": False,
          "repetition": False
        }
        
        if len(self.memory.short_memory) > 0:
          last = self.memory.short_memory[-1]
          if last["type"] == msg_type:
            analysis["linked"] = True
          
        if any(text == msg["text"] for msg in self.memory.short_memory):
          analysis["repetition"] = True
        
        
        if analysis["repetition"]:
          response = "Daccord, tu reviens sur lamême idee."
      
        elif problem["type"] == "question":
          response = "Je réflechis à ta question."
          if analysis["linked"]:
            response += "Elle est liée à la précédente."
            
        elif problem["type"] == "commande":
          response = "Commande comprise."
        
        else:
          response = "Message reçu."
            
        return response
          