print(lambda n:("Odd" if all(len(sub) % 2 for sub in list(i for i in (n[i:j+1] for i in range(len(n)) for j in range(i, len(n))) if i == i[::-1])) else "Even"))(raw_input())
