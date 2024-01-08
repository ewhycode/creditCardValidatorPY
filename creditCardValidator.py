#Credit Card Validator

#1 Remove "-" or " "
#2 Add al digits in the odd places from right to left
#3 Double every second digit from right to left
#       (If result is a two-digit number,
#       add the two-digit number together to get a single digit)
#4 Sum the totals of steps 2 & 3
#5 If sum is divisble by 10, the credit card is valid
#TEST: sample credit card numbers https://www.paypalobjects.com/en_AU/vhelp/paypalmanager_help/credit_card_numbers.htm

sumOddDigits = 0
sumEvenDigits = 0
total = 0

#STEP 1
cardNumber = input("Enter a credit card number: ")
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")
cardNumber = cardNumber [::-1]

#STEP 2
for x in cardNumber[::2]:
    sumOddDigits += int(x)

#STEP 3
for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        sumEvenDigits += (1+(x % 10))
    else:
        sumEvenDigits += x

#STEP 4
total = sumOddDigits + sumEvenDigits

#STEP 5
if total % 10 == 0:
    print('Valid')
else:
    print('Invalid')