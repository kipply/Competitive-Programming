import sys
input = sys.stdin.readline 

d, L, v_1, v_2 = map(int, input().split())

d_per_s = v_1 + v_2
print(float(L - d) / float(v_1 + v_2))