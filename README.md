# MISP Monitor

Various bits and pieces to monitor a MISP instance

## Create a sync user

To make sure to not lose your data, make sure to create a [sync user](https://www.circl.lu/doc/misp/GLOSSARY.html#sync-user)

## Test things first

Now that you have a Sync User, copy the secrets file in place.

```
cp secrets/keys.py.sample secrets/keys.py
# Change the URL and API Key
./test.py
```

## Installing MISP Munin plugin

```
sudo cp munin/misp_health /usr/share/munin/plugins/
# configure secrets/keys.py for the target misp instance
sudo cp -r secrets /etc/munin/plugins/
# Index 0 instance
sudo ln -s /usr/share/munin/plugins/misp_health /etc/munin/plugins/munin_health_0
# Index 1 instance (etc...)
sudo ln -s /usr/share/munin/plugins/misp_health /etc/munin/plugins/munin_health_1
# OpenBSD has the plugins directory somewhere else.
# doas cp munin/misp_health /usr/local/libexec/munin/plugins/
```

## Testing MISP Munin plugin

```
sudo munin-run misp_health_0
sudo munin-run misp_health_1
.
.
.
sudo munin-run misp_health 199
```
