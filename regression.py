def regression_model(column_x, column_y):

    X = statsmodels.add_constant(new_df[column_x])
    Y = new_df[column_y]
    regressionmodel = statsmodels.OLS(Y,X).fit() #"ordinary lease squares"

    #Getting and calculating relevant values and round them up to 3 decimal points.
    Rsquared = round(regressionmodel.rsquared,3)
    slope = round(regressionmodel.params[1],3)
    intercept = round(regressionmodel.params[0],3)

    #plotting them into #dataviz
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(12,4))
    sns.regplot(x=column_x, y=column_y, data=new_df, marker="x", ax=ax1, color = 'g', scatter_kws={"s": 0.1}) # scatter
    sns.residplot(x=column_x, y=column_y, data=new_df, ax=ax2, scatter_kws={"s": 1}) # residual
    ax2.set(ylabel='Residuals')
    ax2.set_ylim(min(regressionmodel.resid)-1,max(regressionmodel.resid)+1)
    plt.figure()
    sns.distplot(regressionmodel.resid, kde=False, axlabel='Residuals', color='red') # histogram
    qqplot = statsmodels.qqplot(regressionmodel.resid,fit=True,line='45') #QQ plot created
    qqplot.suptitle("QQ Plot for Residuals",fontweight='bold',fontsize=14)

    #print the calculations and regression model
    print("R-squared = ",Rsquared)
    print("Regression equation: "+column_y+" = ",slope,"* "+column_x+" + ",intercept)
    #This python code is adpated from CS51 Session 1.2 and session 2.2. Revised by Steven Yang'24.
