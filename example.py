# source: https://crpropa.github.io/CRPropa3/pages/example_notebooks/basics/basics.html
# This script is a simple example of a cosmic ray propagation simulation with CRPropa.

from crpropa import *

# simulation: a sequence of simulation modules
sim = ModuleList()

# add propagator for rectalinear propagation
sim.add(SimplePropagation())

# add interaction modules
sim.add(PhotoPionProduction(CMB()))
sim.add(ElectronPairProduction(CMB()))
sim.add(NuclearDecay())
sim.add(MinimumEnergy(1 * EeV))

cosmicray = Candidate(nucleusId(1, 1), 200 * EeV, Vector3d(100 * Mpc, 0, 0))

sim.run(cosmicray)
print(cosmicray)
print('Propagated distance', cosmicray.getTrajectoryLength() / Mpc, 'Mpc')
