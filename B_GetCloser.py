'''
AtCoder Beginner Contest 246
B問題
URL：https://atcoder.jp/contests/abc246/tasks/abc246_b
'''
#入力
A,B = map(int,input().split())
#出力
ans =['','']
if A ==0:
    ans[0] =0
    ans[1] =1
else :
    ans[0] = (1/((B/A)**2+1))**0.5
    ans[1] = (B/A)*ans[0]
print(*ans)
#complete