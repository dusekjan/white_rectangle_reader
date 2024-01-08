from PIL import Image


TO_LIGHT = [204, 218, 240]
TO_LIGHT2 = [224, 230, 239]
TO_LIGHT3 = [240, 242, 251]


def clean_noise(image: Image):
    data = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b, _ = data[x, y]

            if abs(TO_LIGHT[0] - r) < 15 and \
                    abs(TO_LIGHT[1] - g) < 15 and \
                    abs(TO_LIGHT[2] - b) < 15:
                data[x, y] = (249, 249, 247)
            elif abs(TO_LIGHT2[0] - r) < 15 and \
                    abs(TO_LIGHT2[1] - g) < 15 and \
                    abs(TO_LIGHT2[2] - b) < 15:
                data[x, y] = (249, 249, 247)
            elif abs(TO_LIGHT3[0] - r) < 15 and \
                    abs(TO_LIGHT3[1] - g) < 15 and \
                    abs(TO_LIGHT3[2] - b) < 15:
                data[x, y] = (249, 249, 247)

    image.save("./obrazku.png")

#clean_noise(Image.open("noty (1).png"))
