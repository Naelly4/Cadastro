from views.tela import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle('fusion')
    from views.cadastro_view import App
    aplicativo = App()  
    aplicativo.show()
    sys.exit(app.exec_())
    
       
            
 
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

