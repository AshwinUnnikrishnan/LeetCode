class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        i = len(nums2)-1
        
        while i>=0:
            
            if len(stack) == 0:
                stack.append(nums2[i])
                i -= 1
            else:
                if stack[-1] >= nums2[i]:
                    greater[nums2[i]]=stack[-1]
                    stack.append(nums2[i])
                    i -= 1
                else:
                    while len(stack) !=0 and stack[-1]<nums2[i]:
                        stack.pop()
        print(greater)
        
        res = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            if nums1[i] in greater.keys():
                res[i] = greater[nums1[i]]
            
        
        
        return res
        