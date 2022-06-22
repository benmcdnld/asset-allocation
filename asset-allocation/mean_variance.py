import numpy as np
import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier

def algorithm(sims=1000, max_w=0.3, ret_sd=0.01, risk_sd=0.01):
    """
    
    
    """
    # Reads risk/return inputs and correlation matrix

    return_risk_df = pd.read_excel('..\docs\optimization_assumptions_2022.xlsx',
                                sheet_name='return_risk', index_col=0)

    corr_df = pd.read_excel('..\docs\optimization_assumptions_2022.xlsx',
                        sheet_name='corr', index_col=0)

    expected_returns = return_risk_df.exp_return
    
    total_weights = []
    total_performance = []

    for sim in np.arange(sims):

        #Adds a layer of randomness to returns
        expected_returns = [er + ret_sd * np.random.randn() for er in return_risk_df.exp_return]

        #Adds a layer of randomness to risk
        expected_risk = [er + risk_sd * np.random.randn() for er in return_risk_df.exp_risk]

        # Produces covariance matrix from correlation matrix and standard deviation
        cov_df = corr_df.copy()
        
        for i in np.arange(return_risk_df.exp_risk.shape[0]):

            for j in np.arange(return_risk_df.exp_risk.shape[0]):

                cov_df.iloc[i,j] = cov_df.iloc[i,j] * return_risk_df.exp_risk[i] * return_risk_df.exp_risk[j]
        
        # Setup mean variance
        ef = EfficientFrontier(expected_returns, cov_df, weight_bounds=(0,max_w)) 
        clean_weights = ef.efficient_risk(0.12)  # find the portfolio that minimises volatility and L2_reg
        cleaned_weights = ef.clean_weights()

        # Saves each simulation's portfolios weights and performance 
        total_weights.append(list(cleaned_weights.values()))
        total_performance.append(list(ef.portfolio_performance(verbose=False)))
    
    print('WEIGHTS')
    # Takes the average of the simulation weights for each asset class 
    average_weights = np.mean(total_weights, axis=0)

    # Prints the weights
    for i in np.arange(average_weights.shape[0]):
        print(f'{corr_df.columns[i]}: {np.round(average_weights[i]*100, 2)}')

    print('')
    print('PERFORMANCE')

    # Takes the average of the simulation performance for each metric
    average_performance = np.mean(total_performance, axis=0)

    # Prints the metrics
    print(f'Expected return: {np.round(average_performance[0]*100,2)}')
    print(f'Expected risk: {np.round(average_performance[1]*100,2)}')
    print(f'Expected Sharpe: {np.round(average_performance[2],3)}')