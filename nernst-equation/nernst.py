from utils import charge_calculation, nernst_potential

if __name__ == '__main__':

    # user interface
    ion = input('\nIon: ')
    charge = charge_calculation(ion)

    ext_conc = float(input('Extracellular Concentration: '))
    int_conc = float(input('Intracellular concentration: '))

    nernst_potential = nernst_potential(ext_conc, int_conc, charge)

    print(f'\nNernst potential: {nernst_potential} mV')
    print(f'\nConcentration used in calculattion: ')
    print(f'Ion: {ion}')
    print(f'Extracellular concentration: {ext_conc} mM')
    print(f'Intracellular concentration: {int_conc} mM')
    print(f'charge: {charge}')