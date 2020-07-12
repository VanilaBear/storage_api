# Simple storage api
  
## Methods:
* [GET] /store/list - show existing hashcodes
```
curl -i -X GET localhost:5000/store/list
```
* [GET] /store/upload - upload file
```
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/.../text.txt" localhost:5000/store/upload
```
* [POST] /store/download - download file by hashcode
```
curl -i -X POST localhost:5000/store/download?hashcode=6813dcfaae3ebdfc1911b924bf52c80f3bd089ea
```
* [POST] /store/delete - delete file by hashcode
```
curl -i -X POST -F "hashcode=d588b803980b40255bcc9711c3a53a33e9e0d1ca" localhost:5000/store/delete
```

## Simple ui
All methods can be used from ui 
* [GET] localhost:5000

## Docker

Build: 
```
docker build -t storage_api .
```

Run:
```
docker run -it -p 5000:5000 --network host storage_api
```