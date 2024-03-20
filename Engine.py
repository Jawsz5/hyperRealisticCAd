"""
combustion_thermodynamics:
--------------------------

Combustion reaction thermodynamical properties.

Authored by: MRodriguez, 2020-2022

"""
import numpy as np
import warnings
from pyturb.gas_models import ThermoProperties
from pyturb.gas_models import PerfectIdealGas
from pyturb.gas_models import SemiperfectIdealGas
from pyturb.gas_models import GasMixture
from pyturb.utils import units


oxidizers = ['Air', 'O', 'O2', 'O3'] # Allowed oxidizers

fuels = ['hydrocarbon',
         'CH4', 'C2H6', 'C3H8', 'C4H10', 'C5H12', 'C6H14', 'C7H16', 'C8H18',
         'C9H19', 'C10H8',
         'CH4O', 'CH3OCH3',
         'C2H2',
         'H2'] # Allowed fuels

inert_gases = ['He', 'Ar', 'N2',
               'CO2', 'CO',
               'H2O']

print(inert_gases[2])



