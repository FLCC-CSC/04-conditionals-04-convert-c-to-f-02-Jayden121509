# FILE NAME - convert_C_to_F_02.py

# NAME: Jayden Blair
# DATE: 3/1/26
# BRIEF DESCRIPTION:  Convert a temperature from Celsius to Fahrenheit or from Fahrenheit to Celsius based on user input.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====\n")
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius\n")
choice = input("Please choose from the above menu: ")
temp = float(input("Enter a temperature to convert: "))
if choice == "1":
    converted_temp = (temp * 9/5) + 32
    print(f"\n{temp} degrees Celsius is {converted_temp} degrees Fahrenheit.")
elif choice == "2":
    converted_temp = (temp - 32) * 5/9
    print(f"\n{temp} degrees Fahrenheit is {converted_temp} degrees Celsius.")
else:
    print("\nInvalid choice. Please choose either 1 or 2.")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I learned how to use elif statements, which are really helpful when you have more than two options to choose from.





'''