import sys
import requests 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_l=QLabel("Enter City name: ",self)
        self.city_in=QLineEdit(self)
        self.weather_b=QPushButton("Get Weather",self)
        self.temp_l=QLabel(self)
        self.emoji_l=QLabel(self)
        self.descrp_l=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox=QVBoxLayout()

        vbox.addWidget(self.city_l)
        vbox.addWidget(self.city_in)
        vbox.addWidget(self.weather_b)
        vbox.addWidget(self.temp_l)
        vbox.addWidget(self.emoji_l)
        vbox.addWidget(self.descrp_l)
        
        self.setLayout(vbox)
        self.city_l.setAlignment(Qt.AlignCenter)
        self.city_in.setAlignment(Qt.AlignCenter)
        self.temp_l.setAlignment(Qt.AlignCenter)
        self.emoji_l.setAlignment(Qt.AlignCenter)
        self.descrp_l.setAlignment(Qt.AlignCenter)

        self.city_l.setObjectName("city_l")
        self.city_in.setObjectName("city_in")
        self.weather_b.setObjectName("weather_b")
        self.temp_l.setObjectName("temp_l")
        self.emoji_l.setObjectName("emoji_l")
        self.descrp_l.setObjectName("descrp_l")

        self.setStyleSheet("""
                        QLabel,QPushButton{
                           font-family:calibri;
                           }
                           QLabel#city_l{
                           font-size:40px;
                           font-style: italic;
                           }
                           QLineEdit#city_in{
                           font-size:40px;
                           }
                           QPushButton#weather_b{
                           font-size:30px;
                           font-weight:bold;
                           }
                           QLabel#temp_l{
                           font-size:70px;
                           }
                           QLabel#emoji_l{
                           font-size:100px;
                           font-family:'segoe UI emoji';
                           }
                           QLabel#descrp_l{
                           font-size:60px;
                           }
                           """)
        self.weather_b.clicked.connect(self.get_weather)

    def get_weather(self):
        apikey="bd76c79bc532cd965afade878cba3d21"
        city=self.city_in.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            if data["cod"]==200:
                self.disp_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match  response.status_code:                            #print(response.status_code)
                case 400:
                    self.disp_error("Bad request:\nPlease check your input")
                case 401:
                    self.disp_error("Bad request:\nPlease check your input")
                case 402:
                    self.disp_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.disp_error("Forbidden:\nAccess is denied")
                case 404:
                    self.disp_error("Not found:\nCity not found")
                case 500:
                    self.disp_error("Internal Server error:\nPlease try again later")
                case 502:
                    self.disp_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.disp_error("Service Unavailable:\nServer is Down")
                case 504:
                    self.disp_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.disp_error(f"HTTP error occured:\n{http_error}")
                
        except requests.exceptions.ConnectionError:
            self.disp_error("Connection error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.disp_error("Timeout error:\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.disp_error("Too many Redirects:\ncheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.disp_error(f"Request Error:\n{req_error}")

    def disp_error(self,msg):
        self.temp_l.setStyleSheet("font-size:30px;")
        self.temp_l.setText(msg)
        self.emoji_l.clear()
        self.descrp_l.clear()

    def disp_weather(self,data):
        self.temp_l.setStyleSheet("font-size:70px;")
        temp_k=data["main"]["temp"]
        temp_c=temp_k-273.15
        temp_f=(temp_k*9/5)-459.67
        weather_id=data["weather"][0]["id"]
        weath_desc=data["weather"][0]["description"]
        
        self.temp_l.setText(f"{temp_f:.0f}°F")
        self.emoji_l.setText(self.get_emoji(weather_id))
        self.descrp_l.setText(weath_desc)

    @staticmethod
    def get_emoji(weather_id):
        if 200<=weather_id<=232:
            return "⛈️"
        elif 300<=weather_id<=321:
            return "☁️"
        elif 500<=weather_id<=531:
            return "🌧️"
        elif 600<=weather_id<=622:
            return "🌨️❄️"
        elif 701<=weather_id<=741:
            return "🌫️"
        elif weather_id==762:
            return "🌋"
        elif weather_id==771:
            return "💨"
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "☀️"
        elif 801<=weather_id<=804:
            return "☁️☁️"
        else:
            return ""



if __name__=="__main__":
    app=QApplication(sys.argv)
    wa=WeatherApp()
    wa.show()
    sys.exit(app.exec_()) 

