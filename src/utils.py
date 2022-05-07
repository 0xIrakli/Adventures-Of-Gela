from . import *

def generate_tilemap(res):
    tiles = []
    tilemap = Image.open('assets/levels/0/tilemap.png')
    for y in range(tilemap.height//res):
        tiles.append([])
        tiles[y].append([])
        tiles[y].append([])
        for x in range(4):
            tiles[y][x//2].append(tilemap.crop((x*res, y*res, (x*res)+res, (y*res)+res)))  
    return tiles