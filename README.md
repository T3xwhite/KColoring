# k-Coloring and  Graph Isomorphism
This project uses object oriented programming in python with the Pygame module to allow the user to draw graphs and automatically compute whether the graph is k-Colorable and if two graphs are isomorphic.

## Usage

The following command launches the Pygame instance with set value of k used for computing the k-Coloring.

```bash
python main.py <k>
```
Once the instance is launched, the user can do the following actions:

* Click anywhere to create a vertex.
* Click two consecutive vertices to create an edge between them.
* Press `s` to switch between the two graphs.
* Press `k` to compute a k-Coloring for the current graph.
  * The program will display if a k-Coloring exists, and print a possible coloring to the terminal.
  * If there is a possible k-Coloring, the program will also color the corresponding vertices with a valid coloring.
* Press `i` to compute if the two drawn graphs are isomorphic.

## Algorithm Details

Both k-Coloring is known to be NP-Complete and no known polynomial time algorithm exists for Graph-Isomorphism. Since exact solutions were desired for both of these problems, the algorithms used to solve these problems do not run in polynomial time. To limit these runtime issues, the program has a hardcoded maximum vertex count for the graphs, which is set by default to 20 vertices. This value can be changed by changing the `MAX_VERTICES` global variable at the top of `main.py`. 

The algorithm for k-Coloring iterates through all possible colorings, check each to find a valid k-Coloring. The runtime for computing a $k$-Coloring on a graph G = (V, E) is
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;O(k^{|V|}&space;\cdot&space;M^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;O(k^{|V|}&space;\cdot&space;M^2)" title="O(k^{|V|} \cdot M^2)" /></a> where M is `MAX_VERTICES` and $|V|$ is the number of vertices in $G$.

The algorithm for Graph-Isomorphism iterates through the possible permuations of vertex conversions between the two graphs. As a result, the runtime for computing an isomorphism between graphs G1 = (V1, E1) and G2 = (V2, E2) is <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;O(|V|&space;\cdot&space;|V|!&space;\cdot&space;M^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;O(|V|&space;\cdot&space;|V|!&space;\cdot&space;M^2)" title="O(|V| \cdot |V|! \cdot M^2)" /></a> where M is `MAX_VERTICES` and given that |V| = |V1| = |V2|.

## Requirements

The required modules to run this program:

* `math`
* `itertools`
* `copy`
* `random`
* `click`
* `pygame`