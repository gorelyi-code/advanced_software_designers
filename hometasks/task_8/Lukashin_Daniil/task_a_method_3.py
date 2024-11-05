import re
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection

#  Read file
def input_filter(pipe: Connection, filename: str):
    with open(filename, 'r') as f:
        for line in f:
            pipe.send(line.strip())
    pipe.send(None)

# Filter to search for the required word
def processing_filter(pipe_in: Connection, pipe_out: Connection, keyword: str):
    while True:
        line = pipe_in.recv()
        if line is None:
            pipe_out.send(None)
            break

        # We find keywords and form the context
        words = re.split(r'\s+', line)
        for i, word in enumerate(words):
            # Punctuation filter
            word = re.sub(r'[^\w\s]', '', word)
            if word.lower() == keyword.lower():
                # Takes a slice of the words next to the found one
                context = ' '.join(words[max(0, i-2):min(len(words), i+3)])
                pipe_out.send(context)

# Output of the result
# Potentially not needed. Made for demonstration
def output_filter(pipe: Connection, stop_pip: Connection):
    results = []
    while True:
        context = pipe.recv()
        if context is None:
            break
        results.append(context)
    for result in results:
        print(result)
    stop_pip.send(None)

if __name__ == '__main__':
    # Reference values
    keyword = 'sweet'
    filename = 'file_for_task_b.txt'

    # Communication primitives in the form of pipe from multiprocessing
    pipe1, pipe2 = Pipe()
    pipe3, pipe4 = Pipe()
    pipe5, pipe6 = Pipe()

    input_process = Process(target=input_filter, args=(pipe1, filename))
    processing_process = Process(target=processing_filter, args=(pipe2, pipe3, keyword))
    output_process = Process(target=output_filter, args=(pipe4, pipe5))

    input_process.start()
    processing_process.start()
    output_process.start()

    # Without a loop, the program closes before the output of information ends
    while True:
        line = pipe6.recv()
        if line is None:
            break
    
    # We send a signal to turn off the processes for sure
    pipe2.send(None)
    pipe3.send(None)

    input_process.join()
    processing_process.join()
    output_process.join()
