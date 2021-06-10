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
        self.setWindowTitle("Editos de imagens - EDIFOTO")
        self.setWindowIcon(QtGui.QIcon("logo/logo.png"))
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):

        # Criando barra de menu
        self.barraDeMenu = self.menuBar()
        
        # Criando os menus
        self.menuArquivo = self.barraDeMenu.addMenu("Arquivo")
        self.menuTransformacao = self.barraDeMenu.addMenu("Transformações") 
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

        # Criando as actions do sobre
        self.sobre = self.menuSobre.addAction("Sobre")
        self.sobre = self.sobre.triggered.connect(self.exibir_mensagem)
        
        self.sobreImagem = self.menuSobre.addAction("Sobre imagem...")
        self.sobreImagem = self.sobreImagem.triggered.connect(self.exibir_sobre_imagem)

        # Criação de QLabel        
        self.texto = QLabel("Processamento Digital de Imagens (IFTM) - Trabalho final", self)
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
        self.pixmap1 = self.pixmap1.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)    

        self.imagem2 = QLabel(self)
        self.endereco2 = 'imagens/balao.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        self.mySlider = QSlider(Qt.Horizontal, self)
        self.mySlider.valueChanged[int].connect(self.changeValue)
        
        # Organizando os widgets dentro do GridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.texto2, 3, 0, 1, 2)
        self.layout.addWidget(self.mySlider, 4, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0,1)
        self.layout.setRowStretch(2,1)
   
    
    # Método de ação dos botões do menu

    def exibir_mensagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Detralhes sobre")
        self.msg.setText("Desenvolvido por Leandro Henrick Silva Nunes e Isaque da Silva Silveira")
        self.msg.setInformativeText("Aplicativo com diversos filtros.\nItuiutaba - MG\nProjeto concluído em 22/06/2021")
        self.msg.exec_()     

    def exibir_sobre_imagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Detralhes sobre a imagem")
        self.msg.setText("Todos os detalhes sobre a imagem:")
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
        self.pixmap1 = self.pixmap1.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
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
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
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
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def changeValue(self, value = ""):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.png'
        self.script = '.\efeito_transparencia.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida + ' \"' + str(value) 
        subprocess.run(self.program, shell=True)
        
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)    


    def transform_me_countour(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\efeito_countour.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me_emboss(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\efeito_emboss.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)        
    
    def transform_me_findEdges(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\efeito_find_edges.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(350, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()