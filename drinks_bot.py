import sys
from io import BytesIO

from time import sleep

import telegram

from flask import Flask, request, send_file

from telegram.error import TelegramError

from transitions import State
from transitions.extensions import GraphMachine

import urllib.request
from bs4 import BeautifulSoup as bs

import time

import os

API_TOKEN = '496932762:AAE3EDchNRRw8hir76yoBlPwnCvcN8DQA5o'
WEBHOOK_URL = 'https://dade98e9.ngrok.io/hook'
lastMessageId = 0
sign = ''


app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)

states = [
        'init',
        'daily_sign',
        'order',
        'finish_order',
        'phone_number',
        'drink_info',
        'store_loca',
        'input_loca',
        'input_drink_for_search'
        ]
transitions = [
        ['o','init','order'],
        ['d','init','drink_info'],
        ['s','init','store_loca'],
        ['fo','order','finish_order'],
        ['pn','finish_order','phone_number'],
        ['ds','init','daily_sign'],
        ['ds','daily_sign','daily_sign'],
        ['i_lo','store_loca','input_loca'],
        ['i_lo','input_loca','input_loca'],
        ['i_d_f_s','drink_info','input_drink_for_search'],
        ['i_d_f_s','input_drink_for_search','input_drink_for_search'],
        ['back',['order','drink_info','store_loca','input_loca','input_drink_for_search','daily_sign','phone_number'],'init']
        ]

class TocMachine(GraphMachine):
    def __init__(self,**machine_configs):
        self.machine = GraphMachine(
                model = self,
                **machine_configs
         )
class Game(object):
       
    def res0(self):
        bot.sendMessage(getUserId(Update),'您好!!我是 {} , 很高興為你服務 \n點餐請輸入o\n飲料查詢請輸入 d\n分店查詢請輸入 s\n查看今日星座運勢請輸入欲查詢星座'.format(bot.getMe().username))
    def res1(self):
        bot.sendMessage(getUserId(Update),'請輸入您的手機號碼')
    def res2(self):
        bot.sendMessage(getUserId(Update),'請輸入欲查詢飲料名稱\n(名稱依menu上為準)')
        bot.sendMessage(getUserId(Update),'輕紅茶\n陽光麥香紅/奶茶\n香禾錫蘭紅/奶茶\n竹山觀音紅/奶茶\n皇家伯爵紅/奶茶\n魚池阿薩姆紅/奶茶\n魚池有機紅玉紅茶\n花蓮瑞穗密香紅茶\n阿里山高山紅茶\n黑糖鮮奶\n黑石鮮奶\n扁實香檬紅茶\n火山奶茶\n藍莓紅茶\n')

    def res3(self):
        bot.sendMessage(getUserId(Update),'請輸入欲查詢縣市名稱\nex:台北,新北,台南...等')
    def res4(self):
        bot.sendMessage(getUserId(Update),"請輸入欲訂購飲料名稱及甜度冰塊")
        print(text)
        

    def res5(self):
        if(text == '台北'):
            bot.sendMessage(getUserId(Update),'台北四維店:\n台北市大安區四維路170巷18號\n02-2708-7034')
        elif(text == '新北'):
            bot.sendMessage(getUserId(Update),'新北板橋店:\n新北市板橋區莒光路7號\n02-2250-2525')
        elif(text == '新竹'):
            bot.sendMessage(getUserId(Update),'新竹光復店:\n新竹市光復路一段366號\n03-668-6780')
        elif(text == '台中'):
            bot.sendMessage(getUserId(Update),'台中逢甲店:\n台中市西屯區逢甲路19巷3號\n04-2452-6958\n\n台中勤美店:\n台中市西區美村路一段145號\n04-2327-2816\n\n台中一中店:\n台中市北區三民路三段136號\n04-2229-5515\n\n台中豐原店:\n台中市豐原區三民路109號\n04-2520-3300\n\n台中大里店:\n台中市大里區中興路二段175號\n04-2483-6519')
        elif(text == '嘉義'):
            bot.sendMessage(getUserId(Update),'嘉義新生店:\n嘉義市東區新生路816號\n05-275-1181\n\n新光三越垂楊店:\n嘉義新光三越垂楊店B1\n05-222-2268')
        elif(text == '台南'):
            bot.sendMessage(getUserId(Update),'台南長榮店:\n台南市東區長榮路三段13號\n06-236-2029\n\n台南安平店:\n台南市安平區華平路709號\n06-250-3816\n\n台南中華店:\n台南市永康區中華路311號\n06-312-1777\n\n台南公園店:\n台南市北區公園路587號\n06-251-6816\n\n台南崇德店:\n台南市東區崇德路654號\n06-260-6066\n\n台南忠義店:\n台南市中西區忠義路二段244號\n06-220-9889\n\n台南善化店:\n台南市善化區中正路509號\n06-581-5999\n\n新光三越中山店:\n台南新光三越中山店B2\n06-222-2716')
        elif(text == '高雄'):
            bot.sendMessage(getUserId(Update),'高雄十全店:\n高雄市三民區十全一路359號\n07-313-3359\n\n高雄鼎中店:\n高雄市三民區鼎中路678號\n07-310-8080\n\n高雄岡山店:\n高雄市岡山區岡山路354號\n07-621-9360')
        elif(text == '返回'):
            print('back to the init state')
        else:
            bot.sendMessage(getUserId(Update),'不好意思,該地區沒有我們的分店喔QQ')
    def res6(self):
        if(text == '輕紅茶'):
            bot.sendMessage(getUserId(Update),'輕盈悠揚的斯里蘭卡產區精選紅茶，淡雅的清香適合入門的簡單幸福。\n NT$ 45')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/a/wTLHz')
        elif(text == '陽光麥香紅/奶茶'):
            bot.sendMessage(getUserId(Update),'經典印度阿蕯姆紅茶與澳洲大麥的完美協奏，沉穩的茶韻伴隨田野的大麥香氣，甘潤圓滑，香醇厚實的紅茶韻，調製成麥香奶茶，香氣更是豐富多元。\n NT$ 35/45')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/YZ9qxbp')
        elif(text == '香禾錫蘭紅/奶茶'):
            bot.sendMessage(getUserId(Update),'馬達加斯加頂級天然香草莢、黃金蕎麥、斯里蘭卡紅茶的完美協奏曲。\n NT$ 40/50')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/aMqnuu3')
        elif(text == '竹山觀音紅/奶茶'):
            bot.sendMessage(getUserId(Update),'獨家首創結合台灣鐵觀音與印度阿蕯姆，時而烏龍、時而紅茶的黃金組合。\n NT$ 45/55')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/sNZDtbl')
        elif(text == '皇家伯爵紅/奶茶'):
            bot.sendMessage(getUserId(Update),'格雷伯爵打翻佛手柑油，卻送給全世界紅茶迷的一份意外驚喜\n NT$ 65/65')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/x2laTb9')
        elif(text == '魚池阿蕯姆紅/奶茶'):
            bot.sendMessage(getUserId(Update),'無毒農法栽種出帶福爾摩沙水果乾香氣的台茶八號，如台灣人情味般紮實而渾厚的喉韻。\n NT$ 80/70')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/z0oznkB')
        elif(text == '魚池有機紅玉紅茶'):
            bot.sendMessage(getUserId(Update),'「台灣香」的代表，MOA有機認證，淡淡薄荷與肉桂香氣餘韻的三日繞梁。\n NT$ 80')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/jrDXiSE')
        elif(text == '花蓮瑞穗蜜香紅茶'):
            bot.sendMessage(getUserId(Update),'茶葉栽種過程中受小綠葉蟬叮咬，意外產出聞名世界的紅茶。經小綠葉蟬吸吮著涎後，產生天然淡雅花果及蜂蜜香氣，十分迷人。\n NT$ 75')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/VoZzFki')
        elif(text == '阿里山高山紅茶'):
            bot.sendMessage(getUserId(Update),'住在海拔1100公尺以上的小葉金萱，想品嚐它的清新與山氣芬芳只能限時限量。\n NT$ 80')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/BR579Na')
        elif(text == '黑糖鮮奶'):
            bot.sendMessage(getUserId(Update),'溫潤的傳統黑糖加鮮乳，無咖啡因老少咸宜的選擇。\n NT$ 45')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/iCRlIsx')
        elif(text == '黑石鮮奶'):
            bot.sendMessage(getUserId(Update),'手工製糖產量稀少，龍眼木柴燒香氣豐富多元，含多種微量元素，古法文化的新生\n NT$ 60')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/fkjaBFY')
        elif(text == '扁實香檬紅茶'):
            bot.sendMessage(getUserId(Update),'台灣原生種扁實檸檬，流傳至日本長壽村的秘果，帶來沁涼豐富柑橘香氣及三倍維生素C\n NT$ 60')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/Wuip3iF')
        elif(text == '火山奶茶'):
            bot.sendMessage(getUserId(Update),'老薑、桂圓、紅棗在口腔中爆發出口感的漸層，是寒冬中屬於奶茶的小幸運\n NT$ 65')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/oZi7Tm9')
        elif(text == '藍莓紅茶'):
            bot.sendMessage(getUserId(Update),'莓果類特有的酸甜香氣，跟紅茶樸實的韻味，共譜的樂章，在炎夏時期特別凸顯出多元的清新感。\n NT$ 60')
            bot.sendPhoto(getUserId(Update),'https://imgur.com/bCuWtHJ')
        elif(text == '返回'):
            print('back to init state')
        else:
            bot.sendMessage(getUserId(Update),'不好意思,我們沒有販賣該品項ㄛQQ')
    def res7(self):
        URL = 'http://daily-zodiac.herokuapp.com/mobile/zodiac/' + sign
        print(URL)
        response = urllib.request.urlopen(URL)
        html_cont = response.read()
        soup = bs(html_cont,'html.parser',from_encoding = 'utf-8')
        tp1 = soup.find('p')
        tp2 = soup.find('article')
        bot.sendMessage(getUserId(Update),tp1.text + '\n' + tp2.text[11:len(tp2.text)])
    def res8(self):
        bot.sendMessage(getUserId(Update),'成功！！訂單已送出。')
        


drinks_bot = Game()
machine = GraphMachine(model = drinks_bot , states = states , transitions = transitions , initial = 'init' , ignore_invalid_triggers = True)

graph_machine = TocMachine(states = states , transitions = transitions , initial = 'init', auto_transitions = False , show_conditions = True)

machine.on_enter_init('res0')
machine.on_enter_order('res4')
machine.on_enter_finish_order('res1')
machine.on_enter_phone_number('res8')
machine.on_enter_drink_info('res2')
machine.on_enter_store_loca('res3')
machine.on_enter_input_loca('res5')
machine.on_enter_input_drink_for_search('res6')
machine.on_enter_daily_sign('res7')



def getText(Update):
    return Update["message"]["text"]
def getMessageId(Update):
    return Update["update_id"]
def getchatId(Update):
    return Update["message"]["chat"]["id"]
def getUserId(Update):
    return Update["message"]["from_user"]["id"]
def messageHandler(Update):
    global lastMessageId
    global text
    text = getText(Update)
    msg_id = getMessageId(Update)
    user_id = getUserId(Update)
    lastMessageId = msg_id
    print(text)
    global sign
    if text == 'o' and drinks_bot.state == 'init':
        drinks_bot.o()
    elif text == 'd' and drinks_bot.state == 'init':
        drinks_bot.d()
    elif text == 's' and drinks_bot.state == 'init':
        drinks_bot.s()
    elif text == '牡羊座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Aries'
        drinks_bot.ds()
    elif text == '金牛座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Taurus'
        drinks_bot.ds()
    elif text == '雙子座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Gemini'
        drinks_bot.ds()
    elif text == '巨蟹座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Cancer'
        drinks_bot.ds()
    elif text == '獅子座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Leo'
        drinks_bot.ds()
    elif text == '處女座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Virgo'
        drinks_bot.ds()
    elif text == '天秤座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Libra'
        drinks_bot.ds()
    elif text == '天蠍座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Scorpio'
        drinks_bot.ds()
    elif text == '射手座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Sagittarius'
        drinks_bot.ds()
    elif text == '摩羯座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Capricorn'
        drinks_bot.ds()
    elif text == '水瓶座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Aquarius'
        drinks_bot.ds()
    elif text == '雙魚座' and (drinks_bot.state == 'init' or drinks_bot.state == 'daily_sign'):
        sign = 'Pisces'
        drinks_bot.ds()
    elif text != '' and drinks_bot.state == 'order':
        fo = open('list.txt','a')
        fo.write(time.strftime('%Y/%m/%d  %H:%M:%S') + '\n')
        fo.write(text + '\n')
        fo.close()
        drinks_bot.fo()
    elif text != '' and drinks_bot.state == 'finish_order':
        if len(text) == 10:
            fo = open('list.txt','a')
            fo.write(text + '\n\n\n')
            fo.close()
            drinks_bot.pn()
            os.system("notify-send -t 0 有新訂單來啦!!!")
            drinks_bot.back()
        else:
            bot.sendMessage(getUserId(Update),'請重新輸入正確的手機號碼喔^^')
    elif text != '' and text != '返回' and (drinks_bot.state == 'store_loca' or drinks_bot.state == 'input_loca'):
        drinks_bot.i_lo()
    elif text != '' and text != '返回' and (drinks_bot.state == 'drink_info' or drinks_bot.state == 'input_drink_for_search'):
        drinks_bot.i_d_f_s()
    elif text == '返回':
        drinks_bot.back()
    elif text != '' and drinks_bot.state == 'init':
        bot.sendMessage(user_id,'您好!!我是 {} , 很高興為你服務 \n點餐請輸入 o\n飲料查詢請輸入 d\n分店查詢請輸入 s\n查看今日星座運勢請輸入欲查詢星座'.format(bot.getMe().username))
    print(drinks_bot.state)
    
    return


def _send_msg():
    
    lastMessageId = 0
    Updates = bot.getUpdates()
    if(len(Updates)>0):
        lastMessageId = Updates[-1]["update_id"]
    
    while(1):
        Updates = bot.getUpdates(offset=lastMessageId)
        Updates = [Update for Update in Updates if Update["update_id"]>lastMessageId]
        global Update
        
        for Update in Updates:
            messageHandler(Update)
            
        Updates = bot.getUpdates()
        if(len(Updates)>0):
            lastMessageId = Updates[-1]["update_id"]
        tim = time.strftime('%H:%M:%S')
        if tim == '7:00:00':
                       
            URL = 'http://taqm.epa.gov.tw/taqm/tw/AqiForecast.aspx'
            response = urllib.request.urlopen(URL)
            html_cont = response.read()
            soup = bs(html_cont,'html.parser',from_encoding = 'utf-8')
            temp1 = soup.find('span',id = 'ctl09_labDay1')
            temp2 = soup.find_all('th',align = 'center')
            psi = '1'
            level = ''
            temp3 = soup.find('span',id = 'ctl09_labPsi1_' + psi + '_2')
            bot.sendMessage(getUserId(Update),temp1.text)
            bot.sendMessage(getUserId(Update),'地區      AQI指標     指標等級')
            
            for i in range(12,22):
                psi = str(i-11)
                param = str(i-11)
                temp3 = soup.find('span',id = 'ctl09_labPsi1_' + psi + '_2')
                
                if int(temp3.text) <= 50:
                    level = '良好'
                elif int(temp3.text) <=100 and int(temp3.text) >50:
                    level = '普通'
                elif int(temp3.text) <=150 and int(temp3.text) >100:
                    level = '對敏感族群不健康'
                elif int(temp3.text) <=200 and int(temp3.text) >150:
                    level = '對所有族群不健康'
                elif int(temp3.text) <=300 and int(temp3.text) >200:
                    level = '非常不健康'
                else:
                    level = '危害'
                if i == 15:
                    bot.sendMessage(getUserId(Update),'%-9s%-12s%-30s'%(temp2[i].text,temp3.text,level))
                    continue
                bot.sendMessage(getUserId(Update),'%-10s%-12s%-30s'%(temp2[i].text,temp3.text,level))
                
        
        sleep(0.5)

@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    graph_machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    graph_machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    
    app.run(port=5000)
    #_send_msg()
    
