## This snippet has allowed me to outline a number of important algorithms and data structures, each of which contributes to a specific aspect of problem solving. So here is a brief of what I learnt and implemented:

## Sorting Algorithms

* The first crude version I wrote was just Quick Sort, Bubble Sort, and a Hybrid Merge Sort. Quick Sort : It is a very efficient, in place algorithm, which splits the array smaller sub-array and sorting it recursively. Bubble Sort, on the other hand, is easy to understand but inefficient and works by swapping adjacent elements if they are in the wrong order. Contains Merge Sort and Insertion Sort What hybrid merge sort does is, it uses the benefits of both merge sort and insertion sort such that even though merge sort runs in n*logn time, if the number of elements is smaller then you can use insertion sort to sort those smaller sub-arrays.

## Representing and traversing graphs

* I created a Graph class that represents an undirected graph as an adjacency list. You can add vertices and edges — which is critical for any algorithm related to graphs. Two well-known graph traversal algorithms that I used are Depth-First Search (DFS) and the much simpler Breadth-First Search (BFS) algorithm. DFS goes as deep as possible along each branch before backtracking while BFS explores all neighbors of a node before moving on to the next node.

## Finding paths and Detecting cycles

* I worked on implementation of getting all paths between two vertices and cycle detection in a graph as well. All paths and cycle detection: One can have multiple paths between two points, so finding all paths may be useful, and cycle detection (using DFS) to find loops in the graph.

## Weighted graphs and shortest paths, Dijkstra’s algorithm.

* Finally, I worked on Dijkstra's algorithm that calculates shortest paths in a weighted graph. Using a priority queue, this algorithm efficiently calculates the shortest distance between a starting vertex and all other vertices in the graph.

###### The combination of these algorithms gave me a better understanding of more advanced real-world problems, such as working with graphs, sorting data, and pathfinding. These algorithms are applied in real-world scenarios. They have applications such as routing systems, data analysis, etc. Some algorithms (SQ, BFS) are suited for bigger datasets while others (BS, DFS) are better for smaller, less complex datasets but they all teach us something. Merge Sort implements a hybrid approach to edge case optimization which serves to render the overall solution more flexible.