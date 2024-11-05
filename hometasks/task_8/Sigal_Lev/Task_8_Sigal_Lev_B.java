import java.util.ArrayList;
import java.util.List;

class Queen {
    private final int row;
    private final int col;

    public Queen(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public boolean conflictsWith(Queen other) {
        return this.row == other.row ||
               this.col == other.col ||
               Math.abs(this.row - other.row) == Math.abs(this.col - other.col);
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }
}

class Board {
    public final int size;
    private final List<Queen> queens;

    public Board(int size) {
        this.size = size;
        this.queens = new ArrayList<>();
    }

    public boolean placeQueen(int row, int col) {
        Queen queen = new Queen(row, col);
        for (Queen q : queens) {
            if (queen.conflictsWith(q)) {
                return false;
            }
        }
        queens.add(queen);
        return true;
    }

    public void removeQueen(int row) {
        queens.removeIf(q -> q.getRow() == row);
    }

    public boolean isSolved() {
        return queens.size() == size;
    }

    public void display() {
        String[][] board = new String[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                board[i][j] = "-  ";
            }
        }
        for (Queen queen : queens) {
            board[queen.getRow()][queen.getCol()] = "Q  ";
        }
        for (String[] row : board) {
            for (String cell : row) {
                System.out.print(cell);
            }
            System.out.println();
        }
        System.out.println();
    }
}

class EightQueensSolver {
    private final Board board;

    public EightQueensSolver(int size) {
        this.board = new Board(size);
    }

    public boolean solve(int row) {
        if (row >= board.size) {
            return true;
        }
        for (int col = 0; col < board.size; col++) {
            if (board.placeQueen(row, col)) {
                if (solve(row + 1)) {
                    return true;
                }
                board.removeQueen(row);
            }
        }
        return false;
    }

    public void displaySolution() {
        if (solve(0)) {
            board.display();
        } else {
            System.out.println("Решение не найдено.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        EightQueensSolver solver = new EightQueensSolver(8);
        solver.displaySolution();
    }
}
