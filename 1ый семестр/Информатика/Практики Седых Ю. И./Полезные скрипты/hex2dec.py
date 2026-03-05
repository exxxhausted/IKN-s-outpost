nums = input("Введите коды символов через пробел")
dec_codes = [str(int(i, 16)) for i in nums.split(" ")]
print(" ".join(dec_codes))