"""
    Sets não podem ter elementos duplicados
    add -> adiciona um dado
    update -> atualiza
    clear ->
    discard -> 
    union ou | ->  une
    intersection ou & -> todos os elementos presentes nos dois sets
    difference ou - -> elementos apenas no set da esquerda
    symmetric_difference ou ^ -> elementos que estao nos dois sets
"""

# Maneiras de criar um Set
set1 = {1, 2, 3, 4, 5, 6}
set2 = set()
set2.add(1)
set2.add(2)
set2.add(3)

print(set2)

set2.discard(2)
print(set2)

set3 = set1 | set2
