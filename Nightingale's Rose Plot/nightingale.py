#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:27:09 2020

@author: snitch30

PLEASE RUN THIS IN JUPYTER NOTEBOOK

"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import math
import plotly
import ipywidgets as widgets
from IPython.display import display

#df = px.data.wind()
direc='/data/'
fname='nightingale-data.xlsx'
dfs = pd.read_excel(direc+fname, sheet_name=None, header=1)['Sheet1']

asa=list(dfs['Average size of army'][:12].values)
aoc=list(dfs['All other causes'][:12].values)
for i in range(len(aoc)):
    aoc[i]=math.sqrt(aoc[i]*(1000/12))/(asa[i]*math.pi)
wi=list(dfs['Wounds & injuries'][:12].values)
for i in range(len(wi)):
    wi[i]=math.sqrt(wi[i]*(1000/12))/(asa[i]*math.pi)
zd=list(dfs['Zymotic diseases'][:12].values)
for i in range(len(zd)):
    zd[i]=math.sqrt(zd[i]*(1000/12))/(asa[i]*math.pi)


fig = go.Figure()

fig.add_trace(go.Barpolar(
    r=aoc,
    name='All other causes',
    marker_color='rgb(102, 102, 102)'
    ))


fig.add_trace(go.Barpolar(
    r=wi,
    name='Wounds & injuries',
    marker_color='rgb(210, 121, 121)'
))


fig.add_trace(go.Barpolar(
    r=zd,
    name='Zymotic diseases',
    marker_color='rgb(173, 216, 230)'
))


fig.update_traces(text=list(dfs['Month'][:12].values))
fig.update_traces(theta=list(dfs['Month'][:12].values))


fig.update_layout(
    title='Nightingale: Apr 1854 to Mar 1855, Zoomed and Rotated',
    font_size=12,
    legend_font_size=10,
    polar_bargap=0,
    polar_radialaxis_showgrid=True,
    polar_radialaxis_showline=True,
    polar_radialaxis_visible=False,
    polar_angularaxis_rotation=0,
    polar_angularaxis_showgrid=True,
    polar_angularaxis_showline=True,
    polar_angularaxis_showticklabels=True,
    polar_angularaxis_direction='clockwise',
    showlegend=False
    
)

fig.update_layout(height=520,width=520) 

fw1 = go.FigureWidget(fig)

fig2 = go.Figure()

fig2.add_trace(go.Barpolar(
    r=aoc,
    name='All other causes',
    marker_color='rgb(102, 102, 102)'
    ))


fig2.add_trace(go.Barpolar(
    r=wi,
    name='Wounds & injuries',
    marker_color='rgb(210, 121, 121)'
))


fig2.add_trace(go.Barpolar(
    r=zd,
    name='Zymotic diseases',
    marker_color='rgb(173, 216, 230)'
))


fig2.update_traces(text=list(dfs['Month'][:12].values))
fig2.update_traces(theta=list(dfs['Month'][:12].values))

fig2.update_layout(
    title='Nightingale: Apr 1854 to Mar 1855',
    font_size=12,
    legend_font_size=10,
    polar_bargap=0,
    polar_radialaxis_showgrid=True,
    polar_radialaxis_showline=True,
    polar_radialaxis_visible=False,
    polar_angularaxis_rotation=180,
    polar_angularaxis_showgrid=True,
    polar_angularaxis_showline=True,
    polar_angularaxis_showticklabels=True,
    polar_angularaxis_direction='clockwise',
    
)

fig2.update_layout(height=450,width=450) 

fw2 = go.FigureWidget(fig2)
sp = widgets.HBox([fw1,fw2])
display(sp)




