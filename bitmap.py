#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '12/17/14'

"""Generate tile render list efficiently using rendered tile bitmap

The theme given must be a white on black map which white defines area
to render.
"""
import argparse
from PIL import Image
import mapnik
import numpy as np


def render_bitmap(map_theme, tile_size):
    assert tile_size<=32768
    map = mapnik.Map(tile_size, tile_size)
    mapnik.load_map(map, map_theme)
    # Zoom to EPSG:3857 bounding box
    bbox = mapnik.Box2d(-20037508.34, -20037508.34, 20037508.34, 20037508.34)
    map.zoom_to_box(bbox)

    image = mapnik.Image(tile_size, tile_size)
    mapnik.render(map, image)

    raw_data = image.tostring()
    pil_image = Image.frombuffer('RGBA', (tile_size, tile_size), raw_data,
                                 'raw', 'RGBA', 0, 1)
    del raw_data
    pil_image = pil_image.convert(mode='L')
    return np.array(pil_image)


def read_bitmap(image, z, threshold=25):
    bitmap = image > threshold
    del image
    slices = np.transpose(np.nonzero(np.transpose(bitmap)))
    del bitmap
    return slices


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-z', type=int, default=10,
                        help='tile level of the render list generated')

    parser.add_argument('map_theme', type=str,
                        help='location of the mapnik theme xml')

    parser.add_argument('render_list', type=argparse.FileType('w'),
                        help='location of the rende list csv')

    args = parser.parse_args()

    tile_size = 2 ** args.z
    bitmap = render_bitmap(args.map_theme, tile_size)

    slices = read_bitmap(bitmap, args.z)
    for (x, y) in slices:
        args.render_list.write('%d,%d,%d\n' % (args.z, x, y))


if __name__ == '__main__':
    main()
