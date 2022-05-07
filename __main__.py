from src import *
from player import Player

win = init((800, 800))

base = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

levels = [
    {
        1: Image.open('levels/0/wall.png'),
        0: Image.open('levels/0/tile.png')
    }
]

def build_levels(levels):
    img = Image.new("RGB", ( len(base[0])*8, len(base)*8 ))
    for level in levels:
        for y in range(len(base)):
            for x in range(len(base[0])):
                img.paste(level[base[y][x]], box=(x*8, y*8, (x+1)*8, (y+1)*8))
    img.save('img.png')

build_levels(levels)

def main():
    player = Player([20, 20])
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
        player.draw(win)
        disp.update()
main()