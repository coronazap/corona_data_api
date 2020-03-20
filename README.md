# Coronazap API 

API para consulta dos dados a respeito do COVID-19 em 185 países que alimenta o WhatsAppBot [Coronazap](http://coronazap.guru/). 

## Fonte de Dados 

Os dados são extraídos três vezes por dia do site (WorldOMeter)[https://www.worldometers.info/coronavirus/].

## Request & Response Examples 

### GET /api 

[http://cororazap-api.azurewebsites.net/api](http://cororazap-api.azurewebsites.net/api)


```
{
   "_source":{
      "last_updated":"March 20, 2020, 19:37 GMT",
      "link":"https://www.worldometers.info/coronavirus/",
      "name":"WorldOMeter"
   },
   "data":{
      "AFEGANISTAO":{
         "active_cases":23,
         "name":"afeganistao",
         "new_cases":2,
         "new_deaths":0,
         "serious_critical":0,
         "total_cases":24,
         "total_cases_per_million":0,
         "total_deaths":0,
         "total_recovered":1
      },
      "AFRICA DO SUL":{
         "active_cases":202,
         "name":"africa do sul",
         "new_cases":52,
         "new_deaths":0,
         "serious_critical":0,
         "total_cases":202,
         "total_cases_per_million":3,
         "total_deaths":0,
         "total_recovered":0
      },
      (...)
      "ZAMBIA":{
         "active_cases":2,
         "name":"zambia",
         "new_cases":0,
         "new_deaths":0,
         "serious_critical":0,
         "total_cases":2,
         "total_cases_per_million":0,
         "total_deaths":0,
         "total_recovered":0
      }
   }
}
``` 

## GET /api/{país} 

[http://cororazap-api.azurewebsites.net/api/mundo](http://cororazap-api.azurewebsites.net/api/mundo)


``` 
{
   "_source":{
      "last_updated":"March 20, 2020, 19:37 GMT",
      "link":"https://www.worldometers.info/coronavirus/",
      "name":"WorldOMeter"
   },
   "data":{
      "MUNDO":{
         "active_cases":168294,
         "name":"mundo",
         "new_cases":25279,
         "new_deaths":1248,
         "serious_critical":7798,
         "total_cases":270173,
         "total_cases_per_million":34,
         "total_deaths":11276,
         "total_recovered":90603
      },
   }
```

## Comunidade 

Quer colaborar? [Coronazap on GitHub](https://github.com/coronazap)

Uma iniciativa OpenSource [Nindoo](http://nindoo.ai/)