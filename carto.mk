PYTHON = /usr/bin/env python
CARTO = /usr/bin/env carto
YAML2MML = ../yaml2mml.py
BITMAP = ../bitmap.py
CLUSTERIFY = ../clusterify.py

%.mml : %.yaml ${YAML2MML}
	${PYTHON} ${YAML2MML} $< > $@

%.xml : %.mml style.mss
	${CARTO} -n $< > $@

$(stylesheets) : $(wildcard *.yaml)

%.csv : $(stylesheets) 
	${PYTHON} ${BITMAP} -z $(lastword $(subst _, ,$(basename $@))) $< $@
	${PYTHON} ${CLUSTERIFY} $@

clean :
	$(RM) carto/*.mml carto/*.xml
	$(RM) *.csv
.PHONY : clean
