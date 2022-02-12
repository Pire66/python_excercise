if __name__ == '__main__':
    l=[]
    grades=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        grades.append(score)
    unicgrades=list(set(grades))
    unicgrades.sort()
    secondgrades=unicgrades[1]
    l.sort()
    for i in range(len(l)):
        if l[i][1]==secondgrades:
          print(l[i][0])
#    print(l[i][0] for i in range(len(l)) if l[i][1]==secondgrades)    
