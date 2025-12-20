from config import Config

cfg= Config()
    
def test_configuration():
    
    print(f"Nom: {cfg.IDENTITE['nom']}")
    print(f" Version: {cfg.IDENTITE['version']}")