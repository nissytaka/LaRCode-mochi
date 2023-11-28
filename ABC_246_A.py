'''
AtCoder Beginner Contest 246
A問題
URL：https://atcoder.jp/contests/abc246/tasks/abc246_a
'''
#入力
X_Y  = [list(map(int,input().split())) for _ in range(3)] 
#出力
ans =[]
#x座標判定
#0と1で等しいなら、2個目と同じ
if X_Y[0][0] == X_Y[1][0] :
    ans.append(X_Y[2][0])
    
#0と1で違う、1と2で同じなら0個目と同じ
if X_Y[0][0] != X_Y[1][0] and X_Y[1][0] == X_Y[2][0]:
    ans.append(X_Y[0][0])
    
#0と1で、1と2で違うなら1個目と同じ
if X_Y[0][0] != X_Y[1][0] and X_Y[1][0] != X_Y[2][0]:
    ans.append(X_Y[1][0])


#y軸判定
#0と1で等しいなら、2個目と同じ
if X_Y[0][1] == X_Y[1][1] :
    ans.append(X_Y[2][1])
    
#0と1で違う、1と2で同じなら0個目と同じ
if X_Y[0][1] != X_Y[1][1] and X_Y[1][1] == X_Y[2][1]:
    ans.append(X_Y[0][1])
    
#0と1で違う、1と2で違うなら1個目と同じ
if X_Y[0][1] != X_Y[1][1] and X_Y[1][1] != X_Y[2][1]:
    ans.append(X_Y[1][1])
print(*ans)

