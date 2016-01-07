#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '12/17/14'

"""Generate tile render list efficiently using rendered tile bitmap

The theme given must be a white on black map which white defines area
to render.
"""

import mapnik
import numpy as np
import scipy.ndimage
import argparse
import os
import tempfile
import random

TEMP_IMAGE = os.path.join(tempfile.gettempdir(),'~temp~image.tif')
# TEMP_IMAGE = os.path.join('temp_image.tiff')

tempfile._get_candidate_names()

def render_bitmap(map_theme, tile_size):
    map = mapnik.Map(tile_size, tile_size)
    mapnik.load_map(map, map_theme)
    # Zoom to EPSG:3857 bounding box
    bbox = mapnik.Box2d(-20037508.34, -20037508.34, 20037508.34, 20037508.34)
    map.zoom_to_box(bbox)

    image = mapnik.Image(tile_size, tile_size)
    mapnik.render(map, image)

    image.save(TEMP_IMAGE)


def read_bitmap(z, threshold=25):
    image = scipy.ndimage.imread(TEMP_IMAGE, flatten=True)
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
    render_bitmap(args.map_theme, tile_size)

    slices = read_bitmap(args.z)
    for (x, y) in slices:
        args.render_list.write('%d,%d,%d\n' % (args.z, x, y))


if __name__ == '__main__':
    main()
