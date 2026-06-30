class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = 101
        max_profits = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profits = price - min_price 
                if profits > max_profits:
                    max_profits = profits
            
        return max_profits