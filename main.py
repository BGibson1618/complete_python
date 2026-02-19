def pic_printer(image: list) -> None:
    for row in image:
        for pixel in row:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')

my_pic = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

pic_printer(my_pic)
