# Boundary Value Analysis is a testing technique that helps to identify errors at
# boundaries of the input domain - a frequent source of errors. We test values on
# either side of the boundary.
#
# For example, if:
# - Ages of less than 0 should be rejected.
# - Children under 13 years pay £8.
# - Adults between 13 and 59 years pay £12.
# - Seniors 60 years and above pay £9.
#
# Boundary Value Analysis reveals four boundaries: 0, 13, and 60.
#
# Testing the boundaries:
# +-----------------------+
# | Age | Expected Result |
# +-----+-----------------+
# | -1  | Reject input    |
# |  0  | 8               |
# |  1  | 8               |
# | 12  | 8               |
# | 13  | 12              |
# | 14  | 12              |
# | 59  | 12              |
# | 60  | 9               |
# | 61  | 9               |
# +-----+-----------------+

def debugged_get_ticket_price(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")

    if age < 13:
        return 8
    elif 13 <= age <= 59:
        return 12
    elif age >= 60:
        return 9


print(debugged_get_ticket_price(0))   # Should print 8
print(debugged_get_ticket_price(1))   # Should print 8
print(debugged_get_ticket_price(12))  # Should print 8
print(debugged_get_ticket_price(13))  # Should print 12
print(debugged_get_ticket_price(14))  # Should print 12
print(debugged_get_ticket_price(59))  # Should print 12
print(debugged_get_ticket_price(60))  # Should print 9
print(debugged_get_ticket_price(61))  # Should print 9
print(debugged_get_ticket_price(-1))  # Should raise an error
