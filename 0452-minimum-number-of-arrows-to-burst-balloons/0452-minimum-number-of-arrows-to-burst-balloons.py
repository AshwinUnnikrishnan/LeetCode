class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
    
        # Sort balloons by their end points
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        initial_arrow = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0]<=initial_arrow:
                print("AD")
                continue
            arrows += 1
            initial_arrow = points[i][1]
        
        print(points)
        return arrows