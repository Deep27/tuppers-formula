from PIL import Image


def draw(k: int) -> list:
    k //= 17
    binary = bin(k)[2:]
    binary = ("0" * (1802 - len(binary))) + binary

    lists = [[] for x in range(17)]

    for x in range(1802):
        lists[-(x % 17)].append(binary[x])

    image = Image.new("1", (106, 17), 0)
    draw = image.load()
    for y in range(17):
        for x in range(106):
            image.putpixel(xy=(105 - x, 16 - y), value=(int(lists[y][x]),))
    image.save("image.png")


def f(x, y): return ((y // 17) // (1 << (17 * x + (y % 17)))) % 2




draw(int(input("Enter k")))
