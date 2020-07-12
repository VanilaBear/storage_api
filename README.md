# Simple storage api
  
## Methods:
* [GET] /store/list - show existing hashcodes
```
curl -i -X GET localhost:5000/store/list
```
* [POST] /store/upload - upload file
```
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/.../text.txt" localhost:5000/store/upload
```
* [GET] /store/download - download file by hashcode
```
wget --content-disposition localhost:5000/store/download?hashcode=7d59263317f0fabee60b688f47d88b28507cc4e9 -O filename
```
* [POST] /store/delete - delete file by hashcode
```
curl -i -X POST -F "hashcode=7d59263317f0fabee60b688f47d88b28507cc4e9" localhost:5000/store/delete
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
