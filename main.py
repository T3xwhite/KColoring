import math
import click
import pygame


WIN_WIDTH = 1000
WIN_HEIGHT = 600
VERTEX_RAD = 10
VERTEX_COLOR = (100, 100, 100)
MAX_VERTICES = 20


class Graph():
    """Maintain the Graph drawn on the Board."""

    def __init__(self, k):
        """Graph Initialization."""
        self.k_coloring = int(k)
        self.vertex_locs = []
        self.adj_matrix = [[0 for i in range(MAX_VERTICES)] for i in range(MAX_VERTICES)]

    def draw(self, surface):
        """Draw Vertices and Edges for Graph."""
        for loc in self.vertex_locs:
            pygame.draw.circle(surface, VERTEX_COLOR, loc, VERTEX_RAD)
        for i in range(MAX_VERTICES):
            for j in range(MAX_VERTICES - i):
                if self.adj_matrix[i][j] == 1:
                    loc_i = self.vertex_locs[i]
                    loc_j = self.vertex_locs[j]
                    pygame.draw.line(surface, VERTEX_COLOR, loc_i, loc_j)

    def click_in_vertex(self, pos):
        """Return the index of the vertex the user clicked on."""
        x, y = pos
        for i, loc in enumerate(self.vertex_locs):
            x_loc, y_loc = loc
            dist = math.sqrt((x_loc - x) ** 2 + (y_loc - y) ** 2)
            if dist <= VERTEX_RAD:
                return i
        return -1

    def create_vertex(self, loc):
        """Create new vertex at location loc."""
        self.vertex_locs.append(loc)

    def create_edge(self, v_id1, v_id2):
        """Add edge between input vertices in adjacency matrix."""
        self.adj_matrix[v_id1][v_id2] = 1
        self.adj_matrix[v_id2][v_id1] = 1

    def is_colorable(self):
        """Return bool of whether the graph is k-colorable."""
        # Brute force algorithm for checking if graph is k-colorable
        # Runtime O(k * num_vertices * MAX_VERTICES^2)
        k = self.k_coloring
        num_vertices = len(self.vertex_locs)
        for i in range(k * num_vertices):
            valid_coloring = True
            coloring = []
            for j in range(num_vertices):
                coloring.append((i // k ** j) % k)
            for x in range(num_vertices):
                for y in range(x + 1, num_vertices):
                    if (self.adj_matrix[x][y] == 1
                            and coloring[x] == coloring[y]):
                        valid_coloring = False
            if valid_coloring:
                print(coloring)
                return True
        return False


class Board():
    """Maintain the Pygame Board."""

    def __init__(self):
        """Initialize Pygame Board."""
        self.graphs = []
        self.mode = 0   # mode in [0, 1]
        self.making_edge = False
        self.v_1 = -1

    def create_graph(self, k):
        """Create Graph Object on Board."""
        self.graphs.append(Graph(k))

    def handle_click(self, pos):
        """Create Edges and Vertices Based on Input."""
        v_id = self.graphs[self.mode].click_in_vertex(pos)
        if v_id == -1:
            self.making_edge = False
            self.graphs[self.mode].create_vertex(pos)
        elif self.making_edge:
            self.making_edge = False
            self.graphs[self.mode].create_edge(self.v_1, v_id)
        else:
            self.making_edge = True
            self.v_1 = v_id

    def handle_keys(self):
        """Manage User's Pygame Key Input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    print(self.graphs[self.mode].adj_matrix)
                    print(self.graphs[self.mode].is_colorable())
        return True

    def draw(self, surface):
        """Draw Current Graph to Screen."""
        self.graphs[self.mode].draw(surface)


@click.command()
@click.argument('k', required=True)
def main(k):
    """Program Driver."""
    # Initialize Pygame Window
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), 0, 32)
    pygame.display.set_caption("K-Coloring Calculator")
    surface = pygame.Surface(win.get_size())
    surface = surface.convert()

    # Initialize Screen (Board) Manager
    board = Board()
    board.create_graph(k)

    while board.handle_keys():
        surface.fill((0, 0, 0))
        board.draw(surface)
        win.blit(surface, (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
