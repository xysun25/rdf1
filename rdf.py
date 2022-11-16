import MDAnalysis as mda
import numpy as np
from MDAnalysis.analysis import rdf
import matplotlib.pyplot as plt

u = mda.Universe ("lmp.data","eq_6ns.xyz")
# print(u)
il_num = 500
resnames = ['cati']*il_num+['anio']*il_num+['lmxene']*1+['rmxene']*1
ag1 = u.select_atoms("resid 1001 and type 23")
# print(lmxO)
ag2 = u.select_atoms("resid 1:500 and type 16")
# print(catiH)
ss_rdf =rdf.InterRDF_s(ag1,ag2,nbin=75,range=(0.0,15.0),density=True)
ss_rdf.run()
