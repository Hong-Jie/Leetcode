"""

1.  Max Heapify the first K points by their Euclidean distances.
2.  From the K+1 point to the end, we calculate its Euclidean distance and compare to the
    K-point heap
3.  If the distance is larger than the root (maximum) of the K-point heap, then
    1) pop the root,
    2) insert the point,
    3) heapify the K-point heap

"""

class Solution:
    def maxHeapify(self, hList, i):
        largest = i
        left = i*2+1
        right = i*2+2
        n = len(hList)
                            
        if left<n and hList[left][0]>hList[largest][0]:
            largest = left
        if right<n and hList[right][0]>hList[largest][0]:
            largest = right
            
        if largest != i:
            hList[i], hList[largest] = hList[largest], hList[i]
            self.maxHeapify(hList, largest)
    
    def kClosest(self, points, K):
        
        if len(points) == 1:
            return points
        
        heapDistances = []
        
        for idx in range(K):
            heapDistances.append((pow(points[idx][0], 2)+pow(points[idx][1], 2),idx))
        
        for idx in reversed(range(len(heapDistances)//2)):
            self.maxHeapify(heapDistances, idx)
            
        for idx in range(K, len(points)):
            eud = pow(points[idx][0], 2)+pow(points[idx][1], 2)
            if eud < heapDistances[0][0]:
                heapDistances[0] = (eud, idx)
                self.maxHeapify(heapDistances, 0)
        
        KClosestPoints = [points[idx] for eud, idx in heapDistances]
        return KClosestPoints