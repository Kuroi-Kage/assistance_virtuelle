from core.memory import Memory
import pytest 

# -------------------------
# Test ajout de message normal
# -------------------------
def test_add_message():
    mem = Memory()
    result = mem.add("bonjour")
    assert result is True
    assert len(mem.data) == 1
    assert mem.data[0]["text"] == "bonjour"

# -------------------------
# Test ajout message vide

# -------------------------
def test_add_empty_message():
    mem = Memory()
    result = mem.add("   ")
    assert result is False
    assert mem.data == []

# -------------------------
# Test limite mémoire courte
# -------------------------
def test_short_memory_limit():
    mem = Memory(max_short=2)
    mem.add("a")
    mem.add("b")
    mem.add("c")
    
    assert len(mem.short_memory) == 2
    assert mem.short_memory[0]["text"] == "b"
    assert mem.short_memory[1]["text"] == "c"

# -------------------------
# Test récupérer les derniers messages
# -------------------------
def test_get_last_n():
    mem = Memory()
    mem.add("1")
    mem.add("2")
    mem.add("3")

    last = mem.get_last_n(2)
    assert len(last) == 2
    assert last[0]["text"] == "2"
    assert last[1]["text"] == "3"

# -------------------------
# Test sauvegarde et chargement fichier
# -------------------------
def test_save_and_load(tmp_path):
    file_path = tmp_path / "memory.json"
    mem = Memory(save_file=str(file_path))

    mem.add("hello")
    mem.save_to_file()

    mem2 = Memory(save_file=str(file_path))
    mem2.load_from_file()

    assert len(mem2.data) == 1
    assert mem2.data[0]["text"] == "hello"

# -------------------------
# Test fichier inexistant
# -------------------------
def test_load_missing_file(tmp_path):
    file_path = tmp_path / "not_exist.json"
    mem = Memory(save_file=str(file_path))
    mem.load_from_file()
    assert mem.data == []

# -------------------------
# Test exists()
# -------------------------
def test_exists():
    mem = Memory()
    mem.add("test")
    assert mem.exists("test") is True
    assert mem.exists("autre") is False

# -------------------------
# Test clear()
# -------------------------
def test_clear():
    mem = Memory()
    mem.add("msg")
    mem.clear()
    assert mem.data == []

# -------------------------
# Test last() pour dernier message
# -------------------------
def test_last():
    mem = Memory()
    assert mem.last() is None
    mem.add("dernier")
    assert mem.last()["text"] == "dernier"

