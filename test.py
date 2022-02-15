import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def mul(x,c):
    d = x * c
    return d

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


def tellMe(a):
    if a == 1:
        print("tell me!!!")

tellMe(1)
# print(tellMe(1))
tellMe(1)
tellMe(1)
tellMe(1)