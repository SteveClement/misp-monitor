#!/usr/bin/env python
# -*- coding: utf-8 -*-

from secrets.keys import misps

from pymisp import ExpandedPyMISP
import json

relative_path = 'servers/serverSettings/diagnostics'

body = None

misp = ExpandedPyMISP(misps[0].split('|')[0], misps[0].split('|')[1], misps[0].split('|')[2])

result=misp.direct_call(relative_path, body)

print(result['version']['upToDate'])
print(result['gpgStatus'])
print(result['zmqStatus'])
print(result['moduleStatus']['Enrichment'])
print(result['moduleStatus']['Import'])
print(result['moduleStatus']['Export'])
print(result['dbSchemaDiagnostics']['checked_table_column'])
print(json.dumps(result['dbSchemaDiagnostics'], indent=2, sort_keys=True))

print(len(result['dbSchemaDiagnostics']['diagnostic']))
