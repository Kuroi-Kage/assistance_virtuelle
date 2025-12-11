

class Memory:
    def __init__(self):
        self.data = []
        
    def add(self, item):
        self.data.append(item)
        
    def get_last(self):
        # Retourn le dernier élément ou None si la mémoire est vide
        return self.data[-1] if self.data else None
        