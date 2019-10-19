# HTTP-RESTful-API-Without-Framework
HTTP Server yang melayani API dengan arsitektur REST berbasis bahasa pemrograman Python 3. API ini melayani penyediaan dan pengelolaan data informasi kost-kostan yang tersedia.  
  
Data informasi kost-kostan yang terdapat pada API ini diperoleh dengan melakukan crawling data pada website penyedia jasa informasi pesan kost online yaitu infokost.id. Proses crawling data menggunakan library Scrapy pada Python 3 dan akan selalu dijalankan ketika program HTTP server dimulai, hasil crawling ini disimpan dalam satu file output_http_server.json.(Pada repository ini file output_http_server.json merupakan contoh hasil file yang diproses melalui crawling tersebut)

File http_server_final.py pada repository ini akan melakukan hosting server yang melayani API dengan methods seperti berikut:

LIST      : Menggunakan methods GET untuk mendapat seluruh value pada file output_http_server.json  
GET       : Menggunakan methods GET untuk mendapat satu record value spesifik berdasar ID pada file output_http_server.json  
UPDATE    : Menggunakan methods PUT untuk update value pada satu record data spesifik berdasar ID pada file output_http_server.json  
CREATE    : Menggunakan methods POST untuk membuat satu record value baru dengan ID tertentu pada file output_http_server.json  
DELETE    : Menggunakan methods DELETE untuk menghapus satu record value spesifik berdasar ID pada file output_http_server.json

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
