from pathlib import Path

# base = Path.home()

# guia = Path(base,"europa","españa",Path("Barcelona", "sagrada_familia.txt"))
# guia2 = guia.with_name("la_pedreda.txt")
# print(guia)
# print(guia.parent)

# guia = Path("Europa")

# for txt in Path(guia).glob("*.txt"):
#     print(txt)

# Manera recursiva de listar todos los txt

# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)

guia = Path("europa","españa","Barcelona", "sagrada_familia.txt")
en_auropa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","España"))
print(en_auropa)
print(en_espania)

