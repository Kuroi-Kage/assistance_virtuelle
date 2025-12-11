from core.memory import Memory

mem = Memory()
mem.add("Hello")
mem.add("")

print("Dernier élement : ", mem.get_last())