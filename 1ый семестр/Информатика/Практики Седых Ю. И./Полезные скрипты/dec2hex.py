nums = input("Введите коды символов через пробел")
dec_codes = [int(i) for i in nums.split(" ")]
hex_codes = [hex(i)[2:] for i in dec_codes]
print(" ".join(hex_codes))