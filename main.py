import sys
import math
import pygame


WIN_WIDTH = 1000
WIN_HEIGHT = 600
VERTEX_RAD = 10
VERTEX_COLOR = (100, 100, 100)
MAX_VERTICES = 20

# class Vertex(object):
#     """Information for a Vertex in a Graph"""
#     def __init__(self, x_in, y_in):
#         self.x = x_in
#         self.y = y_in

class Graph(object):
    """Maintains the Graph drawn on the Board"""
    def __init__(self):
        self.vertex_locs = []
        self.adj_matrix = [[0 for i in range(MAX_VERTICES)] for i in range(MAX_VERTICES)]


    def draw(self, surface):
        for loc in self.vertex_locs:
            pygame.draw.circle(surface, VERTEX_COLOR, loc, VERTEX_RAD)
        for i in range(MAX_VERTICES):
            for j in range(MAX_VERTICES - i):
                if self.adj_matrix[i][j] == 1:
                    loc_i = self.vertex_locs[i]
                    loc_j = self.vertex_locs[j]
                    pygame.draw.line(surface, VERTEX_COLOR, loc_i, loc_j)


    def click_in_vertex(self, pos):
        x, y = pos
        for i, loc in enumerate(self.vertex_locs):
            x_loc, y_loc = loc
            dist = math.sqrt((x_loc - x) ** 2 + (y_loc - y) ** 2)
            if dist <= VERTEX_RAD:
                return i
        return -1


    def create_vertex(self, loc):
        self.vertex_locs.append(loc)


    def create_edge(self, v_id1, v_id2):
        self.adj_matrix[v_id1][v_id2] = 1
        self.adj_matrix[v_id2][v_id1] = 1


class Board(object):
    """Maintains the Pygame Board"""
    def __init__(self):
        self.graphs = []
        self.mode = 0 # mode in [0, 1]
        self.making_edge = False
        self.v_1 = -1


    def create_graph(self):
        self.graphs.append(Graph())


    def handle_click(self, pos):
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_click(pygame.mouse.get_pos())
        return True


    def draw(self, surface):
        self.graphs[self.mode].draw(surface)


def main():
    """Program Driver"""
    
    # Initialize Pygame Window
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), 0, 32)
    pygame.display.set_caption("K-Coloring Calculator")
    surface = pygame.Surface(win.get_size())
    surface = surface.convert()

    # Initialize Screen (Board) Manager
    board = Board()
    board.create_graph()
    print ("peepeepoopoo i love texy")

    while board.handle_keys():
        surface.fill((0,0,0))
        board.draw(surface)
        win.blit(surface, (0,0))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
