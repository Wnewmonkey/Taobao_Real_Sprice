from urllib.request import Request, build_opener, HTTPCookieProcessor,HTTPHandler,ProxyHandler,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent
import re
class Login_Getst(object):
    def Get_st(self):
        # 登录的URL，获取token
        self.request_url = 'https://login.taobao.com/member/login.jhtml'
        self.proxy_ip = "********"
        self.request_headers = {
            'authority': 'login.taobao.com',
            'User-Agent': UserAgent().firefox,
            'Referer': 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive'
        }
        # 用户名
        self.username = '*********'
        # ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '********'
        # 密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '***********'
        self.post = {
            "referer": "https://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.58c77370Oo6I7E&id=578101773230&_u=t2dmg8j26111",

            'TPL_username': self.username,
            'TPL_password': '',
            'ua': self.ua,
            'slideCodeShow': 'false',
            'useMobile': 'false',
            'lang': 'zh_CN',
            'loginsite': '0',
            'newlogin': '0',
            'TPL_redirect_url': 'http://i.taobao.com/my_taobao.htm',
            'from': 'tbTop',
            'fc': 'default',
            'style': 'default',
            'css_style': '',
            'keyLogin': 'false',
            'qrLogin': 'true',
            'newMini': 'false',
            'newMini2': 'false',
            'tid': '',
            'loginType': '3',
            'minititle': '',
            'minipara': '',
            'pstrong': '3',
            'sign': '',
            'need_sign': '',
            'isIgnore': '',
            'full_redirect': '',
            'sub_jump': '',
            'popid': '',
            'callback': '',
            'guf': '',
            'not_duplite_str': '',
            'need_user_id': '',
            'poy': '',
            'gvfdcname': '10',
            'gvfdcre': '68747470733A2F2F7777772E74616F62616F2E636F6D2F',
            'from_encoding ': '',
            'TPL_password_2': self.password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'allp': '',
            'sr': '1440 * 900',
            'osVer': 'windows | 6.1',
            'naviVer': 'chrome | 71.035788',

        }
        # 将POST的数据进行编码转换
        self.post_data = urlencode(self.post).encode(encoding='GBK')
        # 设置代理
        self.proxy = ProxyHandler({'http': self.proxy_ip})
        # 设置cookie处理器
        self.cookieHandler = HTTPCookieProcessor()
        # 设置登录时用到的opener，它的open方法相当于urllib.urlopen
        self.opener = build_opener(self.cookieHandler, self.proxy, HTTPHandler)
        #请求登录
        request = Request(self.request_url, self.post_data, self.request_headers)
        response = self.opener.open(request)
        html = response.read().decode('gbk')
        #print(html)
        # 抓取页面中的两个获取st的js
        pattern = re.compile('<script src=\"(.*)\"><\/script>')
        match = pattern.findall(html)
        #https://passport.alibaba.com/mini_apply_st.js?site=0&token=133vqFwzThkJ9i1FJTNkLzg&callback=callback
        #https://g.alicdn.com/kissy/k/1.4.2/seed-min.js
        # 其中第一个是我们需要请求的JS，它会返回我们需要的st
        #rint(match[0])

        # 如果匹配到了则去获取st
        if match:
            # 此时可以看到有两个st， 一个alibaba的，一个alipay的，我们用alibaba的去实现登录
            request = Request(match[0])
            response = urlopen(request)
            content = response.read().decode('gbk')

            # {"code":200,"data":{"st":"1lmuSWeWh1zGQn-t7cfAwvw"} 这段JS正常的话会包含这一段，我们需要的就是st
            # print(content)

            # 正则匹配st
            pattern = re.compile('{"st":"(.*?)"}')
            match = pattern.findall(content)
            #print(match)
            if match:
                return match[0]
            else:
                print(u'无法获取到st，请检查')
                return
