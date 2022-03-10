import numpy as np
from matplotlib import pyplot as plt
# import pandas as pd

def mul(x,c):
    d = x * c
    return d
def tellMe(a):
    print(a[1])

x = np.arange(0, 2, 0.2)
tellMe(x)


# plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g-.')

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**4, color='forestgreen', marker='^', markersize=9)
plt.grid(True, axis='both', color='red', alpha=0.1, linestyle='--')
# plt.xticks([0, 1, 2])
plt.xticks(np.arange(0,2.2,0.2))
plt.yticks(np.arange(0, 13, 1))

plt.show()

    # def dist(xm,ym,xo,yo,dl,mod,mod0):
#     ii = np.where((xm>xo-dl)&(xm<xo+dl))[0]
#     jj = np.where((ym>yo-dl)&(ym<yo+dl))[0]
#     H = [];    xx = xm[ii];    yy = ym[jj]
# #    print(ii,jj,xx,yy)
#     if (len(ii)>=1) & (len(jj)>=1):
#        a = np.where(mod0[0,jj,ii].mask == False);
#        if (len(a) > 0):
#            dis = np.sqrt((yy-yo)**2+(xx-xo)**2)
#            pt  = np.where(dis == np.min(dis))
#            Htmp= mod[:,jj,ii]
#            if len(pt[0]) > 0 :
#               H   = np.mean(Htmp,axis=1)
#            else:
#               H   = Htmp[pt[0]]
#     return H



