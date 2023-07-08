# -*- coding: utf-8 -*-
from random import random

from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = ['*骰*{正整數}d{正整數}*']
        self._repr = '骰'
    
    def check(self, msg, **kwargs):
        return '骰' in msg
        
    def run(self, msg, **kwargs):
        return self.dicer_speak(msg)
        
    def dice_row(self, ndice_in, nface_in):
        ndice = int(ndice_in)
        nface = int(nface_in)
        if (ndice < 1) | (nface < 1):
            return ''
        concise = (ndice > 8) | (nface > 1000)
        
        dices = []
        for d in range(ndice):
            row = int(random() * float(nface)) + 1
            dices.append(row)
        
        dice_sum = sum(dices)
        dice_ave = float(sum(dices)) / float(ndice)
        dice_str = [str(dice) for dice in dices]
        if concise:
            dice_list = ''
        else:
            dice_list = ', '.join(dice_str)
            
        sentence = '{}d{}丟出{}'.format(
            ndice, nface, dice_list)
        if ndice > 1:
            sentence += '，共{}點，平均{:.2f}'.format(dice_sum, dice_ave)
        if (ndice == 42) & (nface == 42):
            sentence += "  don't panic!"
        return sentence

    def number(self, s):
        if s in '0123456789':
            return s
        else:
            return ''

    def find_dice_input(self, msg):
        ender = 0
        endmsg = len(msg)
        dices = []
        print('msg :: [{}]'.format(msg))
        for i in range(1,endmsg-1):
            if i < ender:
                continue
            if msg[i] in ['d', 'D']:
                print('  msg[{}]=[{}]'.format(i, msg[i]))
                cdice = []
                for c in range(i-1, ender-1, -1):
                    C = self.number(msg[c])
                    print('    msg[{}]=[{}]  ndice'.format(c, C))
                    if C:
                        cdice.append(C)
                    else:
                        break
                if not cdice:
                    continue
                cface = []
                for c in range(i+1, endmsg):
                    C = self.number(msg[c])
                    print('    msg[{}]=[{}]  nface'.format(c, C))
                    if C:
                        cface.append(C)
                    else:
                        break
                if not cface:
                    continue
                else:
                    ender = c
                cdice.reverse()
                ndice = int(''.join(cdice))
                nface = int(''.join(cface))
                print('    ndice=[{}]  nface=[{}]'.format(ndice, nface))
                dices.append((ndice, nface))
        return dices
                
    def dicer_speak(self, msg):
        rows = self.find_dice_input(msg)
        if not rows:
            #return '聽不懂，工三小'
            return ''
            
        sentences = []
        for row in rows:
            ndice, nface = row
            dice = self.dice_row(ndice, nface)
            if dice:
                sentences.append(dice)
        if not sentences:
            #return '聽不懂，工三小'
            return ''
            
        speech = '\n'.join(sentences)
        return speech

#if __name__ == '__main__':
#    msg = '骰個42d42'
#    reply = speak(msg)
#    print('[[[{}]]]'.format(reply))
                    