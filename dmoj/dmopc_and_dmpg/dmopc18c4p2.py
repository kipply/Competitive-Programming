import sys
input = sys.stdin.readline

n = int(input()) 

tasks = list(map(int, input().split()))

s = sum(tasks) 

dp = [[False for cute in xrange(s + 1)] for cute in xrange(2)]
for i in xrange(2): 
	dp[i][0] = True 

for i in xrange(1, n + 1): 
	cur = dp[i & 1]
	if i & 1 == 0: 
		cute = 1
	else: 
		cute = 0 
	prev = dp[cute]
	for j in xrange(1, s + 1): 
		cur[j] = prev[j] 
		if tasks[i - 1] <= j: 
			cur[j] = prev[j] - tasks[i - 1] or cur[j]
			
ans = 1 << 30 
for i in xrange(s/2, -1, -1): 
	if dp[n & 1][i]: 
		ans = s - 2 * i
		break
print ans
