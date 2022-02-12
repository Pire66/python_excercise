from functools import reduce
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    allemark=student_marks[query_name]
    averagemark=reduce(lambda x,y:x+y,allemark)/len(allemark)
    print('%.2f' % averagemark)
