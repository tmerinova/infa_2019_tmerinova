from graph import *

windowSize(800, 600)
canvasSize(800, 600)
brushColor('light blue')
rectangle(0, 0, 800, 300)
brushColor('green')
penColor('green')
rectangle(0, 300, 800, 600)

penSize(0.001)

k = 5


def house():
    brushColor('olive')
    penColor('black')
    rectangle(house_position_x, house_position_y, house_position_x + k * 26, house_position_y + k * 22)

    brushColor('turquoise')
    rectangle(house_position_x + k * 9, house_position_y + k * 8, house_position_x + k * 17, house_position_y + k * 15)

    brushColor('firebrick')
    polygon([(house_position_x, house_position_y), (house_position_x + k * 26, house_position_y),
             (house_position_x + k * 26 / 2, house_position_y - k * 14), (house_position_x, house_position_y)])


def cloud():
    brushColor('white')
    penColor('black')
    x = cloud_position_x

    for i in range(4):
        circle(x, cloud_position_y, k * 5)
        x += k * 4.6
    for i in range(2):
        circle(x - k * 14, cloud_position_y - 20, k * 5)
        x += k * 4.6


def tree():
    brushColor('black')
    brushColor('dark green')

    tree_leaves = k * 5
    tree_position_x = house_position_x + k * 51
    tree_position_y = house_position_y + k
    rectangle(tree_position_x, tree_position_y, tree_position_x + k * 2.4, tree_position_y + k * 14)

    circle(tree_position_x + k, tree_position_y - k * 14.4, tree_leaves)
    circle(tree_position_x - k * 4, tree_position_y - k * 10, tree_leaves)
    circle(tree_position_x + k * 7, tree_position_y - k * 10, tree_leaves)
    circle(tree_position_x + k, tree_position_y - k * 7, tree_leaves)
    circle(tree_position_x - k * 3, tree_position_y - k * 3, tree_leaves)
    circle(tree_position_x + k * 5, tree_position_y - k * 3, tree_leaves)


house_position_x = 50
house_position_y = 270

house()
cloud_position_x = 210
cloud_position_y = 100

cloud()

cloud_position_x = 650
cloud_position_y = 80
cloud()

tree()

house_position_x = 400
house_position_y = 250
k = 4

cloud_position_x = 430
cloud_position_y = 110

cloud()

tree()

house()

run()
