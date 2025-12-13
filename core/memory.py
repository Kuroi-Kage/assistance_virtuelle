import json
from datetime import datetime
from typing import List, Dict, Optional

class Memory:
    def __init__(self, max_length: Optional[int] = None, save_file: str ="memory.json"):
        self.data: List[Dict] = []
        self.max_length = max_length
        self.save_file = save_file
     
    def _now_iso(self) -> str:
         return datetime.now().isoformat()   
     
    def exists(self, text:str) -> bool:
        # Retourn true si le texte déja existe
        return any(entry["text"]== text for entry in self.data)
     
    # Ajouter un message
    def add(self, text: str, msg_type: str = "normal") -> bool:
        text = text.strip() # retire espace avant:apres
        if not text:
            return False 
        
        # vérifier doublon
        if text in [entry["text"] for entry in self.data]:
            return False
        
        entry = {
            "text": text,
            "type": msg_type,
            #"timestamp": datetime.now().isoformat()
            "timestamp" : self._now_iso()
            }
        self.data.append(entry)
        
        # Limite de mémoire
        if self.max_length is not None:
            while len(self.data) > self.max_length:
                self.data.pop(0)
        return True
    
    # Obtenir tout
    def get_all(self) -> List[Dict]:
        return self.data
    
    # Obtenir le dernier message   
    def get_last(self):
        # Retourn le dernier élément ou None si la mémoire est vide
        return self.data[-1] if self.data else FileNotFoundError
    
    def last(self) -> Optional[Dict]:
        # Retourne la derniere entree ou None.
        return self.data[-1] if self.data else None
    
    def get_last_n(self, n:int) -> List[Dict]:
        # Retourne les dernieur entrées
        if n <= 0:
            return []
        return self.data[-n:]
    
    def clear(self):
        #vide la memoire en memoire
        self.data = []
    
    # Sauvegarder 
    def save_to_file(self):
        try:
            # s'assurer que le dossier existe
            import os
            folder = os.path.dirname(self.save_file)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
                
            with open(self.save_file, 'w', encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            # NE PAS LEVEL D'EXCEPTION BRUTALE ICI : retourner l'erreur pour debug
            raise RuntimeError(f"Erreur sauvegarder memoire: {e}")
                
    
    # Charger depuis fichier JSON
    def load_from_file(self):
        try:
            with open(self.save_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            # fchier corropu -> on garde mémoire vide mais signale
            self;data = []
            raise RuntimeError("Fichier memoire corrompu(JSON invalide).")
        
    # utilitaire pour debug / affichage
    def __repr__(self):
        return f" <Memory len={len(self.data)} max_length={self.max_length} file='{self.save_file}'>"

        