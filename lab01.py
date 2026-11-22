# # 1. Implement search(nums: List[int], target: int) -> int and myPow(x: float, n: int) ->
# # float functions taking an integer array/target and base/exponent pairs, returning index and computed
# # value respectively.

          # binary search 
def search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

         
def myPow(x,n):
    if n == 0:
        return 1

    if n < 0:
        x = 1/x
        n = -n

    result = 1

    while n > 0:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result

    # for searching
s=search([1,2,3,4,5,6,7,8,9] ,8)
print("index of given number is :",s)

     #for base and exponent
p = myPow(5,2)
print("value of given base and exponent:",p)



