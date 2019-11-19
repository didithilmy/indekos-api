## HTTP WEB SERVER - APPLICATION PROGRAMMING INTERFACE
## API CRAWLER DAN PROVIDER DATA INFORMASI PENYEDIA KOST
## FADEL NARARIA RAHMAN - 18217005
## COPYRIGHT(C) 2019



#import untuk keperluan Crawling Data response
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
import random
import string


#import untuk keperluan HTTP Server
import http.server
from http.server import HTTPServer,SimpleHTTPRequestHandler
import base64
import cgi
import json

#import untuk parsing url path
from urllib.parse import urlparse

#define generator ID
def randomID(stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

#define untuk class Crawler Data dari website infokost.id
class crawlFirst(scrapy.Spider):
    name = "info"

    def start_requests(self):
        list_web = [
           "https://www.infokost.id/search?type=kost&view=box&price_type=monthly&checkin=18+Oct+2019&q=&offset=0&page=1",
            "https://www.infokost.id/search?type=kost&view=box&price_type=monthly&checkin=18+Oct+2019&q=&offset=12&page=2",
            "https://www.infokost.id/search?type=kost&view=box&price_type=monthly&checkin=18+Oct+2019&q=&offset=24&page=3",
            "https://www.infokost.id/search?type=kost&view=box&price_type=monthly&checkin=18+Oct+2019&q=&offset=36&page=4",
            "https://www.infokost.id/search?type=kost&view=box&price_type=monthly&checkin=18+Oct+2019&q=&offset=48&page=5"
            ]
        for j in range(len(list_web)):
            url = list_web[j]
            yield scrapy.Request(url=url, meta={'cookiejar':j},callback=self.parse)    

        #url = "https://www.infokost.id/search?type=kost&price_type=monthly"
        #yield scrapy.Request(url=url, callback=self.parse)
    
    custom_settings={ 'FEED_URI': "output_http_server.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, response):
        for row in response.css("div.bg-white"):
            yield {
                "id"        : randomID(8),
                "nama"      : row.css("div.property-content div.property-title a.no-change h1::text").get(),
                "alamat"    : row.css("div.property-content div.property-address::text").get(),
                "fasilitas" : row.css('div.property-content div.property-facility span::attr(title)').extract(),
                "harga"     : row.css("div.property-content div.property-price a.no-change-grey h3::text").get(),
                "gambar"    : row.css('div.property-img a img::attr(data-src)').get()
            }

#Fungsi spider_results akan melakukan proses crawling dengan class Crawler yang telah dibuat dan menyimpan output dalam satu variabel
def spider_results():
    results = []

    def crawler_results(signal,sender,item,response,spider):
        results.append(item)
    
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(crawlFirst)
    process.start()

    return results


dataInfo = spider_results()

with open("output_http_server.json","r") as cust_response:
    data = json.load(cust_response)


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin','*')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_GET(self):
        parsed_query = urlparse(self.path)
        path = parsed_query.path
        query = parsed_query.query
        if path == '/info' :
            if query == '' :
                #penangan request tanpa query
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            else :
                #penanganan request dengan query ID
                param = query.split('=')[0]
                if param == 'id':
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    id = query.split('=')[1]
                    data_custom = next(item for item in data if item["id"] == id)
                    self.wfile.write(json.dumps(data_custom).encode())
                else :
                    self.send_response(404)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()                
        else :
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()        

    def do_DELETE(self):
        parsed_query = urlparse(self.path)
        path = parsed_query.path
        query = parsed_query.query
        if path == '/info' :
            if query == '' :
                #penangan request tanpa query
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
            else :
                #penanganan request dengan query ID
                param = query.split('=')[0]
                status = False
                if param == 'id':
                    id = query.split('=')[1]
                    for i in range(len(data)):
                        if data[i]['id']==id:
                            del data[i]
                            status = True
                            break
                    if status == True :
                        self.send_response(200)
                        self.send_header("Content-type","text/html")
                        self.end_headers()
                        with open("output_http_server.json","w") as current_data:
                            json.dump(data,current_data)
                    else :
                        self.send_response(204)
                        self.send_header("Content-type","text/html")
                        self.end_headers()    
                else :
                    self.send_response(404)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()                
        else :
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers() 

    def do_POST(self):
        parsed_query = urlparse(self.path)
        path = parsed_query.path
        if path == '/info' :
            length = int(self.headers.get("Content-length",0))
            raw_post_body = self.rfile.read(length)
            str_post_body = raw_post_body.decode("utf-8")
            post_body = json.loads(str_post_body)
            data.append(post_body)
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            with open("output_http_server.json","w") as current_data:
                json.dump(data,current_data)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()  

    def do_PUT(self):
        parsed_query = urlparse(self.path)
        path = parsed_query.path
        query = parsed_query.query
        if path == '/info' :
            if query == '' :
                #penangan request tanpa query
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
            else :
                #penanganan request dengan query ID
                param = query.split('=')[0]
                status = False
                if param == 'id':
                    #membaca body dari PUT request
                    length = int(self.headers.get("Content-length",0))
                    raw_put_body = self.rfile.read(length)
                    str_put_body = raw_put_body.decode("utf-8")
                    put_body = json.loads(str_put_body)

                    #proses pencarian ID dan menimpa data dictionary pada Index ID hasil query
                    id = query.split('=')[1]
                    for i in range(len(data)):
                        if data[i]['id']==id:
                            data[i] = put_body
                            status = True
                            break
                    if status == True :
                        self.send_response(200)
                        self.send_header("Content-type","text/html")
                        self.end_headers()
                        with open("output_http_server.json","w") as current_data:
                            json.dump(data,current_data)
                    else :
                        self.send_response(204)
                        self.send_header("Content-type","text/html")
                        self.end_headers()    
                else :
                    self.send_response(404)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()                
        else :
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()  

port = 4040
with HTTPServer(("",port), RequestHandler) as httpd:
    print("serving at port ",port)
    httpd.serve_forever()