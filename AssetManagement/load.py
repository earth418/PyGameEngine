from ..pyopengl import *
from PIL import Image

def get_data_from_png(filename):

    positions, colors = [], []

    data_columns = list(Image.open(filename).getdata())

    print(data_columns)

    # len(data[0])

    for index1, row in enumerate(data_columns):
        for index2, pixel in enumerate(row):
            colors.append(Color(pixel[0], pixel[1], pixel[2]))
            positions.append(Vec3(index1, index2, 0))


    # return Mesh()

get_data_from_png("D:\\AsepriteProjects\\Sword_PNG.png")

        
