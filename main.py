import requests
import tkinter as tk


def gerenateWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city_entry.get()
    CITY = CITY.capitalize()
    api_key = '53596b36083cd780e19b66efd6b45c86'

    URL = BASE_URL + "q=" + CITY + "&appid=" + api_key

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']

        window.destroy()

        weather_window = tk.Tk()
        weather_window.title(f"{CITY} Weather")
        weather_window.config(padx=20, pady=100)

        temperature_label = tk.Label(weather_window, text=f'Weather: {round(temperature - 273.15, 2)} ºC')
        temperature_label.pack()

        humidity_label = tk.Label(weather_window, text=f'Humidity: {humidity}%')
        humidity_label.pack()

        pressure_label = tk.Label(weather_window, text=f'Pressure: {pressure/1000} KPa')
        pressure_label.pack()

        weather_report_label = tk.Label(weather_window, text=f'Dresciption: {report[0]["description"]}')
        weather_report_label.pack()

        print(f"{CITY:-^30}")
        print(f"Temperature: {round(temperature - 273.15, 2)} ºC")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure / 1000} KPa")
        print(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in the HTTP request")


if __name__ == "__main__":
    # window = Tk()
    # window.title("Weather App")
    # window.config(padx=10, pady=100, bg='orange')

    # label
    # website_label = Label(text="Cidade:", bg='orange')
    # website_label.grid(row=2, column=0)

    # Entries
    # website_entry = Entry(width=35)
    # website_entry.grid(row=2, column=1, columnspan=2)
    # website_entry.focus()
    # add_button = Button(text="Condições Climáticas", width=30, height=1, command=gerenateWeather)
    # add_button.grid(row=4, column=1, columnspan=2)
    # add_button.place(x=25, y=50)

    # window.mainloop()
    window = tk.Tk()
    window.title("Weather App")
    window.config(padx=10, pady=50)

    city_label = tk.Label(window, text="Nome da cidade: ")
    city_label.pack()

    city_entry = tk.Entry(window)
    city_entry.pack()

    get_weather_button = tk.Button(window, text="Get Weather", command=gerenateWeather)
    get_weather_button.pack()

    window.mainloop()
