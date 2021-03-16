
new_price_mean = round(new_price.mean(),2) #round up to two digits
new_price_median = new_price.median() 
sd_new_price = round(np.std(new_price),2) #round up to two digits
new_living_area_mean = round(new_living_area.mean(),2)
new_living_area_median = new_living_area.median()
sd_new_iving_area = round(np.std(new_living_area),2)

def mode(lst): #since I have multiple modes, I created another function for mode
    L1=[] #count the occurrence of each number and append or add findings to the list
  
    i = 0 #count the numbers and put them into L1
    while i < len(lst) : 
        L1.append(lst.count(lst[i])) 
        i += 1

    # the occurrences for each number in sorted lst 
    # create a custom dictionary d1 for k : V 
    # k = value, v = occurence

    d1 = dict(zip(lst, L1))  
    d2=[k for (k,v) in d1.items() if v == max(L1)] # the k values with the highest v values. 
    return d2

print("Your # of data for price is:",len(new_price))
print("Mean for price is:", price_mean)
print("Median for price is:", price_median)
print("Mode for price is:", sorted(mode(price.to_list())))
print("Standard Deviation for price is:", sd_price)
print("Your range for price is:", max(price) - min(price))
print("######")
print("Your # of data for living_area is:",len(new_living_area))
print("Mean for living_area is:", living_area_mean)
print("Median for living_area is:", living_area_median)
print("Mode for living_area is:", sorted(mode(living_area.to_list())))
print("Standard Deviation for living_area is:", sd_living_area)
print("Your range for living_area is:", max(living_area) - min(living_area))
