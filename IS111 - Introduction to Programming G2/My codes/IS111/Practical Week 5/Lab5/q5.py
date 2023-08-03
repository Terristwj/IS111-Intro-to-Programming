TAX_INFO = [
    (20000, 0, 0.02),
    (30000, 200, 0.035),
    (40000, 550, 0.07),
    (80000, 3350, 0.115),
    (120000, 7950, 0.15),
    (160000, 13950, 0.18),
    (200000, 21150, 0.19),
    (240000, 28750, 0.195),
    (280000, 36550, 0.2),
    (320000, 44550, 0.22)
]

# Put your code below
######################
def calculate_tax(income):
    if income < TAX_INFO[0][0]:
        return 0.0
    
#     Solution 1
    for tax in TAX_INFO[::-1]:
        if income - tax[0] >= 0:
            return tax[1] + (income - tax[0]) * tax[2]

#         Solution 2
#     for i in range(len(TAX_INFO)):
#         if i == len(TAX_INFO)-1:
#             return TAX_INFO[i][1] + TAX_INFO[i][2] * (income - TAX_INFO[i][0])
#         if income < TAX_INFO[i+1][0]:
#             return TAX_INFO[i][1] + TAX_INFO[i][2] * (income - TAX_INFO[i][0])
# Test Cases to test your code
##############################

tax = calculate_tax(15000)
print("Expected: 0.0")
print("Actual  : " + str(tax))
print()
    
tax = calculate_tax(35000)
print("Expected: 375.0")
print("Actual  : " + str(tax))
print()
    
tax = calculate_tax(100000)
print("Expected: 5650.0")
print("Actual  : " + str(tax))
print()

tax = calculate_tax(350000)
print("Expected: 51150.0")
print("Actual  : " + str(tax))
print()

