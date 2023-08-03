# Name:
# Email ID:

def is_compatible(patient_group, donor_group):
    # Replace the code below with your implementation.
    if donor_group == "AB":
        return True
    if patient_group == donor_group:
        return True
    if patient_group == "O":
        if donor_group == "A" or donor_group == "B":
            return True
    return False