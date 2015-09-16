Frog-Pi
-------

An example script to upload data to [data.sparkfun.io](https://data.sparkfun.com/) and [numerous](http://numerousapp.com/).

[Project details on Hackaday.io](https://hackaday.io/project/7667-poison-dart-frog-humidity-sensor)

# Usage

An ansible playbook is provided to upload files to a raspberry pi

## Ansible

Create a node list at `~/.ansible/raspi.ini`

```
[raspi]
192.168.1.125
```

Then run the playbook

    ansible-playbook humidity.yaml -i ~/.ansible/raspi.ini -vvv

On your raspberry pi you will then have scripts in `/home/pi/temperature`

ssh into your pi, and run the following commands (where 11 = DST11 and 4 = GPI pin)

## Script

Edit the following scripts with your api keys

```bash
/home/pi/temperature/secrets/numerousapi.sh
/home/pi/temperature/secrets/phantapi.sh
```

Then run the following  

```bash
sudo su -
source /home/pi/temperature/secrets/numerousapi.sh
source /home/pi/temperature/secrets/phantapi.sh
python /home/pi/temperature/humidity.py 11 4
```

## Automatic startup

To poll run the script on a schedule

    watch -n 60 python /home/pi/temperature/humidity.py 11 4

To make sure the script runs at startup, start with `NOHUP` or create a `screen` session. 

![](http://cl.ly/image/3n2e0j1J1w3f/Screen%20Shot%202015-09-15%20at%209.45.18%20PM.png)
