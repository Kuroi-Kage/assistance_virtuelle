#from core.rules import RULES
from core.precessor import Precessor

class Reasonning:
    def __init__(self, memory):
        self.memory = memory
        self.processor = Precessor()
        self.first_message = True
    
    def think(self, text: str) ->str:
      
        msg_type = self.processor.detect(text)
         
        problem = {
          "text": text,
          "type": msg_type
        }
        
        analysis = {
          "linked": False,
          "repetition": False,
          "priority": 0
        }
        
        DECISION = {
          "repeat": lambda: "D'accord, tu reviens sur la même idée.",
          "deep_link": lambda: "Je réflechis à ta question. Elle est liée au contexte. ",
          "question": lambda: "Je réfléchis à ta question.",
          "command": lambda: "Commande comprise",
          "default": lambda: "Message reçu.",
          "greeting": lambda: "Bonjour ! Comment vas-tu ?"
        }
        
        # Vérification lien avec dernier message
        if len(self.memory.short_memory) > 0:
          last = self.memory.short_memory[-1]
          if last["type"] == msg_type:
            analysis["linked"] = True 
            analysis["priority"] += 3
            
        
         # Vérification répétition 
        if not self.first_message and any(text == msg["text"] for msg in self.memory.short_memory):
          analysis["repetition"] = True
          analysis["priority"] += 2
        
        
        if analysis["repetition"] and analysis["priority"] >= 2:
          response = DECISION["repeat"]()
          
        elif analysis["linked"] and analysis["priority"] >= 3:
          response = DECISION["deep_link"]()
      
        elif problem["type"] == "question":
          response = DECISION["question"]()
            
        elif problem["type"] == "command":
          response = DECISION["command"]()
        
        elif problem["type"] == "greeting":
          response = DECISION["greeting"]()
        
        else:
          if self.first_message:
            response = "Bonjour ! Comment puis-je vous aider ?"
            self.first_message = False
          response = DECISION["default"]()
          
        self.memory.add(text, msg_type)

            
        return response
          