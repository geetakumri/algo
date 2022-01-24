import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom
#n, p = 10, .5  # number of trials, probability of each trial

s = np.random.binomial(100, .5, 10**5)
ax=sns.distplot(s,kde=True,color='pink',hist_kws={"linewidth": 22,'alpha':0.77})
ax.set(xlabel='Binomial',ylabel='Frequency')
plt.show()

def prob():
    return random.randint(0,1)

def simulation_hund_times():
    head_count = 0
    for i in range(0,100):
        if(prob()==0):
            head_count+=1
    return head_count

def simulation_multi_times():
    prob_list = []
    for i in range(0,100000):
        prob_list.append(simulation_hund_times())  
    return prob_list

prob_list = simulation_multi_times()

def plot_sumulation(prob_list):
    ax=sns.distplot(prob_list,kde=True,color='pink',hist_kws={"linewidth": 22,'alpha':0.77})
    ax.set(xlabel='Binomial',ylabel='Frequency')
    plt.show()  


plot_sumulation(prob_list)
    

print(prob_list)
plot_sumulation(prob_list)