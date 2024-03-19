class Solution(object):
    def findMinArrowShots(self, points):

        points.sort()
        n = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                n -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr

        return n

    '''
    class Solution(object):
    def findMinArrowShots(self, points):
        
        points.sort()
        arrows = 1
        end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > end: 
                arrows += 1  
                end = balloon[1] 
            else:
                end = min(end, balloon[1])
        
        return arrows
    '''