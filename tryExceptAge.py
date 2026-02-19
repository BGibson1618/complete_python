def age_calc() -> None:
    print('What year were you born?')
    in_year = input()
    try:
        int_year = int(in_year)
        age = 2026 - int_year
        print(f'Your age is {age}')
        return None
    except ValueError:
        print(f'"{in_year}" cannot be converted to an integer')
        age_calc()
    except TypeError:
        print(f'Your input is dumb')
        age_calc()

age_calc()