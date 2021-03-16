plt.hist(new_living_area, alpha=1, linewidth=5)
plt.title("Distribution of Living Areas", fontsize = 15)
plt.xlabel("Living Areas (sqft)", fontsize = 10)
plt.ylabel("Frequency of data", fontsize = 10)
plt.gcf().set_figwidth(10)

plt.axvline(new_living_area_mean, color='g', label = "Mean = 2012.41") #label legend for mean
plt.axvline(new_living_area_median, color='r', label = "Median = 1890.00")#label legend for median
plt.legend()
ax=plt.gca()
ax.set_facecolor('w')
plt.show()
