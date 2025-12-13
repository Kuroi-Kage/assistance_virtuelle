from core.memory import Memory

mem = Memory(max_short=3)

#mem.add("bonjour")
#mem.add("quoi qu'il arriver?", msg_type="question")
#mem.add('je pense')
#mem.add("Encore et encore")

#mem.save_to_file()
#mem.load_from_file()
#for entry in mem.get_all():
  #  print(entry)
  
def print_mem(mem):
    print("-----Mémoire (len={}) -----".format(len(mem.get_all())))
    for i, e in enumerate(mem.get_all(), 1):
        print(f"{i}. [{e['type']}] {e['text']} ({e['timestamp']})")
    print("----------------------\n")
    
mem = Memory(max_short=None, save_file="memory.json")

mem.clear()

#Ajouts
print("Ajout 'Bonjour' =>", mem.add("Bonjour", "normal"))
print("Ajout 'Comment ça va?' =>", mem.add("Comment ça va", "question"))
print("Ajout doublon 'Bonjour' =>", mem.add("Bonjour", "normal"))
print("Ajout ''(vide) =>", mem.add("   ", "normal"))

print_mem(mem)


print('Last 2:', mem.get_last_n(2))

mem.save_to_file()
mem.clear()
print("Après clear :", mem.get_all())
mem.load_from_file()
print("Apres load :")
print_mem(mem)