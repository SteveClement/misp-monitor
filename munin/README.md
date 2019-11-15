# Sample munin plugin

apt_ubuntu is provided as a sample script for munin

# Dependencies

```
sudo apt-get install python-apt
```

# Testing

To test if it works, simply execute the script.

```
$ ./apt_ubuntu 
security.value 0
updates.value 10
proposed.value 0
backports.value 0
other.value 4
total.value 14
```

# Using

To use this script, copy to the munin modules folder and restart munin-node.

```
$ sudo cp apt_ubuntu /etc/munin/plugins/
$ sudo munin-run apt_ubuntu
security.value 0
updates.value 10
proposed.value 0
backports.value 0
other.value 4
total.value 14
$ sudo systemctl restart munin-node
```
