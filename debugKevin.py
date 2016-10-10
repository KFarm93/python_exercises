bill_amt = float(raw_input("How much was the bill?"))
service_lvl = raw_input("How was the service?")
split_ways = int(raw_input("Split how many ways?"))
if service_lvl == 'good':
    total_bill = bill_amt * .20 + bill_amt
if service_lvl == 'fair':
    total_bill = bill_amt * .15 + bill_amt
if service_lvl == 'bad':
    total_bill = bill_amt * .10 + bill_amt

print 'Total amount ''$%.2f' % total_bill
split_amt = total_bill / split_ways
print 'Split amount ''$%.2f' % split_amt
