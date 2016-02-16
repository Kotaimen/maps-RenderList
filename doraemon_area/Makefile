stylesheets = $(patsubst %.yaml,%.xml,$(wildcard carto/*.yaml))

renderlists = \
	topmesh_01.csv topmesh_02.csv topmesh_03.csv topmesh_04.csv topmesh_05.csv \
    middlemesh_05.csv middlemesh_06.csv middlemesh_07.csv middlemesh_08.csv middlemesh_09.csv \
    basemesh_09.csv basemesh_10.csv basemesh_11.csv basemesh_12.csv basemesh_13.csv \
    basemesh_14.csv basemesh_15.csv \
    cityadmin_13.csv cityadmin_14.csv cityadmin_15.csv

default_1x = \
    topmesh_01.csv topmesh_02.csv topmesh_03.csv topmesh_04.csv \
    middlemesh_05.csv middlemesh_06.csv middlemesh_07.csv middlemesh_08.csv \
    basemesh_09.csv basemesh_10.csv basemesh_11.csv basemesh_12.csv \
    cityadmin_13.csv cityadmin_14.csv cityadmin_15.csv

default_2x = \
    $(default_1x) basemesh_13.csv

ipc_gelded = \
    topmesh_01.csv topmesh_02.csv topmesh_03.csv topmesh_04.csv \
    middlemesh_05.csv middlemesh_06.csv middlemesh_07.csv middlemesh_08.csv \
    basemesh_09.csv basemesh_10.csv basemesh_11.csv basemesh_12.csv \
    basemesh_13.csv basemesh_14.csv

all : $(renderlists) default_1x.csv default_2x.csv ipc_gelded.csv
.PHONY : all

VPATH = carto
include ../carto.mk

# Special combined render list
default_1x.csv: $(default_1x)
	cat $(default_1x) | sort | uniq > $@
	${PYTHON} ${CLUSTERIFY} $@

default_2x.csv: $(default_2x)
	cat $(default_2x) | sort | uniq > $@
	${PYTHON} ${CLUSTERIFY} $@

ipc_gelded.csv: $(ipc_gelded)
	cat $(ipc_gelded) | sort | uniq > $@
	${PYTHON} ${CLUSTERIFY} $@
