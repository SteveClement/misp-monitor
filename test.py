#!/usr/bin/env python
# -*- coding: utf-8 -*-

from secrets.keys import misp_url, misp_key, misp_verifycert, misp_client_cert

from pymisp import ExpandedPyMISP
import json

relative_path = 'servers/serverSettings/diagnostics'

body = None

misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
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
