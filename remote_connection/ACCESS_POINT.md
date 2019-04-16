# Setting up a Raspberry Pi as an access point in a standalone network 

## Requirements

Follow [this tutorial](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

Note: this is the hostapd configuration on the Raspberry Pi on the car

```
interface=wlan0
driver=nl80211
ssid=RaspberryCar
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=InternetOfThings
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

## Start the access point service

```
sudo systemctl start dnsmasq
sudo systemctl start hostapd
```

## Stop the access point service

```
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
```

## Make the service run when the Pi boots

```
sudo systemctl enable dnsmasq
sudo systemctl enable hostapd
```

See [this tutorial](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) for more details