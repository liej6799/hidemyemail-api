### HideMyEmail API
very small iCloud's HME API wrapper

special thanks to made [pyIcloud](https://github.com/picklepete/pyicloud) and [hidemyemail-generator](https://github.com/rtunazzz/hidemyemail-generator)

#### Why?
This is due to iCloud's HME need to pass cookie, and caused extenal app like bitwarden client cant call the said api. 

Maybe related to CORS issue, where cookie cant be passed to the headers, If anyone able to pass the cookie to the request, then we just need to convert [pyIcloud](https://github.com/picklepete/pyicloud) python wrapper to node, and call directly without external webservice running.


#### How it works?
bitwarden generated email -> call this api to generate email -> call [pyIcloud](https://github.com/picklepete/pyicloud) library to access the iCloud server to generate the email.

#### Installation

```bash
git clone https://github.com/liej6799/hidemyemail-api
cd hidemyemail-api
pip3 install -r requirements.txt
```

#### Usage
1. Perform login to your iCloud's account, only need to do one time, and it will save the details on the temp folder
```bash
python3 login.py
```

2. Once success login, you may run the api server by
```bash
uvicorn main:app
```
3. Access the api from browser
http://localhost:8000/generate?username=test@icloud.com


#### Limitation
1. This is not a permanent solution as the token might expired, and you might need to login again.

2. This is not an ideal solution as we need to run seperate server, see the Why? above

#### Implementation
1. bitwarden's generate email

Currently bitwarden support to generate emails for
- SimpleLogin
- AnonAddy
- FirefoxRelay

For these services, you are able to generate token from their website and access their api directly with bearer token, no cookie required.