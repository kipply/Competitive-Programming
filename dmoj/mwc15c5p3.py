n, m = map(int, input().split())
nn = input().split()
mm = input().split()
print(len(list(set(nn).intersection(mm))))
# This is exactly how I'd do the "intersection" problem on an interview. 
