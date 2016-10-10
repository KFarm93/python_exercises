name = raw_input("What is your name? ")
print str.upper("Hello, " + name + "!")
print str.upper("There are " + str(len(name)) + " letters in your name!")

subject = raw_input("What is your favorite subject? " )
print name + "\'s favorite subject in school is " + subject + "."

day = int(raw_input('Day (0-6)? '))
dayList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print dayList[day]

if day = 0
    print "Sleep in."
elif day = 6
    print "Sleep in."
else:
    print "Go to work."

tempC = int(raw_input("Temperature in C? "))
print tempC * 1.8 + 32

bill_amt = float(raw_input("How much was the bill?"))
service_lvl = raw_input("How was the service?")
if service_lvl == 'good':
    total_bill = bill_amt * .20 + bill_amt
if service_lvl == 'fair':
    total_bill = bill_amt * .15 + bill_amt
if service_lvl == 'bad':
    total_bill = bill_amt * .10 + bill_amt
print total_bill

bill_amt = float(raw_input("How much was the bill?"))
service_lvl = raw_input("How was the service?")
split_ways = int(raw_input("Split how many ways?"))
if service_lvl == 'good':
    total_bill = bill_amt * .20 + bill_amt
if service_lvl == 'fair':
    total_bill = bill_amt * .15 + bill_amt
if service_lvl == 'bad':
    total_bill = bill_amt * .10 + bill_amt
print "Total amount: ",  total_bill
print "Split amount: ", total_bill / split_ways
