from datetime import datetime

with open('NFO_symbols.txt', 'r') as file:

    fn_date = set()
    nf_date = set()

    for line in file:
        values = line.strip().split(',')
        if values[3] == 'FINNIFTY':
            fn_date.add(values[5])
        elif values[3] == 'NIFTY':
            nf_date.add(values[5])

fn_date = [datetime.strptime(date, '%d-%b-%Y') for date in fn_date]
nf_date = [datetime.strptime(date, '%d-%b-%Y') for date in nf_date]


fn_min = min(fn_date)
nf_min = min(nf_date)

fn_min = fn_min.strftime('%Y-%m-%d')
nf_min = nf_min.strftime('%Y-%m-%d')

#print('Current expiry for:')
#print('FINNIFTY:', fn_min)
#print('NIFTY:', nf_min)

#Save ithe dates in the expiry dates file from where your main code fetches the expiry dates
#fn_expiry_dates.txt and nf_expiry_dates.txt are the text files where you save your expiry date.
with open('/address_to_your_folder/fn_expiry_dates.txt', 'w') as f:
    f.write(fn_min)
with open('/address_to_your_folder/expiry_dates.txt', 'w') as f:
    f.write(nf_min)


