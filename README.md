# Technical Task

In the beginning, I tried to quickly sketch my own solution, bypassing the conventional algorithms. But soon, after realizing that I was driving myself into a dead end, I decided to resort to the method of transform and conquer.    
I had a simple list of words, and a certain rule that linked the words together. This naturally resembled a graph.   
I then proceeded to create a method for transforming the word list into a graph in the form of a dictionary, with all the words as keys, and the values as lists of other words that differed from the key word by only one letter.  
This made it possible to turn the problem into a search for the shortest path in the graph. And there is more than one algorithm for this. In my solution, I used breadth-first search.  
The algorithm guarantees the shortest path because it goes through each nearest node placed in the queue until it is the given final node  

If I had more time to develop it, I would have added a few more features. For example, for large datasets, the program builds a new graph every time. So this is a reason to add caching of graph creation result, to skip this processing in future, when it is run again on the same data. Also, I could add my own validation functions for each argument, replacing the usual string validation.  

So, the program is designed to find the shortest path between the specified words, among the words specified in the file.   
The solution has been created based on a graph, with words as nodes. Connections between them, are set in case of difference between words only one letter.  
To find the shortest path the algorithm of breadth-first search was used. This algorithm is more suitable for finding nodes that are closer to a given source.

To activate poetry environment, run the following command:  
`poetry shell`

To start the program, run the following command:  
`python main.py DictionaryFile StartWord EndWord ResultFile`

DictionaryFile - the file name of a text file containing four letter words  
StartWord - a four letter word (that you can assume is found in the DictionaryFile file)  
EndWord - a four letter word (that you can assume is found in the DictionaryFile file)  
ResultFile - the file name of a text file that will contain the result 

To start program tests, run:  
`pytest -v`
 