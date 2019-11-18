# MISP Monitor

Various bits and pieces to monitor a MISP instance

## Create a sync user

To make sure to not lose your data, make sure to create a [sync user](https://www.circl.lu/doc/misp/GLOSSARY.html#sync-user)

:warning: This might not be good enough ATM. You might need an elevated user privileges API key. This might get addressed soon(TM)

## Test things first

Now that you have a Sync User, copy the secrets file in place.

```
cp secrets/keys.py.sample secrets/keys.py
# Change the URL and API Key
./test.py
```

## Installing MISP Munin plugin

```
# Health Plugin
sudo cp munin/misp_health /usr/share/munin/plugins/
# configure secrets/keys.py for the target misp instance
sudo cp -r secrets /usr/share/munin/plugins/
sudo chmod 750 /usr/share/munin/plugins/secrets/keys.py
sudo chgrp munin /usr/share/munin/plugins/secrets/keys.py
# Index 0 instance
sudo ln -s /usr/share/munin/plugins/misp_health /etc/munin/plugins/misp_health_0
# Index 1 instance (etc...)
sudo ln -s /usr/share/munin/plugins/misp_health /etc/munin/plugins/misp_health_1

# Stats Plugin
sudo cp munin/misp_stats /usr/share/munin/plugins/
# Index 0 instance
sudo ln -s /usr/share/munin/plugins/misp_stats /etc/munin/plugins/misp_stats_0
# Index 1 instance (etc...)
sudo ln -s /usr/share/munin/plugins/misp_stats /etc/munin/plugins/misp_stats_1

# OpenBSD has the plugins directory somewhere else.
# doas cp munin/misp_health /usr/local/libexec/munin/plugins/
```

## Testing MISP Munin plugin

```
$ sudo munin-run misp_health_0
database.value 0
workersCache.value 0
workersDefault.value 0
workersEmail.value 0
workersPrio.value 0
workersUpdate.value 0
workersScheduler.value 0
version.value 0
zmq.value 0
gpg.value 0
moduleEnrichment.value 0
moduleExport.value 0
moduleImport.value 0
mispLive.value 0
total.value 0
$ sudo munin-run misp_health_1
database.value 7
workersCache.value 0
workersDefault.value 0
workersEmail.value 0
workersPrio.value 0
workersUpdate.value 0
workersScheduler.value 0
version.value 0
zmq.value 1
gpg.value 1
moduleEnrichment.value 0
moduleExport.value 0
moduleImport.value 0
mispLive.value 0
total.value 9
.
.
.
$ sudo munin-run misp_health 199
. . .
$ sudo munin-run misp_stats_0
eventCount.value 21
attribCount.value 4825
correlationCount.value 3
userCount.value 2
orgCount.value 4
localOrgCount.value 1
proposalCount.value 0
```

## Known issues

:warning: The stats module only works on Python 3.6+

### PyMISP

You might see the following:

```
/etc/munin/plugins/misp_health_1:133: DeprecationWarning: Call to deprecated method __init__. (Please use ExpandedPyMISP instead (requires Python 3.6+). This class will be an alias of ExpandedPyMISP early 2020 and your code will most probably fail.)
  misp = PyMISP(misp_url, misp_key, misp_verifycert)
/usr/local/lib/python3.5/dist-packages/pymisp/api.py:101: DeprecationWarning: Call to deprecated method get_recommended_api_version. (Use ExpandedPyMISP.recommended_pymisp_version) -- Deprecated since version 2.4.110.
  response = self.get_recommended_api_version()
/usr/local/lib/python3.5/dist-packages/pymisp/api.py:118: DeprecationWarning: Call to deprecated method get_live_describe_types. (Use ExpandedPyMISP.describe_types_remote) -- Deprecated since version 2.4.110.
  self.describe_types = self.get_live_describe_types()
/etc/munin/plugins/misp_health_1:134: DeprecationWarning: Call to deprecated method direct_call. (Use ExpandedPyMISP.direct_call)
  result = misp.direct_call(relative_path, body)
```


This means you are using an older version of python3 (<3.6)

[PyMISP](https://github.com/MISP/PyMISP) runs best on 3.6+

### Too many underscores or other index issues

```
$ sudo munin-run misp_health_42
Something went wrong, the munin script needs to be in the form of: misp_health_0 ; where 0 is index 0 of the misp instance defined in keys.py
```

This might mean that you call the script in a path where an addition underscore (_) is present.
Make sure the only underscores in the absolute path are in the `misp_health_` script.
In addition, double check `keys.py`

### Index errors

```
$ sudo munin-run misp_health_42
You seem to try and access a configuration index that does not exist. Bye.
```

This certainly means that you are trying to call an instance configuration that is not listed in `keys.py` double check the config.


