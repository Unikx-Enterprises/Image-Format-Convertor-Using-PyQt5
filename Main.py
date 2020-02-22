import sys,os,time
from PyQt5.QtWidgets import QDialog, QApplication, QFontDialog,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter,QPrintPreviewDialog
from IEC_Ui import *
from PIL import Image ,ImageEnhance as ih


allow_files={".gif":(66, 165 , 245),".png":(66, 165 , 245),".jpg":(0, 255 , 0),".bmp":(255, 0 , 113),".jpeg":(27, 140 , 113)}
files={}
cur_fil=""
clicked_image = []

        
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label_3.setPixmap(QtGui.QPixmap("no_image.png"))
        self.ui.pushButton_3.clicked.connect(self.add_file)
        self.ui.pushButton_8.clicked.connect(self.add_folder)
        self.ui.pushButton_7.clicked.connect(self.remove_all) 
        self.ui.pushButton_6.clicked.connect(self.select_all)
        self.ui.listWidget.itemClicked.connect(self.list_item_click)
        self.ui.pushButton_9.clicked.connect(self.current_loc)
        self.ui.pushButton_11.clicked.connect(self.browse)
        self.ui.pushButton_5.clicked.connect(self.edit_file)
        self.ui.pushButton_10.clicked.connect(self.convert)
        
        no =self.ui.listWidget.selectedItems()
        if len(no)>1:
            self.ui.pushButton_5.setEnabled(False)
        elif len(no)==0:
            self.ui.pushButton_5.setEnabled(False)
            self.ui.comboBox.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
        else:
            self.ui.pushButton_5.setEnabled(True)
            
        self.show()
        
# ===============================================================================================================================   
    def edit_file(self):
        global files,clicked_image
        click_file = str(self.ui.lineEdit_6.text() +self.ui.lineEdit_4.text())
        print(click_file)
        clicked_image.append(click_file)
        print(1)
        try:
            img = Image.open(str(click_file))
            img.save("C://enhancer.png")
        except Exception as e:
            print(e.args)
            
        print(1)

        sel_img = self.ui.listWidget.selectedItems()[0].text()

        names=list(files.keys())
      
        folders=list(files.values())
        for i in names:
            
            if i==sel_img:

           
                im=QtGui.QPixmap(str(files.get(i)))
                print(im)
                
                # pix=im.getbbox()
             
                # self.ui.lineEdit_6.setText(str(files.get(i)))
              
                # self.ui.lineEdit_5.setText(str(f"{round(os.path.getsize(files.get(i))/1024, 2)} KB"))
           
                # self.ui.lineEdit_4.setText(str(im.format))
            
                # dimension_=f"{im.size[0]}x{im.size[1]}"
                # cur_fil=str(files.get(i)).replace(os.path.basename(files.get(i)),"")
                
                
                # out.save("check.jpg")
                
                
                # self.ui.label.setPixmap(QtGui.QPixmapstr(str(os.getcwd())+"\check." + str(im.format)))
                # os.remove("check." + str(im.format))        
            else:
                pass

        
        Dialog=QDialog(self)
        Dialog.resize(1117, 570)
        Dialog.setStyleSheet("background-color: rgb(213, 211, 242);")
        Dialog.setWindowTitle( "Edit")
        
         
        label = QtWidgets.QLabel(Dialog)
        label.setGeometry(QtCore.QRect(0, 0, 621, 511))
        label.setScaledContents(True)
    
        try:
            
            label.setPixmap(im)
            
            # os.remove(r"check.jpg")
            #label.setText("")
        except:
            label.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            label.setText("No Image Selected..")
            
    
    # --------------------------------------------------------------- Tab 1 ----------------------------------------------     
        tabWidget = QtWidgets.QTabWidget(Dialog)
        tabWidget.setGeometry(QtCore.QRect(620, 0, 491, 561))
        tabWidget.setAutoFillBackground(False)
        tabWidget.setStyleSheet("background-color: rgb(213, 228, 242);")
        tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        tabWidget.setMovable(True)
        
        tab = QtWidgets.QWidget()
        horizontalSlider = QtWidgets.QSlider(tab)
        horizontalSlider.setGeometry(QtCore.QRect(10, 50, 261, 19))
        horizontalSlider.setMinimum(-100)
        horizontalSlider.setMaximum(100)
        horizontalSlider.setSingleStep(1)
        horizontalSlider.setPageStep(10)
        horizontalSlider.setSliderPosition(1)
        horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        horizontalSlider.setTracking(True)
        horizontalSlider.valueChanged[int].connect(bright_change)
        
        horizontalSlider_2 = QtWidgets.QSlider(tab)
        horizontalSlider_2.setGeometry(QtCore.QRect(10, 110, 261, 19))
        horizontalSlider_2.setMinimum(-100)
        horizontalSlider_2.setMaximum(100)
        horizontalSlider_2.setSliderPosition(1)
        horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        
        
        line_2 = QtWidgets.QFrame(tab)
        line_2.setGeometry(QtCore.QRect(0, 140, 481, 16))
        line_2.setFrameShape(QtWidgets.QFrame.HLine)
        line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        spinBox = QtWidgets.QSpinBox(tab)
        spinBox.setGeometry(QtCore.QRect(290, 50, 91, 22))
        spinBox.setMinimum(-100)
        spinBox.setMaximum(100)
        
        spinBox_2 = QtWidgets.QSpinBox(tab)
        spinBox_2.setGeometry(QtCore.QRect(290, 110, 101, 22))
        spinBox_2.setMinimum(-100)
        spinBox_2.setMaximum(100)
        spinBox_2.setProperty("value", 1)  

        font_button = QtGui.QFont()
        font_button.setPointSize(10)
        font_button.setBold(True)
        font_button.setWeight(75)             
        pushButton = QtWidgets.QPushButton(tab)
        pushButton.setGeometry(QtCore.QRect(90, 220, 311, 31))
        pushButton.setFont(font_button)
        pushButton.setStyleSheet("color: rgb(0, 85, 255);")

        label_2 = QtWidgets.QLabel(tab)
        label_2.setGeometry(QtCore.QRect(10, 170, 451, 20))
        label_2.setStyleSheet("color: rgb(0, 128, 255);")

        font_label = QtGui.QFont()
        font_label.setBold(True)
        font_label.setWeight(75)
        label_29 = QtWidgets.QLabel(tab)
        label_29.setGeometry(QtCore.QRect(10, 10, 81, 16))
        label_29.setFont(font_label)

        line_11 = QtWidgets.QFrame(tab)
        line_11.setGeometry(QtCore.QRect(0, 30, 471, 20))
        line_11.setStyleSheet("")
        line_11.setFrameShape(QtWidgets.QFrame.HLine)
        line_11.setFrameShadow(QtWidgets.QFrame.Sunken)

        line_12 = QtWidgets.QFrame(tab)
        line_12.setGeometry(QtCore.QRect(0, 90, 471, 20))
        line_12.setStyleSheet("")
        line_12.setFrameShape(QtWidgets.QFrame.HLine)
        line_12.setFrameShadow(QtWidgets.QFrame.Sunken)

        label_31 = QtWidgets.QLabel(tab)
        label_31.setGeometry(QtCore.QRect(10, 70, 81, 16)) 
        label_31.setFont(font_label)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brightness.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
        tabWidget.addTab(tab,icon,"Brightness and Contrast")
        
        
    
    def bright_change(self,value):
        print(value)
        print("hghyg")
            # global clicked_image
            # print(clicked_image[0])
            # print(12)
            # imge = Image.open(clicked_image[0])
            # enhancer = ih.Brightness(imge)
            # enhancer.enhance(value)
            # print(13)
            # enhancer.save("C://enhancer.png")
            # label.setPixmap(QtGui.QPixmap("C://enhancer.png"))
            
        
            
            
        
    # --------------------------------------------------------------- Tab 2 ---------------------------------------------- 
        tab_3 = QtWidgets.QWidget()
        
        label_3 = QtWidgets.QLabel(tab_3)
        label_3.setGeometry(QtCore.QRect(10, 10, 81, 16))
        label_3.setFont(font_label)

        line_3 = QtWidgets.QFrame(tab_3)
        line_3.setGeometry(QtCore.QRect(10, 30, 471, 20))
        line_3.setFrameShape(QtWidgets.QFrame.HLine)
        line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        label_4 = QtWidgets.QLabel(tab_3)
        label_4.setGeometry(QtCore.QRect(10, 50, 71, 16))
        label_4.setStyleSheet("color: rgb(0, 128, 255);")

        comboBox = QtWidgets.QComboBox(tab_3)
        comboBox.setGeometry(QtCore.QRect(80, 50, 81, 22))
        comboBox.setStyleSheet("color: rgb(0, 128, 255);")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")

        radioButton = QtWidgets.QRadioButton(tab_3)
        radioButton.setGeometry(QtCore.QRect(30, 80, 82, 17))
        radioButton.setStyleSheet("color: rgb(0, 128, 255);")
        
        radioButton_2 = QtWidgets.QRadioButton(tab_3)
        radioButton_2.setGeometry(QtCore.QRect(30, 100, 82, 17))
        radioButton_2.setStyleSheet("color: rgb(0, 128, 255);")

        line_4 = QtWidgets.QFrame(tab_3)
        line_4.setGeometry(QtCore.QRect(10, 150, 471, 20))
        line_4.setFrameShape(QtWidgets.QFrame.HLine)
        line_4.setFrameShadow(QtWidgets.QFrame.Sunken)

        label_5 = QtWidgets.QLabel(tab_3)
        label_5.setGeometry(QtCore.QRect(10, 130, 81, 16))      
        label_5.setFont(font_label)
        gridFrame = QtWidgets.QFrame(tab_3)
        gridFrame.setGeometry(QtCore.QRect(10, 170, 160, 131))
        gridFrame.setStyleSheet("color: rgb(0, 128, 255);")
        gridFrame.setObjectName("gridFrame")
        gridLayout_2 = QtWidgets.QGridLayout(gridFrame)
        gridLayout_2.setObjectName("gridLayout_2")
        spinBox_4 = QtWidgets.QSpinBox(gridFrame)
        spinBox_4.setObjectName("spinBox_4")
        # spinBox_4.setValue(pix[1])
        gridLayout_2.addWidget(spinBox_4, 1, 1, 1, 1)
        
        spinBox_3 = QtWidgets.QSpinBox(gridFrame)
        spinBox_3.setObjectName("spinBox_3")
        # spinBox_3.setValue(pix[0])
        gridLayout_2.addWidget(spinBox_3, 0, 1, 1, 1)
        
        spinBox_5 = QtWidgets.QSpinBox(gridFrame)
        spinBox_5.setObjectName("spinBox_5")
        # spinBox_5.setValue(pix[1])
        gridLayout_2.addWidget(spinBox_5, 2, 1, 1, 1)
        label_8 = QtWidgets.QLabel(gridFrame)
        label_8.setObjectName("label_8")
        gridLayout_2.addWidget(label_8, 2, 0, 1, 1)
        label_7 = QtWidgets.QLabel(gridFrame)
        label_7.setObjectName("label_7")
        gridLayout_2.addWidget(label_7, 1, 0, 1, 1)
        label_6 = QtWidgets.QLabel(gridFrame)
        label_6.setObjectName("label_6")
        gridLayout_2.addWidget(label_6, 0, 0, 1, 1)
        label_9 = QtWidgets.QLabel(gridFrame)
        label_9.setObjectName("label_9")
        gridLayout_2.addWidget(label_9, 3, 0, 1, 1)
        spinBox_6 = QtWidgets.QSpinBox(gridFrame)
        spinBox_6.setObjectName("spinBox_6")
        # spinBox_6.setValue(pix[3])
        gridLayout_2.addWidget(spinBox_6, 3, 1, 1, 1)
        label_10 = QtWidgets.QLabel(tab_3)
        label_10.setGeometry(QtCore.QRect(20, 330, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_10.setFont(font)
        label_10.setObjectName("label_10")
        line_5 = QtWidgets.QFrame(tab_3)
        line_5.setGeometry(QtCore.QRect(20, 350, 471, 20))
        line_5.setStyleSheet("")
        line_5.setFrameShape(QtWidgets.QFrame.HLine)
        line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_5.setObjectName("line_5")
        label_11 = QtWidgets.QLabel(tab_3)
        label_11.setGeometry(QtCore.QRect(10, 330, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_11.setFont(font)
        label_11.setObjectName("label_11")
        line_6 = QtWidgets.QFrame(tab_3)
        line_6.setGeometry(QtCore.QRect(10, 350, 471, 20))
        line_6.setStyleSheet("")
        line_6.setFrameShape(QtWidgets.QFrame.HLine)
        line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_6.setObjectName("line_6")
        label_12 = QtWidgets.QLabel(tab_3)
        label_12.setGeometry(QtCore.QRect(20, 370, 51, 16))
        label_12.setStyleSheet("color: rgb(0, 128, 255);")
        label_12.setObjectName("label_12")
        label_13 = QtWidgets.QLabel(tab_3)
        label_13.setGeometry(QtCore.QRect(20, 390, 51, 16))
        label_13.setStyleSheet("color: rgb(0, 128, 255);")
        label_13.setObjectName("label_13")
        lineEdit = QtWidgets.QLineEdit(tab_3)
        lineEdit.setEnabled(False)
        lineEdit.setGeometry(QtCore.QRect(70, 370, 113, 20))
        lineEdit.setStyleSheet("color: rgb(0, 128, 255);")
        lineEdit.setObjectName("lineEdit")
        # lineEdit.setText(dimension_)
        lineEdit_4 = QtWidgets.QLineEdit(tab_3)
        lineEdit_4.setEnabled(False)
        lineEdit_4.setGeometry(QtCore.QRect(70, 390, 113, 20))
        lineEdit_4.setStyleSheet("color: rgb(0, 128, 255);")
        lineEdit_4.setObjectName("lineEdit_4")
        pushButton_2 = QtWidgets.QPushButton(tab_3)
        pushButton_2.setGeometry(QtCore.QRect(10, 460, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        pushButton_2.setFont(font)
        pushButton_2.setStyleSheet("color: rgb(0, 85, 255);")
        pushButton_2.setObjectName("pushButton_2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("crop.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tabWidget.addTab(tab_3, icon1, "")
        tab_4 = QtWidgets.QWidget()
        tab_4.setObjectName("tab_4")
        label_14 = QtWidgets.QLabel(tab_4)
        label_14.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_14.setFont(font)
        label_14.setObjectName("label_14")
        label_15 = QtWidgets.QLabel(tab_4)
        label_15.setGeometry(QtCore.QRect(20, 50, 21, 16))
        label_15.setStyleSheet("color: rgb(0, 128, 255);")
        label_15.setText("")
        label_15.setPixmap(QtGui.QPixmap("rotate_left.PNG"))
        label_15.setObjectName("label_15")
        line_7 = QtWidgets.QFrame(tab_4)
        line_7.setGeometry(QtCore.QRect(0, 30, 471, 20))
        line_7.setStyleSheet("")
        line_7.setFrameShape(QtWidgets.QFrame.HLine)
        line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_7.setObjectName("line_7")
        label_16 = QtWidgets.QLabel(tab_4)
        label_16.setGeometry(QtCore.QRect(20, 70, 21, 16))
        label_16.setStyleSheet("color: rgb(0, 128, 255);")
        label_16.setText("")
        label_16.setPixmap(QtGui.QPixmap("rotate_right.PNG"))
        label_16.setObjectName("label_16")
        label_17 = QtWidgets.QLabel(tab_4)
        label_17.setGeometry(QtCore.QRect(20, 90, 21, 16))
        label_17.setText("")
        label_17.setPixmap(QtGui.QPixmap("by_degree.PNG"))
        label_17.setObjectName("label_17")
        label_18 = QtWidgets.QLabel(tab_4)
        label_18.setGeometry(QtCore.QRect(10, 120, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_18.setFont(font)
        label_18.setObjectName("label_18")
        line_8 = QtWidgets.QFrame(tab_4)
        line_8.setGeometry(QtCore.QRect(0, 140, 471, 20))
        line_8.setStyleSheet("")
        line_8.setFrameShape(QtWidgets.QFrame.HLine)
        line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_8.setObjectName("line_8")
        label_19 = QtWidgets.QLabel(tab_4)
        label_19.setGeometry(QtCore.QRect(20, 160, 21, 16))
        label_19.setStyleSheet("color: rgb(0, 128, 255);")
        label_19.setText("")
        label_19.setPixmap(QtGui.QPixmap("flip_hor.PNG"))
        label_19.setObjectName("label_19")
        label_20 = QtWidgets.QLabel(tab_4)
        label_20.setGeometry(QtCore.QRect(20, 180, 21, 16))
        label_20.setStyleSheet("color: rgb(0, 128, 255);")
        label_20.setText("")
        label_20.setPixmap(QtGui.QPixmap("flip_ver.PNG"))
        label_20.setObjectName("label_20")
        pushButton_3 = QtWidgets.QPushButton(tab_4)
        pushButton_3.setGeometry(QtCore.QRect(40, 160, 81, 20))
        pushButton_3.setStyleSheet("color: rgb(0, 128, 255);")
        pushButton_3.setFlat(True)
        pushButton_3.setObjectName("pushButton_3")
        pushButton_4 = QtWidgets.QPushButton(tab_4)
        pushButton_4.setGeometry(QtCore.QRect(40, 180, 71, 20))
        pushButton_4.setStyleSheet("color: rgb(0, 128, 255);")
        pushButton_4.setFlat(True)
        pushButton_4.setObjectName("pushButton_4")
        label_22 = QtWidgets.QLabel(tab_4)
        label_22.setGeometry(QtCore.QRect(50, 90, 61, 20))
        label_22.setStyleSheet("color: rgb(0, 128, 255);")
        label_22.setObjectName("label_22")
        spinBox_7 = QtWidgets.QSpinBox(tab_4)
        spinBox_7.setGeometry(QtCore.QRect(120, 90, 71, 21))
        spinBox_7.setStyleSheet("color: rgb(0, 128, 255);")
        spinBox_7.setMinimum(-360)
        spinBox_7.setMaximum(360)
        spinBox_7.setObjectName("spinBox_7")
        pushButton_7 = QtWidgets.QPushButton(tab_4)
        pushButton_7.setGeometry(QtCore.QRect(40, 70, 81, 20))
        pushButton_7.setStyleSheet("color: rgb(0, 128, 255);")
        pushButton_7.setFlat(True)
        pushButton_7.setObjectName("pushButton_7")
        pushButton_8 = QtWidgets.QPushButton(tab_4)
        pushButton_8.setGeometry(QtCore.QRect(40, 50, 71, 20))
        pushButton_8.setStyleSheet("color: rgb(0, 128, 255);")
        pushButton_8.setFlat(True)
        pushButton_8.setObjectName("pushButton_8")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("rotate.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tabWidget.addTab(tab_4, icon2, "")
        tab_5 = QtWidgets.QWidget()
        tab_5.setObjectName("tab_5")
        line_9 = QtWidgets.QFrame(tab_5)
        line_9.setGeometry(QtCore.QRect(10, 30, 471, 20))
        line_9.setStyleSheet("")
        line_9.setFrameShape(QtWidgets.QFrame.HLine)
        line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_9.setObjectName("line_9")
        label_21 = QtWidgets.QLabel(tab_5)
        label_21.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_21.setFont(font)
        label_21.setObjectName("label_21")
        line_10 = QtWidgets.QFrame(tab_5)
        line_10.setGeometry(QtCore.QRect(10, 300, 471, 20))
        line_10.setStyleSheet("")
        line_10.setFrameShape(QtWidgets.QFrame.HLine)
        line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_10.setObjectName("line_10")
        label_23 = QtWidgets.QLabel(tab_5)
        label_23.setGeometry(QtCore.QRect(10, 280, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_23.setFont(font)
        label_23.setObjectName("label_23")
        radioButton_3 = QtWidgets.QRadioButton(tab_5)
        radioButton_3.setGeometry(QtCore.QRect(10, 50, 91, 17))
        radioButton_3.setObjectName("radioButton_3")
        radioButton_4 = QtWidgets.QRadioButton(tab_5)
        radioButton_4.setGeometry(QtCore.QRect(10, 80, 151, 17))
        radioButton_4.setObjectName("radioButton_4")
        comboBox_2 = QtWidgets.QComboBox(tab_5)
        comboBox_2.setGeometry(QtCore.QRect(30, 110, 181, 22))
        comboBox_2.setObjectName("comboBox_2")
        radioButton_5 = QtWidgets.QRadioButton(tab_5)
        radioButton_5.setGeometry(QtCore.QRect(10, 140, 141, 17))
        radioButton_5.setObjectName("radioButton_5")
        spinBox_8 = QtWidgets.QSpinBox(tab_5)
        spinBox_8.setGeometry(QtCore.QRect(30, 170, 71, 22))
        spinBox_8.setObjectName("spinBox_8")
        label_24 = QtWidgets.QLabel(tab_5)
        label_24.setGeometry(QtCore.QRect(110, 170, 16, 21))
        label_24.setObjectName("label_24")
        spinBox_9 = QtWidgets.QSpinBox(tab_5)
        spinBox_9.setGeometry(QtCore.QRect(130, 170, 71, 22))
        spinBox_9.setObjectName("spinBox_9")
        label_25 = QtWidgets.QLabel(tab_5)
        label_25.setGeometry(QtCore.QRect(210, 170, 91, 21))
        label_25.setObjectName("label_25")
        radioButton_6 = QtWidgets.QRadioButton(tab_5)
        radioButton_6.setGeometry(QtCore.QRect(10, 200, 221, 17))
        radioButton_6.setObjectName("radioButton_6")
        spinBox_10 = QtWidgets.QSpinBox(tab_5)
        spinBox_10.setGeometry(QtCore.QRect(30, 230, 71, 22))
        spinBox_10.setObjectName("spinBox_10")
        label_26 = QtWidgets.QLabel(tab_5)
        label_26.setGeometry(QtCore.QRect(110, 232, 47, 21))
        label_26.setObjectName("label_26")
        lineEdit_5 = QtWidgets.QLineEdit(tab_5)
        lineEdit_5.setEnabled(False)
        lineEdit_5.setGeometry(QtCore.QRect(60, 320, 113, 20))
        lineEdit_5.setStyleSheet("color: rgb(0, 128, 255);")
        lineEdit_5.setObjectName("lineEdit_5")
        # lineEdit_5.setText(dimension_)
        lineEdit_6 = QtWidgets.QLineEdit(tab_5)
        lineEdit_6.setEnabled(False)
        lineEdit_6.setGeometry(QtCore.QRect(60, 340, 113, 20))
        lineEdit_6.setStyleSheet("color: rgb(0, 128, 255);")
        lineEdit_6.setObjectName("lineEdit_6")
        label_27 = QtWidgets.QLabel(tab_5)
        label_27.setGeometry(QtCore.QRect(10, 320, 51, 16))
        label_27.setStyleSheet("color: rgb(0, 128, 255);")
        label_27.setObjectName("label_27")
        label_28 = QtWidgets.QLabel(tab_5)
        label_28.setGeometry(QtCore.QRect(10, 340, 51, 16))
        label_28.setStyleSheet("color: rgb(0, 128, 255);")
        label_28.setObjectName("label_28")
        pushButton_5 = QtWidgets.QPushButton(tab_5)
        pushButton_5.setGeometry(QtCore.QRect(10, 380, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        pushButton_5.setFont(font)
        pushButton_5.setStyleSheet("color: rgb(0, 85, 255);")
        pushButton_5.setObjectName("pushButton_5")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resize.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tabWidget.addTab(tab_5, icon3, "")
        tab_2 = QtWidgets.QWidget()
        tab_2.setObjectName("tab_2")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("color.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tabWidget.addTab(tab_2, icon4, "")
        pushButton_6 = QtWidgets.QPushButton(Dialog)
        pushButton_6.setGeometry(QtCore.QRect(4, 512, 611, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        pushButton_6.setFont(font)
        pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 85, 255);")
        pushButton_6.setObjectName("pushButton_6")  
        tabWidget.setCurrentIndex(3)     
        
        pushButton.setText( "Auto Brightness")
        label_2.setText( "To Automatically Correct the Brightness level of Selected Picture, Click On button give below")
        label_29.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Brightness</span></p><p><br/></p></body></html>")
        label_31.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Contrast</span></p><p><br/></p></body></html>")
        tabWidget.setTabText(tabWidget.indexOf(tab),  "Brightness and Contrast")
        label_3.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Crop settings</span></p></body></html>")
        label_4.setText( "Aspect Ratio:")
        comboBox.setItemText(0,  "None")
        comboBox.setItemText(1,  "3 x 4")
        comboBox.setItemText(2,  "3 x 5")
        comboBox.setItemText(3,  "4 x 6")
        comboBox.setItemText(4,  "5 x 7")
        comboBox.setItemText(5,  "8 x 10")
        radioButton.setText( "Landscape")
        radioButton_2.setText( "Portrait")
        label_5.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Crop Handles</span></p></body></html>")
        label_8.setText( "Top :")
        label_7.setText( "Right :")
        label_6.setText( "Left :")
        label_9.setText( "Bottom :")
        label_10.setText( "<html><head/><body><p>Picture Dimension</p></body></html>")
        label_11.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Picture Dimension</span></p></body></html>")
        label_12.setText( "Original :")
        label_13.setText( "New :")
        pushButton_2.setText( "Ok")
        tabWidget.setTabText(tabWidget.indexOf(tab_3),  "Crop")
        label_14.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Rotate</span></p><p><br/></p></body></html>")
        label_18.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Flip</span></p><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>")
        pushButton_3.setText( "Flip Horizontal")
        pushButton_4.setText( "Flip Vertical")
        label_22.setText( "By Degree :")
        pushButton_7.setText( "Rotate Right")
        pushButton_8.setText( "Rotate Left")
        tabWidget.setTabText(tabWidget.indexOf(tab_4),  "Rotate and Flip")
        label_21.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Resize settings</span></p></body></html>")
        label_23.setText( "<html><head/><body><p><span style=\" color:#0055ff;\">Size Setting Summary</span></p></body></html>")
        radioButton_3.setText( "Original Size")
        radioButton_4.setText( "Predefined width x height :")
        radioButton_5.setText( "Custom width x height :")
        label_24.setText( "x")
        label_25.setText( "pixels")
        radioButton_6.setText( "Percentage of original width x height :")
        label_26.setText( "%")
        label_27.setText( "Original :")
        label_28.setText( "New :")
        pushButton_5.setText( "Ok")
        tabWidget.setTabText(tabWidget.indexOf(tab_5),  "Resize")
        tabWidget.setTabText(tabWidget.indexOf(tab_2),  "Color")
        pushButton_6.setText( "Convert")        
        
        
        
        
        
        
        
        
        Dialog.setWindowTitle("Edit")   
        Dialog.show()
        
         
 # --------------------------------------------------------------- add file ----------------------------------------------              
    def add_file(self):
        global allow_files,files
        sel_file= QFileDialog.getOpenFileName(self,'Open file', '',"""
                                                         Png files (*.png);;
                                                         Jpg files (*.jpg);;
                                                        
                                                         Bmp files (*.bmp);;
                                                         GIF files (*.gif);;
                                                         """)
        if sel_file[0]=="":
            print(" You doesn't have seleted any file .")
        else:

            keyss=allow_files.keys()
            valuess=allow_files.values()
            file_name=os.path.basename(sel_file[0]).lower()
            for i in list(keyss):
                
                if file_name.endswith(i):
                    item = QtWidgets.QListWidgetItem()    
                    icon = QtGui.QIcon() 
                    icon.addPixmap(QtGui.QPixmap(str(sel_file[0])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item.setIcon(icon)
                    # brush=QtGui.QBrush(QtGui.QColor(allow_files.get(i)[0],allow_files.get(i)[1],allow_files.get(i)[2]))
                    # brush.setStyle(QtCore.Qt.Dense6Pattern)
                    # item.setBackground(brush)
                    name=str(os.path.basename(sel_file[0]))[0:file_name.find(".")]
                    item.setText(name)
                    #item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.ui.listWidget.addItem(item)
                    new_item={str(os.path.basename(sel_file[0])[0:(os.path.basename(sel_file[0])).find(".")]):sel_file[0]}
                    files.update(new_item)
                    self.ui.pushButton_6.setEnabled(True)
                    self.ui.pushButton_7.setEnabled(True)
# =================================================== add folder ==============================================================        
    def add_folder(self):
        global allow_files,files

        
        sel_fol= QFileDialog.getExistingDirectory(self, 'Select Folder', '')
        if sel_fol=="":
            print("You doesn't have selcted any folder.")
        else:
            list_file=os.listdir(sel_fol)
            nu=(100/len(list_file))
            hj=(100/len(list_file))
            for i in list_file :
                
                self.ui.progressBar.setValue(nu)
              
              
                if nu==100:
                    self.ui.progressBar.setValue(0)
                    
                nu=hj+nu
                if i==list_file[-2]:
                    nu=100

                
                fullname=(f"{sel_fol}/{i}")

                item = QtWidgets.QListWidgetItem()   
           
                icon = QtGui.QIcon() 

            
                keyss=allow_files.keys()
            
                valuess=allow_files.values()
              
                file_name=i.lower()
             
                for j in list(keyss):
                    
                    
                    
                   
                    if file_name.endswith(j):
                        
                        icon.addPixmap(QtGui.QPixmap(str(fullname)),QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        item.setIcon(icon)
                    
                        # brush=QtGui.QBrush(QtGui.QColor(allow_files.get(j)[0],allow_files.get(j)[1],allow_files.get(j)[2]))
                        
                        # brush.setStyle(QtCore.Qt.Dense6Pattern)
                       
                        # item.setBackground(brush)
                        name=i[0:i.find(".")]
                        item.setText(name)
                       #item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                        self.ui.listWidget.addItem(item)
                        new_item={name:fullname}
                        files.update(new_item)
                        self.ui.pushButton_6.setEnabled(True)
                        self.ui.pushButton_7.setEnabled(True)
                       
                        
                        
                    else:
                        pass    
                      
                      
 
        # icon.addPixmap(QtGui.QPixmap("../../../../Pictures/jj.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # item.setIcon(icon)
# ==================================================== select all =============================================================
    def select_all(self):
        try:
            self.ui.listWidget.setFocus()
            g.hotkey("ctrl","a")  
        except:
            pass   
# ==================================================== remove all ==========================================================
    def remove_all(self):
        global files
        
        try:
            self.ui.listWidget.clear()  
            files.clear()
            self.ui.label_3.setPixmap(QtGui.QPixmap("no_image.png"))
            self.ui.lineEdit_2.setText("")
            self.ui.lineEdit_3.setText("")
            self.ui.lineEdit_4.setText("")
            self.ui.lineEdit_5.setText("")
            self.ui.lineEdit_6.setText("")
            self.ui.lineEdit_7.setText("")
            self.ui.pushButton_5.setEnabled(False)
            self.ui.comboBox.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
        except:
            pass 
# ===================================================== current loc ==========================================================
    def current_loc(self):
        global cur_fil
        self.ui.lineEdit_2.setText(os.getcwd())
# ====================================================== browse ===========================================================
    def browse(self):
        sel_fol= QFileDialog.getExistingDirectory(self, 'Select Folder', '')
        if sel_fol=="":
            pass
        else:
            self.ui.lineEdit_2.setText(sel_fol+"/")         
# ====================================================== click on item ============================================================        
    def list_item_click(self):
        global files,cur_fil

        click_=[]
        np = self.ui.listWidget.selectedItems()
        for t in np:
            click_.append(t.text())
            
       
        if len(click_)>1:
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.comboBox.setEnabled(True)
            
        elif len(click_)==0:
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.comboBox.setEnabled(False)
            self.ui.lineEdit_5.setText("")
            self.ui.lineEdit_6.setText("")
            self.ui.lineEdit_4.setText("")
            self.ui.lineEdit_3.setText("")
            self.ui.lineEdit_7.setText("")
            self.ui.label_3.setPixmap(QtGui.QPixmap("no_image.png"))
            
            
        elif len(click_)==1:
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.comboBox.setEnabled(True)
         
                
            item=click_[0]
    
            names=list(files.keys())
      
            folders=list(files.values())

            for i in names:
            
                if i==item:
                    imm = Image.open(files.get(i))
                    
                    folder_name,format_img =os.path.splitext(str(files.get(i)))
                    
                    im=QtGui.QPixmap(str(files.get(i)))
             
                    self.ui.lineEdit_6.setText(folder_name)
              
                    self.ui.lineEdit_5.setText(str(f"{round(os.path.getsize(files.get(i))/1024, 2)} KB"))
           
                    self.ui.lineEdit_4.setText(format_img)
            
                    self.ui.lineEdit_7.setText(f"{imm.size[0]} x {imm.size[1]}")
                    cur_fil=str(files.get(i)).replace(os.path.basename(files.get(i)),"")
                
                    self.ui.label_3.setPixmap(im)         
                else:
                    pass
          
            self.ui.lineEdit_3.setText(item)
        # ================================================================================
        
    def convert(self):
 
        list_files = []
        sel_item =  self.ui.listWidget.selectedItems()
        list_files.clear()
        for i in sel_item:
            list_files.append(i.text())
        print(list_files)
        
        ao = list(files.keys())
        print(ao)
        # if len(list_files)>1:
        for j in list_files:
            if j in ao:
                out_fol = self.ui.lineEdit_2.text()
                out_for = self.ui.comboBox.currentText()
                
                if out_fol=="":
                    out_fol = files.get(j).replace(j + files.get(j)[files.get(j).find("."):],"")
                print(out_fol)
                print(out_for)
                print(files.get(j))
                img = Image.open(files.get(j))
                print("g")
                img.save(f"{out_fol}\{j}.{out_for}")
            else:
                print("no")

# ===============================================================================================================================          

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())