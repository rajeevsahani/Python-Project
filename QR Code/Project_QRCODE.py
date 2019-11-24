
#pip install pyqrcode
#pip install pypng
import pyqrcode
web = pyqrcode.create('http://www.rtu.ac.in/RTU/')
web.png('web1.png',scale=10)
web.show()

