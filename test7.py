def normalize(name):
    name=name.lower()
    name=name.capitalize()
    return name
name = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, name))
print(L2)