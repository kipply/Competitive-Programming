# this program doesn't get full points because it's too long :( )
print(lambda n,r:(lambda m:" ".join(`i`+bool(m&{i+2,i-2})*"*"for i in {2}|m))(reduce(lambda c,x:c&{x}and c.difference_update(r(x*x,n,x*2))or c,r(n),set(r(3,n,2)))))(input(),range)
