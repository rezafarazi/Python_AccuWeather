#libs Start
import requests
import json


#Global Variables Start
api_key_accuweather="oLO3FkTqWQEWgtdh7pN6MD2TcxGPWYA7"
#Global Variables End


#Get Wather Start
def Get_Weather(City):
    Api_Value=Get_Api(City)
    Final_Values=Deserilize(Api_Value)
    return Final_Values
#Get Wather End



#Get Read Api From Server Start
def Get_Api(City):
    url="http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+api_key_accuweather+"&q="+City+"&details=true"    
    response=requests.get(url)
    return response.text
#Get Read Api From Server End



#Descrilaize Start
def Deserilize(json_value):
    json_array=json.loads(json_value)
    js="NUll"

    for i in json_array:
        js=i["Details"]
        break
    
    air=""

    for i in js["Sources"]:
        if(i["DataType"]=="AirQualityCurrentConditions"):
            air=i["Source"]
            break


    return air
#Descrilaize End
