import datetime as dt

def IsPalindrome(num):
    nums = list(str(num))
    for left in range(len(nums)):

        right = (len(nums)-1)-left
        if left > right:
            return True

        if nums[left] != nums[right]:
            return False

def LargetPalinddromeProduct(largest, smallest, smallestFactor, largestFactor, places):
    original = smallestFactor
    while largest > smallest:
        smallestFactor = original
        if IsPalindrome(largest):
            while smallestFactor <= largestFactor:
                if largest % smallestFactor == 0 and len(list(str(largest/smallestFactor))) == places:
                    return largest
                smallestFactor += 1
        largest -= 1


n1 = dt.datetime.now()
print LargetPalinddromeProduct(999999, 100001, 100, 999, 3)
n2 = dt.datetime.now()
print (n2-n1).microseconds/1e6
