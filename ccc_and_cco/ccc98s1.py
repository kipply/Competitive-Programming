n = int(input())
for i in range(n):
    a = input().split(" ")
    for word in a:
        if len(word) == 4:
            word = "****"
        print(word + " ", end="")
    print("")
