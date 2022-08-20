import sys

def max_profit(price_list):
	profit = 0 #최댓값 선언 : 원래는 profit = -sys.maxsize으로 설정할 텐데 입력값이 빈 배열일 경우를 대비하여 0으로 설정함.
	min_price = sys.maxsize #최솟값 선언

	for price in price_list:
		min_price = min(min_price, price)
		profit = max(profit, price - min_price)

	return profit

print(max_profit([7,1,6,3,6,4]))
