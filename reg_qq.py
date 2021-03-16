
global regressionmodel 
regressionmodel = statsmodels.OLS(new_df['Price ($ in millions)'],statsmodels.add_constant(new_df['Living Area (sqft)'])).fit() # OLS = "ordinary least squares"
regressionmodel.summary() #print the summary of OLS Regression Results
#This python code is adpated from CS51 Session 2.2 and revised by Steven Yang.


qqplot = statsmodels.qqplot(regressionmodel.resid,fit=True,line='45')
qqplot.suptitle("Normal Probability (\"QQ\") Plot for Residuals",fontweight='bold',fontsize=14)
