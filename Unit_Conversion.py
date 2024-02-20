import tkinter as tk
from tkinter import ttk

def length_conversion():
    length_dict = {
        1: "Centimeter to Meter",
        2: "Meter to Centimeter",
        3: "Centimeter to INCH",
        4: "INCH to Centimeter",
        5: "Centimeter to KiloMetre",
        6: "KiloMetre to Centimeter",
        7: "Centimeter to FOOT",
        8: "FOOT to Centimeter",
        9: "Kilometre to Mile",
        10: "Mile to Kilometre",
        11: "Feet to Inches",
        12: "Sqft to Sqmtrs",
        13: "Sqft to Hectre",
        14: "Sqft to Acres"
    }
    
    def convert_length():
        try:
            value = float(length_entry.get())
            conversion = length_dict[length_choice.get()]
            if length_choice.get() == 1:
                result_label.config(text=f"{value} cm is equal to {value / 100} m.")
            elif length_choice.get() == 2:
                result_label.config(text=f"{value} m is equal to {value * 100} cm.")
            elif length_choice.get() == 3:
                result_label.config(text=f"{value} cm is equal to {value / 2.54} inch.")
            elif length_choice.get() == 4:
                result_label.config(text=f"{value} inch is equal to {value * 2.54} cm.")
            elif length_choice.get() == 5:
                result_label.config(text=f"{value} cm is equal to {value / 100000} km.")
            elif length_choice.get() == 6:
                result_label.config(text=f"{value} km is equal to {value * 100000} cm.")
            elif length_choice.get() == 7:
                result_label.config(text=f"{value} cm is equal to {value / 30.48} feet.")
            elif length_choice.get() == 8:
                result_label.config(text=f"{value} feet is equal to {value * 30.48} cm.")
            elif length_choice.get() == 9:
                result_label.config(text=f"{value} km is equal to {value / 1.609} mile")
            elif length_choice.get() == 10:
                result_label.config(text=f"{value} mile is equal to {value * 1.609} km")  
            elif length_choice.get() == 11:
                result_label.config(text=f"{value} feet is equal to {value * 12:.2f} inches.")
            elif length_choice.get() == 12:
                result_label.config(text=f"{value} sqft is equal to {value * 0.092903:.2f} sqm.")
            elif length_choice.get() == 13:
                result_label.config(text=f"{value} sqft is equal to {value * 0.0000092903:.2f} hectares.")
            elif length_choice.get() == 14:
                result_label.config(text=f"{value} sqft is equal to {value * 0.0000229568:.2f} acres.")
            else:
                result_label.config(text="Invalid input")
        except ValueError:
            result_label.config(text="Invalid input")
    
    length_window = tk.Toplevel(root)
    length_window.title("Length Conversion")
    
    ttk.Label(length_window, text="Enter value:").grid(row=0, column=0, padx=5, pady=5)
    length_entry = ttk.Entry(length_window, width=10)
    length_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(length_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    length_choice = tk.IntVar()
    for key, value in length_dict.items():
        ttk.Radiobutton(length_window, text=value, variable=length_choice, value=key).grid(row=key, column=1, padx=5, pady=5)
    
    convert_button = ttk.Button(length_window, text="Convert", command=convert_length)
    convert_button.grid(row=len(length_dict) + 1, column=1, padx=5, pady=5)
    
    result_label = ttk.Label(length_window, text="")
    result_label.grid(row=len(length_dict) + 2, columnspan=2, padx=5, pady=5)


def mass_conversion():
    mass_dict = {
        1: "Gram to Kilogram",
        2: "Kilogram to Gram",
        3: "Kilogram to Tonne",
        4: "Tonne to Kilogram",
        5: "Milligram to Kilogram",
        6: "Kilogram to Milligram",
        7: "Milligram to Gram",
        8: "Gram to Milligram",
        9: "kilogram to pound (lb)",
        10: "pound (lb) to Kilogram",
        11: "Micrograms to gram",
        12: "Micrograms to Kilogram"
    }
    
    def convert_mass():
        try:
            value = float(mass_entry.get())
            conversion = mass_dict[mass_choice.get()]
            if mass_choice.get() == 1:
                result_label.config(text=f"{value} g is equal to {value / 1000} kg")
            elif mass_choice.get() == 2:
                result_label.config(text=f"{value} kg is equal to {value * 1000} g")
            elif mass_choice.get() == 3:
                result_label.config(text=f"{value} kg is equal to {value / 1000} tonne")
            elif mass_choice.get() == 4:
                result_label.config(text=f"{value} tonne is equal to {value * 1000} kg")
            elif mass_choice.get() == 5:
                result_label.config(text=f"{value} mg is equal to {value / 1000000} kg")
            elif mass_choice.get() == 6:
                result_label.config(text=f"{value} kg is equal to {value * 1000000} mg")
            elif mass_choice.get() == 7:
                result_label.config(text=f"{value} mg is equal to {value / 1000} g")
            elif mass_choice.get() == 8:
                result_label.config(text=f"{value} g is equal to {value * 1000} mg")
            elif mass_choice.get() == 9:
                result_label.config(text=f"{value} kg is equal to {value * 2.20462} lb")
            elif mass_choice.get() == 10:
                result_label.config(text=f"{value} lb is equal to {value / 2.20462} kg")
            elif mass_choice.get() == 11:
                result_label.config(text=f"{value} μg is equal to {value / 1e+6} g")
            elif mass_choice.get() == 12:
                result_label.config(text=f"{value} μg is equal to {value / 1e+9} kg")
            else:
                result_label.config(text="Invalid input")
        except ValueError:
            result_label.config(text="Invalid input")
    
    mass_window = tk.Toplevel(root)
    mass_window.title("Mass Conversion")
    
    ttk.Label(mass_window, text="Enter value:").grid(row=0, column=0, padx=5, pady=5)
    mass_entry = ttk.Entry(mass_window, width=10)
    mass_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(mass_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    mass_choice = tk.IntVar()
    for key, value in mass_dict.items():
        ttk.Radiobutton(mass_window, text=value, variable=mass_choice, value=key).grid(row=key, column=1, padx=5, pady=5)
    
    convert_button = ttk.Button(mass_window, text="Convert", command=convert_mass)
    convert_button.grid(row=13, column=1, padx=5, pady=5)
    
    result_label = ttk.Label(mass_window, text="")
    result_label.grid(row=14, columnspan=2, padx=5, pady=5)

def temperature_conversion():
    Temp_dict = {
        1: "Celsius to Fahrenheit",
        2: "Celsius to Kelvin",
        3: "Fahrenheit to Celsius",
        4: "Fahrenheit to Kelvin",
        5: "Kelvin to Celsius",
        6: "Kelvin to Fahrenheit"
    }

    def convert_temperature():
        try:
            value = float(temperature_entry.get())
            conversion = Temp_dict[temperature_choice.get()]
            if temperature_choice.get() == 1:
                result_label.config(text=f"{value} °C is equal to {(value * 9/5) + 32} °F")
            elif temperature_choice.get() == 2:
                result_label.config(text=f"{value} °C is equal to {value + 273.15} K")
            elif temperature_choice.get() == 3:
                result_label.config(text=f"{value} °F is equal to {(value - 32) * 5/9} °C")
            elif temperature_choice.get() == 4:
                result_label.config(text=f"{value} °F is equal to {(value - 32) * 5/9 + 273.15} K")
            elif temperature_choice.get() == 5:
                result_label.config(text=f"{value} K is equal to {value - 273.15} °C")
            elif temperature_choice.get() == 6:
                result_label.config(text=f"{value} K is equal to {(value - 273.15) * 9/5 + 32} °F")
            else:
                result_label.config(text="Invalid input")
        except ValueError:
            result_label.config(text="Invalid input")

    temperature_window = tk.Toplevel(root)
    temperature_window.title("Temperature Conversion")

    ttk.Label(temperature_window, text="Enter value:").grid(row=0, column=0, padx=5, pady=5)
    temperature_entry = ttk.Entry(temperature_window, width=10)
    temperature_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(temperature_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    temperature_choice = tk.IntVar()
    for key, value in Temp_dict.items():
        ttk.Radiobutton(temperature_window, text=value, variable=temperature_choice, value=key).grid(row=key, column=1, padx=5, pady=5)

    convert_button = ttk.Button(temperature_window, text="Convert", command=convert_temperature)
    convert_button.grid(row=7, column=1, padx=5, pady=5)

    result_label = ttk.Label(temperature_window, text="")
    result_label.grid(row=8, columnspan=2, padx=5, pady=5)

def time_conversion():
    Time_dict = {
        1: "Second to Minute",
        2: "Minute to Second",
        3: "Second to Hour",
        4: "Minute to Hour",
        5: "Hour to Minute",
        6: "Day to Hour",
        7: "Hour to Day"
    }

    def convert_time():
        try:
            value = float(time_entry.get())
            conversion = Time_dict[time_choice.get()]
            if time_choice.get() == 1:
                result_label.config(text=f"{value} S is equal to {value / 60} M")
            elif time_choice.get() == 2:
                result_label.config(text=f"{value} M is equal to {value * 60} S")
            elif time_choice.get() == 3:
                result_label.config(text=f"{value} S is equal to {value / 3600} H")
            elif time_choice.get() == 4:
                result_label.config(text=f"{value} M is equal to {value / 60} H")
            elif time_choice.get() == 5:
                result_label.config(text=f"{value} H is equal to {value * 60} M")
            elif time_choice.get() == 6:
                result_label.config(text=f"{value} day is equal to {value * 24} H")
            elif time_choice.get() == 7:
                result_label.config(text=f"{value} H is equal to {value / 24} day")
            else:
                result_label.config(text="Invalid input")
        except ValueError:
            result_label.config(text="Invalid input")

    time_window = tk.Toplevel(root)
    time_window.title("Time Conversion")

    ttk.Label(time_window, text="Enter value:").grid(row=0, column=0, padx=5, pady=5)
    time_entry = ttk.Entry(time_window, width=10)
    time_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(time_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    time_choice = tk.IntVar()
    for key, value in Time_dict.items():
        ttk.Radiobutton(time_window, text=value, variable=time_choice, value=key).grid(row=key, column=1, padx=5, pady=5)

    convert_button = ttk.Button(time_window, text="Convert", command=convert_time)
    convert_button.grid(row=8, column=1, padx=5, pady=5)

    result_label = ttk.Label(time_window, text="")
    result_label.grid(row=9, columnspan=2, padx=5, pady=5)

def speed_conversion():
    Spead_dict = {
        1: "Mile per hour to kilometer per hour",
        2: "Kilometer per hour to Mile per hour",
        3: "Mile per hour to Meter per Second",
        4: "Meter per Second to Mile per hour",
        5: "Kilometer per hour to Meter per Second",
        6: "Meter per Second to Kilometer per hour"
    }

    def convert_speed():
        try:
            value = float(speed_entry.get())
            conversion = Spead_dict[speed_choice.get()]
            if speed_choice.get() == 1:
                result_label.config(text=f"{value} Ml is equal to {value * 1.609} Km")
            elif speed_choice.get() == 2:
                result_label.config(text=f"{value} Km is equal to {value / 1.609} Ml")
            elif speed_choice.get() == 3:
                result_label.config(text=f"{value} Ml is equal to {value / 2.237} M")
            elif speed_choice.get() == 4:
                result_label.config(text=f"{value} M is equal to {value * 2.237} Ml")
            elif speed_choice.get() == 5:
                result_label.config(text=f"{value} Km is equal to {value / 3.6} M")
            elif speed_choice.get() == 6:
                result_label.config(text=f"{value} M is equal to {value * 3.6} Km")
            else:
                result_label.config(text="Invalid input")
        except ValueError:
            result_label.config(text="Invalid input")

    speed_window = tk.Toplevel(root)
    speed_window.title("Speed Conversion")

    ttk.Label(speed_window, text="Enter value:").grid(row=0, column=0, padx=5, pady=5)
    speed_entry = ttk.Entry(speed_window, width=10)
    speed_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(speed_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    speed_choice = tk.IntVar()
    for key, value in Spead_dict.items():
        ttk.Radiobutton(speed_window, text=value, variable=speed_choice, value=key).grid(row=key, column=1, padx=5, pady=5)

    convert_button = ttk.Button(speed_window, text="Convert", command=convert_speed)
    convert_button.grid(row=7, column=1, padx=5, pady=5)

    result_label = ttk.Label(speed_window, text="")
    result_label.grid(row=8, columnspan=2, padx=5, pady=5)


def energy_conversion():
    Energy_dict = {
        1: "Joule to Kilojoule",
        2: "Kilojoule to Joule",
        3: "Joule to Kilocalorie",
        4: "Kilocalorie to Joule",
        5: "Kilojoule to Kilocalorie",
        6: "Kilocalorie to Kilojoule"
    }
    def convert_energy():
        try:
            value = float(energy_entry.get())
            conversion = Energy_dict[energy_choice.get()]


            if energy_choice.get() == 1:
                result_label.config(text=f"{value} J is equal to {value / 1000} Kj")
            elif energy_choice.get() == 2:
                result_label.config(text=f"{value} Kj is equal to {value * 1000} J")
            elif energy_choice.get() == 3:
                result_label.config(text=f"{value} J is equal to {value / 4184} Kc")
            elif energy_choice.get() == 4:
                result_label.config(text=f"{value} Kc is equal to {value * 4184} J")
            elif energy_choice.get() == 5:
                result_label.config(text=f"{value} Kj is equal to {value / 4.184} Kc")
            elif energy_choice.get() == 6:
                result_label.config(text=f"{value} Kc is equal to {value * 4.184} Kj")
            else:
                result_label.config(text="Sorry, Please type correct number from 1 to 6.")
        except ValueError:
            result_label.config(text="Invalid input")

    energy_window = tk.Toplevel(root)
    energy_window.title("Energy Conversion")

    ttk.Label(energy_window, text="Enter value:").grid(row=0, column=0, padx=5, pady=5)
    energy_entry = ttk.Entry(energy_window, width=10)
    energy_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(energy_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    energy_choice = tk.IntVar()
    for key, value in Energy_dict.items():
        ttk.Radiobutton(energy_window, text=value, variable=energy_choice, value=key).grid(row=key, column=1, padx=5, pady=5)

    convert_button = ttk.Button(energy_window, text="Convert", command=convert_energy)
    convert_button.grid(row=7, column=1, padx=5, pady=5)

    result_label = ttk.Label(energy_window, text="")
    result_label.grid(row=8, columnspan=2, padx=5, pady=5)

    
def pressure_conversion():
    Pressure_dict = {
        1: "Bar to Pascal",
        2: "Bar to Standard atmosphere",
        3: "Pascal to Bar",
        4: "Pascal to Standard atmosphere",
        5: "Standard atmosphere to Pascal",
        6: "Standard atmosphere to Bar"
    }
    def convert_pressure():
        try:
            value = float(pressure_entry.get())
            conversion = Pressure_dict[pressure_choice.get()]

            if pressure_choice.get() == 1:
                result_label.config(text=f"{value} Bar is equal to {value * 100000} P")
            elif pressure_choice.get() == 2:
                result_label.config(text=f"{value} Bar is equal to {value / 1.013} atm")
            elif pressure_choice.get() == 3:
                result_label.config(text=f"{value} P is equal to {value / 100000} Bar")
            elif pressure_choice.get() == 4:
                result_label.config(text=f"{value} P is equal to {value / 101300} atm")
            elif pressure_choice.get() == 5:
                result_label.config(text=f"{value} atm is equal to {value * 101300} P")
            elif pressure_choice.get() == 6:
                result_label.config(text=f"{value} atm is equal to {value * 1.013} Bar")
            else:
                result_label.config(text="Sorry, Please type correct number from 1 to 6.")
        except ValueError:
            result_label.config(text="Invalid input")

    pressure_window=tk.Toplevel(root)
    pressure_window.title("Pressure Conversion")

    ttk.Label(pressure_window, text="Enter value:").grid(row=0,column=0, padx=5, pady=5)
    pressure_entry = ttk.Entry(pressure_window,width=10)
    pressure_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(pressure_window, text="Choose conversion:").grid(row=1, column=0, padx=5, pady=5)
    pressure_choice=tk.IntVar()
    for key, value in Pressure_dict.items():
        ttk.Radiobutton(pressure_window, text=value, variable=pressure_choice, value=key).grid(row=key, column=1, padx=5, pady=5)

    convert_button=ttk.Button(pressure_window, text="Convert", command=convert_pressure)
    convert_button.grid(row=7, column=1, padx=5, pady=5)

    result_label=ttk.Label(pressure_window, text="")
    result_label.grid(row=8, columnspan=2,padx=5, pady=5)
root = tk.Tk()
root.title("Unit Converter")

unit_frame = ttk.LabelFrame(root, text="Choose Conversion Type")
unit_frame.grid(row=0, column=0, padx=10, pady=5)

unit_change = {
    1: "Length",
    2: "Mass",
    3: "Temperature",
    4: "Time",
    5: "Speed",
    6: "Energy",
    7: "Pressure"
}


for i, (key, value) in enumerate(unit_change.items(), start=1):
    if key == 1:
        ttk.Button(unit_frame, text=value, command=length_conversion).grid(row=i, column=0, padx=5, pady=5)
    elif key == 2:
        ttk.Button(unit_frame, text=value, command=mass_conversion).grid(row=i, column=0, padx=5, pady=5)
    elif key == 3:
        ttk.Button(unit_frame, text=value, command=temperature_conversion).grid(row=i, column=0, padx=5, pady=5)
    elif key == 4:
        ttk.Button(unit_frame, text=value, command=time_conversion).grid(row=i, column=0, padx=5, pady=5)
    elif key == 5:
        ttk.Button(unit_frame, text=value, command=speed_conversion).grid(row=i, column=0, padx=5, pady=5)
    elif key == 6:
        ttk.Button(unit_frame, text=value, command=energy_conversion).grid(row=i, column=0, padx=5, pady=5)
    elif key == 7:
        ttk.Button(unit_frame, text=value, command=pressure_conversion).grid(row=i, column=0, padx=5, pady=5)

root.mainloop()
