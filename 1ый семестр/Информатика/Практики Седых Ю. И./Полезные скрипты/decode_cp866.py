input_text = input()
cp866_bytes = input_text.encode('cp866')
codes = [byte for byte in cp866_bytes]
print(' '.join(map(str, codes)))