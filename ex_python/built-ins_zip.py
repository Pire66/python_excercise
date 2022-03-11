if __name__ == '__main__':
    number_of_student, number_of_subject= map(int,input().split())
    marks = list(list(map(float,input().split())) for i in range(number_of_subject))
    students_marks = list(zip(*marks))
    for i in range(number_of_student):
        print(f'{round(sum(students_marks[i])/len(students_marks[i]),1)}')
