# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:22:04 2026

@author: fisch
"""

import pandas as pd

url = "https://gitlab.opencode.de/StadtBochum/open-data/umwelt-graslandfeuerindex/-/raw/main/data/bochum_graslandfeuerindex_summary.csv"

# CSV herunterladen
df = pd.read_csv(url)

# Lokal speichern
df.to_csv("glfi.csv", index=False)

print("CSV saved.")