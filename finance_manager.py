import numpy as np
import pandas as pd

import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')

import tabula as tb



# PDF --> CSV: Download new PDF bank balance. Convert to CSV. Add them at top of same CSV file, separated by blank line. 

df = tb.read_pdf('1410890-80_releve_de_postes_2024-02-17_00-50-44695.pdf',pages="all")