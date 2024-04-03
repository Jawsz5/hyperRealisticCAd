"""
combustion_thermodynamics:
--------------------------

Combustion reaction thermodynamical properties.

Authored by: MRodriguez, 2020-2022

"""
## just found out that the facotry module isn't even finished. So, I'll swithc to chemical reactions, and I might just end up setting everythign up on my own without MRod's stuff

## when importing from pyturb remember to include which file in pyturb I'm importing from
import numpy as np
import warnings
from pyturb.gas_models import ThermoProperties
from pyturb.gas_models import PerfectIdealGas
from pyturb.gas_models import SemiperfectIdealGas
from pyturb.gas_models import GasMixture
from pyturb.utils import units
from pyturb.power_plant import Combustor
from pyturb.power_plant import nozzle
from pyturb.power_plant import control_volume
from pyturb.power_plant import intake
from pyturb.gas_models import gas_mixture


#semiperfect ideal gases
# utilize the notebook folder for examples and readme
oxidizers = ['Air', 'O', 'O2', 'O3'] # Allowed oxidizers

#semi perfect ideal gases
fuels = ['hydrocarbon',
         'CH4', 'C2H6', 'C3H8', 'C4H10', 'C5H12', 'C6H14', 'C7H16', 'C8H18',
         'C9H19', 'C10H8',
         'CH4O', 'CH3OCH3',
         'C2H2',
         'H2'] # Allowed fuels

#semiperfect ideal gases
inert_gases = ['He', 'Ar', 'N2',
               'CO2', 'CO',
               'H2O']

part1 = gas_mixture.GasMixture();

part1.Ru()





