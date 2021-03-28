import sys
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pytube 

from pytube import YouTube 
def om():
    app = QApplication(sys.argv)
    win = QWidget()
    win2 = QWidget()
    dio = QMessageBox(win2)       
    previousprogress = 0    
    
    url = "https://www.desktopbackground.org/download/o/2011/05/01/196385_light-blue-gradient-blur-wallpaper-800x500-jpg_800x500_h.jpg"
    image = QImage()
    image.loadFromData(requests.get(url).content)
    
    
    def open():
        
        fname = QFileDialog.getExistingDirectory(win,'select a directory')
        fname = QDir.toNativeSeparators(fname)
        loc1.setText(str(fname))
            
           
    
    def progress(stream, chunk, bytes_remaining,previousprogress = 0):
        
        total_size = stream.filesize
        bytes_download = total_size - bytes_remaining
        
        liveprogress = (int)(bytes_download / total_size * 100)
        if liveprogress > previousprogress:
            previousprogress = liveprogress
            p.setValue(liveprogress)
            print(liveprogress)
        
            
            
            
        
        
    def down():
      try: 
            down_om = url.text()
            ranloc = loc1.text()  
            
            youtube = pytube.YouTube(down_om) 
            video = youtube.streams.first()  
            video.download(ranloc)
            
            yt = YouTube(url.text())
            yt.register_on_progress_callback(progress)
            yt.streams.filter(only_audio=True).first().download()
            
               
      except Exception:
            
            dio.setIcon(QMessageBox.Information)
            dio.setText("Warning")
            dio.setInformativeText("Please enter correct URL")
            dio.setWindowTitle("Warning")
            dio.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
            retval = dio.exec_()
            
           
                      
               
            
            
            
            
            
              
                    
            
          
    img = QLabel(win)
    img.setPixmap(QPixmap(image))
    img.show()
          
    p = QProgressBar(win)
    p.setGeometry(100,100,500,30)
    p.setFont(QFont("Arial",20))
    p.setStyleSheet("QProgressBar::chunk {background-color: skyblue;color : white}")
    p.setValue(0)
    p.move(110,380)   
       
    l1 = QLabel(win)
    l1.setText("URL")
    l1.move(50,70)
    l1.setFont(QFont("Arial",20))
    l1.setStyleSheet("QLabel {color : White}")
    
    l2 = QLabel(win)
    l2.setText("Location")
    l2.setFont(QFont('Arial',20))
    l2.setStyleSheet("QLabel {color : White}")
    l2.move(50,150)
    
    url = QLineEdit(win)
    url.setStyleSheet("QLineEdit {background-color : rgba(0,0,0,100); color :  White}")
    url.setGeometry(100,100,500,50)
    url.setFont(QFont("Arial",15))
    url.move(190,70)
    
    loc1 = QLineEdit(win)
    loc1.setStyleSheet("QLineEdit{background-color: rgba(0,0,0,100);color : White}")
    loc1.setGeometry(100,100,500,50)
    loc1.setFont(QFont("Arial",15))
    loc1.move(190,150)
    
    d = QPushButton(win)
    d.setText("Download")
    d.setFont(QFont("Arial",20))
    d.setGeometry(100,100,210,80)
    d.setStyleSheet("QPushButton {background-color : rgba(0,0,0,100);color : White}")
    d.move(110,280)
    d.clicked.connect(down)

    b = QPushButton(win)
    b.setText("Save")
    b.setFont(QFont("Arial",13))
    b.setStyleSheet("QPushButton {background-color : rgba(0,0,0,100); color: White }")
    b.setGeometry(100,100,90,50)
    b.move(700,150)
    b.clicked.connect(open)
    
    win.setFixedHeight(500)
    win.setFixedWidth(800)
    win.setWindowTitle("youtube downloader")
    win.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    om()      