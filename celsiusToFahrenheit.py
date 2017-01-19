def celsiusToFahrenheit(temp):
    if temp < -273.15:
        return
    else:
        return temp*1.8 + 32.0

temperatures=[10,-20,-289,100]
temperatures = [celsiusToFahrenheit(i) for i in temperatures]
with open('testePy.txt','w') as file:
    for temp in temperatures:
        if not temp is None:
            file.write(str(temp) + '\n')
#print(temperatures)
