# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:20:13 2021

@author: Besitzer
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Besitzer/Documents/ds_salary_proj/chromedriver"

pd = gs.get_jobs("data scientist", 15, False, path, 15)