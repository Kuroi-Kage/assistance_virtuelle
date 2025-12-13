#from core.rules import RULES
from core.precessor import Precessor

class Reasonning:
    def __init__(self, memory):
        self.memory = memory
        self.processor = Precessor()
    
    def think(self, text: str) ->str:
        msg_type = self.processor.detect(text)
        last_messages = [msg["text"] for msg in self.memory.short_memory]
        
        if text in last_messages:
            return "Rebonjour ! Tu viens de dire ça récemment"
      
        else:
        # logiqement : enregistrer dans la mémoire
            self.memory.add(text, msg_type)
      
             ##  response = f" Message enregistré: '{text}'"  
            if  msg_type == "question":
              response = "Je réflechis à la question"
              # Regarde le dernier message pour un debut de contexte
              last = self.memory.short_memory[-2] if len(self.memory.short_memory) >= 2 else None
              if last and last["type"] == "question":
               response = "(lié à ta derniere question)"
            elif msg_type == "commande":
              response = f"Commande notée: '{text}'"
            else:
              response = "Message reçu."
        return response
          