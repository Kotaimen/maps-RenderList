# RenderList

Generate stonemason render list for various map projects.

Because calculating a complex render area's intersection with the tile grid is `very` slow (using ``GDAL``), 
trade performance for speed by render the area on a black background and counting pixels with ``numpy``.
