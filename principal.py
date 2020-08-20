from PyQt5 import  uic,QtWidgets
import requests
import time
import threading

def atualiza_dados():
    while 1:
        time.sleep(2)
        resposta = requests.get('http://192.168.0.104/')
        dados = resposta.text
        dados_separados = dados.split("e")  
        print(dados_separados[0])
        print(dados_separados[1])
        tela.label_6.setText(dados_separados[1][0:4] + " °C")
        tela.label_7.setText(dados_separados[0][0:4] + "%")


app=QtWidgets.QApplication([])
tela=uic.loadUi("tela_monitor.ui")
threading.Thread(target=atualiza_dados).start()
tela.show()
app.exec()




    


