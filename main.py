import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QMessageBox, QSlider, QWidget
from PyQt5.QtCore import QSize, Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()       

    def setup_main_window(self):
        self.valor = False
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Dialog - untiled")
        #self.setWindowIcon(QtGui.QIcon("imagens/logo.png"))
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):

        # Criando barra de menu
        self.barraDeMenu = self.menuBar()
        
        # Criando os menus
        self.menuArquivo = self.barraDeMenu.addMenu("Arquivo")
        self.menuTransformacao = self.barraDeMenu.addMenu("Transformação")
        self.menuSobre = self.barraDeMenu.addMenu("Sobre")

        # Criando as actions menuArquivo
        self.opcaoabrir = self.menuArquivo.addAction("Abrir")
        self.opcaoFechar = self.menuArquivo.addAction("Fechar")
        self.opcaoabrir.triggered.connect(self.open_file)
        self.opcaoabrir.setShortcut("Ctrl+A")
        self.opcaoFechar.triggered.connect(self.close)
        self.opcaoFechar.setShortcut("Alt+F4")

        # Criando as actions menuTransformações
        self.efeito_find = self.menuTransformacao.addAction("FIND EDGES")
        self.efeito_find.triggered.connect(self.transform_me_findEdges)        
        self.efeito_contour = self.menuTransformacao.addAction("CONTOUR")
        self.efeito_contour.triggered.connect(self.transform_me_countour)        
        self.efeito_emboss = self.menuTransformacao.addAction("EMBOSS")
        self.efeito_emboss.triggered.connect(self.transform_me_emboss)
        self.informacao_imagem = self.menuTransformacao.addAction("Adicionar esteganografia")
        self.informacao_imagem.triggered.connect(self.add_esteganografia)

        # Criando as actions do sobre
        self.sobre = self.menuSobre.addAction("Sobre")
        self.sobre = self.sobre.triggered.connect(self.exibir_mensagem)

        # Criação de QLabel        
        self.texto = QLabel("Processamento Digital de Imagens", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)     

        self.texto2 = QLabel("Insira a quantidade de trânsparência da imagem", self)
        self.texto2.adjustSize()
        self.largura = self.texto2.frameGeometry().width()
        self.altura = self.texto2.frameGeometry().height()
        self.texto2.setAlignment(QtCore.Qt.AlignCenter)   

        # Criando as imagens (QLabel)
        self.imagem1 = QLabel(self)
        self.endereco1 = 'imagens/balao.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)    

        self.imagem2 = QLabel(self)
        self.endereco2 = 'imagens/balao.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        # Criando botões
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Espelhar")
        self.b1.clicked.connect(self.espelhar)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Girar")
        self.b2.clicked.connect(self.girar)

        self.mySlider = QSlider(Qt.Horizontal, self)
        self.mySlider.valueChanged[int].connect(self.changeValue)
        
        # Organizando os widgets dentro do GridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.texto2, 3, 0, 1, 2)
        self.layout.addWidget(self.mySlider, 4, 0, 1, 2)
        self.layout.addWidget(self.b1, 2, 0)        
        self.layout.addWidget(self.b2, 2, 1)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0,0)
        self.layout.setRowStretch(1,1)
        self.layout.setRowStretch(2,0)      
    
    # Método de ação dos botões do menu

    def exibir_mensagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Detralhes sobre")
        self.msg.setText("Desenvolvido por Leandro Henrick Silva Nunes")
        self.msg.setInformativeText("Aplicativo para uso dos filtros: 'Countour', 'Emboss' e 'Find Edges'.\nItuiutaba - MG\nProjeto concluído em 10/05/2021")
        self.msg.exec_()        

    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Open image', 
                                                            directory=QtCore.QDir.currentPath(),
                                                            filter='All files (*.*);;Images (*.png; *.jpg)',
                                                            initialFilter='Images (*.png; *.jpg)')
        #print(fileName)
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)

    def girar (self):
        if (self.valor == False):
            self.entrada = self.endereco1
            self.saida = 'imagens/arquivo_novo.jpg'
            self.script = '.\girar.py'
            self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
            subprocess.run(self.program, shell=True)  
        else:
            self.entrada = 'imagens/arquivo_novo.jpg'
            self.saida = 'imagens/arquivo_novo1.jpg'
            self.script = '.\girar.py'
            self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
            subprocess.run(self.program, shell=True)
        
        self.valor = True        

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def espelhar (self):
        if (self.valor == False):
            self.entrada = self.endereco1
            self.saida = 'imagens/arquivo_novo.jpg'
            self.script = '.\espelhar.py'
            self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
            subprocess.run(self.program, shell=True)  
        else:
            self.entrada = 'imagens/arquivo_novo.jpg'
            self.saida = 'imagens/arquivo_novo1.jpg'
            self.script = '.\espelhar.py'
            self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
            subprocess.run(self.program, shell=True)
        
        self.valor = True        

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def add_esteganografia(self):
        return print(1)

    def changeValue(self, value = ""):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.png'
        self.script = '.\efeito_transparencia.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida + ' \"' + str(value) 
        subprocess.run(self.program, shell=True)
        
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)    


    def transform_me_countour(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\efeito_countour.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me_emboss(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\efeito_emboss.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)        
    
    def transform_me_findEdges(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\efeito_find_edges.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()