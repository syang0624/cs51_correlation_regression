
def scatter_plot1(x, y, title, color): #define the scatter plot function
    plt.figure()
    plt.scatter(x, y, s=5, c=color)
    plt.title(title, fontsize=20,y=1.2, pad=-14)
    plt.xlabel('living area (sqft)', fontsize=15)
    plt.ylabel('price ($ in millions)', fontsize=15)
    xmax = max(x) #get the maximum value of x
    ymax = max(y) #get the maximum value of y

    #calculation
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.plot([0, xmax], [intercept, slope * xmax + intercept]) #plot the equation

    # adding legend
    equation = 'y = ' + str(round(slope,3)) + 'x' + ' + ' + str(round(intercept,3))
    rvalue = 'r = ' + str(round(r_value,3))
    plt.text(3000, 7000000, equation,fontsize=15,fontweight='bold')
    plt.text(300, 7000000, rvalue,fontsize=15,fontweight='bold')
    #This python code is adpated from CS51 Session 1.2 and revised by Steven Yang.
def scatter_plot2(x, y, title, color):
    plt.figure()
    plt.scatter(x, y, s=5, c=color)
    plt.title(title, fontsize=20,y=1.2, pad=-14)
    plt.xlabel('Living area (sqft)', fontsize=15)
    plt.ylabel('Price ($ in millions)', fontsize=15)
    xmax = max(x)
    ymax = max(y)

    #calculation
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.plot([0, xmax], [intercept, slope * xmax + intercept])
    

    # adding legend
    equation = 'y = ' + str(round(slope,3)) + 'x' + ' + ' + str(round(intercept,3))
    rvalue = 'r = ' + str(round(r_value,3))
    plt.text(1500, 1500000, equation,fontsize=15,fontweight='bold')
    plt.text(300, 1500000, rvalue,fontsize=15,fontweight='bold')
    # second function is needed to fix the location of rvalue and equation


scatter_plot1(living_area, price, 'Correlation between living area and price', 'green')
scatter_plot2(new_living_area, new_price, 'Correlation between living area and price', 'yellow')
