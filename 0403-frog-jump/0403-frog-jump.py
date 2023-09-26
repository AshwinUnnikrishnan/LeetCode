class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # As stones.length is <= 2000 we can have a adjacency list to store possible jumps to reach a particular position
        if stones[1] != 1:
            return False
        
        n = len(stones)
        jumps = [[] for _ in range(n)]

        jumps[0].append(0), jumps[1].append(1)
        
        for i in range(1, n):
            
            #get previous jump possible values
            prev_jump_list = jumps[i]
            possible_jumps_next = []
            
            for jump_val in prev_jump_list:
                possible_jumps_next.append(jump_val), possible_jumps_next.append(jump_val-1), possible_jumps_next.append(jump_val+1)
            
            possible_jumps_next = list(set(possible_jumps_next))
            if len(possible_jumps_next) != 0:
                max_jump = max(possible_jumps_next)
                min_jump = min(possible_jumps_next)

                #if stones[i] > stones[i-1] + min_jump:
                #    return False

                for j in range(i+1, n):

                    dif = stones[j] - stones[i]
                    if dif in possible_jumps_next:
                        jumps[j].append(dif)
        if len(jumps[n-1]) != 0:
            return True
        return False