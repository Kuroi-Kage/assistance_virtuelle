from config import Config
from datetime import datetime
import json
import os
from core.agents import AgentIntent




conf = Config()
agent = AgentIntent()
History_file = "save_memory.json"

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
    # Sauvegarder l'historique vide
    save_history(history)
    print("Historique effacé")   
    print()
            
def save_history(history):
    """Sauvegarde l'historique dans un fichier JSON

    Args:
        history (_type_): _description_
    """
    try:
        with open(History_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        print(f"Historique sauvegardé dans {History_file}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde: {e}")
    
def _load_history():
    """Charge l'historique depuis un fichier JSON"""
    if not os.path.exists(History_file):
        print(f"Aucun historique trouvé. Création d'un nouveau.")
        return []
    
    try:
        with open(History_file, 'r', encoding='utf-8') as f:
            history = json.load(f)
        print(f"Historique chargé depuis {History_file}")
        return history
    except Exception as e:
        print(f"Erreur lors du chargement: {e}")
        return []
def main():
    
    # Initialisation de l'historique
    history = _load_history()
    #agent = agent(Config)
    
    print(f"Configuration chargée: {conf.IDENTITE['nom']}")
    print(f"Messages dans l'historique: {len(history)}")
    while True:
        # Lire l'entrée utilisateur
        user_input = input("Moi: ").strip()
        #regles = AgentInssstent.apply_rules(user_input)
        #response = agent.generate_response(user_input, regles)
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
            #response= f"'{user_input}' (Je vais apprendre à mieux répondre bientôt!)"
            regle = agent.apply_rules(user_input)
            response = agent.generate_response(user_input, regle)
            
            # Enregistrer dans l'historique
            current_time = datetime.now().strftime("%H:%M:%S")
            history.append(("utilisateur", user_input, current_time))
            history.append(("IA", response, current_time))
            
            save_history(history)
            
            
            # Afficher la réponse
            print(f"IA: {response}")

if __name__ == "__main__":
    main()