class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices.append(0)
        inc_stack = []
        max_profits = 0

        for price_i in range(len(prices)):

            while len(inc_stack) != 0 and prices[price_i] < prices[inc_stack[-1]]:

                prev_price = prices[inc_stack.pop()]
                if len(inc_stack) > 0:
                    curr_profits = prev_price - prices[inc_stack[0]]
                    if curr_profits > max_profits:
                        max_profits = curr_profits

            inc_stack.append(price_i)
                
            
        return max_profits