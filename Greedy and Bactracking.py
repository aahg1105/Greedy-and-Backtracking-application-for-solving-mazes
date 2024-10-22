import turtle

"""
Las siguientes lineas de código son para setear la ventana de Turtle
"""
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver with Turtle")
wn.setup(width=800, height=800)
pixels = 300

"""
La siguiente lista "maze" crea el laberinto representado por caractares.

'#' representa las paredes y ' ' (espacio) representa el libre sendero
La 'S' represanta el origen de partida y la 'G' representa el final del recorrido
"""

maze = [
    "################################",
    "#S      #     #                #",
    "# ##### # # # # #### ######### #",
    "#   #   # #   #    # # #     # #",
    "# ### ### # # # ## ### # ### # #",
    "#   #   # # # ###  #     #     #",
    "### ### # # # #   ## ##### ### #",
    "#   #   # # # # ###  #     #   #",
    "# ##### # # # # #   ## ##### ###",
    "# #     # # #   # ###  #     # #",
    "# # ##### # # ###     ## ##### #",
    "# #     # #   # # ### ## # # # #",
    "# ##### # ### #   # # #  # # # #",
    "# #   # #   ####### # ##       #",
    "#   ### # #   #G       # #######",
    "# # #   # ### ##########       #",
    "### ## ##     #   #    ### ### #",
    "#    #    ##### # # ##   #     #",
    "# #########   ###   #### ## ####",
    "#           ### ### #### ## ####",
    "# ###### ##   # ###   #        #",
    "# #    #  ### #   # # ##########",
    "#   ## ##  ## # # # #          #",
    "# ####  ##    # # ############ #",
    "# #   #  #### # # #            #",
    "# # # ## #### # # ### ##########",
    "# # #  #    # # # #            #",
    "# # ## #### # # # ############ #",
    "# #             #              #",
    "################################"
]

# Laberinto del pdf
"""
maze = [
    "############",
    "#S         #",
    "########## #",
    "#          #",
    "# ##########",
    "# #        #",
    "# ######## #",
    "#          #",
    "# ##########",
    "#          #",
    "# ###### # #",
    "#        # #",
    "# ######## #",
    "#G#        #",
    "############"
]
"""
""""
Lo siguiente crea la clase que permite dibujar el laberinto
"""
class MazeTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
    
    def change_color(self, coordinate_type):
        if coordinate_type == "start_point":
            self.color("green")
        elif coordinate_type == "end_point":
            self.color("yellow")
        elif coordinate_type == "default":
            self.color("black")
        

"""
Lo siguiente crea la clase que permite utilizar a la tortuga como un objeto
"""
class SolverTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.speed(1)


"""
El siguiente métod dibuja el laberinto
"""
def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '#':
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
            elif maze[y][x] == 'S':
                start_pos = (x, y)
                maze_turtle.change_color("start_point")
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
                maze_turtle.change_color("default")
            elif maze[y][x] == 'G':
                end_pos = (x, y)
                maze_turtle.change_color("end_point")
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
                maze_turtle.change_color("default")
    return start_pos, end_pos


"""
El siguiente método  sirve como instrucción para mover a la tortuga a la 
siguiente casilla deseada del laberinto
"""
def move_turtle(x, y):
    solver_turtle.goto(x * 20 - pixels, pixels - y * 20) 


"""
El siguiente método es el que corresponde a trabajar por parte de los alumnos.
Es el método encargado de resolver el laberinto.

Tiene 3 argumentos de entrada: El mapa del laberinto, la posición inicial y
la posición de destino.

Los métodos deben regresar ("return <valor / valores>") todos los posibles 
caminos especificando el más corto tanto vía Greedy como Backtracking.
"""
def blocked(path,end):
    direcciones = [(1,0),(-1,0),(0,-1),(0,1)]
    x,y = path[-1]
    cont = 0
    for dx,dy in direcciones:
            nx, ny = x+dx, y+dy
            if (maze[ny][nx] == "#" and (x,y) != end):
                cont+=1
    if cont==3: return True
    else: return False

def girar(actual_position, last_position):
    dx = last_position[0] - actual_position[0]
    dy = last_position[1] - actual_position[1]

    if (dx,dy) == (0,1): 
        return 270
    elif (dx,dy) == (0,-1):  
        return 90
    elif (dx,dy) == (1,0):  
        return 0
    elif (dx,dy) == (-1,0): 
        return 180
    else:
        return 0  

def regresar(new_path,intersect,visit,end):
    direcciones = [(1,0),(0,-1),(-1,0),(0,1)]

    while intersect:
        x, y = new_path.pop()
        move_turtle(x, y)
        if len(new_path)>1:
            solver_turtle.seth(girar((x,y),new_path[-1]))
        if (x, y) in intersect:
            new_path.append((x,y))
            for dx,dy in direcciones:
                nx, ny = x+dx, y+dy
                if (maze[ny][nx] != "#" and (nx,ny) not in visit):
                    return
        visit.remove((x, y))

def solve_maze_greedy(maze, start, end):
    solver_turtle.speed(0)

    paths = []
    best_path = []
    direcciones = [(1,0),(-1,0),(0,1),(0,-1)]

    intersections = []
    do_not_visit = []
    stack = [start]
    visited = set()
    path = []

    while stack:
        x, y = stack.pop()
        
        if (x,y) in visited:
            continue

        if (x,y) != start:
            solver_turtle.down()

        move_turtle(x,y)

        visited.add((x,y))
        path.append((x,y))
        # print("Path: ", path)
        # print("Visitados", visited)

        if (x, y) == end:
            if path not in paths:
                paths.append(path[:])
            regresar(path,intersections,visited,end) # para la salida
            if len(intersections)>1:
                intersections.pop()
            continue

        n = len(stack)

        for dx,dy in direcciones:
            nx, ny = x+dx, y+dy
            if (maze[ny][nx] != "#" and (nx,ny) not in visited):
                stack.append((nx,ny))
                # print("Stack: ",stack)
                if len(path)>1:
                    solver_turtle.seth(girar(path[-1],stack[-1]))
                else:
                    solver_turtle.seth(girar(start,stack[-1]))

        if len(stack)-n > 1:
            intersections.append(path[-1])
            # print("Intersecciones: ",intersections)

        if len(stack)-n == 0:
            regresar(path,intersections,visited,end) # demas posiciones
            if len(intersections)>1:
                intersections.pop()

    paths.sort()
    best_path = min(paths, key = len)

    solver_turtle.up()

    return best_path, paths


def solve_maze_backtracking(maze, start, end):
    solver_turtle.speed(0)
    best_path = []
    paths = []

    def backtrack(x, y, path, visited):
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if (x, y) == end:
            if path not in paths:
                paths.append(path[:])
            return
        
        if (x,y) in visited:
            return

        visited.add((x, y))
        move_turtle(x, y)
        solver_turtle.down()

        opciones = 0
        intersect = []

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if (maze[ny][nx] != "#" and (nx, ny) not in visited):
                opciones += 1
                if opciones>1:
                    intersect.append(path[-1])
                    a, b = intersect.pop()
                    move_turtle(a, b)
                solver_turtle.seth(girar(path[-1], (nx, ny)))
                path.append((nx, ny))
                backtrack(nx, ny, path, visited)
                path.pop()
                move_turtle(nx, ny)
                solver_turtle.seth(girar((nx, ny), (x, y)))

        visited.remove((x,y))

    backtrack(start[0], start[1], [start], set())

    paths.sort()
    best_path = min(paths, key=len)

    solver_turtle.up()

    return best_path, paths

            

if __name__ == "__main__":
    # Instancia los objetos
    maze_turtle = MazeTurtle()
    solver_turtle = SolverTurtle()
    
    # Dibuja el Laberinto y establece las coordenadas de Inicio y Fin
    start_pos, end_pos = draw_maze(maze)
    
    # Método para resolver el laberinto con enfoque Greedy
    best_path, paths = solve_maze_greedy(maze, start_pos, end_pos)

    print("Paths greedy: ",paths)
    print("Best paths greedy: ",best_path)

    print()
    paths=[]
    best_path=[]
    
    # Método para resolver el laberinto con enfoque Backtracking
    best_path, paths = solve_maze_backtracking(maze, start_pos, end_pos)

    print("Paths Backtracking: ",paths)
    print("Best paths Backtracking: ",best_path)
    
    # Keep the window open
    wn.mainloop()  
