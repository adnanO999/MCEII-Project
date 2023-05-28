#!/usr/bin/env python
# coding: utf-8

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# In[3]:


theta = ctrl.Antecedent(np.arange(-200, 200, 0.5), 'theta')
dtheta = ctrl.Antecedent(np.arange(-600, 600, 1), 'dtheta')
voltage = ctrl.Consequent(np.arange(-2, 2, 0.01), 'voltage')


# In[11]:


theta['tilt_neg'] = fuzz.trapmf(theta.universe, [-204, -200, -60, 0])
theta['average'] = fuzz.trimf(theta.universe, [-60, 0, 60])
theta['tilt_pos'] = fuzz.trapmf(theta.universe, [0, 60, 200, 204])


# In[12]:



# In[6]:


dtheta['neg'] = fuzz.trimf(dtheta.universe, [-1200, -600, 600])
dtheta['pos'] = fuzz.trimf(dtheta.universe, [-600, 600, 1200])


# In[7]:





# In[8]:


voltage['high_neg'] = fuzz.trapmf(voltage.universe, [-5, -4.5, -0.56, -0.28])
voltage['low_neg'] = fuzz.trimf(voltage.universe, [-0.56, -0.28, 0])
voltage['average'] = fuzz.trimf(voltage.universe, [-0.14, 0, 0.14])
voltage['low_pos'] = fuzz.trimf(voltage.universe, [0, 0.28, 0.56])
voltage['high_pos'] = fuzz.trapmf(voltage.universe, [0.28, 0.56, 2.25, 3])


# In[9]:





# In[13]:


rule1 = ctrl.Rule(theta['tilt_pos'] & dtheta['pos'], voltage['high_pos'])
rule2 = ctrl.Rule(theta['tilt_pos'] & dtheta['neg'], voltage['low_neg'])
rule3 = ctrl.Rule(theta['tilt_neg'] & dtheta['neg'], voltage['high_neg'])
rule4 = ctrl.Rule(theta['tilt_neg'] & dtheta['pos'], voltage['low_pos'])
rule5 = ctrl.Rule(theta['average'] & dtheta['neg'], voltage['average'])
rule6 = ctrl.Rule(theta['average'] & dtheta['pos'], voltage['average'])


# In[14]:


# In[16]:


balancing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])


# In[17]:


balance_controller = ctrl.ControlSystemSimulation(balancing_ctrl)

if __name__ == "__main__":
    balance_controller.input['theta'] = 5
    balance_controller.input['dtheta'] = 1

    balance_controller.compute()

    print(balance_controller.output['voltage'])
    # voltage.view(sim=balance)
