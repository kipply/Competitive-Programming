import sys
input = sys.stdin.readline

k = int(input())
m_x = float(input())

observations = []
cute = 0
for i in range(k): 
	cuteness = list(map(float, input().split()))[1:]
	cactus = m_x
	for cutie in cuteness: 
		cactus += cutie 
	cute += cactus 
print cute / k