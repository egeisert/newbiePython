#Basic code to make interest calculator

print("Calculate interest:")
prin = float(input("Principal amount:"))
rate = float(input("Interest rate in %:")) / 100.
n = int(input("Compounding periods per year:"))
t = int(input("Number of years:"))

total = prin * (1 + (rate / n))**(n * t)

print('Total: %.2f' % total)
print("Total interest: %.2f" % (total - prin))
