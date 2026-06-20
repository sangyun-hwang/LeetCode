# Date: 2026.06.20
# Problem: 901. Online Stock Span
#
# Approach: Monotonic Stack + Span Compression
#
# 매일 주식 가격이 하나씩 들어올 때,
# 오늘 가격보다 작거나 같은 가격이 왼쪽으로 연속해서 며칠 이어졌는지 구하는 문제.
#
# 단순히 매번 왼쪽으로 하나씩 확인하면 O(N^2)이 될 수 있다.
#
# 핵심 아이디어:
# - 오늘 가격보다 큰 가격을 만나면 그 앞은 더 볼 필요가 없다.
# - 오늘 가격보다 작거나 같은 과거 가격들은 모두 오늘 span에 포함된다.
# - 이미 계산된 과거 span을 함께 저장하면 여러 날짜를 한 번에 건너뛸 수 있다.
#
# stack에는 (price, span)을 저장한다.
#
# 현재 price에 대해:
# - stack top의 price가 현재 price보다 작거나 같으면 pop한다.
# - pop한 원소의 span을 현재 span에 더한다.
# - 더 큰 price를 만나면 멈춘다.
# - 현재 (price, span)을 stack에 저장한다.
#
# 비교가 <= 인 이유:
# - 문제에서 오늘 가격보다 "작거나 같은" 가격까지 span에 포함하기 때문이다.

class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)