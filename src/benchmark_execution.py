from timeit import Timer

IMAGE_SRC = 'src/assets/cover_image_coin.png'
REPETITION = 100
UNIT = 'kB'

LOADS_IN_KB = [98, 118, 200, 494, 642, 1388, 1798, 1926, 10690, 14620]


def run_load(load):
    global IMAGE_SRC, REPETITION, UNIT
    file_src = f'src/assets/{load}{UNIT}.txt'
    content = open(file_src).read()

    time = Timer(stmt=f"encrypt(Image('{IMAGE_SRC}'), '{content}')",
                 setup=f"from implementierung import encrypt; from image import Image;"
                 ).timeit(number=REPETITION)

    execution_time = time / REPETITION
    print(f"Execution for {load}{UNIT} took {execution_time:.4f} seconds")


if __name__ == "__main__":
    for load in LOADS_IN_KB:
        run_load(load)
