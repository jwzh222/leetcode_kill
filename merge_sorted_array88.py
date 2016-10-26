class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        flag=0
        l=[]
        j=0
        while j < n:
            if (nums2[j]<= nums1[flag]):
                l.append(nums2[j])
            elif(nums2[j]>nums1[flag]):
                i=flag+1
                while i<m:
                    if(nums2[j]<=nums1[i]):
                        l+=nums1[flag:i]
                        l.append(nums2[j])
                        flag=i
                        break
                    i+=1
                if(i==m):
                    l+=nums1[flag:]+nums2[j:]
            j+=1 
        return l    

if __name__ == '__main__':
    a=Solution()
    nums1=[1,2,4,5]
    nums2=[1,3,4,6]
    print a.merge(nums1,4,nums2,4)