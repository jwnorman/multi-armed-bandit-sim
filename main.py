from mab import *

def main():
	mab = MAB(3, 1)
	mab.configure_arms(names=["Control", "Treatment1", "Treatment2"],
		prior_adjs=[.6, .5, .4],
		sample_sizes=[100, 100, 100],
		true_metrics=[.9, .30, .01],
		costs=[0.0, 0.0, 0.0],
		revenues=[1.0, 1.0, 1.0])
	mab.simulate()
	mab.print_arms()
	mab.print_mab()

main()