# Enter your code here. Read input from STDIN. Print output to STDOUT
def mat(n,m):
    for i in range(0,n//2):
        print('-'*((n//2-i)*3) + '.|.'*(i*2+1) + '-'*((n//2-i)*3))
    print("WELCOME".center(m,'-'))
    for i in range(n//2-1,-1,-1):
        print('-'*((n//2-i)*3) + '.|.'*(i*2+1) + '-'*((n//2-i)*3))
    
n, m = map(int , input().split())
mat(int(n),int(m))