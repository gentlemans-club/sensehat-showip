# sensehat-showip
Shows local IP on a Sense Hat!

This simple script gets the Raspberry Pi's local IP
and shows it on the Sense Hat LED matrix. After this,
you could SSH into the box without the need of a
computer screen connected to the device.

The IP is printed 10 times before the process
finishes, which is hopefully enough time for you to
note down what the IP is.

## Requirements

* Raspberry Pi
* Sense HAT
  * [The Sense HAT Python library](https://pythonhosted.org/sense-hat/#install)

## Setup

After cloning this repository, modify the `ExecStart`
line in `showip.service` to point to a valid path to
`showip.py`.  Then copy the service file:

```sh
cp showip.service /etc/systemd/system/
```

`showip.py` should also be possible to execute:

```sh
chmod +x showip.py
```

Then reload daemon files, enable (and alternatively,
start) the service. When the service is enabled, the
script will run on boot, after a network connection
has been established.

```sh
systemctl daemon-reload
systemctl enable showip
systemctl start showip
```

In order to connect to the Raspberry Pi at this point,
it is highly likely that you must be connected to the
same network as it is connected to. The SSH daemon
must also be [enabled](https://www.raspberrypi.org/documentation/remote-access/ssh/).
