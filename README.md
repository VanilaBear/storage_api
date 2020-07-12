# Simple storage api
  
### Methods:
* [GET] /store/list - show existing files
```
curl -i -X GET localhost:5000/store/list
```
* [GET] /store/upload - show existing files
```
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/.../text.txt" localhost:5000/store/upload
```
* [POST] /store/download - show existing files
```
curl -i -X POST localhost:5000/store/download?6813dcfaae3ebdfc1911b924bf52c80f3bd089ea
```
* [POST] /store/delete - show existing files
```
curl -i -X POST localhost:5000/store/download?6813dcfaae3ebdfc1911b924bf52c80f3bd089ea
```

