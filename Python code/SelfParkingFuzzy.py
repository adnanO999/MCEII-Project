#!/usr/bin/env python
# coding: utf-8

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# In[3]:


distance = ctrl.Antecedent(np.arange(-500, 500, 1), 'distance')
# dtheta = ctrl.Antecedent(np.arange(-600, 600, 1), 'dtheta')
voltage = ctrl.Consequent(np.arange(-2, 2, 0.01), 'voltage')


# In[11]:


distance['neg'] = fuzz.trapmf(distance.universe, [-511, -510, -100, 0])
distance['zero'] = fuzz.trimf(distance.universe, [-100, 0, 100])
distance['pos'] = fuzz.trapmf(distance.universe, [0, 100, 510, 511])


# In[12]:





# In[6]:

#
# dtheta['neg'] = fuzz.trimf(dtheta.universe,[-1200,-600,600])
# dtheta['pos'] = fuzz.trimf(dtheta.universe,[-600,600,1200])


# In[7]:





# In[8]:


voltage['neg'] = fuzz.trapmf(voltage.universe, [-3, -2.5, -1, 1])
voltage['zero'] = fuzz.trapmf(voltage.universe, [-0.15, -0.14, 0.14, 0.15])
voltage['pos'] = fuzz.trapmf(voltage.universe, [-1, 1, 2.5, 3])


# In[9]:





# In[13]:


rule1 = ctrl.Rule(distance['pos'], voltage['pos'])
rule2 = ctrl.Rule(distance['neg'], voltage['neg'])
rule3 = ctrl.Rule(distance['zero'], voltage['zero'])
# rule4 = ctrl.Rule(theta['tilt_neg'] & dtheta['pos'], voltage['low_pos'])
# rule5 = ctrl.Rule(theta['average'] & dtheta['neg'], voltage['average'])
# rule6 = ctrl.Rule(theta['average'] & dtheta['pos'], voltage['average'])


# In[14]:


# In[16]:


parking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])


# In[17]:


parking_controller = ctrl.ControlSystemSimulation(parking_ctrl)

if __name__ == "__main__":
    parking_controller.input['distance'] = 5

    parking_controller.compute()

    print(parking_controller.output['voltage'])
    # voltage.view(sim=balance)
