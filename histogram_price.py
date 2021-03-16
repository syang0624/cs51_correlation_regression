plt.hist(new_price, alpha=1, linewidth=5)
plt.title("Distribution of house prices", fontsize = 15)
plt.xlabel("House Prices ($ millions)", fontsize = 10)
plt.ylabel("Frequency of data", fontsize = 10)
plt.gcf().set_figwidth(10)

plt.axvline(new_price_mean, color='g', label = "Mean = 503113.84") #label legend for mean
plt.axvline(new_price_median, color='r', label = "Median = 445000.00")#label legend for median
plt.legend()
ax=plt.gca()
ax.set_facecolor('w')
plt.show()
