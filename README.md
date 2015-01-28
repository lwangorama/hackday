# hackday
Test project to use tornado web and elastic search client api.

## Foundation UI Framework
The sample code is rely on foundation v5.

## Tornado Web
The server will be started when launching the program. It uses port 8888 for incoming web requests.

## Elastic search backend
In order to search for specific product index, you can use following command to import json content into local elastic search index.

Import command:

```
curl --ipv4 -XPOST 'localhost:9200/product/book/_bulk?pretty' --data-binary @product-es.json 
```

