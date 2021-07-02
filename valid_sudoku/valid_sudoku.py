class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for x in range(9)]
        cols = [[] for x in range(9)]
        boxes = [[] for x in range(9)]
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n in rows[i]:
                    return False
                elif n in cols[j]:
                    return False
                elif n in boxes[3 * (i // 3) + j // 3]:
                    return False
                elif n != ".":
                    rows[i].append(n)
                    cols[j].append(n)
                    boxes[3 * (i // 3) + j // 3].append(n)
        
        return True
