from config import Config

conf = Config()

class AgentIntent:
    def __init__(self):
        self.regles = conf.REGLE_COMPORTEMENT
        self.memoire = []
        
    def _check_condition(self, regle, user_message):
        """Vérifie si la condition d'une regle est satisfaite"""
        condition = regle.get("condition", "")
        
        #SI CONDITON = "QUESTION_FACTUELLE"
        #On vérifie si "question " ou "factuelle" est dans e message
        
        mots_condition = condition.split('_')
        for mot in mots_condition:
            if mot.lower() in user_message.lower():
                return True
            return False
        
    def __apply_action(self, regle, message):
        action = regle.get("action", "")
        details = regle.get("details", "")
        
        return f"Régle '{regle['id']}' : {action}. {details}"
        
                
    def apply_rules(self, user_input):
        """Cherche quelles règles s'appliquent"""
        applicable_rules = []
        for regle in self.regles:
            if self._check_condition(regle, user_input):
                applicable_rules.append(regle)
        return applicable_rules
    
    def generate_response(self, message, applicable_rules):
        """Genere une réponse basée sur les regles"""
        if applicable_rules:
            # Appliquer la règle la plus prioritaire
            return self._apply_action(applicable_rules[0], message)
        else:
            return "Je réflechis à votre demande..."
        