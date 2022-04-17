cash_flows = [100, 200, -300, 400, 500, -600]

# List comprehension
inflows = [x for x in cash_flows if x > 0]

print(inflows)