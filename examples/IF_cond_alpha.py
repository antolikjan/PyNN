"""
Simple test to compare iaf_neuron in NEST with StandardIF in NEURON.

Andrew Davison, UNIC, CNRS
May 2006

$Id$
"""

import sys

simulator_name = sys.argv[-1]

exec("from pyNN.%s import *" % simulator_name)

setup(timestep=0.1, min_delay=0.1, max_delay=4.0, debug=True)

ifcell = create(IF_cond_alpha, {'i_offset' : 0.1,    'tau_refrac' : 3.0,
                                'v_thresh' : -51.0,  'tau_syn_E'  : 2.0,
                                'tau_syn_I': 5.0,    'v_reset'    : -70.0,
                                'e_rev_E'  : 0.,     'e_rev_I'    : -80.})

spike_sourceE = create(SpikeSourceArray, {'spike_times': [float(i) for i in range(5,105,10)]})
spike_sourceI = create(SpikeSourceArray, {'spike_times': [float(i) for i in range(155,255,10)]})

connE = connect(spike_sourceE, ifcell, weight=0.006, synapse_type='excitatory',delay=2.0)
connI = connect(spike_sourceI, ifcell, weight=0.02, synapse_type='inhibitory',delay=4.0)
    
record_v(ifcell, "Results/IF_cond_alpha_%s.v" % simulator_name)

run(200.0)

end()
