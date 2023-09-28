# charge calculation helper function calculation
def charge_calculation(ion):
    ion = ion.lower()
    charge = 0
    if (ion == 'na' or ion == 'sodium'
        or ion == 'k' or ion == 'potassium'):
            charge = 1
    elif (ion == 'cl' or ion == 'chloride'):
            charge = -1
    elif (ion == 'ca' or ion == 'calcium'):
            charge = 2
    else:
         print('Enter name of ion either by chemical abbreviation (without charge) or english name')
         print('e.g na or sodium')
    return charge