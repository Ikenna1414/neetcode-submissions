class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       index=0
       for index in range(len(arr)):
        if index < len(arr)-1:
            arr[index] = max(arr[index+1:])
        else:
            arr[index] = -1
    

       return arr 

        