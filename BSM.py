import math
from scipy.stats import norm

#function N is th cdf of Standard Normal distribution
def N(x):
    y = norm.cdf(x, loc=0, scale=1)
    return y

#BS_model means Black-Scholes model
#for the outputs, the first one is the price of call option
#and the second one is the price of put option
def BS_model(S0, K, r, T, sigma):
    d1 = (math.log(S0/K) + (r+(sigma**2)/2)*T)/(sigma*math.sqrt(T))
    d2 = d1 - (sigma*math.sqrt(T))
    return S0*N(d1) - K*math.exp(-1*r*T)*N(d2), \
        K*math.exp(-1*r*T)*N(-d2) - S0*N(-d1)

if __name__ == "__main__":
    print("test")



