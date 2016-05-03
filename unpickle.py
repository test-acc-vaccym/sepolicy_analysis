#!/usr/bin/env python3
import selinux
import sepolicy  

import pickle
import networkx as nx

import os, sys, inspect
# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"setools")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import setools

import policy_data_collection as data
import evaluation_functions as evaluation

from collections import defaultdict



file = open('data/rules_grouping_file_process.bin', 'rb')
G_g = pickle.load(file)
file.close()

file = open('data/rules_file_process.bin', 'rb')
G = pickle.load(file)
file.close()

#print("Edges> ", len(G.edges()), " nodes> ", len(G.nodes()))
#print(G.edges(data=True)[0])
#print(str(G.edges(data=True)[0][0]))
#print(str(G.edges(data=True)[0][1]))
'''for edge in G.edges(data=True):
	if edge[0] != edge[1] and edge[2].get("process") != None:
		print(edge)
		break
'''

results, transitions = evaluation.find_type_transition_execution(G_g)
'''
for a,b,c in results:
	if (str(a) == "accountsd") and (str(b) == "abrt") and (str(c) == "abrt"):
		print("YEAH")
		print(a.domains, "\n" ,b.domains, "\n" , c.types)
		print(G_g.get_edge_data(a,b))
		print(G_g.get_edge_data(b,c))
		print(G_g.get_edge_data(a,c))
'''
results2, suspicious = evaluation.expand_type_transition_execution(G,transitions)
#print(results-results2)
suspicious_p = defaultdict(set)
for a,b,c in suspicious:
	suspicious_p[(a,b)].add(c)
#print("\n\n".join([str(x)+" > " + ", ".join(y) for x,y in suspicious_p.items() if len(y) > 5]))
sus pmes= set()
for key, value in suspicious_p.items():
#	if len(value) > 5:
		susp.add(key)

print("\n".join([str(x) for x in susp]))