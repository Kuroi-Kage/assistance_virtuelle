class Precessor:
    # Détecte le type de message
    QUESTIONS = ["?"]
    SALUTATIONS = ["bonjour", "salut", "hello", "coucou", "hey", "yo"]
    INTERROGATIFS = ["comment", "quoi", "pourquoi", "ou", "qui", "quand"]
    COMMANDS = ["ouvre", "ferme", "montre", "ajoute", "supprime"]
    
    def detect(self, text: str) -> str:
        text_lower = text.lower().strip()
        # Vérifier question
        if "?" in text_lower or any(text_lower.startswith(word) for word in self.INTERROGATIFS ):
            return "question"
       # if any(q in text_lower for q in self.QUESTIONS):
           # return "question"
        #Vérifier commande
        if any(text_lower.startswith(cmd) for cmd in self.COMMANDS):
            return "command"
        
        if any(salut in text_lower for salut in self.SALUTATIONS):
            return "greeting"
        # sinon message normal
        return "normal"