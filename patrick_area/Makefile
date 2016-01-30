stylesheets = $(patsubst %.yaml,%.xml,$(wildcard carto/*.yaml))

renderlists = \
	srtm30plus_01.csv srtm30plus_02.csv srtm30plus_03.csv srtm30plus_04.csv \
	ned30m_05.csv ned30m_06.csv ned30m_07.csv ned30m_08.csv ned30m_09.csv ned30m_10.csv \
	ned10m_10.csv ned10m_11.csv ned10m_12.csv ned10m_13.csv ned10m_14.csv \
	ned3m_12.csv ned3m_13.csv ned3m_14.csv

# ned10m_15.csv ned4m_15.csv

terrain_4_16 = \
	srtm30plus_01.csv srtm30plus_02.csv srtm30plus_03.csv srtm30plus_04.csv \
	ned30m_05.csv ned30m_06.csv ned30m_07.csv ned30m_08.csv ned30m_09.csv \
    ned10m_10.csv ned10m_11.csv ned10m_12.csv ned10m_13.csv

all : $(renderlists) terrain_4_16.csv
.PHONY : all

VPATH = carto
include ../carto.mk

# Special combined render list
terrain_4_16.csv: $(terrain_4_16)
	cat $^ > $@
#	${PYTHON} ${CLUSTERIFY} $@

