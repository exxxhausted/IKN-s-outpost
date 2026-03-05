nums = input("Введите коды символов через пробел")
dec_codes = [int(i) for i in nums.split(" ")]
bin_codes = [bin(i)[2:] for i in dec_codes]
print(" ".join(bin_codes))