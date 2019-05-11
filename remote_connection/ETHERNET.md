# How to remotely connect to your Raspberry Pi usign your Laptop

## Requirements

Follow [this tutorial](https://www.raspberrypi.org/documentation/remote-access/vnc/) to enable the VNC Server on your Raspberry Pi and install the [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) on your laptop

## Prepare your Laptop

Install the DHCP Server

```bash
sudo apt install isc-dhcp-server
```

Add to /etc/dhcp/dhcpd.conf this lines (with superuser permissions)

```
subnet 10.1.1.0 netmask 255.255.255.0 {
    range 10.1.1.1 10.1.1.127;
    option broadcast-address 10.1.1.255;
}

# Get the Raspberry Pi MAC address of the ethernet interface
# and put it after 'hardware ethernet'
host raspberry {
    hardware ethernet b8:27:eb:59:04:65;
    fixed-address 10.1.1.200;
    option host-name "raspberry";
}
```

Get the name of the ethernet interface of your laptop using `ifconfig`, e.g. eth0

Statically assign an IP address inside the subnet you want to create to the ethernet interface

```bash
sudo ip addr flush dev eth0
sudo ip address add 10.1.1.254/24 dev eth0
```

Run a DHCP Server on the ethernet interface 

```bash
sudo chmod a+w /var/lib/dhcp/dhcpd.leases
sudo dhcpd -4 eth0
sudo systemctl restart isc-dhcp-server.service
```

## Prepare your Raspberry Pi

Get the name of the ethernet interface of your Raspberry Pi using `ifconfig`, e.g. eth0

Delete the current IP on the ethernet interface

```bash
sudo ip addr flush dev eth0
```

Then, connect the device to the laptop using an ethernet cable and reboot. It will automatically get the IP address 10.1.1.200 that you can use in the VNC Viewer
