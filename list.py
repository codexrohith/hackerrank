if __name__ == '__main__':
    N = int(input())
    result=[]
    for i in range(N):
        str_=input()
        list_=str_.split()
        if list_[0]=="insert":
            result.insert(int(list_[1]),int(list_[2]))
        elif list_[0]=="print":
            print(result)
        elif list_[0]=="remove":
            result.remove(int(list_[1]))
        elif list_[0]=="append":
            result.append(int(list_[1]))
        elif list_[0]=="sort":
            result.sort()
        elif list_[0]=="pop":
            result.pop()
        elif list_[0] == "reverse":
            result.reverse()
