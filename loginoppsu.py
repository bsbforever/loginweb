#!/usr/bin/python
#coding=gbk
#coding=utf-8
import urllib,urllib2,httplib,cookielib
class LoginOppsu:
    login_headers={
        'User-Agent':' Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KB974488'
    }
    signin_headers={
        'User-Agent':' Mozilla//5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KB974488'
    }
    cookie = None
    cookieFile = './cookie.dat'
    def __init__(self):
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)
    def Login(self):
        login_url = 'http://www.oppsu.cn/login.php?nowtime=1397524426343&verify=afaa6aa0'
        login_post = {'pwuser' : 'bsbforever',
                     'pwpwd' : '296701298a',
                    'jumpurl':'http://www.oppsu.cn/index.php',
                    'step':'2',
                    'ajax':'1',
                    'lgt':'0'}
        login_post = urllib.urlencode(login_post)
        req = urllib2.Request(url=login_url,data=login_post,headers=self.login_headers)   #�γ�һ��url����
        response = urllib2.urlopen(req)   #����ǰ�������
        result = response.read()       #��ȡ���ص�ҳ��
        self.cookie.save(self.cookieFile)
        if 'success' in result:
            print 'Login Successed'

    def SignIn(self):
        signin_url='http://www.oppsu.cn/hack.php?H_name=xqqiandao&'
        signin_post = {'action' : 'qiandao',
                      'qdxq' : '3',
                      'toflower':'zdkqiya',
                      'tozhufu':''}
        signin_post = urllib.urlencode(signin_post)   # ���ύ�����ݽ��б���
        req = urllib2.Request(url=signin_url, data=signin_post,headers=self.login_headers)   #�γ�һ��url����
        response = urllib2.urlopen(req)   #����ǰ�������
        result = response.read()  #��ȡ���ص�ҳ��
        self.cookie.save(self.cookieFile)
        if '�ɹ�' in result:
            print 'Signin Successed'
        elif '�Բ���ÿ���������ǩ�� ' in result:
            print 'You have already Sign in once!'
        else:
            print result

if __name__ == '__main__':
    user= LoginOppsu()
    user.Login()
    user.SignIn()
