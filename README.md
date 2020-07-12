# Simple storage api
  
### Methods:
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
curl -i -X POST localhost:5000/store/download?6813dcfaae3ebdfc1911b924bf52c80f3bd089ea
```
* [POST] /store/delete - delete file by hashcode
```
curl -i -X POST localhost:5000/store/download?6813dcfaae3ebdfc1911b924bf52c80f3bd089ea
```

### Simple ui
* [GET] localhost:5000
