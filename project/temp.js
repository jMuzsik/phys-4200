/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
  const rowLen = board.length;
  const colLen = board[0].length;
  function backtrack(newBoard, row, col, index) {
    /* Step 1). check the bottom case. */
    console.log(index)
    if (index >= word.length) return true;

    /* Step 2). Check the boundaries. */
    if (
      row < 0 ||
      row === rowLen ||
      col < 0 ||
      col === colLen ||
      newBoard[row][col] !== word[index]
    ) {
      return false;
    }

    /* Step 3). explore the neighbors in DFS */
    // mark the path before the next exploration
    newBoard[row][col] = null;
    const rowOffsets = [0, 1, 0, -1];
    const colOffsets = [1, 0, -1, 0];
    for (let d = 0; d < 4; d++) {
      if (backtrack(newBoard, row + rowOffsets[d], col + colOffsets[d], word, index + 1)) {
        // return without cleanup
        return true;
      }
    }

    /* Step 4). clean up and return the result. */
    newBoard[row][col] = word[index];
    return false;
  }
  for (let i = 0; i < rowLen; i++) {
    for (let j = 0; j < colLen; j++) {
      if (backtrack(board, i, j, 0)) return true;
      console.log(backtrack(board, i, j, 0));
    }
  }
  return false;
};
