def computepay(h,r):
    if h <= 40:
        pay = h * r
    elif h > 40:
        pay = 40 * r + (h-40) * r * 1.5
    return pay
# buld a function to compute payment first.
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
