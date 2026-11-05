## --- LIST ---

# Kumpulan data_numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data_string
data_string = ["ucup", "adit", "siti"]
print(data_string)

# Kumpulan data_boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bakwan", 2, "cireng", "ucup" , True , "adit" , False]
print(data_campuran)

## Cara alternatif membuat List
data_range = range(0, 10, 2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat List dengan For Loop, List Comprehension
list_for = [i ** 2 for i in range(0,10)]
print(list_for)

# Membuat List dengan For If
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_for_if)