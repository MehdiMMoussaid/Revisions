import random
equipe_hockey = ["Toronto", "Montreal", "Calgary", "Edmonton"]
print(equipe_hockey)

equipe_hockey.insert(2, "Vancover")
print(equipe_hockey)
equipe_hockey.pop(4)
print(equipe_hockey)
equipe_hockey.append("Winnepeg")
print(equipe_hockey)
print(random.choice(equipe_hockey))