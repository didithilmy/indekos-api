# HTTP-RESTful-API-Without-Framework
HTTP Server yang melayani API dengan arsitektur REST berbasis bahasa pemrograman Python 3. API ini melayani penyediaan dan pengelolaan data informasi kost-kostan yang tersedia.  

Untuk penggunaan methods pada API ini dengan menggunakan ketentuan seperti berikut:

usage of LIST   :  
```$curl -X GET http://localhost:4040/info```  
  
usage of GET    :  
```$curl -X GET http://localhost:4040/info?id=<ID>```  
  
usage of UPDATE :  
```$curl -X PUT -H "Content-Type: application/json" -d '{"id":<ID:integer>,"nama":<Nama:string>,"alamat":<Alamat:string>,"harga":<Harga:string>}' http://localhost:4040/info?id=<ID>```  
  
usage of CREATE :  
```$curl -H "Content-Type: application/json" -X POST -d '{"id":<ID:integer>,"nama":<Nama:string>,"alamat":<Alamat:string>,"harga":<Harga:string>}' http://localhost:4040/info?id=<ID>```  
  
usage of DELETE :  
```$curl -X DELETE http://localhost:4040/info?id=<ID>```  


### Sebagai contoh penggunaan command tersebut pada terminal sebagai berikut:
note : karakter '$' hanya sebagai simbol representatif pada terminal berbasis UNIX  
```
$curl -X GET http://localhost:4040/info  
  
$curl -X GET http://localhost:4040/info?id=5  
  
$curl -X PUT -H "Content-Type: application/json" -d '{"id":1,"nama":"Kost Mantep","alamat":"Jakarta","harga":"IDR 500.000"}' http://localhost:4040/info?id=1  
  
$curl -H "Content-Type: application/json" -X POST -d '{"id":62,"nama":"Kost Lengkap","alamat":"Tebet","harga":"IDR 250.000"}' http://localhost:4040/info?id=62  
  
$curl -X DELETE http://localhost:4040/info?id=1  
```
