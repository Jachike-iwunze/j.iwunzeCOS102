#simple interest 
r = 3
t = 4
p = 7



b = r / 100
c = b * t
d = 1 + c
simple_interest = p * d
print(simple_interest)

#compound interest 
p = 7
n = 4
t = 4
r = 3

z = r / n
y = 1 + z
x = y ** (n * t)
compound_interest  = p * x

print(compound_interest)

# annuity plan
pmt = 5
p = 7
n = 4
t = 4
r = 3

o = r / n
k = 1 + o
j = k ** (n * t)
m = j - 1
g = m / o
annuity_plan = pmt * g 
print(annuity_plan)

