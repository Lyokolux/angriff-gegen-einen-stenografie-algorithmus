from timeit import Timer

UNIT = 'mB'
file_src = f'src/assets/1{UNIT}.txt'
image_src = 'src/assets/cover_image_coin.png'
repetition = 100

print("Please wait...")

t = Timer(stmt="[choice(encryption_table[c]) for c in msg]",
          setup=f"from image import Image; from random import choice; content = open('{file_src}').read(); msg = [ord(c) for c in content]; encryption_table = Image('{image_src}').getEncryptionTable();"
          ).timeit(number=repetition)


fileSize = len(open(file_src).read())
list_comprehension_creation_time = Timer(
    stmt=f"[c for c in range({fileSize})]").timeit(number=repetition)

second_for_one_run = (t - list_comprehension_creation_time) / repetition
throughput = 1 / second_for_one_run
print(f"Throughput of {throughput:.4f} {UNIT}/s")
