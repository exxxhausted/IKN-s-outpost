input_str = input()
codes = [int(code) for code in input_str.split() if 0 <= int(code) <= 255]
cp866_bytes = bytes(codes)
utf8_text = cp866_bytes.decode('cp866')  
print(utf8_text)