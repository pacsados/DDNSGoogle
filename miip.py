
import urllib.request
import urllib.parse
import http.client
import base64
import socket
import time
import os
import sys
sys.stdout.write('DDNS Google domain arrancado')
sys.stdout.write("\n")
try: 
	Dominio =os.environ['dominio']
	Usuario = os.environ['usuario']
	Passwd = os.environ['passwd']
except:
	sys.stdout.write('DDNS Google Domains - Faltan Datos en ENV.  (dominio, usuario o passwd)')
	sys.stdout.write("\n")
	exit()
while True:
	extIP4 = urllib.request.urlopen('https://domains.google.com/checkip').read().decode('utf8')
	sys.stdout.write ('Mi IP Externa:' +extIP4)
	currentIP = socket.gethostbyname(Dominio)
	sys.stdout.write (' -- IP de' + Dominio + ':'+currentIP)
	sys.stdout.write("\n")
	if currentIP != extIP4:
		UsrPass = Usuario + ":" + Passwd
		UsrPass = base64.b64encode(bytes(UsrPass, 'utf-8')).decode("ascii")
		Data = urllib.parse.urlencode({'hostname' : Dominio, 'myip' : extIP4 }).encode('utf8')
		upUrl= '/nic/update?'
		upHost = 'domains.google.com'
		headers = {'Content-Type'  : "application/x-www-form-urlencoded",
			'User-Agent'    : 'Chrome/41.0','Authorization' : 'Basic %s' % UsrPass}
		conn = http.client.HTTPSConnection(upHost)
		conn.request("POST", upUrl, Data, headers)
		upResp = conn.getresponse()
		sys.stdout.write (upResp.read().decode('utf-8')+"\n")
	else:
		sys.stdout.write ("DNS tiene tu IP " + extIP4 + " no necesita cambiarse en Google DNS")
		sys.stdout.write("\n")
	time.sleep(1800)




