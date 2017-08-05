import mimetypes
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from os.path import isfile
from datetime import datetime as dtt

def atualiza_arquivo( new_text ):
	archive = open('log.txt', 'r')
	text = archive.readlines()
	archive.close()
	archive = open('log.txt', 'w')
	text.append( new_text )
	archive.writelines( text )
	archive.close()
def enviar_email( conf ):
	# sending email...
	def adiciona_anexo( msg, filename ):
		if not isfile( filename ):
			print("Hey Bro! (%s) This file is not here, please, check.." %(filename))
			return None
		ctype, encoding = mimetypes.guess_type( filename )
		if ctype is None or encoding is not None:
			ctype = 'application/octet-stream'
		maintype, subtype = ctype.split('/',1)
		if maintype == 'text':
			with open( filename ) as f:
				mime = MIMEText(f.read(), _subtype=subtype)
		else:
			with open(filename, 'rb') as f:
				mime = MIMEBase(maintype, subtype)
				mime.set_playload(f.read())
			encoders.encode_base64(mime)
		mime.add_header('Content-Disposition', 'attachment', filename=filename)
		msg.attach( mime )

	now = str(str(dtt.now().hour) +':'+
		str(dtt.now().minute) +':'+
		str(dtt.now().second) +' '+
		str(dtt.now().day) +'/'+
		str(dtt.now().month) +'/'+
		str(dtt.now().year))
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
