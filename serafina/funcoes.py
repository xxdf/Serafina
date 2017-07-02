import mimetypes
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from os.path import isfile
from datetime import datetime

def atualiza_arquivo(novo_texto):
	arquivo = open('log.txt','r')
	texto = arquivo.readlines()
	arquivo.close()
	arquivo = open('log.txt','w')
	texto.append(novo_texto)
	arquivo.writelines(texto)
	arquivo.close()
def enviar_email(conf):
	#print('\n sending email...')
	def adiciona_anexo(msg, filename):
		if not isfile(filename):
			print("Hey Bro! (%s) This file is not here, please, check.." %(filename))
			return None
		ctype, encoding = mimetypes.guess_type(filename)
		if ctype is None or encoding is not None:
			ctype = 'application/octet-stream'
		maintype, subtype = ctype.split('/',1)
		if maintype == 'text':
			with open(filename) as f:
				mime = MIMEText(f.read(), _subtype=subtype)
		else:
			with open(filename, 'rb') as f:
				mime = MIMEBase(maintype, subtype)
				mime.set_playload(f.read())
			encoders.encode_base64(mime)
		mime.add_header('Content-Disposition', 'attachment', filename=filename)
		msg.attach(mime)


	now = str(datetime.now().hour) +':'+str(datetime.now().minute) +':'+str(datetime.now().second) +' '+ str(datetime.now().day) +'/'+ str(datetime.now().month) +'/'+ str(datetime.now().year)
	msg = MIMEMultipart()
	msg['From'] = conf['de']
	msg['To'] = ', '.join(conf['para'])
	msg['Subject'] = conf['msg_assunto']
	msg.attach(MIMEText('Serafina: ' + conf['msg_corpo'] + '::' + now))
	adiciona_anexo(msg, conf['filename'])

	raw = msg.as_string()

	smtp = smtplib.SMTP_SSL(conf['host'], conf['port'])
	# SUBSTITUIR POR EMAIL TESTE
	smtp.login(conf['de'], conf['senha'])
	smtp.sendmail(conf['de'], conf['para'], raw)
	smtp.quit()

	a = open(conf['filename'], 'w')
	a.write('Novas informacoes\n--------\n')
	a.close()
