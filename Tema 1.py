# tama_1 17.03.2022

# declara o lista care contine elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (In aceasta ordine)
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list, type(my_list))

# afisieaza lista initiala ordonata ascendent (lista initiala trebuie pastrata in acelasi forma)
my_list.sort()
print(my_list)

# afiseaza lista initiala ordonata descendent (lista initiala trebuie pastrata in aceasi forma)
my_list.reverse()
print(my_list)

# afiseaza o lista ce contine numerele pare din lista ordonata (folosind slice)
print(my_list[::2])

# afiseaza o lista ce contine numerele impare din lista ordonata (folosind slice)
print(my_list[1::2])

# afiseaza o lista ce contine numerele ce sunt multipli ai numarului 3 (folosind slice)
print(my_list[1:5:3])
