# sensehat-showip
Shows local IP on a Sense Hat!

This simple script gets the Raspberry Pi's local IP
and shows it on the Sense Hat LED matrix. After this,
you could SSH into the box without the need of a
computer screen connected to the device.

The IP is printed 10 times before the process
finishes, which is hopefully enough time for you to
note down what the IP is.

## Setup

After cloning this repository, modify the `ExecStart`
line in `showip.service` to point to a valid path to
`showip.py`.  Then copy the service file:

```sh
cp showip.service /etc/systemd/system/
```

Then reload daemon files, enable (and alternatively,
start) the service.

```sh
systemctl daemon-reload
systemctl enable showip
systemctl start showip
```
