def is_leap_year(year):
    """
    A leap year happens every 4 years, meaning it must be a year divisible by 4
    End-of-century years must be divisible by 400

    This function determines if a given integer is a leap year!
    """
    isinstance(year, int)

    requirement_value =  0

    if year % 4 == 0:
        requirement_value += 1

    if year % 100 == 0:
     requirement_value += 1

    if year % 400 == 0:
        requirement_value += 1
   
    if requirement_value == 3:
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year...")