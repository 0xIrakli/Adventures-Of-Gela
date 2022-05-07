from . import Image, rand


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


def build_level(tilemap, level, level_n, res):
    img = Image.new("RGBA", (len(level[0]) * res, len(level) * res))

    for y in range(len(level)):
        for x in range(len(level[0])):
            img.paste(
                rand.choice(tilemap[level_n][level[y][x]]),
                box=(x * res, y * res, (x + 1) * res, (y + 1) * res)
            )
            
    return img