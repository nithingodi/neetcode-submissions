class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_valid_rows(board) and self.is_valid_cols(board) and self.is_valid_boxes(board) 
        
    def is_valid_rows(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen=set()
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        return True

    def is_valid_cols(self, board: List[List[str]]) -> bool:
        for c in range(9):
            seen=set()
            for r in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        return True

    def is_valid_boxes(self, board: List[List[str]]) -> bool:

        for box_r in range(0,9,3):
            for box_c in range(0,9,3):
                seen=set()

                for r in range(3):
                    for c in range(3):
                        val= board[box_r+r][box_c+c]
                        if val==".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True



