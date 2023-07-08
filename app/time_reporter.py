# -*- coding: utf-8 -*-
from datetime import datetime
import pytz
from pyowm import OWM
from pyowm.utils.config import get_default_config
from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword_2 = ['氣溫', '溫度', '濕度', '天氣']
        self._keyword = ['報時', '幾點'] + self._keyword_2
        self._repr = '報時'
        self.time_zones = [
            # ('US/Pacific', '加州:　 ', 'Palo Alto,us'),
            ('Canada/Pacific', '溫哥華: ', 'Vancouver,ca'),
            ('America/Chicago', '香檳:　 ', 'Champaign,us'),
            ('Europe/Amsterdam', '荷蘭:　 ', 'Amsterdam,nl'),
            ('Asia/Taipei', '台北:　 ', 'Taipei,tw'),
            ('Asia/Tokyo', '東京:　 ', 'Tokyo,jp'),
            ('Australia/Melbourne', '墨爾本: ', 'Melbourne,au'),
        ]
        self.weather_zones = [
            ('桃園:', 'Taoyuan,tw'),
            ('新竹:', 'Hsinchu,tw'),
            ('台中:', 'Taichung,tw'),
            ('宜蘭:', 'Yilan,tw'),
        ]
        self.fmt = '%H:%M %m/%d'
        with open('weather') as f:
            API_key = f.readline()
        config_dict = get_default_config()
        config_dict['language'] = 'zh_TW'
        self.owm = OWM(API_key, config_dict)
    
    def check(self, msg, **kwargs):
        if msg in self._keyword_2:
            return [True, True]
        return msg in self._keyword
        
    def run(self, msg, **kwargs):
        system_time = pytz.timezone('GMT').localize(datetime.now())
        message = ''
        for key, value, place in self.time_zones:
            local_time = system_time.astimezone(pytz.timezone(key))
            weather = ''
            obs = self.owm.weather_at_place(place)
            w = obs.get_weather()
            weather = '  {:04.1f}C {:3.0f}% {}'.format(
                w.get_temperature(unit='celsius')['temp'],
                w.get_humidity(),
                w.get_detailed_status().replace('，', ',')
            )
            message += (value + local_time.strftime(self.fmt) + weather + '\n')
        if msg in self._keyword_2:
            s = []
            for value, place in self.weather_zones:
                obs = self.owm.weather_at_place(place)
                w = obs.get_weather()
                s  += ['{}  {:04.1f}C {:3.0f}%  {}'.format(
                    value,
                    w.get_temperature(unit='celsius')['temp'],
                    w.get_humidity(),
                    w.get_detailed_status().replace('，', ',')
                )]
            return [message[:-1], '\n'.join(s)]
        else:
            return message[:-1]
