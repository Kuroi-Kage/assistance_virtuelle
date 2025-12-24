from config import Config
from datetime import datetime

conf = Config()

def aff_aide():
    """NOTRE PREMIERE FONCTION UTILE"""
    
    print("COMMANDES DISPONIBLES")
    print(" aide     - Affiche ce message")
    print(" config   - Montre la configuration")
    print(" regles   - Liste les règles de comportement")
    print(" historique - Affiche l'historique de la conversation")
    print(" effacer - Efface l'historique")
    print(" stop     - Quitte le programme")
    print()

def aff_config():
    print("Configuration")
    print(f"Nom: {conf.IDENTITE['nom']}")
    print(f"Createur: {conf.IDENTITE['createur']}")
   # print(f"Objectif: {conf.IDENTITE['objectif']}")
    print()
    
    
def aff_rules():
    print(f" RÈGLES ({len(conf.REGLE_ABSLUTES)} absolues):")
    for regle in conf.REGLE_ABSLUTES:
        print(f"   .{regle['description']}")

def aff_history(history):
    if not history:
        print("l'historique est vide")
        return
    
    for i, (role, message, heure) in enumerate(history, 1):
        if role == "utilisateur":
            print(f"{i}. [{heure}] Vous: {message}")
        else:
            print(f"{i}. [{heure}] IA: {message}")
    
    print()
    
def _clean_history(history):
    history.clear()
    print("Historique effacé")           

def main():
    
    # Initialisation de l'historique
    history = []
    
    print(f"Configuration chargée: {conf.IDENTITE['nom']}")
    while True:
        # Lire l'entrée utilisateur
        user_input = input("Moi: ").strip()
        
        # Condition de sortie
        if user_input.lower() == 'stop':
            print("Arrêt . Merci d'avoir utilisé l'IA!")
            break
        
        elif user_input.lower() == 'aide':
            aff_aide()
            
        elif user_input.lower() == 'config':
            aff_config()
            
        elif user_input.lower() == 'regles':
            aff_rules()
            
        elif user_input.lower() == 'historique':
            aff_history(history)
            
        elif user_input.lower() == 'effacer':
            _clean_history(history)
            
            
        else:
            # Réponse
            reponse= f"'{user_input}' (Je vais apprendre à mieux répondre bientôt!)"
            
            # Enregistrer dans l'historique
            current_time = datetime.now().strftime("%H:%M:%S")
            history.append(("utilisateur", user_input, current_time))
            history.append(("IA", reponse, current_time))
            
            
            # Afficher la réponse
            print(f"IA: {reponse}")

if __name__ == "__main__":
    main()