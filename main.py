from config import Config

conf = Config()

def main():
    
    print(f"Nom: {conf.IDENTITE['nom']}")
    print(f"Version: {conf.IDENTITE['version']}")
    
    
    while True:
        # Lire l'entrée utilisateur
        user_input = input("Vous: ")
        
        # Condition de sortie
        if user_input.lower() == 'stop':
            print("Arrêt de l'IA. À bientôt")
            break
        
        # Réponse 
        print(f"IA: J'ai reçu: '{user_input}'")
        print (f" (En attente)")
    

if __name__ == "__main__":
    main()