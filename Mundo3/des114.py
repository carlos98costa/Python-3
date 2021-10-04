import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pizaniadesivos.com.br/')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('Tudo ok')

print(site.read())