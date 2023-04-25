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
        weather_window.geometry("390x844")
        weather_window.config(bg='#0B2447')

        hello_msg = tk.Label(weather_window, text="Hello!", font=('Arial', 32), bg='#0B2447', fg='white')
        hello_msg.place(x=10, y=10)

        check_weather = tk.Label(weather_window, text="Check weather location", font=('Arial', 12), bg='#0B2447',
                                 fg='white')
        check_weather.place(x=10, y=55)

        temperature_label = tk.Label(weather_window, text=f'Weather: {round(temperature - 273.15, 2)} ºC', font=("Arial"
                                                                                                                 , 20))
        temperature_label.pack()

        humidity_label = tk.Label(weather_window, text=f'Humidity: {humidity}%', font=("Arial", 20))
        humidity_label.pack()

        pressure_label = tk.Label(weather_window, text=f'Pressure: {pressure/1000} KPa', font=("Arial", 20))
        pressure_label.pack()

        weather_report_label = tk.Label(weather_window, text=f'Dresciption: {report[0]["description"]}', font=("Arial",
                                                                                                               20))
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
    window.geometry("220x200+10+20")

    city_label = tk.Label(window, text="City name: ")
    city_label.place(x=10, y=50)

    city_entry = tk.Entry(window)
    city_entry.place(x=80, y=51)

    get_weather_button = tk.Button(window, text="Get Weather", command=gerenateWeather)
    get_weather_button.place(x=75, y=100)

    window.mainloop()
