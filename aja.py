#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\33[1;96m[!] \1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\33[%s;1m'%str(31+j))
    x += '\33[0m'
    x = x.replace('!0','\33[0m')
    sys.stdout.write(x+'\')


def jalan(z):
	for e in z + '\':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """ 
                        
                       
─█▀▀█ ░█─▄▀ ─█▀▀█ ░█▀▀▀█ ░█─░█ 
░█▄▄█ ░█▀▄─ ░█▄▄█ ─▀▀▀▄▄ ░█▀▀█ 
░█─░█ ░█─░█ ░█─░█ ░█▄▄▄█ ░█─░█
                        
                        
                        
                       
                                          
                                                                                                                                                         
            
        
\33[1;91m=======================================
\33[1;96mAuthor  \33[1;93m: \33[1;92mAKASH ROY
\33[1;96mInstagram \33[1;93m: \33[1:92mUnkown
\33[1;96mFacebook  \33[1;93m: \33[1:92mAkash Roy
\33[1;96mPronhub \33[1;93m: \33[1;92mNai
\33[1;91m======================================="""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\\33[1;96m[●] \1b[1;93mSedang masuk \1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\33[31mNot Vuln"
vuln = "\33[32mVuln"

os.system("clear")
print "\33[1;96m ============================================================="
print  """\33[1;91m
                        
                        
─█▀▀█ ░█─▄▀ ─█▀▀█ ░█▀▀▀█ ░█─░█ 
░█▄▄█ ░█▀▄─ ░█▄▄█ ─▀▀▀▄▄ ░█▀▀█ 
░█─░█ ░█─░█ ░█─░█ ░█▄▄▄█ ░█─░█
                      
                      
                                
                                                                                                                                                                 
       
          
\33[1;96mAuthor  \33[1;93m: \33[1;92mAkASH ROY
\33[1;96mInstagram \33[1;93m: \33[1;92mUNNOWN
\33[1;96mFacebook  \33[1;93m: \33[1;92mAkash Roy
\33[1;96mPronhub \33[1;93m: \33[1;92mNai
\33[1;91m======================================="""
print " \1b[1;93m============================================================="

CorrectUsername = "akash"
CorrectPassword = "roy"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\33[1;96m[☆] \1b[1;93mUsername Of Tool \1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\33[1;96m[☆] \1b[1;93mPassword Of Tool \1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged By Nabil" + username
            loop = 'false'
        else:
            print "Baler Password"
            os.system('https://www.youtube.com/channel/UC8km4e4REGBnOSknq82h_ew_confirmation=1 ')
    else:
        print "Wrong Username"
        os.system('https://www.youtube.com/channel/UC8km4e4REGBnOSknq82h_ew_confirmation=1 ')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\33[1;96m="
		print('\33[1;96m[☆] \1b[1;93mLOGIN WITH FACEBOOK \1b[1;96m[☆]' )
		id = raw_input('\33[1;96m[+] \1b[1;93mID/Email \1b[1;91m: \1b[1;92m')
		pwd = raw_input('\33[1;96m[+] \1b[1;93mPassword \1b[1;91m: \1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\\33[1;96m[!] \1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
