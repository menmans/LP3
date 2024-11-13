class ItemValue:
    def __init__(self, wt_, val_, ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ / wt_  # Calculate value per unit weight

    def __lt__(self, other):
        # Define comparison for sorting to ensure descending order by cost (value per weight)
        return self.cost > other.cost  


def fractionalKnapSack(wt, val, capacity):
    # Create list of ItemValue objects
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
    
    # Sort items by descending cost (value per weight)
    iVal.sort()  # No reverse needed since __lt__ is defined for descending order
    
    totalValue = 0.0  # Initialize total value in the knapsack as a float for precision
    
    for i in iVal:
        if capacity == 0:
            break  # Stop if knapsack is full

        curWt = i.wt
        curVal = i.val
        
        if capacity >= curWt:
            # If the item can be fully added to the knapsack
            capacity -= curWt
            totalValue += curVal
        else:
            # If only part of the item can be added, add the fraction of its value
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = 0  # Knapsack is now full

    return round(totalValue, 2)  # Rounding the result for clarity


# Example usage
if __name__ == "__main__":
    wt = [1, 3, 5, 4, 1, 3, 2]
    val = [5, 10, 15, 7, 8, 9, 4]
    capacity = 15
    
    maxValue = fractionalKnapSack(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
