"""from Tela.tela import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os

class App(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **argvs):
        super(App, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle('fusion')
    aplicativo = App()  
    aplicativo.show()
    sys.exit(app.exec_())

"""

class Forma():

    def __init__(self, leite, farinha , ovos, fermento_em_po, achocolatado) -> bool:
        self.lei = leite
        self.farinha = farinha
        self.ovos = ovos
        self.fermento_em_po = fermento_em_po
        self.achocolatado = achocolatado
        self.retorno = str
        self.set_validar_ingredientes()


    def set_validar_ingredientes(self, ):
        
        for item in self.__dict__.values():
            if not item:
                self.retorno = 'Ingrediente vazio{}'.format(item)
                break
            self.retorno = "ingrediente preenchido"    
        print(self.retorno)

bolo = Forma(achocolatado='sa', farinha='sa', fermento_em_po='s', leite='sa', ovos='sa')
bolo.set_validar_ingredientes()