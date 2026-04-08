records = [
    {"month": "1月", "type": "收入", "amount": 5000},
    {"month": "1月", "type": "支出", "amount": 1200},
    {"month": "2月", "type": "收入", "amount": 5200},
    {"month": "2月", "type": "支出", "amount": 1800},
    {"month": "3月", "type": "收入", "amount": 5500},
    {"month": "3月", "type": "支出", "amount": 2100}
]
month_record = {}

for record in records:
    if record['month'] in month_record:
        if record['type'] == '收入':
            month_record[record['month']]['收入'] += record['amount']
            month_record[record['month']]['结余'] += record['amount']
        elif record['type'] == '支出':
            month_record[record['month']]['支出'] += record['amount']
            month_record[record['month']]['结余'] -= record['amount']
    else:
        if record['type'] == '收入':
            month_record[record['month']] = {'收入':record['amount'], '支出':0, '结余':record['amount'] - 0}
        elif record['type'] == '支出':
            month_record[record['month']]= {'收入':0, '支出':record['amount'], '结余':0 - record['amount']}

total_earn = 0
total_cost = 0
total_balance = 0
max_balance = 0
max_balance_month = ''
max_cost = 0
max_cost_month = ''

for month in month_record:
    print(f"{month}的收入为{month_record[month]['收入']},支出为{month_record[month]['支出']},结余为{month_record[month]['结余']}")
    total_earn += month_record[month]['收入']
    total_cost += month_record[month]['支出']
    total_balance += month_record[month]['结余']
    if month_record[month]['支出'] > max_cost:
        max_cost = month_record[month]['支出']
        max_cost_month = month

    if (month_record[month]['结余']) > max_balance:
        max_balance = month_record[month]['结余']
        max_balance_month = month


print(f"全年总收入为:{total_earn}")
print(f"全年总支出为:{total_cost}")
print(f"全年总结余为:{total_balance}")
print(f"结余最高的月份为{max_balance_month},结余为{max_balance}")
print(f"支出最高的月份为{max_cost_month},支出为{max_cost}")