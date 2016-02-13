import numpy as np
from arm import *

class MAB(object):
	def __init__(self, n=None, learning_rate=0.0):
		self.n = n
		self.arms = [Arm() for i in xrange(n)]
		self.max_multiplier = 0.0
		self.regret = 0.0
		self.total_revenue = 0.0
		self.optimal_revenue = 0.0
		self.learning_rate = learning_rate

	def configure_arms(self, names, prior_adjs, sample_sizes, true_metrics, costs, revenues):
		if (len(names) != self.n) or (len(prior_adjs) != self.n) or \
		(len(sample_sizes) != self.n) or (len(true_metrics) != self.n):
			print "Incorrect lengths"
			return 0
		for i in range(self.n):
			self.arms[i].name = names[i]
			self.arms[i].prior_adj = prior_adjs[i]
			self.arms[i].sample_size = sample_sizes[i]
			self.arms[i].true_metric = true_metrics[i]
			self.arms[i].cost = costs[i]
			self.arms[i].revenue = revenues[i]
			self.arms[i].get_multiplier()
		self.max_multiplier = max([self.arms[i].multiplier for i in xrange(self.n)])

	def simulate(self, B=1000):
		for i in xrange(B):
			self.iterate()
		self.compute_regret()

	def iterate(self):
		results = map(self.generate_results, self.arms)
		self.total_revenue += self.compute_revenue(results)
		self.optimal_revenue += self.max_multiplier*self.get_total_sample_size()
		self.adjust_sample_sizes(results)

	def adjust_sample_sizes(self, results):
		total_sample_size = self.get_total_sample_size()
		max_res = max(results)
		if max_res < 1:
			scaled_results = [1.0]*self.n
			max_res = 1.0
		else:
			scaled_results = [result/max_res for result in results]
		
		for i in range(self.n):
			self.arms[i].running_sample_size += self.arms[i].sample_size
			self.arms[i].sample_size *= (scaled_results[i] + (1-scaled_results[i])*self.learning_rate*scaled_results[i])
			# self.arms[i].sample_size *= scaled_results[i]/(1+scaled_results[i]*self.learning_rate)
		scaler = (self.get_total_sample_size()) / (total_sample_size)
		for i in range(self.n):
			self.arms[i].sample_size /= scaler

	def compute_revenue(self, results):
		sum_temp = 0.0
		for i in range(self.n):
			temp_multiplier = (self.arms[i].revenue - self.arms[i].cost) * results[i]
			sum_temp += temp_multiplier * self.arms[i].sample_size
		return sum_temp

	def compute_regret(self):
		self.regret = 1 - self.total_revenue/self.optimal_revenue

	def generate_results(self, arm):
		if arm.sample_size < 1:
			return 0
		return np.mean(np.random.binomial(1, arm.true_metric, arm.sample_size))

	def get_total_sample_size(self):
		return sum([self.arms[i].sample_size for i in xrange(self.n)])

	def print_arms(self):
		for i in range(self.n):
			self.arms[i].print_arm()

	def print_mab(self):
		print "Number of arms: " + str(self.n)
		print "Max Multiplier: " + str(self.max_multiplier)
		print "Regret: " + str(self.regret)
		print "Total Revenue: " + str(self.total_revenue)
		print "Optimal Revenue: " + str(self.optimal_revenue)
		print ""

# Not necessarily binomial
# How to use prior adjustments 
# Didn't I have a learning rate?
# acceleration and robustness


# adjustment rate
# random adjustment rate
# 
# novelty, primacy
# 
# track regret, loss
# 
# true relative worth of each
# sample size for each
# prior adjustment rate for each



