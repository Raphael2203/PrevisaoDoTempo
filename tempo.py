import requests
import tkinter as tk
from tkinter import messagebox

#Função para obter previsão do tempo
def get_weather(city):
    api_key = "8e1170e614ed46be621069b82aaf42f6"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        wind = data.get("wind", {})
        clouds = data.get("clouds", {}).get('all', 'N/A')

        temperature = main.get("temp", "N/A")
        humidity = main.get("humidity", "N/A")
        pressure = main.get("pressure", "N/A")
        wind_speed = wind.get("speed", "N/A")
        description = weather.get("description", "N/A")

        weather_info = (f"Temperature: {temperature}ºC\n"
                        f"Humidity: {humidity}%\n"
                        f"Pressure: {[pressure]}hPa\n"
                        f"Wind Speed: {wind_speed}m/s\n"
                        f"Cloudiness: {clouds}%\n"
                        f"Description: {description.capitalize()}"
                        )
    else:
        weather_info = "City Not Found"

    return weather_info

#Função para exibir previsão do tempo
def show_weather():
    city = city_entry.get()
    if city: #Verifica se o nome da cidade foi inserido
        weather_info = get_weather(city)
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Input Error", "Please enter a city name")

#Cria a interface gráfica
app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack()

app.mainloop()