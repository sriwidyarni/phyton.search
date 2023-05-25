def find_insertion_position(nums, target):
    left = 0
    right = len(nums) - 1
    insert_pos = len(nums)  # Inisialisasi dengan posisi di luar daftar

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            insert_pos = mid  # Mengupdate posisi sisipan
            right = mid - 1

    return insert_pos

# Contoh penggunaan
numbers = [2, 5, 7, 10, 13, 17, 19]
target = 12

insertion_position = find_insertion_position(numbers, target)

print("Elemen", target, "akan disisipkan pada indeks", insertion_position)