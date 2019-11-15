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
