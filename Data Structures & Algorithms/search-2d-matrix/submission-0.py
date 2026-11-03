class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        row = 0

        while l < r:
            c = (l+r)//2
            if target >= matrix[c][0] and target <= matrix[c][-1]:
                row = c
                break
            elif target < matrix[c][0]:
                r = c
            else:
                l = c + 1
  

        l,r = 0, len(matrix[row])-1
        while l < r:
            c = (l+r)//2
            if matrix[row][c] == target:
                return True
            elif target < matrix[row][c]:
                r = c
            else:
                l = c + 1
        return False
