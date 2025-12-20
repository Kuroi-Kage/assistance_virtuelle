from config import Config


cfg= Config()
    
def test_configuration():
    
    print(f"Nom: {cfg.IDENTITE['nom']}")
    print(f" Version: {cfg.IDENTITE['version']}")
    
    
    print(f"Règles absolues: {len(cfg.REGLE_ABSLUTES)}")
    for regle in cfg.REGLE_ABSLUTES:
        print(f"  -{regle['description']}")
    
test_configuration()