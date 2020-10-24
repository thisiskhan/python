name = input("What is your name? ")
temp = int(input( name + " what is the terprature out there? "))

if temp >= 30:
    print(name + " It's a hot day today")
elif temp <10 and temp > 1:
    print(name + " It's very cold out there")
elif temp <0 and temp > -10:
    print(name + " It's very cold out there . hope you are safe")    
else : print("Have a good day")    