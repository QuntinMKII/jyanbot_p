# -*- coding: utf-8 -*-
from math import *
import pandas
import time
from random import random as rnd

from app.base_app import base_app

def _round(x, n=0):
    if type(x) ==  complex:
        return round(x.real, n) + round(x.imag, n) * 1j
    else:
        return round(x, n)

class temperature():
    def __init__(self, deg, unit='C'):
        self.unit = unit
        self.deg = deg
    
    def __str__(self):
        if self.unit == 'C':
            return '{}F'.format(round(self.deg *1.8 + 32, 1))
        if self.unit == 'F':
            return '{}C'.format(round((self.deg - 32) / 1.8, 1))
    
    def __truediv__(self, b):
        return temperature(output_deg, output_unit)
    
    def __rmul__(self, a):
        return temperature(self.deg * a, self.unit)
    
class app(base_app):
    def __init__(self):
        self._keyword = ['{數學式}=', '{output_format};{數學式}=', '{匯率換算 AUD/CNY/EUR/GBP/JPY/NTD/RMB/TWD/USD}=', '{長度, 重量. 溫度 換算 mi/km/ft/inch/cm. lb/kg, C/F}=', '{random number rnd}=']
        self._repr = 'calculate'
        self._ok_function = ['abs', 'all', 'any', 'bin', 'bool', 'complex', 'dict', 'divmod', 'enumerate', 'float', 'format', 'filter', 'hex', 'int', 'len', 'list', 'map', 'max', 'min', 'oct', 'ord', 'pow', 'range', 'reversed', 'round', 'set', 'sorted', 'str', 'sum', 'tuple', 'zip']
        self._ban_function = ['ascii', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile',  'delattr', 'dir', 'eval', 'exec', 'frozenset', 'getattr', 'globals', 'hasattr', 'has', 'help', 'id', 'import ', 'input', 'isinstance', 'issubclass', 'iter', 'locals', 'memoryview', 'next', 'object', 'open', 'print', 'property', 'repr', 'setattr', 'slice', 'staticmethod', 'super', 'type', 'vars']
        self._ok_constants = ['False', 'True', 'None']
        self._ban_constants = ['NotImplemented', 'Ellipsis', '__debug__', 'quit', 'exit', 'copyright', 'credits', 'license']
        self._ban_word = ['raise', 'try', 'except', 'import', 'from', 'break', 'continue', 'return', 'pass', 'def', 'class', 'while', 'del', 'with', 'as', 'self']
        self.currency_time = 0
        self._ans = ''
    
    def check(self, msg, **kwargs):
        if time.time() - self.currency_time > 86400:
            currency = pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
            currency = currency[0].ix[:,:5]
            currency.columns = ['name','現金買入','現金賣出','即期買入','即期賣出']
            currency['name'] = currency['name'].str.extract('\((\w+)\)')
            currency[['現金買入' ,'現金賣出' ,'即期買入' ,'即期賣出']] = currency[['現金買入' ,'現金賣出' ,'即期買入' ,'即期賣出']].apply(pandas.to_numeric, errors='coerce')
            self.currency = currency
            self.currency_time = time.time()
        else:
            currency = self.currency
            
        while msg[-1] == ' ':
            msg = msg[:-1]
        if msg[-1:] == '=':
            for _ban in self._ban_function + self._ban_constants + self._ban_word + ['msg', 'kwargs', 'app', 'base_app', 'time', 'pandas', 'currency', 'temperature']:
                if _ban in msg:
                    return False
            try:
                output = ''
                replace_list = [['ans', self._ans]] + [['round', '_round']] + [[_+'i', _+'j'] for _ in '1234567890'] + [[_+_2, _+'*'+_2] for _ in '1234567890' for _2 in ['AUD', 'CNY', 'EUR', 'GBP', 'JPY', 'NTD', 'RMB', 'TWD', 'USD', 'mi', 'km', 'ft', 'inch', 'cm', 'm', 'lb', 'kg', 'C', 'F', 'c', 'f', 'rnd', 'ans']] + [['rnd', 'rnd()']] + [[_+'x', _+'*'] for _ in '1234567890.)j ']
                for s1, s2 in replace_list:
                    msg = msg.replace(s1, s2)
                msg = msg.split(';')
                
                i = 1j
                
                AUD = float(currency[currency['name']=='AUD'][['即期買入','即期賣出']].mean(1))
                CNY = float(currency[currency['name']=='CNY'][['即期買入','即期賣出']].mean(1))
                EUR = float(currency[currency['name']=='EUR'][['即期買入','即期賣出']].mean(1))
                GBP = float(currency[currency['name']=='GBP'][['即期買入','即期賣出']].mean(1))
                JPY = float(currency[currency['name']=='JPY'][['即期買入','即期賣出']].mean(1))
                NTD = 1
                RMB = CNY
                TWD = NTD
                USD = float(currency[currency['name']=='USD'][['即期買入','即期賣出']].mean(1))
                
                mi = 1610
                km = 1000
                ft = 0.3048
                inch = 0.0254
                cm = 0.01
                m = 1
                
                lb = 0.453592
                kg = 1
                
                C = temperature(1, 'C')
                c = temperature(1, 'C')
                F = temperature(1, 'F')
                f = temperature(1, 'F')
                
                if '=' not in msg[0]:
                    output = msg[0]
                    msg = msg[1:]
                for _msg in msg[:-1]:
                    exec(_msg)
                self._ans = (' {:' + output + '}').format(eval(msg[-1][:-1]))
                for s1, s2 in [[_+'j', _+'i'] for _ in '1234567890'] + [[' 0i', ' 0']]:
                    self._ans = self._ans.replace(s1, s2)
                return True
            except:
                return False
        else:
            return False
        
    def run(self, msg, **kwargs):
        return msg + self._ans
