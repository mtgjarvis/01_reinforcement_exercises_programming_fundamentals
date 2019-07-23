def grade_calc():
    grade_in = int(input('Enter the grade as a percentage: '))
    if grade_in == 100:
        print('You got an A+')
    elif grade_in >= 95:
        print('You got an A')
    elif grade_in >= 90:
        print('You got an A-')
    elif grade_in >= 85:
        print('You got an B+')
    elif grade_in >= 80:
        print('You got an B')
    elif grade_in >= 75:
        print('You got an B-')
    elif grade_in >= 70:
        print('You got an C+')
    else:
        print('Study harder!')
    return


grade_calc()