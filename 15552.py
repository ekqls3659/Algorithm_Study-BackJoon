# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
import sys
cases = int(input())

for i in range(cases):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)