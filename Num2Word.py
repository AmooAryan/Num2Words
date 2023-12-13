# Number to Words by AMOOARYAN



from os import system

while True:

    menu = int(input("\n\n1.English 2.Persian: "))

    system("clear")

    #region MENU 1
    if menu == 1:
        def eng(number):
        
            bank = {
                0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
                7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
                13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
                18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
                50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety" }

            big = {
                1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion", 5: "Quadrillion", 6: "Quintillion",
                7: "Sextillion", 8: "Septillion", 9: "Octillion", 10: "Nonillion", 11: "Decillion", 12: "Undecillion",
                13: "Duodecillion", 14: "Tredecillion", 15: "Quattuordecillion", 16: "Quindecillion", 17: "Sexdecillion",
                18: "Septendecillion", 19: "Octodecillion", 20: "Novemdecillion", 21: "Vigintillion", 22: "Unvigintillion",
                23: "Duovigintillion", 24: "Trevigintillion", 25: "Quattuorvigintillion", 26: "Quinvigintillion", 27: "Sexvigintillion",
                28: "Septenvigintillion", 29: "Octovigintillion", 30: "Nonvigintillion", 31: "Trigintillion", 32: "Untrigintillion",
                33: "Duotrigintillion", 34: "Googol" }

            if number in bank:
                return bank[number]

            elif 21 <= number <= 99:
                tens_digit = (number // 10) * 10
                ones_digit = number % 10
                return bank[tens_digit] + " " + bank[ones_digit]

            elif 100 <= number <= 999:
                hundreds_digit = number // 100
                remain = number % 100
                if remain == 0:
                    return bank[hundreds_digit] + " Hundred "
                else:
                    return bank[hundreds_digit] + " Hundred and " + eng(remain)

            elif number >= 1000:
            
                part = 0

                temp = number

                while temp // 1000 >= 1:
                    temp //= 1000
                    part += 1

                remain = number - (temp * ((10 ** 3) ** part))

                return eng(temp) + f" {big[part]} and " + eng(remain)

        number = int(input("\n\nEnter a number: "))
        words = eng(number)
        print(f"\n{number} in words: {words}\n")
    #endregion

    #region MENU 2
    elif menu == 2:
        def fa(number):
        
            bank = {
                0: "صفر", 1: "یک", 2: "دو", 3: "سه", 4: "چهار", 5: "پنج", 6: "شش",
                7: "هفت", 8: "هشت", 9: "نه", 10: "ده", 11: "یازده", 12: "دوازده",
                13: "سیزده", 14: "چهارده", 15: "پانزده", 16: "شانزده", 17: "هفده",
                18: "هجده", 19: "نوزده", 20: "بیست", 30: "سی", 40: "چهل",
                50: "پنجاه", 60: "شصت", 70: "هفتاد", 80: "هشتاد", 90: "نود", 200: "دویست", 300: "سی صد", 500: "پانصد" }

            big = {
                1: "هزار", 2: "میلیون", 3: "میلیارد", 4: "بیلیون", 5: "بیلیارد", 6: "تریلیون",
                7: "تریلیارد", 8: "کوآدریلیون", 9: "کادریلیارد", 10: "کوینتیلیون", 11: "کوانتینیارد", 12: "سکستیلیون",
                13: "سکستیلیارد", 14: "سپتیلیون", 15: "سپتیلیارد", 16: "اکتیلیون", 17: "اکتیلیارد",
                18: "نانیلیون", 19: "نانیلیارد", 20: "دسیلیون", 21: "دسیلیارد", 22: "آندسیلیون",
                23: "آندسیلیارد", 24: "دودسیلیون", 25: "دودسیلیارد", 26: "تریدسیلیون", 27: "تریدسیلیارد",
                28: "کوادردسیلیون", 29: "کوادردسیلیارد", 30: "کویندسیلیون", 31: "کویندسیلیارد", 32: "سیدسیلیون",
                33: "سیدسیلیارد", 34: "گوگول" }

            if number in bank:
                return bank[number]

            elif 21 <= number <= 99:
                tens_digit = (number // 10) * 10
                ones_digit = number % 10
                return bank[tens_digit] + " و " + bank[ones_digit]

            elif 100 <= number <= 999:
                hundreds_digit = number // 100
                remain = number % 100

                if hundreds_digit == 2:
                    if remain == 0:
                        return bank[200]
                    else:
                        return bank[200] + " و " + fa(remain)
                    
                if hundreds_digit == 3:
                    if remain == 0:
                        return bank[300]
                    else:
                        return bank[300] + " و " + fa(remain)
                    
                if hundreds_digit == 5:
                    if remain == 0:
                        return bank[500]
                    else:
                        return bank[500] + " و " + fa(remain)

                else:    
                    if remain == 0:
                        return bank[hundreds_digit] + " صد "
                    else:
                        return bank[hundreds_digit] + " صد و " + fa(remain)

            elif number >= 1000:
            
                part = 0

                temp = number

                while temp // 1000 >= 1:
                    temp //= 1000
                    part += 1

                remain = number - (temp * ((10 ** 3) ** part))

                return fa(temp) + f" {big[part]} و " + fa(remain)

        number = int(input("\n\nEnter a number: "))
        words = fa(number)
        print(f"\n{number} به حروف: {words}\n")
    #endregion
