from core.precessor import Precessor

proc = Precessor()


tests = [
    "Bonjour",
    "Comment ça va?",
    "ouvre la porte",
    "Montre-moi les fichiers",
    "Quoi de neuf?",
    "Simple message"
]

for t in tests:
    result = proc.detect(t)
    print(f"Message: '{t}' => Type: {result}")
