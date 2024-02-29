# Gozle disk api
Gozle disk api is an unofficial api for the gozle disk service which provides the ability to log into your account, see the amount of space on your account and get account data. There is a function to update outdated cookies.

## For reference
The fact is that cookies last about 1-2 hours. Therefore, a function was written to detect invalid cookies and update them. To implement re-authorization, a code was written that saves your login and password. It is not transferred to third parties.
I don't understand OOP well, so there is a lot of hard code in the library, if you want, you can correct my hard code. In the future I will do this myself as I learn OOP.

Implemented functions: authorization, viewing profile information, viewing the amount of disk space.

Soon:
Uploading files.

To use the get_info_profile function you must pass the required user_api argument. This is your personal api for your account of this type: https://disk.gozle.com.tm/api/v1/users/1234/. You must find out this address yourself in the developer console by analyzing all network requests.

![image](https://github.com/seratclemency/gozle-disk-api/assets/102463399/28753284-bad0-4e1e-9bee-f892be1a5b82)

Log in to your account, press f12, go to the Network tab and reload the page. Find the API shown in the screenshot (4 digits at the end will be different)

## Installation
Install from pip using this command: ```pip install gozle-disk-api```

Import: ```from gozle_disk_api import gozle_disk```

To authorize, you must activate this code. It is executed once, after which you will have 2 files created, these are cookies.txt and data.txt. You don't need to touch these files.

```python
gozle_disk.auth('email', 'password')
```
