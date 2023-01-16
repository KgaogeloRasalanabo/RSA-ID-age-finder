# calculate age based on the RSA ID number
from datetime import date


def date_of_birth(new_id_num, era_num):
    # inserts 20 to ID for people born from year 2000 or 19 from year 1900 to 1999 etc
    birth_date = new_id_num[0:6]
    birth_date.insert(0, identity(int(era_num))[0])
    birth_date.insert(1, identity(int(era_num))[1])

    # year, month and day finder
    yea = "".join([str(y) for y in birth_date[0:4]])
    month = "".join([str(m) for m in birth_date[4:6]])
    day = "".join([str(d) for d in birth_date[6:8]])
    print("Year:", yea)
    print("Month:", month_converter(int(month)))
    print("Day:", int(day))
    return yea


# era translator
def identity(era):
    match era:
        case 20:
            return [2, 0]
        case 19:
            return [1, 9]
        case 18:
            return [1, 8]
        case 17:
            return [1, 7]
        case 16:
            return [1, 6]
        case 15:
            return [1, 5]
        case 14:
            return [1, 4]
        case 13:
            return [1, 3]
        case 12:
            return [1, 2]
        case 11:
            return [1, 1]
        case 10:
            return [1, 0]
        case 9:
            return [0, 9]
        case 8:
            return [0, 8]
        case 7:
            return [0, 7]
        case 6:
            return [0, 6]
        case 5:
            return [0, 5]
        case 4:
            return [0, 4]
        case 3:
            return [0, 3]
        case 2:
            return [0, 2]
        case 1:
            return [0, 1]
        case 0:
            return [0, 0]


# month translator
def month_converter(month):
    match month:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"


# age calculator
def age_calculator(yea):
    age = date.today().year - int(yea)
    return age


# female or male identifier
def gender(new_id_num):
    if int(new_id_num[6]) <= 4:
        return 'Female'
    else:
        return 'Male'


# ID validator
def id_validator(a, b, name):
    # array of strings for ID
    k = [str(j) for j in b]
    # ID reference
    isvalid_id = [str(i) for i in (list(range(0, 10)))]

    for x in k:
        # foreign characters checker
        while x not in isvalid_id:
            print("Invalid input '", x.upper(), "'entered try again")
            questionnaire()

    # Month and day extractor
    mo = "".join(k[2:4])
    da = "".join(k[4:6])

    # validator for ID length, month, day and ID digit number 11
    if len(k) < 13:
        print("ID length not 13, try again")
        questionnaire()
    elif len(k) > 13:
        print("ID length not 13, try again")
        questionnaire()
    elif int(mo) > 12:
        print("Month number", mo, "invalid, try again")
        questionnaire()
    elif int(da) > 31:
        print("Day number", da, "invalid, try again")
        questionnaire()
    elif int(k[10]) != 0:
        print("ID digit 10 invalid", k[10], "entered instead of zero, try again")
        questionnaire()
    # output if all conditions are valid
    else:
        print('\n'"Name :", name)
        print("Age:", age_calculator(date_of_birth(b, int(a))))
        print("Gender:", gender(b))


# era validator
def era_validator(n, m, q):
    #  era reference
    isvalid_era = [str(i) for i in (list(range(0, 21)))]

    # comparator
    if n in isvalid_era:
        # ID comparator initializer
        id_validator(n, m, q)

    # runs if era invalid
    else:
        print("Invalid era entered try again")
        print('\n')
        questionnaire()


# inputs and calling comparator
def questionnaire():
    user_name = input("Enter name: ")

    # era initializer
    print('\n'"Hello", user_name, ",", "please choose era. 2000 = 20; 1900 = 19; 1800 =  18; 1700 = 17; 1600 = 16; "
                                       "1500 = 15; 1400 = 14; 1300 = 13; 1200 = 12; 1100 = 11; 1000 = 10; 0900 = 9; "
                                       "0800 = 8; 0700 = 7; 0600 = 6; 0500 = 5; 0400 = 4; 0300 = 3; 0200 = 2; 0100 = "
                                       "1; 0000 = 0")
    num = input("Choose era: ")

    # convert id_num to array
    id_number = input("Enter RSA ID number: ")
    new_id = [i for i in str(id_number)]

    # era comparator
    era_validator(num, new_id, user_name)


if __name__ == "__main__":
    questionnaire()
