# Enter your code here. Read input from STDIN. Print output to STDOUT
def mat(n,m):
    for i in range(0,n//2):
        print( ('.|.'*(i*2+1)).center(m,"-"))
    print("WELCOME".center(m,'-'))
    for i in range(n//2-1,-1,-1):
        print(('.|.'*(i*2+1)).center(m,"-"))
    
n, m = map(int , input().split())
mat(int(n),int(m))