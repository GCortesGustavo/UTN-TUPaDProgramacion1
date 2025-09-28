def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")

main()