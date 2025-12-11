from core.rules import RULES

class Reasonning:
    def __init__(self, memory):
        self.memory = memory
    
    def think(self, text):
        # logiqement : enregistrer dans la mémoire
        last = self.memory.get_last()
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
        if last and text == last:
            response = "Tu viens de dire la même chose !"
        
        # Décision avancée : vérifier si le message est similaire à plusieur précédents
        elif last and any(text == msg for msg in self.memory.data[-3:]):
            response = f"Ce message ressemble à ce que tu as déja récemment : '{text}'"
        
        # Décision par defaut : premier message ou nouveau contenu
        elif not last:
            response = f"Je note ton premier message: '{text}'"
        else:
            response = f" Message enregistré: '{text}'"
            
        self.memory.add(text)
        
        return response