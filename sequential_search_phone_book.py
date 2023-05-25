def sequential_search_phone_number(names, phone_numbers, target_name):
    for i in range(len(names)):
        if names[i] == target_name:
            return phone_numbers[i]
    return "Nomor telepon tidak ditemukan."

# Daftar nama dan nomor telepon
names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis"]
phone_numbers = ["081234567890", "089876543210", "087811223344", "082122232425"]

# Nama yang ingin dicari nomor teleponnya
target_name = "Jane Smith"

# Cari nomor telepon Jane
phone_number = sequential_search_phone_number(names, phone_numbers, target_name)

# Tampilkan hasil
print("Nomor telepon Jane Smith:", phone_number)