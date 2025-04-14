# this is a very simple way to convert fahrenheit to celsius. 

# example user enter the fahrenheit 124F, which is used mostly in america or in some other countries 
# from 32F cooling point to 212F hot point

# then if we want to convert into celsius, whis is used in mostly pakistan or in other countries. 
# formula: c = (f-32) * 5.0 / 9.0 i.e...

# 124F - 32F =  answer is 92 then multiply 
# 92 * 5.0 = 460 / 9.0 so answer will be of celsius = 51.11C

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5.0 / 9.0

print(f"Temperature: {fahrenheit}F = {celsius:.2f}C")


# if you want to convert celsius into fahrenheit then change the formula 
# F=(C × 9.0 /5.0)+32