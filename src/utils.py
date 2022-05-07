from . import Image


def generate_tilemap(res):
    tilemap = Image.open('assets/levels/0/tilemap.png')

    tiles = [
        [
            tilemap.crop((x*res, y*res, (x*res)+res, (y*res)+res))
            for x in range(tilemap.width // res)
        ]
        for y in range(tilemap.height // res)
    ]

    return tiles
