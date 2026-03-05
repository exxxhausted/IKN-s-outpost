input_text = input()
koi8_bytes = input_text.encode('koi8-r')
codes = [byte for byte in koi8_bytes]
print(' '.join(map(str, codes)))