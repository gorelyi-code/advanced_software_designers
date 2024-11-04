#!/usr/bin/env python
# coding: utf-8

# # Problem A. Key Word in Context (KWIC)
# 
# ## Method 1. Abstract Data Types

# In[13]:


class KWICindex:
    """The main class of the KWIC index system which handle the text input (titles),
    process the text, and generate a KWIC index.

    Attributes:
        titles      A list to hold titles for processing.
        stop_words  A set of stop words that should be excluded from indexing.
    """
    def __init__(self, stop_words=None):
        self.titles = []
        self.stop_words = stop_words or {"and", "is", "the", "an", "in", "on", "for", "of", "to"}
    
    # Adds a title to the titles list for processing.
    def add_title(self, title):
        self.titles.append(Title(title))
    
    # Processes each title to create the KWIC index and returns a list of formatted KWIC lines.
    def generate_index(self):
        indexes = []
        for title in self.titles:
            title.prepare_words(self.stop_words)
            for line in title.generate_kwic_lines():
                indexes.append(line.format_line())
        return sorted(indexes)
    
    # Outputs the KWIC index in a human-readable format.
    def display_index(self):
        for index in self.generate_index():
            print(index)

class Title:
    """Title class is responsible for storing, cleaning up and preparing the text for KWIC indexing.

    Attributes:
        text    The raw title text.
        words   A list of words in the title after filtering out stop words.
    """
    def __init__(self, text):
        self.text = text
        self.words = []
    
    # Filters the words in text, excluding any stop words and splitting it into a list of individual words.
    def prepare_words(self, stop_words):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for word in self.text:
            if word in punc:
                self.text = self.text.replace(word, "")
        self.words = [word for word in self.text.split() if word.lower() not in stop_words]
    
    # Generates and returns the KWIC lines for each keyword in the title, showing each keyword in context.
    def generate_kwic_lines(self):
        kwic_lines = []
        for position, keyword in enumerate(self.words):
            kwic_lines.append(KWICLine(keyword, self.words, position))
        return kwic_lines

class KWICLine:
    """KWICLine class represents a single line in the KWIC index, with a focus keyword and its context from the title.

    Attributes:
        keyword             The main keyword in the line.
        context             The surrounding context of the keyword in the title.
        original_position   The index of the keyword in the title to allow correct alignment.
    """
    def __init__(self, keyword, context_words, position):
        self.keyword = keyword
        self.context = context_words
        self.original_position = position
    
    # Returns a formatted string representation of the KWIC line, with the keyword aligned in context.
    def format_line(self):
        context = " ".join(self.context)
        formatted_line = f"{self.keyword.upper():<15} | {context}"
        return formatted_line


# In[14]:


kwic_index = KWICindex()
kwic_index.add_title("KWIC is an acronym for Key Word In Context, the most common format for concordance lines!")
kwic_index.add_title("Wikipedia, the free encyclopedia.")
kwic_index.display_index()


# # Problem B. Eight Queens (8Q)
# 
# ## Method 2. Main/Subroutine with stepwise refinement (also Shared Data)

# In[20]:


def solve_n_queens(n):
    """The main routine initializes the board and starts the solving process"""
    board = [['.' for i in range(n)] for i in range(n)]  # Initialize the chessboard.
    
    if not solve_task(board, 0):
        print("Solution does not exist!") # Handles the case where no solution exists.
    else:
        print_board(board)

def solve_task(board, column):
    """Recursive function attempts to place queens in each row of the specified column"""
    if column >= len(board):
        return True  # All queens are placed successfully.

    for i in range(len(board)):
        if is_safe(board, i, column):
            board[i][column] = 'Q'  # Place queen.
            
            if solve_task(board, column + 1):  # Recur to place rest of the queens.
                return True
            
            board[i][column] = '.'  # Backtrack.

    return False  # Trigger backtracking.

def is_safe(board, row, column):
    """Check if a queen can be placed on cell"""
    # Check this row on left side.
    for i in range(column):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side.
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side.
    for i, j in zip(range(row, len(board)), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def print_board(board):
    """Print the chessboard"""
    for row in board:
        print(" ".join(row))


# In[21]:


n = 8
solve_n_queens(n)


# In[ ]:




