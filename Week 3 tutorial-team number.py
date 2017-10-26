"""""
comments below are test values, left column is number of pupils, middle number of teams,
right is the remainder value

10  2   0
102 20  2
1   0   1
5   1   0
"""""


def valid_number(unknown_number):
    try:
        number = int(unknown_number)
        if number > 0:
            return True
        else:
            print("Invalid number, number has to be greater than 0")
    except ValueError:
        print("Please enter an actual number")


while 1:
    number_of_students = input("Please enter the total number of students: ")
    if valid_number(number_of_students) is True:
        valid_student_number = int(number_of_students)
        break

while 1:
    team_number = input("Please enter how many people per team: ")
    if valid_number(team_number) is True:
        valid_team_number = int(team_number)
        break

print(f"The number of teams is: {valid_student_number // valid_team_number} ", "\n"
      f"Number of students not in a team is: {valid_student_number % valid_team_number}")
