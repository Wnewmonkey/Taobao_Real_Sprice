from urllib.request import Request,build_opener,HTTPCookieProcessor
from fake_useragent import UserAgent
import re
import http.cookiejar
class Login_Byst(object):
    def __init__(self):
        # 登录成功时，需要的Cookie
        self.newCookie = http.cookiejar.CookieJar()
        # 登陆成功时，需要的一个新的opener
        self.newOpener = build_opener(HTTPCookieProcessor(self.newCookie))
    def By_st(self,st):
        # 通过st实现登录的URL
        self.st_url = 'https://login.taobao.com/member/vst.htm?st={st}'
        self.st_url = self.st_url.format(st=st)
        headers = {
            'User-Agent': UserAgent().firefox,
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive',
            'Referer': 'https://item.taobao.com/item.htm',
        }
        request = Request(self.st_url, headers=headers)
        response = self.newOpener.open(request)
        content = response.read().decode('gbk')

        # 检测结果，看是否登录成功
        pattern = re.compile('top.location.href = "(.*?)"', re.S)
        match = re.search(pattern, content)
        #print(match)
        if match:
            print(u'登录网址成功')
            return self.newOpener
        else:
            print(u'登录失败')
            return False
