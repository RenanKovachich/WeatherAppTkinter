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

        hello_msg = tk.Label(weather_window, text="Hello!", font=('Arial', 32, "bold"), bg='#0B2447', fg='white')
        hello_msg.place(x=21, y=30)

        check_weather = tk.Label(weather_window, text="Check weather location", font=('Arial', 12), bg='#0B2447',
                                 fg='#206BD4')
        check_weather.place(x=21, y=73)

        city_name = tk.Label(weather_window, text=f"{CITY}", font=('Arial', 22, "bold"), bg='#0B2447', fg='white')
        city_name.place(x=139, y=140)

        temperature_label = tk.Label(weather_window, text=f'{round(temperature - 273.15)} ', font=("Arial", 72),
                                     bg='#0B2447', fg='white')
        temperature_label.place(x=128, y=180)

        celsius_label = tk.Label(weather_window, text='ºC', font=('Arial', 12), bg='#0B2447', fg='white')
        celsius_label.place(x=252, y=200)

        description = tk.Label(weather_window, text=f'{report[0]["description"]}', font=("Arial", 14), bg='#0B2447',
                               fg='white')
        description.place(x=125, y=298)

        temperature_sentence = tk.Label(weather_window, text="Temperature:", font=("Arial", 20, "bold"), bg='#164B94',
                                        fg='white')
        temperature_sentence.place(x=38, y=462)

        temperature_number = tk.Label(weather_window, text=f"{round(temperature-273.15)}ºC", font=("Arial", 20, "bold"),
                                      bg='#164B94', fg='white')
        temperature_number.place(x=259, y=464)

        humidity_sentence = tk.Label(weather_window, text="Humidity:", font=("Arial", 20, "bold"), bg='#164B94',
                                     fg='white')
        humidity_sentence.place(x=38, y=520)

        humidity_number = tk.Label(weather_window, text=f"{humidity}%", font=("Arial", 20, "bold"), bg='#164B94',
                                   fg='white')
        humidity_number.place(x=259, y=522)

        pressure_sentence = tk.Label(weather_window, text="Pressure:", font=("Arial", 20, "bold"), bg='#164B94',
                                     fg='white')
        pressure_sentence.place(x=38, y=578)

        pressure_number = tk.Label(weather_window, text=f"{pressure/1000} KPA", font=("Arial", 20, "bold"),
                                   bg='#164B94', fg='white')
        pressure_number.place(x=232, y=580)

        def close_window():
            weather_window.destroy()

        close_button = tk.Button(weather_window, text="Close", bg='#081A33', fg='white', font=('Arial', 32),
                                 command=close_window)
        close_button.config(border=0, bd=0, highlightthickness=0, relief='flat')
        close_button.configure(highlightbackground='#081A33', highlightcolor='#081A33')

        close_button.place(x=128, y=752)

    else:
        print("Error in the HTTP request")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Weather App")
    window.geometry("390x844")
    window.config(bg='#0B2447')

    city_label = tk.Label(window, text="City name: ", bg='#0B2447', fg='white', font=('Arial', 32, "bold"))
    city_label.place(x=79, y=133)

    city_entry = tk.Entry(window, bg='#0B2447', fg='white', font=('Arial', 22, "bold"))
    city_entry.place(x=35, y=336)

    get_weather_button = tk.Button(window, text="Get Weather", bg='#0B2447', fg='white', command=gerenateWeather,
                                   font=('Arial', 28, "bold"))
    get_weather_button.place(x=71, y=574)

    window.mainloop()
