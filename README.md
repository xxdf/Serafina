# Serafina
Keylogger example with [Python] + send info to email

![alt text](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

## Compatibilities:
- Python Version: [2.7.x]
- Installed Packages: [pyHook] e [pywin32]
- S.O. Used: Windows 8.1

```sh
$ pip install pyHook
$ pip install pywin32
```
---

### Config. ###
* Open conf.py
![alt text](https://raw.githubusercontent.com/xxdf/Serafina/master/how_to_conf.png)
* set on line 6: Subject (email);
* set on line 7: Email content;
* set on line 8: your email (sender)
* set on line 9: your pass (sender)
* set on line 10: Recipients
* set on line 11: Key to Close/Stop Thread Serafina()

### Functions: ###
* `get_current_process()` : Funcao responsável por pegar o processo atual (Janela aberta em prioridade);
* `KeyStroke(event)` : Responsável por captar as teclas pressionadas, e gravá-las no arquivo de `log.txt`;
* `serafina()` : Nome carinhosamente dado ao programa, e a função que, consiste em ser assumida por uma *Thread* que, de tempo em tempo acessa um email no qual os dados sãs especificados no escopo do programa, e envia o arquivo de `log.txt` gravado e atualizado pelas demais funcoes;
* `atualiza_arquivo(novo_texto)` : Recebe por parametro o texto á adicionar no arquivo de `log.txt` já existente, e assim o faz;
* `enviar_email(de, para, senha, msg_assunto, msg_corpo)` : recebe por parametro as informações necessárias para enviar arquivo `log.txt` no email;
* `adiciona_anexo(msg, filename)` : Recebe por parametro `msg` e `filename`, que corresponde aos dados da mensagem a ser enviada, e ao nome do arquivo que será anexado, deve estar dentro da pasta do executável;
---

### Imports: ###
* Os imports é onde sao feitas as declarações das bibliotecas que serão usadas no decorrer do programa;
* Função `Thread` da biblioteca `threading`, responsável por criar e gerenciar a thread criada para enviar email;
* Função `sleep` da biblioteca `time`, responsável por fazer com que o S.O. espere um tempo especificado para prosseguir com a execução;
* Bibliotecas `pythoncom`, `pyHook`, `win32clipboard`, responsável por gerenciar trocas de telas com prioridade no sistema operacional, além de capturar as teclas pressionadas, e ter acesso as informações de processo necessárias para manipular as operações;
* A biblioteca `funcoes` é um pacote importado, que faz referencia a um programa chamado `funcoes.py` que fica na mesma pasta do programa `serafina` executável, nela contém tres funcoes criadas, `atualiza_arquivo`, `enviar_email` e `adiciona_anexo`. Estas poderão ser referenciadas a qualquer momento no presente executável (`serafina.py`);
* imports referente á bilioteca `email` e `smtplib`, são para gerenciar o acesso e envio das informações via email;

## ATTENTION: This software is fully devoted to de study of the functions and libs. Please Do not use to harm anyone! ##


##### Based on [Black Hat Python Book]
##### Authors [Eber H. S. A.] and [Jeniffer Genoatto]
##### Available on [Serafina]
  [Python]: <http://python.org>
  [2.7.x]: <https://www.python.org/downloads/release/python-2713/>
  [pyHook]: <https://pypi.python.org/pypi/pyHook>
  [pywin32]: <https://pypi.python.org/pypi/pywin32>
  [Black Hat Python Book]: <https://novatec.com.br/livros/black-hat-python/>
  [Eber H. S. A.]: <https://github.com/xxdf>
  [Serafina]: <https://xxdf.github.io/Serafina/>
  [Jeniffer Genoatto]: <https://github.com/JenifferGenoatto>
