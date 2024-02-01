class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        n = len(nums) - 1
        res = [-1] * (n + 1)
        
        while n>=0:
            
            if len(st) == 0:
                st.append(nums[n])
                n -= 1
            
            elif st[-1] > nums[n]:
                res[n] = st[-1]
                st.append(nums[n])
                n -= 1
            
            elif st[-1] <= nums[n]:
                while len(st) != 0 and st[-1] <= nums[n]:
                    st.pop()
        n = len(nums)-1
        while len(st) != 0:
            while len(st) != 0 and st[-1] <= nums[n]:
                    st.pop()
            if len(st) == 0:
                break

            res[n] = st[-1]
            st.append(nums[n])
            n -= 1
        return res
                
        