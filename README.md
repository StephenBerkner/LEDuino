# LEDuino
An Arduino Based, IOT LED Sign

## Build-Instructions

You must manually create `server/credentials.hpp` with the following contents:

```c++
#define MY_SSID         "YOUR_SSID"
#define MY_PASSWORD     "YOUR_PASSWORD"
```

Replace `YOUR_SSID` and `YOUR_PASSWORD` with the name and password of your WiFi network.

**NEVER SHARE YOUR NETWORK CREDENTIALS WITH ANYONE!**

- You should under **no cirumstances** ever do any of the following:
  - Publish your credentials file to *any* repository
    - `server/credentials.hpp` is included in `.gitignore` for this reason specifically
  - Send anybody your credentials file or your WiFi credentials in plain text

## Sending a Message to the Sign

You'll need your sign's IP address which should be displayed through the serial monitor when you upload the code. The defualt port number 8000. is You can send a message to the sign using `client/client.py` as follows:

```shell
python client/client.py --ip LEDUINO_IP_ADDR --port 8000 --message "Hello, World!" 
```