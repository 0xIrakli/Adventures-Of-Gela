from . import Image


def generate_tilemap(res):
    tilemap = Image.open('assets/levels/0/tilemap.png')
    tiles = [
        [
            [
                tilemap.crop((x, y, x + res, y + res)),
                tilemap.crop((x + res, y, x + res * 2, y + res))
            ]
            for x in range(0, tilemap.width, res * 2)
        ]
        for y in range(0, tilemap.height, res)
    ]
    return tiles
