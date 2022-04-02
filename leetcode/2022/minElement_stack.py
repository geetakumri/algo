class Solution:
    def __init__(self):
        pass

    def min_element_stack(self, min_stk):
        if min_stk:
            return min_stk[-1]
        else:
            return None

    def add_element(self, stk, min_stk, ele):
        if not stk or ele < min_stk[-1]:
            min_stk.append(ele)
        stk.append(ele)

    def pop_element(self, stk, min_stk):
        ele = stk[-1]
        if ele in min_stk:
            return stk.pop(), min_stk.pop()
        else:
            return stk.pop()


obj = Solution()
stk = []
min_stk = []

obj.add_element(stk, min_stk, 10)
print(obj.min_element_stack(min_stk))
obj.add_element(stk, min_stk, 20)
print(obj.min_element_stack(min_stk))
obj.add_element(stk, min_stk, 50)
print(obj.min_element_stack(min_stk))
obj.pop_element(stk, min_stk)
print(obj.min_element_stack(min_stk))
obj.pop_element(stk, min_stk)
print(obj.min_element_stack(min_stk))
obj.add_element(stk, min_stk, 5)
print(obj.min_element_stack(min_stk))
obj.pop_element(stk, min_stk)
print(obj.min_element_stack(min_stk))
