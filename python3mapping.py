#!/usr/bin/env python
# coding: utf-8

# ### WattTime Take Home - Part 1
# ### Joshua Carver-Brown
# ### November 2, 2021


### Data Import

import pandas as pd
import os

entso = pd.read_csv('https://raw.githubusercontent.com/JCarverbrown/WattTime/main/entso.csv')
gppd = pd.read_csv('https://raw.githubusercontent.com/JCarverbrown/WattTime/main/gppd.csv')
platts = pd.read_csv('https://raw.githubusercontent.com/JCarverbrown/WattTime/main/platts.csv')

### Data Prep

# data clean up
entso['country'] = entso['country'].str.slice(stop=-5)
entso['plant_name'] = entso['plant_name'].str.upper()
entso['unit_name'] = entso['unit_name'].str.upper()

# prep pre-merge
platts['platts_plant_id'] = platts['platts_plant_id'].astype(str)
gppd['platts_plant_id'] = gppd['platts_plant_id'].astype(str)

# merge dataframes
platts_gppd = platts.merge(gppd, on='platts_plant_id', how='left')

platts_gppd_entso = entso.merge(platts_gppd,
                                how='left',
                                left_on=['plant_name', 'unit_fuel'],
                                right_on=['plant_name_x', 'unit_fuel'])

output = platts_gppd_entso[['entso_unit_id', 'platts_unit_id', 'gppd_plant_id']]

### Output

print("Output to current working directory: {}".format(os.getcwd()))
output_path = os.path.join(os.getcwd(), 'mapping.csv')
output.to_csv(output_path)




