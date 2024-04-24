import authentication

title = "Python Programming Project - 2"
projectName = "Smart Student Management System"
DevelopedSemester = "3rd Semester"
technology = "Computer Science and Technology"
width = 130

strings = [title, projectName, DevelopedSemester, technology]

for string in strings:
    print(string.center(width))
print("________________________________________________________________________________________________________".center(
    width))

authentication.main()
