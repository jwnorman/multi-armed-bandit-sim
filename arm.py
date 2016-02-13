import numpy as np

class Arm(object):	
	def __init__(self, name=None, prior_adj=None, sample_size=None,
			true_metric=None, cost=None, revenue=None, distribution=None):
		self.name = name
		self.prior_adj = prior_adj
		self.sample_size = sample_size
		self.true_metric = true_metric	
		self.cost = cost
		self.revenue = revenue
		self.running_sample_size = 0
		self.multiplier = 0.0
		self.distribution = distribution

	def get_multiplier(self):
		self.multiplier = (np.array(self.revenue) - np.array(self.cost)) * np.array(self.true_metric)

	def print_arm(self):
		print "Name: " + str(self.name)
		print "Prior Adjustment: " + str(self.prior_adj)
		print "Sample Size: " + str(self.sample_size)
		print "True Metric: " + str(self.true_metric)
		print "Cost: " + str(self.cost)
		print "Revenue: " + str(self.revenue)
		print "Running Sample Size: " + str(self.running_sample_size)
		print "Multiplier: " + str(self.multiplier)
		print ""