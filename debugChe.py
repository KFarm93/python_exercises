bill_total = float(raw_input('What was the total bill? '))
service_rating = raw_input('Rate the service (Good, Fair, or Bad): ')
tip_total = 0

if service_rating == 'Good':
    tip_total = bill_total * 0.20
elif service_rating == 'Fair':
    tip_total = bill_total * 0.15
elif service_rating == 'Bad':
    tip_total = bill_total * 0.10
else:
    print 'Please Type Good, Fair, or Bad as a rating.'
total = bill_total + tip_total

print total

split_ways = int(raw_input('Split the bill how many ways? (1 for none): '))

each_person = total / split_ways

print 'Amount per person ''%.2f' % each_person
