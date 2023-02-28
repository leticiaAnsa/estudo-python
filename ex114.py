import urllib
import urllib.request
#Crie um código em python que teste se o site pudim está acessível
#pelo computador usado.

#def site(wifi):
#    try:
#        site = (wifi)
#    except (DesconectionComputer):
#        print('\033[31m Site não assessado \033[m')        
#    else:
#        print('\033[32m Site assessado com sucesso\033[m]')

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('Consegui acessar o site pudim com sucesso!')
    print(site.read())
