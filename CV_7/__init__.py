import numpy as np
import random
from PIL import Image, ImageDraw
import bisect


def displacement(start, end, roughness, vertical_displacement=None,
                 num_of_iterations=16):
    if vertical_displacement is None:
        vertical_displacement = (start[1] + end[1]) / 2
    points = [start, end]
    for iteration in range(1, num_of_iterations):
        points_tup = tuple(points)
        for i in range(len(points_tup) - 1):
            midpoint = list(map(lambda x: (points_tup[i][x] + points_tup[i + 1][x]) / 2,
                                [0, 1]))
            midpoint[1] += random.choice([-vertical_displacement,
                                          vertical_displacement])
            bisect.insort(points, midpoint)
        vertical_displacement *= 2 ** (-roughness)
        iteration += 1
    return points


def draw(layer, width, height):
    landscape = Image.new('RGBA', (width, height), (255, 255, 255))
    landscape_draw = ImageDraw.Draw(landscape)

    final_layers = []
    for layer in layer:
        sampled_layer = []
        for i in range(len(layer) - 1):
            sampled_layer += [layer[i]]

            if layer[i + 1][0] - layer[i][0] > 1:

                m = float(layer[i + 1][1] - layer[i][1]) / (layer[i + 1][0] - layer[i][0])
                n = layer[i][1] - m * layer[i][0]
                r = lambda x: m * x + n
                for j in np.arange(layer[i][0] + 1, layer[i + 1][0], 0.1):
                    sampled_layer += [[j, r(j)]]
        final_layers += [sampled_layer]

    final_layers_enum = enumerate(final_layers)
    for final_layer in final_layers_enum:
        for x in range(len(final_layer[1]) - 1):
            landscape_draw.line((final_layer[1][x][0], height - final_layer[1][x][1],
                                 final_layer[1][x][0], height), (0, 255, 0))

    return landscape


def main():
    width = 1400
    height = 700

    layer = displacement([0, 350], [width, 320], 0.9, 250, 8)
    landscape = draw([layer], width, height)
    landscape.show()


if __name__ == "__main__":
    main()
