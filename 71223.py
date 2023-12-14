t=float(input("Enter a value for temperature: "))
h=int(input("Enter a value for humidity: "))
w=int(input("Enter a value for wind speed: "))
weather=(0.5*(t**2))-(0.2*(h))+(0.1*(w))-15
print(weather)
if weather<=100:
    print("The weather is stormy")
elif weather>300:
    print("The weather is sunny")
elif weather>200 and weather<=300:
    print("The weather is cloudy")
elif weather>100 and weather<=200:
    print("The weather is rainy")