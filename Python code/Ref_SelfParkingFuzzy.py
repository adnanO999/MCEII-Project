#!/usr/bin/env python
# coding: utf-8

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# distance = ctrl.Antecedent(np.arange(-1000, 1000, 1), 'distance')
# reference = ctrl.Consequent(np.arange(-2, 3, 0.01), 'reference')
distance = ctrl.Antecedent(np.arange(-2000, 2000, 1), 'distance')
reference = ctrl.Consequent(np.arange(-1, 3, 0.01), 'reference')

# distance['neg'] = fuzz.trimf(distance.universe, [-2000, -1000, 1000])
# distance['pos'] = fuzz.trimf(distance.universe, [-1000, 1000, 2000])
distance['neg'] = fuzz.trapmf(distance.universe, [-2200, -2000, -200, 200])
distance['pos'] = fuzz.trapmf(distance.universe, [-200, 200, 2000, 2200])

# reference['backwards'] = fuzz.trapmf(reference.universe, [0, 2, 3, 3.1])
# reference['forwards'] = fuzz.trapmf(reference.universe, [-3, -2, 0, 2])
reference['backwards'] = fuzz.trapmf(reference.universe, [-1, 1, 2, 2.1])
reference['forwards'] = fuzz.trapmf(reference.universe, [-2.1, -2, -1, 1])

# rule1 = ctrl.Rule(distance['pos'], reference['forwards'])
# rule2 = ctrl.Rule(distance['neg'], reference['backwards'])
rule1 = ctrl.Rule(distance['pos'], reference['backwards'])
rule2 = ctrl.Rule(distance['neg'], reference['forwards'])


ref_ctrl = ctrl.ControlSystem([rule1, rule2])
reference_controller = ctrl.ControlSystemSimulation(ref_ctrl)

if __name__ == "__main__":
    reference_controller.input['distance'] = 5

    reference_controller.compute()

    print(reference_controller.output['reference'])
    # voltage.view(sim=balance)
