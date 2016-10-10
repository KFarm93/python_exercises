bill_amt = float(raw_input("How much was the bill?"))
service_lvl = raw_input("How was the service?")
split_ways = int(raw_input("Split how many ways?"))



if service_lvl == 'good':
    bill_amt = bill_amt * .20 + bill_amt
elif service_lvl == 'fair':
    bill_amt == bill_amt * .15 + bill_amt
if service_lvl == 'bad':
    bill_amt = bill_amt * .10 + bill_amt


print 'Total amount ''$%.2f' % bill_amt
