#Temukan apakah suatu elemen ada dalam list

def sequential_search(data, key):
    for item in data:
        if item == key:
            return True
    return false 

my_list = [3, 6, 2, 9, 4, 7]
key =6
found = sequential_search(my_list, key)
if found:
    print("Elemen ditemukan")
else:
    print("Elemen tidak ditemukan.")
    
#Output Elemen ditemukan