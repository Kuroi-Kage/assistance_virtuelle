from core.rules import RULES

class Reasonning:
    def __init__(self, memory):
        self.memory = memory
    
    def think(self, text):
        # logiqement : enregistrer dans la mémoire
        last = self.memory.get_last()
        text_lower = text.lower()
        
        # Vérifier les règles d'abord
        for key, response in RULES.items():
            if key in text_lower:
                self.memory.add(text)
                return response
        
        # petit logique: transformer le texte
        #return text.upper()
        
        # Logique simple
        last = self.memory.get_last()
        
        #if len(self.memory.data) ==1:
        if last and text == last:
            response = "Tu viens de dire la même chose !"
        elif last:
            response = f"Le dernier message était : '{last}'"
        else:
            response = f" Je prends note de ton premier message: '{text}'"
            
        self.memory.add(text)
        
        return response