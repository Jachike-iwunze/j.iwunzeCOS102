years_of_experience = int(input('Please nter your years of work experience'))
age_of_staff = int(input('Please enter your age'))

if years_of_experience > 25 and age_of_staff >= 55 :
    print('Your Annual Tax Revenue (ATR) is N5,600,000')

elif years_of_experience > 20 and age_of_staff >= 45:
    print('Your Annual Tax Revenue (ATR) is N4,480,000')
elif years_of_experience > 10 and age_of_staff >= 35:
    print('Your Annual Tax Revenue (ATR) is N1,500,000')
elif years_of_experience < 10 and age_of_staff < 35:
    print('Your Annual Tax Revenue (ATR) is N500,000')
else:
    print('Your havent worked here for up to 10 years')
