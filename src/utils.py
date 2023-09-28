import numpy as np

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

# nernst potential helper function declaration
def nernst_potential_calculation(c_out, c_in, z):
    nernst_potential = (60 / z) * np.log10(c_out/ c_in)
    return round(nernst_potential, 2)

# goldman-hodgkin-katz helper function declaration
def membrane_potential_calculation(p_k, p_na, p_cl, c_kout, 
                                   c_naout, c_clout, c_kin, c_nain, c_clin):
      v_mem = 60 * np.log10( ( (p_k * c_kout) + (p_na * c_naout) + (p_cl * c_clin) ) / ((p_k * c_kin) + (p_na * c_nain) + (p_cl * c_clout)))
      return round(v_mem, 2)