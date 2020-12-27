import random

userDict = {"Mehmet Kas": [], "Ahmet Toprak": [], "Ayse Ozcetin": [],
            "Berfu Yuzgec": [], "Kadir Erturk": [], "Seydi Yıldırım": []}


def failPass(grades):
    totalGrade = int(((int(grades['midterm']) / 100) * 30) + ((int(grades['final']) / 100) * 50)
                     + ((int(grades['project']) / 100) * 20))
    if totalGrade >= 90:
        print("\nYou get 'AA' from course.")
    elif 70 <= totalGrade < 90:
        print("\nYou get 'BB' from course.")
    elif 50 <= totalGrade < 70:
        print("\nYou get 'CC' from course.")
    elif 30 <= totalGrade < 50:
        print("\nYou get 'DD' from course.")
    else:
        print("\nYou get 'FF' from course and you failed in class.")


def gradesofCourse(courseName):
    print(f"\nYou chose {courseName}.\n")
    grades = {'midterm': random.randint(0, 100), 'final': random.randint(0, 100),
              'project': random.randint(0, 100)}
    print(courseName + ": " + str(grades))
    return grades


def examCourse(coursesList):
    print("\nYou should choose one of courses that you want to take an exam.\n")
    for index, courseName in enumerate(coursesList):
        print(f"{index + 1}. {courseName}")
    while True:
        courseNum = int(input("Please enter the number of course that you want to take an exam: "))
        if 0 < courseNum <= len(coursesList):
            break
        else:
            print("Invalid Input")
    return coursesList[courseNum - 1]


def choiceCourse(courseList):
    choiceList = []
    print("\nYou can take at least 3 or maximum 5 courses.")
    t = int(input("\nHow many courses do you want to choose?"))
    if t < 3 or t > 5:
        print("You failed in class")
        exit()
    print("\nPlease Enter The Number of Courses That You Want To Take:")
    i = 1
    numList = []
    while i <= t:
        choiceNum = int(input())
        if choiceNum < 1 or choiceNum > 5:
            print("Invalid Number")
            i -= 1
        else:
            if numList.count(choiceNum) > 0:
                print("You chose before this course.")
                continue
            else:
                numList.append(choiceNum)
                choiceList.append(courseList[choiceNum - 1])
        i += 1
    print("Course selection process is successful.")
    return choiceList


def courses():
    courseList = ["Calculus", "Physics", "Chemistry", "Algorithms", "Circuit"]
    for index, courseName in enumerate(courseList):
        print(f"{index + 1}. {courseName}")
    return courseList


def entryTry():
    nameSurname = input("Please Enter Name and Surname: ")

    if nameSurname in userDict.keys():
        return nameSurname
    else:
        return False


if __name__ == '__main__':

    for i in range(3):
        tempName = entryTry()
        if type(tempName) == bool:
            if i == 2:
                print("Please Try Again Later")
            else:
                print("Incorrect Login Information")
        else:
            print(f"\nWelcome {tempName}\n")
            print("Please make choices from list below\n")
            userDict[tempName] = choiceCourse(courses())
            failPass(gradesofCourse(examCourse(userDict[tempName])))
            break
