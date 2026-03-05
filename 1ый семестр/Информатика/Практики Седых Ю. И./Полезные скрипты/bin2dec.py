nums = input("Введите коды символов через пробел")
dec_codes = [str(int(i, 2)) for i in nums.split(" ")]
print(" ".join(dec_codes))