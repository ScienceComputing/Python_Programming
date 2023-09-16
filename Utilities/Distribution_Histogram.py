from scipy.stats import norm, poisson, gamma

# Sample 1000 times from various distributions and make the histograms on the frequency of observations
x = norm.rvs(loc=1, scale=1, size=1000, random_state=200) # This is a normal distribution, support on reals
# The scale keyword specifies the standard deviation
y = poisson.rvs(mu=6, size=1000, random_state=200) # This is a Poisson distribution, support on nonnegative integers
z = gamma.rvs(a=1,scale=1, size=1000, random_state=200) # This is a Gamma distribution, support on positive reals

bins = np.linspace(-4,20,100)
plt.hist(x, bins=bins, color='blue', alpha=0.7, label='Normal(1,1^2)')
plt.hist(y, bins=bins, color='red', alpha=0.7, label='Poisson(6)')
plt.hist(z, bins=bins, color='purple', alpha=0.7, label='Gamma(1,1)')
plt.legend(loc='upper left')
plt.ylabel('Frequency of observations')
plt.xlabel('Observed value')
