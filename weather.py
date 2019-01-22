# -*- coding: utf-8 -*-
"""

@author: Administrator
"""
import requests
from urllib.parse import urlencode


def getHTML(url):
    try:
        headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.json()
    except:
        print('coonnection error')

def parse_json(jsons):
    today_weather=jsons['result']['today']
    today={}
    today['城市']=today_weather['city']
    today['日期']=today_weather['date_y']
    today['温度']=today_weather['temperature']
    today['天气']=today_weather['weather']
    today['穿衣指数']=today_weather['dressing_index']
    today['穿衣建议']=today_weather['dressing_advice']
    return today

def print_weather(weather):
    for keys in weather:
        print(keys+':'+weather[keys],'\n')
        
def main():
    base_url='http://v.juhe.cn/weather/index?'
    params={
            'cityname':'北京',
            'key':'你从聚合数据网站获取的key'}
    url=base_url+urlencode(params)
    json=getHTML(url)
    weather=parse_json(json)
    print_weather(weather)
    
    
if __name__=='__main__':
    main()
    
