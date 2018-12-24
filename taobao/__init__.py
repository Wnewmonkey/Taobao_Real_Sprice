from taobao.Login_Getst import Login_Getst
from taobao.Login_Byst import Login_Byst
from taobao.Find_Price import Find_Price
if __name__ == '__main__':
    #获取st
    st = Login_Getst().Get_st()
    # 利用st码进行登录
    # 这一步我是参考的崔庆才的个人博客的教程，因为抓包的时候并没有抓取到这个url
    # 但是如果不走这一步，登录又无法成功
    # 区别是并不需要传递user_name字段，只需要st就可以了
    Login_Byst().By_st(st)
    # 获取商品页面
    Find_Price().Find_Shoes()

