import http
import json
import re
from http import cookiejar
from fake_useragent import UserAgent
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener

class Find_Price(object):

    def __init__(self):
        self.shoes = {}
        self.shoes_num = {}
        self.goods_url = 'https://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.58c77370Oo6I7E&id=578101773230&_u=t2dmg8j26111'
        # 登录成功时，需要的Cookie
        self.newCookie = http.cookiejar.CookieJar()
        # 登陆成功时，需要的一个新的opener
        self.newOpener = build_opener(HTTPCookieProcessor(self.newCookie))
    #找到鞋以及尺码
    def Find_Shoes(self):
        response = self.newOpener.open(self.goods_url)
        page = response.read().decode('gb18030')
        #print(page)

        # 正则匹配鞋对应的编号
        pattern = re.compile('data-value="1627207:(.*?)"')    #data-value="1627207:26397110"
        match = pattern.findall(page)
        #print(match)
        #编号对应鞋名
        self.shoes[match[0]] = '白水泥'
        self.shoes[match[1]] = '白银'
        self.shoes[match[2]] = '绿脚趾'
        self.shoes[match[3]] = '南海岸'
        self.shoes[match[4]] = '熊猫'
        #正则表达式匹配鞋码编号
        pattern1 = re.compile('data-value="20549:(.*?)"')
        match = pattern1.findall(page)
        #编号对应鞋码
        self.shoes_num[match[0]]=  '36码'
        self.shoes_num[match[1]] =  '37码'
        self.shoes_num[match[2]] =   '37.5码'
        self.shoes_num[match[3]] =   '38码'
        self.shoes_num[match[4]] =   '38.5码'
        self.shoes_num[match[5]] =    '39码'
        self.shoes_num[match[6]] =    '40码'
        self.shoes_num[7] =      '41码'
        self.shoes_num[8] =      '42码'
        self.shoes_num[match[9]] =     '42.5码'
        self.shoes_num[match[10]] =   '43码'
        self.shoes_num[match[11]] =     '44码'
        self.shoes_num[match[12]] =     '45码'
        self.shoes_num[match[13]] =    '45.5码'
        self.Find_Price()
    def Find_Price(self):
        url = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=578101773230&sellerId=353717148&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'
        headers = {
            "User-Agent": UserAgent().chrome,
            "referer":"https://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.58c77370Oo6I7E&id=578101773230&_u=t2dmg8j26111",
            "callback": "onSibRequestSuccess",
            'Accept': '*/*',
            'accept-language':'zh-CN,zh;q=0.9',
            "cookie":"thw=cn; cna=FBuBFDZFegICAateEj/Eykl5; t=250fcdeaf7169bd3c7fa50709d1d26d2; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; ubn=p; enc=l5nyRg0tUZpnKEfYINDPTX8VmS6mx0u8WbDmQR3uQlS6HDyk15htKSpCfOZ%2B6jZE%2FKkWHpcQ8Gr3IOuMgCGslg%3D%3D; ucn=center; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=898008672127111122; _tb_token_=03yTUQh9femReRwX5Er5; cookie2=1a53f72da85ea4cfbceec245929145c8; v=0; unb=2791965954; sg=%E5%8E%9543; _l_g_=Ug%3D%3D; cookie1=B0T%2BRTWMZ0gMeF%2BAz3tS8ECZKkELlsb5o4%2F9oMRabkA%3D; tracknick=w%5Cu6765%5Cu54AF%5Cu7834%5Cu6D01%5Cu5395; lgc=w%5Cu6765%5Cu54AF%5Cu7834%5Cu6D01%5Cu5395; dnk=w%5Cu6765%5Cu54AF%5Cu7834%5Cu6D01%5Cu5395; _nk_=w%5Cu6765%5Cu54AF%5Cu7834%5Cu6D01%5Cu5395; cookie17=UU8BrR2CAVUC%2Fg%3D%3D; skt=8d1c1ae730167081; csg=6777f7d9; uc3=vt3=F8dByRzDqQI78VVERUU%3D&id2=UU8BrR2CAVUC%2Fg%3D%3D&nk2=FFk7ujNn6bV8pos%3D&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU0NTM4NTQ0NA%3D%3D; _cc_=UIHiLt3xSw%3D%3D; mt=ci=32_1&np=; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTYM8VpIT%2F3Lg%3D%3D&tag=8&lng=zh_CN; x5sec=7b2264657461696c736b69703b32223a22643637386439646431313564386130383937333336656536613733356138623143505370382b4146454c6d6c6a4d755376396e6964426f4d4d6a63354d546b324e546b314e447378227d; whl=-1%260%260%261545394867301; isg=BCAgn8GgaH-MTtOcn8lrcXRo8S4ygQSVG4xBcpox7DvOlcC_QjnUg_akKX2wI7zL; l=aBVnf-L1yHaIGCLKoMaiAl0sH707yCZzu9bq1MazNTEhNPe3Z2r99jno-VwWT_qC5zTy_K-5v"
        }
        req = Request(url,headers=headers)
        res = self.newOpener.open(req).read().decode('gbk')
        jd = json.loads(res)
        #print(jd)

        del jd['data']['originalPrice']['def']  # 注意永久性的删除
        #遍历鞋和鞋码以及价格
        for key,value in jd['data']['originalPrice'].items():
            num = key.split(';')
            print(self.shoes[num[2][8:]]+"  "+self.shoes_num[num[1][6:]]+"  "+value['price'])






