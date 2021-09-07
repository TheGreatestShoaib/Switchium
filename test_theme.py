import matplotlib.pyplot as plt
from numpy as np
import json 
import csv
import os


class Testing():

	def __init__(self,func,args,names,results):
		self.func = func
		self.args = args
		self.names = names
		self.results = results


	def patter_checker(self,hash):

		for _ in range(len(self.results)):
			for x in range(10):
				if self.results[x] == hash:
					content = self.results[x]
					with open("assets.csv","w") as cs:
						cs.write(content)
					return True

		return False
