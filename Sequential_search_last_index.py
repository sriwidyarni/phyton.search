# Temukan indeks terakhir dari elemen yang cocok dalam sebuah list

def sequential_search_last_index(data, key):
    lat_index = -1
    for i in range(len(data)):
        if data[i] == key:
            last_index = i
    return last_index

my_list = [5, 3, 8, 2, 7, 3, 4]
key = 3
last_index = sequential_search_last_index(my_list, key)
if last_index != -1:
    print(f"indeks terakhir elemen {key} adalah {last_index}")
else:
    print(f"Elemen {key} tidak ditemukan.")

# Indeks terakhir elemen 3 adalah 5