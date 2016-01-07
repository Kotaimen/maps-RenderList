PYTHON = /usr/bin/env python3
CARTO = /usr/bin/env carto
YAML2MML = ../yaml2mml.py
BITMAP = ../bitmap.py
CLUSTERIFY = ../clusterify.py

stylesheets = $(patsubst %.yaml,%.xml,$(wildcard carto/*.yaml))

renderlists = \
	srtm30plus_01.csv srtm30plus_02.csv srtm30plus_03.csv srtm30plus_04.csv \
	ned30m_05.csv ned30m_06.csv ned30m_07.csv ned30m_08.csv ned30m_09.csv ned30m_10.csv \
	ned10m_10.csv ned10m_11.csv ned10m_12.csv ned10m_13.csv ned10m_14.csv \
	ned3m_12.csv ned3m_13.csv ned3m_14.csv
	
usa1_9 = \
	srtm30plus_01.csv srtm30plus_02.csv srtm30plus_03.csv srtm30plus_04.csv \
	ned30m_05.csv ned30m_06.csv ned30m_07.csv ned30m_08.csv ned30m_09.csv

usa10_13 = \
	ned10m_10.csv ned10m_11.csv ned10m_12.csv ned10m_13.csv 

all : $(renderlists) usa1_9.csv usa10_13.csv
.PHONY : all

clean :
	$(RM) carto/*.?ml
	$(RM) *.csv
.PHONY : clean

VPATH = carto

%.mml : %.yaml ${YAML2MML}
	${PYTHON} ${YAML2MML} $< > $@

%.xml : %.mml style.mss
	${CARTO} -n $< > $@

$(stylesheets) : $(wildcard *.yaml)

%.csv : $(stylesheets) 
	${PYTHON} ${BITMAP} -z $(lastword $(subst _, ,$(basename $@))) $< $@
	${PYTHON} ${CLUSTERIFY} $@

usa1_9.csv: $(usa1_9)
	cat $(usa1_9) > $@
	${PYTHON} ${CLUSTERIFY} $@

usa10_13.csv: $(usa10_13)
	cat $(usa10_13) > $@
	${PYTHON} ${CLUSTERIFY} $@
