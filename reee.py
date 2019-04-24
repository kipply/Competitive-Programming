# -*- coding: utf-8 -*-
n = int(raw_input()) 
for i in range(n): 
    a, b = raw_input().split()
    a = a.lower()
    b = b.lower()

    chinese = list("一二三四有五六七八九十")

    b = b.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("ten", "10").replace("ix", "9").replace("x", "10").replace("viii", "8").replace("vii", "7").replace("vi", "6").replace("iv", "4").replace("v", "5").replace("iii", "3").replace("ii", "2").replace("i", "1");

    a = a.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("ten", "10").replace("ix", "9").replace("x", "10").replace("viii", "8").replace("vii", "7").replace("vi", "6").replace("iv", "4").replace("v", "5").replace("iii", "3").replace("ii", "2").replace("i", "1");

    for x in range(10): 
        a = a.decode('utf-8').replace(chinese[x],str(x + 1))
        b = b.decode('utf-8').replace(chinese[x],str(x + 1))

    try: 
        print(int(a) + int(b))
    except: 
        print(b)
        pass