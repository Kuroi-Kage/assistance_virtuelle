#from core.rules import RULES
from core.precessor import Precessor

class Reasonning:
    def __init__(self, memory):
        self.memory = memory
        self.processor = Precessor()
    
    def think(self, text: str) ->str:
        msg_type = self.processor.detect(text)
        
        if self.memory.exists(text):
            return f"Tu as déja dit cela : '{text}'"
      
        # logiqement : enregistrer dans la mémoire
        self.memory.add(text, msg_type)
      #  text_lower = text.lower()
        
        # Vérifier les règles d'abord
       # for key, response in RULES.items():
           # if key in text_lower:
             #   self.memory.add(text)
              #  return response
        # petit logique: transformer le texte
        #return text.upper()
        
        # Logique simple
        #last = self.memory.get_last()
        
        #if len(self.memory.data) ==1:
        
       ## if last and text == last:
          ##  response = "Tu viens de dire la même chose !"
        
        # Décision avancée : vérifier si le message est similaire à plusieur précédents
       ## elif last and any(text == msg for msg in self.memory.data[-3:]):
          ##  response = f"Ce message ressemble à ce que tu as déja récemment : '{text}'"
        
        # Décision par defaut : premier message ou nouveau contenu
     ##   elif not last:
        ##    response = f"Je note ton premier message: '{text}'"
     ##   else:
          ##  response = f" Message enregistré: '{text}'"  
        if  msg_type == "question":
            # Regarde le dernier message pour un debut de contexte
            last = self.memory.get_last()
            response = "Je réflechis àla question.."
            if last and last["type"] == "question":
                response += " (lié à ta derniere question)"
        elif msg_type == "commande":
            response = f"Commande notée: '{text}'"
        else:
            response = "Message reçu."
            
        return response
            # lower_text = text.lower()
           # if lower_text.startswith("quoi"):
             #   return "Question 'quoi' détectée : je note et réflechis.."
            #elif lower_text.startswith("pourquoi"):
             #   return "Question 'pourquoi' détectée : je recherche la raison.."
           # elif lower_text.startswith("comment"):
              #  return "Question 'comment' détectée : je réflechis à la methode.."
           # elif lower_text.startswith("qui"):
            #    return "Question 'qui' détectée : je reflechis à la personne.."
          #  else:
              #  return "Question détectée : je réflechis.."
        
        
        # Comportement par défaut
       # return f"Message reçu : '{text}'"


      #  self.memory.add(text)
        
      #  return response