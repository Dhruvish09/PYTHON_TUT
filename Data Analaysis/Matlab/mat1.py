# .ploat
# .label
# .title
# .legend

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[964,287,42,390,64,800,523]

plt.plot(x,y,label='Youtube views')
plt.xlabel('Week days')
plt.ylabel('Views')
plt.title('Youtube view on daily base')
plt.legend(loc='upper left')


plt.show()