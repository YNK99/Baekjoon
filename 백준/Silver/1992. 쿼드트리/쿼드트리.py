N = int(input())
vedio = [list(map(int, input().strip())) for c in range(N)]
result = []

def div(x, y, N):
    if N == 1:   # 최소 사각형인 경우
        result.append(vedio[x][y]) # 바로 리스트에 넣어줌
        return
    start = vedio[x][y]    # 시작 기준(사각형의 맨 왼쪽 위 첫째)
    for i in range(x, x+N):
        for j in range(y, y+N):   # 범위 안에
            if vedio[i][j] != start:   # 다른 게 있으면
                N = N//2               # N을 조정하고 위에 걸 함
                result.append('(')
                div(x, y, N)        
                div(x, y+N, N)
                div(x+N, y, N)
                div(x+N, y+N, N)
                result.append(")")
                return
    result.append(start)    # 사각형이 한 숫자로만 이루어짐
div(0,0,N)

print(*result, sep = "")    # 리스트를 문자열로 합쳐줌
# ['(', '(', '(', 1, 1, 1, 1, ')', ')', '(', 1, 1, 1, 1, ')', '(', ')', '(', ')', '(', 1, 1, 1, 1, ')', '(', ')', '(', ')', '(', 1, 1, 1, 1, ')', ')', '(', '(', 1, 1, 1, 1, ')', ')', '(', 1, 1, 1, 1, ')', '(', ')']
# 원래는 위처럼 나옴