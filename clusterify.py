#!/usr/bin/env python
# -*- encoding: utf-8 -*-

""" Sort render directive csv so tiles are better clustered geographically."""

__author__ = 'kotaimen'
__date__ = '11/18/15'

import os, sys
from stonemason.pyramid import hil_s_from_xy

# z>=17: sort by hilbert curve
# z<17: snap to z=17
CLUSTER_LAYER = 17

def tile_id_to_index(z, x, y):
    if z <= CLUSTER_LAYER:
        # snap to cluster layer
        d = CLUSTER_LAYER - z
        x2 = x << d
        y2 = y << d
        h = hil_s_from_xy(x2, y2, CLUSTER_LAYER)
        return h << 8 | (CLUSTER_LAYER - z), z, x, y
    else:
        h = hil_s_from_xy(x, y, z)
        return h << 8 | (22 - z), z, x, y


if __name__ == '__main__':
    fn = sys.argv[1]

    print('Clustering %s' % fn)

    def gen(fn):
        with open(fn, 'r') as fp:
            for n, line in enumerate(fp):
                yield tile_id_to_index(*tuple(map(int, line.split(','))))

    result = sorted(gen(fn))
    print('Sorted %d lines' % len(result))

    with(open(fn, 'w')) as fp:
        for (h, z, x, y) in result:
            fp.write('%d,%d,%d\n' % (z, x, y))
            
            