from utils import charge_calculation, membrane_potential_calculation

if __name__ == '__main__':
    # permeabilities
    p_k = float(input('Potassium permeability: '))
    p_na = float(input('Sodium permeability: '))
    p_cl = float(input('Chloride permeability: '))

    # potassium concentrations
    c_kout = float(input('Extracellular potassium concentration: '))
    c_kin = float(input('Intracellular potassium concentration: '))

    # sodium concentrations
    c_naout = float(input('Extracellular sodium concentration: '))
    c_nain = float(input('Intracellular sodium concentration: '))

    # chloride concentrations
    c_clout = float(input('Extracellular chloride concentration: '))
    c_clin = float(input('Intracellular chloride concentration: '))

    membrane_potential = membrane_potential_calculation(p_k, p_na, p_cl, c_kout,
                                                       c_naout, c_clout, c_kin, 
                                                       c_nain, c_clin)
    
    print(f'\nMembrane potential: {membrane_potential} mV')


