"""
This is a collection of short scripts that tests the Stats.py package
in the same directory. It calculates the average point buy for each system
that is currently implemented.
"""

calc_pb_prob_roll_three = True
calc_pb_prob_roll_four_dl = True
calc_pb_prob_roll_three_with_reroll = True
calc_pb_prob_roll_four_dl_with_reroll = True

import Stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab

N_rolls = 100000

Stat_obj = Stats.Stats()

if calc_pb_prob_roll_three:
    pb_array = []
    for i in range(N_rolls):
        pb_array.append(Stat_obj.pb_value(Stat_obj.roll_three()))
    pb_array = np.array(pb_array)
    size = max(pb_array)-min(pb_array)
    mu,sigma = norm.fit(pb_array) #Mean and stddev of distribution
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(pb_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.show()

if calc_pb_prob_roll_three_with_reroll:
    pb_array = []
    for i in range(N_rolls):
        pb_array.append(Stat_obj.pb_value(Stat_obj.roll_three(reroll=True)))
    pb_array = np.array(pb_array)
    size = max(pb_array)-min(pb_array)
    mu,sigma = norm.fit(pb_array) #Mean and stddev of distribution
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(pb_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.show()

if calc_pb_prob_roll_four_dl:
    pb_array = []
    for i in range(N_rolls):
        pb_array.append(Stat_obj.pb_value(Stat_obj.roll_four_drop_lowest(reroll=False)))
    pb_array = np.array(pb_array)
    size = max(pb_array)-min(pb_array)
    mu,sigma = norm.fit(pb_array) #Mean and stddev of distribution
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(pb_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.show()

if calc_pb_prob_roll_four_dl_with_reroll:
    pb_array = []
    for i in range(N_rolls):
        pb_array.append(Stat_obj.pb_value(Stat_obj.roll_four_drop_lowest(reroll=True)))
    pb_array = np.array(pb_array)
    size = max(pb_array)-min(pb_array)
    mu,sigma = norm.fit(pb_array) #Mean and stddev of distribution
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(pb_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.show()

find_roll_three_dist = True
find_roll_three_with_reroll_dist = True
find_roll_four_dl_dist = True
find_roll_four_dl_with_reroll_dist = True

N_rolls = 10000

if find_roll_three_dist:
    roll_array = []
    for i in range(N_rolls):
        roll_array.append(Stat_obj.roll_three(reroll=False))
    roll_array = np.array(roll_array).flatten()
    size = max(roll_array)-min(roll_array)
    mu,sigma = norm.fit(roll_array)
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(roll_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.title("Roll three")
    plt.xlabel("Rolls")
    plt.show()

if find_roll_three_with_reroll_dist:
    roll_array = []
    for i in range(N_rolls):
        roll_array.append(Stat_obj.roll_three(reroll=True))
    roll_array = np.array(roll_array).flatten()
    size = max(roll_array)-min(roll_array)
    mu,sigma = norm.fit(roll_array)
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(roll_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.title("Roll three with reroll")
    plt.xlabel("Rolls")
    plt.show()

if find_roll_four_dl_dist:
    roll_array = []
    for i in range(N_rolls):
        roll_array.append(Stat_obj.roll_four_drop_lowest(reroll=False))
    roll_array = np.array(roll_array).flatten()
    size = max(roll_array)-min(roll_array)
    mu,sigma = norm.fit(roll_array)
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(roll_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.title("Roll four drop lowest")
    plt.xlabel("Rolls")
    plt.show()

if find_roll_four_dl_with_reroll_dist:
    roll_array = []
    for i in range(N_rolls):
        roll_array.append(Stat_obj.roll_four_drop_lowest(reroll=True))
    roll_array = np.array(roll_array).flatten()
    size = max(roll_array)-min(roll_array)
    mu,sigma = norm.fit(roll_array)
    print "Mean = %f\nStddev = %f"%(mu,sigma)
    n,bins,patches = plt.hist(roll_array,bins=size+1,normed=True,alpha=0.5,facecolor='g')
    y = mlab.normpdf(bins,mu,sigma)
    plt.plot(bins,y,'r--',linewidth=2)
    plt.title("Roll four drop lowest with reroll")
    plt.xlabel("Rolls")
    plt.show()
