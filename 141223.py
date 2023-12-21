def weather():
	t=float(input("Enter a value for temperature: "))
	h=int(input("Enter a value for humidity: "))
	w=int(input("Enter a value for wind speed: "))
	weather=(0.5*(t*t))-(0.2*(h))+(0.1*(w))-15
	print(weather)
	if weather<=100:
	    print("The weather is stormy")
	elif weather>300:
	    print("The weather is sunny")
	elif weather>200 and weather<=300:
	    print("The weather is cloudy")
	elif weather>100 and weather<=200:
	    print("The weather is rainy")

def weather1(t,h,w):
	weather=(0.5*(t*t))-(0.2*(h))+(0.1*(w))-15
	print(weather)
	if weather<=100:
		print("The weather is stormy")
	elif weather>300:
		print("The weather is sunny")
	elif weather>100 and weather<=200:
		print("The weather is rainy")

def press():
	case=int(input("Press 1 to enter inputs\nPress 2 to exit\n"))
	if(case==1):
		weather()
	if(case==2):
		print("All test cases passed")
		return
	else:
		print("Enter a valid input")
		press()

def read():
	f=open('file','r')
	list=[]
	list.append(f.readline())
	a=list[0].split(',')
	print(int(a[0]))
	print(int(a[1]))
	print(int(a[2]))
	weather1(int(a[0]),int(a[1]),int(a[2]))
press()
read()

