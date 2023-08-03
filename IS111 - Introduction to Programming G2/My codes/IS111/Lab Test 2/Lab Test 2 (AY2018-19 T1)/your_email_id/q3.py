#
# Name: 
# Email ID: 
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.
def format_date(date):
    month = int(date.split('/')[0])
    year = int(date.split('/')[1])
    new_date = str(month) + '/' + str(year)
    return new_date

# End of your additional functions.

def get_total_transactions_in_month(trans_file, month):
    # Modify the code below
    month = format_date(month)
    spendings = 0.0
    with open(trans_file) as f:
        for line in f:
            line = line.rstrip('\n')
            cols = line.split('\t')

            date = cols[0][:cols[0].find('/')+1] + cols[0][-4:]
            date = format_date(date)

            if month == date:
                spendings += float(cols[1][1:])
    return spendings
    
