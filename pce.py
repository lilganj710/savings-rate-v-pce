import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def main():
    pce = pd.read_csv('PCEPI.csv', header=0, names=['index'])
    savings = pd.read_csv('PSAVERT.csv', header=0, names=['rate'])
    pce['index'] = pce['index'].pct_change()
    savings['rate'] = savings['rate'].pct_change()
    
    lag_v_corr = []
    for lag in range(0, 10):
        corr = pce['index'].corr(savings['rate'].shift(lag))
        lag_v_corr.append([lag, corr])
    
    lag_v_corr = pd.DataFrame(lag_v_corr, columns=['Lag', 'Correlation'])
    lag_v_corr.to_csv('lvc.csv', index=False)
    
    plt.plot(lag_v_corr['Lag'], lag_v_corr['Correlation'], 'bo')
    plt.xlabel('Lag')
    plt.ylabel('Correlation')
    plt.title('Correlation between savings rate and future PCE x-months into the future')
    plt.savefig(f'savings_v_PCE.pdf', bbox_inches='tight')
    plt.show()
    
main()