if __name__ == '__main__':
    stu=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu.append([name,score])
    scores=[]
    for i in range(len(stu)):
        scores.append(stu[i][1])
    scores.sort()
    low=min(scores)
    while low in scores:
        scores.remove(low)
    req=min(scores)
    names=[]
    for i in range(len(stu)):
        if stu[i][1]==req:
            names.append(stu[i][0])
    names.sort()
    for i in names :
        print(i)