import asyncio


class ChessBoard:
    def __init__(self, size=8):
        self.solution_count = 0
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]

    def is_safe(self, row, col, queens):
        for q_row, q_col in queens:
            if q_col == col or q_row - q_col == row - col or q_row + q_col == row + col:
                return False
        return True

    async def place_queens(self, row=0, queens=[]):
        if row == self.size:
            # Starting an asynchronous task to record and print a solution
            asyncio.create_task(self.record_solution(queens))
            return

        for col in range(self.size):
            if self.is_safe(row, col, queens):
                await self.place_queens(row + 1, queens + [(row, col)])

    async def record_solution(self, queens):
        solution = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for row, col in queens:
            solution[row][col] = 'Q'
        
        # Print solution
        self.solution_count += 1
        with open('task_b_output.txt', 'a') as file:
            print(f"Solution found {self.solution_count}:")
            file.write(f"Solution found {self.solution_count}: \n")
            for row in solution:
                print(' '.join(row))
                file.write(' '.join(row) + "\n")
            print("\n" + "-" * 20 + "\n")
            file.write("\n" + "-" * 20 + "\n")


async def main():
    with open('task_b_output.txt', 'w') as файл:
        pass

    board = ChessBoard(size=8)
    await board.place_queens()

asyncio.run(main())
