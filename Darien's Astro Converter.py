#THE ASTRO CONVERTER
#welcome and varible setting
print("Welcome to Darien's Astronomical Unit Converter")
Reminder = raw_input("This is only for converting Astronomical units! Do you fucking understand?! say ok(k): ")
ok=("k")

category = raw_input("What catagory will you be doing conversions in? We support Astro to Astro (Astro->Astro) and Astro to Metric (Astro->Metric): ")

if category == ("Astro->Astro"): 
   unit1=raw_input("What are you converting from?: ")
   unit2=raw_input("What are you converting to?: ")
   num1=float(raw_input("Enter your value: "))
   
   
if category == ("Astro->Metric"): 
   unit1=raw_input("What are you converting from?: ")
   unit2=raw_input("What are you converting to?: ")
   num1=float(raw_input("Enter your value: "))


if unit1 == "AU" and unit2 == "lyrs":
    ans = float(num1)/63241.077
    print ans
if unit1 == "lyrs" and unit2 == "AU":
    ans = float(num1)*63241.077
    print ans
if unit1 == "AU" and unit2 == "Parsecs":
    ans = float(num1)/206264.806
    print ans
if unit1 == "Parsecs" and unit2 == "AU":
    ans = float(num1)*206264.806
    print ans
if unit1 == "lyrs" and unit2 == "Parsecs":
    ans = float(num1)/3.262
    print ans
if unit1 == "Parsecs" and unit2 == "lyrs":
    ans = float(num1)*3.262
    print ans
if unit1 == "AU" and unit2 == "gigameters":
    ans = float(num1)*149.598
    print ans
if unit1 == "Gigameters" and unit2 == "AU":
    ans = float(num1)/63241.077
    print ans
if unit1 == "Gigameters" and unit2 == "lyrs":
    ans = float(num1)/9.461e+6
    print ans
if unit1 == "lyrs" and unit2 == "Gigameters":
    ans = float(num1)*9.461e+6
    print ans
if unit1 == "Gigameters" and unit2 == "Parsecs":
    ans = float(num1)/3.086e+7
    print ans
if unit1 == "Parsecs" and unit2 == "Gigameters":
    ans = float(num1)*3.086e+7
    print ans    
if unit1 == "AU" and unit2 == "Kilo-parsecs":
    ans = float(num1)/2.063e+8
    print ans
if unit1 == "Kilo-parsecs" and unit2 == "AU":
    ans = float(num1)*2.063e+8
    print ans
if unit1 == "Kilo-Parsecs" and unit2 == "Gigameters":
    ans = float(num1)*3.086e+10
    print ans
if unit1 == "Gigameters" and unit2 == "Kilo-parsecs":
    ans = float(num1)/3.086e+10
    print ans
if unit1 == "Kilo-parsecs" and unit2 == "lyrs":
    ans = float(num1)*3261.564
    print ans
if unit1 == "lyrs" and unit2 == "Kilo-parsecs":
    ans = float(num1)/3261.564
    print ans
if unit1 == "kilo-parsecs" and unit2 == "Parsecs":
    ans = float(num1)*1000
    print ans
if unit1 == "Parsecs" and unit2 == "Kilo-Parsecs":
    ans = float(num1)/1000
    print ans
if unit1 == "Gigameters" and unit2 == "Mega-parsecs":
    ans = float(num1)/9.461e+6
    print ans
if unit1 == "Mega-parsecs" and unit2 == "Gigameters":
    ans = float(num1)*9.461e+6
    print ans
if unit1 == "Mega-parsecs" and unit2 == "Parsecs":
    ans = float(num1)/3.086e+7
    print ans
if unit1 == "Parsecs" and unit2 == "Mega-parsecs":
    ans = float(num1)/1e+6
    print ans
if unit1 == "Mega-Parsecs" and unit2 == "Parsecs":
    ans = float(num1)*1e+6
    print ans
if unit1 == "Kilo-parsecs" and unit2 == "Mega-parsecs":
    ans = float(num1)/1000
    print ans
if unit1 == "Mega-Parsecs" and unit2 == "Kilo-parsecs":
    ans = float(num1)*1000
    print ans
if unit1 == "Mega-parsecs" and unit2 == "AU":
    ans = float(num1)*2.063e+11
    print ans
if unit1 == "AU" and unit2 == "Mega-parsecs":
    ans = float(num1)/2.063e+11
    print ans
if unit1 == "lyrs" and unit2 == "Mega-parsecs":
    ans = float(num1)/3.262e+6
    print ans
if unit1 == "Mega-parsecs" and unit2 == "lyrs":
    ans = float(num1)*3.262e+6
    print ans

#ASTRO->Metric
if unit1 == "AU" and unit2 == "Km":
    ans = float(num1)*1.496e+8
    print ans
if unit1 == "lyrs" and unit2 == "Km":
    ans = float(num1)*9.461e+12
    print ans
if unit1 == "Parsecs" and unit2 == "Km":
    ans = float(num1)*3.086e+13
    print ans
if unit1 == "Gigameters" and unit2 == "Km":
    ans = float(num1)*1e+6
    print ans
if unit1 == "Kilo-parsecs" and unit2 == "Km":
    ans = float(num1)*3.086e+16
    print ans
if unit1 == "Mega-parsecs" and unit2 == "Km":
    ans = float(num1)*3.086e+19
    print ans
if unit1 == "Km" and unit2 == "AU":
    ans = float(num1)/1.496e+8
    print ans
if unit1 == "Km" and unit2 == "lyrs":
    ans = float(num1)/9.461e+12
    print ans
if unit1 == "Km" and unit2 == "Parsecs":
    ans = float(num1)/3.086e+13
    print ans
if unit1 == "Km" and unit2 == "Kilo-parsecs":
    ans = float(num1)/3.086e+16
    print ans
if unit1 == "Km" and unit2 == "Mega-parsecs":
    ans = float(num1)/3.086e+19
    print ans
if unit1 == "Gigameters" and unit2 == "Km":
    ans = float(num1)/1e+6
    print ans    
if unit1 == "AU" and unit2 == "m":
    ans = float(num1)*1.496e+11
    print ans
if unit1 == "lyrs" and unit2 == "m":
    ans = float(num1)*9.461e+15
    print ans
if unit1 == "Gigameters" and unit2 == "m":
    ans = float(num1)*1e+9
    print ans
if unit1 == "Parsecs" and unit2 == "m":
    ans = float(num1)*3.086e+16
    print ans
if unit1 == "Kilo-parsecs" and unit2 == "m":
    ans = float(num1)*3.086e+19
    print ans
if unit1 == "Mega-Parsecs" and unit2 == "m":
    ans = float(num1)*3.086e+22
    print ans
if unit1 == "m" and unit2 == "AU":
    ans = float(num1)/1.496e+11
    print ans
if unit1 == "m" and unit2 == "lyrs":
    ans = float(num1)/9.461e+15
    print ans
if unit1 == "m" and unit2 == "Parsecs":
    ans = float(num1)/3.086e+16
    print ans
if unit1 == "m" and unit2 == "Gigameters":
    ans = float(num1)/1e+9
    print ans
if unit1 == "m" and unit2 == "Kilo-parsecs":
    ans = float(num1)/3.086e+19
    print ans
if unit1 == "m" and unit2 == "Mega-parsecs":
    ans = float(num1)/3.086e+22
    print ans








































