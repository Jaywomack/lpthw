stock_prices = [('APPLE', 200), ('GOOGLE', 400), ('MICROSOFT', 100)]

for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(f"A ten percent increase would look like this {ticker}: {price + price * 0.1}")

work_hours = [('Abby', 100), ('Sean', 1000), ('Billy', 400), ('Cassie', 800)]


def employee_check(employee_time_sheets):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if current_max < hours:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    # return a tuple
    return employee_of_month, current_max


employee_of_the_month = employee_check(work_hours)

employee_name, employee_hours = employee_of_the_month

print(type(employee_of_the_month))
print(employee_name)
print(employee_hours)
