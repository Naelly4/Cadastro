from Tela.tela import Ui_MainWindow
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
             
             
             
    
    '''
    class CadastroVeiculos(QtWidgets.QMainWindow):
    def __init__(self, *args, **argvs):# Metodo construtor da aplicação
        super(CadastroVeiculos, self).__init__(*args, **argvs)
        self.ui = Ui_cadastro_Veiculos()
        self.ui.setupUi(self)
        self.dataDeHoje = datetime.datetime.now()
        self.ui.dateEdit.setDate(self.dataDeHoje)
        self.ui.pushButton_3.clicked.connect(self.set_cadastrarnovoveiculo)
        self.log = logging.getLogger(__name__)
        self.log.debug("Inicializando Cadastro de veiculos")
        self.db = DataBase()
        #self.catalogarveiculos()
        self.ui.pushButton_2.clicked.connect(self.pesquisarveiculo)'''
    
    
     def set_cadastrar_cliente(self):
        try:
            nome = self.ui.lineEdit.text()
            CPF  =  self.ui.lineEdit_2.text()
            email =  self.ui.lineEdit_3.text()
            numero_telefone = self.ui.lineEdit_5.text()
             = self.ui.lineEdit_6.text()
            = self.ui.lineEdit_6.text()
            = self.ui.lineEdit_6.text()
            = self.ui.lineEdit_6.text()
    
    
    
    
    
    
    


'''
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
bolo.set_validar_ingredientes()'''
