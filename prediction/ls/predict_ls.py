
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import requests

import tensorflow as tf




#url = 'https://coronapolation.baremetal.rocks/infizierte/05111?since=2020-03-1'


url = 'https://coronapolation.baremetal.rocks/api/infizierte/05111?since=2020-03-1'
response = requests.get(url)
resp = response.json()


rest_data = []

for data in resp['days']:
    rest_data.append(data[1])

arr_data = np.asanyarray(rest_data)


mu, std = norm.fit(arr_data)



# Generate some data for this demonstration.
data = norm.rvs(10.0, 2.5, size=500)


#mu1 = 9.84
#std1 = 4
# Fit a normal distribution to the data:
mu, std = norm.fit(arr_data)



# Plot the histogram.
plt.hist(arr_data, bins=25, density=True, alpha=0.6, color='g')



#plt.plot(arr_data)
# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)

plt.show()







if False:




    print('Done')