#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '1/6/16'

import yaml
import json
import sys

print(json.dumps(yaml.load(open(sys.argv[1])), indent=2))

