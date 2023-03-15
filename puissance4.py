#0 si vide
#1 si joueur 1
#2 si joueur 2
"""

équations
lignes faisable pour un joueur multiplié par le nombre de ses jetons dans la ligne théorique
lignes * jetons

uniquement les lignes
lignes

lignes faisable pour un joueur multiplié par le nombre de ses jetons dans la ligne théorique au carré
lignes * jetons**2

"""

def get_value(grid):
    j1=0
    j2=0
    #vérifie les lignes de manières horizontal pour le j1
    for i in range(6):
        for j in range(4):
            if (grid[i][j]==0 or grid[i][j]==1) and (grid[i][j+1]==0 or grid[i][j+1]==1) and (grid[i][j+2]==0 or grid[i][j+2]==1) and (grid[i][j+3]==0 or grid[i][j+3]==1):
                for h in range(4):
                    if grid[i][j+h]==1:
                        j1+=1
                
    #vérifie les lignes de manières horizontal pour le j2
    for i in range(6):
        for j in range(4):
            if (grid[i][j]==0 or grid[i][j]==2) and (grid[i][j+1]==0 or grid[i][j+1]==2) and (grid[i][j+2]==0 or grid[i][j+2]==2) and (grid[i][j+3]==0 or grid[i][j+3]==2):
                for h in range(4):
                    if grid[i][j+h]==2:
                        j2+=1

    #vérifie verticalement pour le j1
    for i in range(7):
        for j in range(3):
            if (grid[j][i]==0 or grid[j][i]==1) and (grid[j+1][i]==0 or grid[j+1][i]==1) and (grid[j+2][i]==0 or grid[j+2][i]==1) and (grid[j+3][i]==0 or grid[j+3][i]==1):
                for h in range(4):
                    if grid[j+h][i]==1:
                        j1+=1
    
    #vérifie verticalement pour le j2
    for i in range(7):
        for j in range(3):
            if (grid[j][i]==0 or grid[j][i]==2) and (grid[j+1][i]==0 or grid[j+1][i]==2) and (grid[j+2][i]==0 or grid[j+2][i]==2) and (grid[j+3][i]==0 or grid[j+3][i]==2):
                for h in range(4):
                    if grid[j+h][i]==2:
                        j2+=1

    #vérifie diagonalement1 pour le j1
    for i in range(4):
        for j in range(3):
            if (grid[j][i]==0 or grid[j][i]==1) and (grid[j+1][i+1]==0 or grid[j+1][i+1]==1) and (grid[j+2][i+2]==0 or grid[j+2][i+2]==1) and (grid[j+3][i+3]==0 or grid[j+3][i+3]==1):
                for h in range(4):
                    if grid[j+h][i+h]==1:
                        j1+=1
    
    #vérifie diagonalement1 pour le j2
    for i in range(4):
        for j in range(3):
            if (grid[j][i]==0 or grid[j][i]==2) and (grid[j+1][i+1]==0 or grid[j+1][i+1]==2) and (grid[j+2][i+2]==0 or grid[j+2][i+2]==2) and (grid[j+3][i+3]==0 or grid[j+3][i+3]==2):
                for h in range(4):
                    if grid[j+h][i+h]==2:
                        j2+=1

    #vérifie diagonalement2 pour le j1
    for i in range(3,7):
        for j in range(3):
            if (grid[j][i]==0 or grid[j][i]==1) and (grid[j+1][i-1]==0 or grid[j+1][i-1]==1) and (grid[j+2][i-2]==0 or grid[j+2][i-2]==1) and (grid[j+3][i-3]==0 or grid[j+3][i-3]==1):
                for h in range(4):
                    if grid[j+h][i-h]==1:
                        j1+=1
    
    #vérifie diagonalement2 pour le j2
    for i in range(3,7):
        for j in range(3):
            if (grid[j][i]==0 or grid[j][i]==2) and (grid[j+1][i-1]==0 or grid[j+1][i-1]==2) and (grid[j+2][i-2]==0 or grid[j+2][i-2]==2) and (grid[j+3][i-3]==0 or grid[j+3][i-3]==2):
                for h in range(4):
                    if grid[j+h][i-h]==2:
                        j2+=1

    
    return j1-j2


def get_result(grid):
    result = 0

    #check nulle
    pomme=True
    for i in grid:
        if 0 in i:
            pomme=False
            break
    if pomme:
        result=None

    #check horizontal
    for i in range(6):
        for j in range(4):
            if grid[i][j]==1 and grid[i][j+1]==1 and grid[i][j+2]==1 and grid[i][j+3]==1:
                result = 1
            elif grid[i][j]==2 and grid[i][j+1]==2 and grid[i][j+2]==2 and grid[i][j+3]==2:
                result = 2

    #check vertical
    for i in range(7):
        for j in range(3):
            if grid[j][i]==1 and grid[j+1][i]==1 and grid[j+2][i]==1 and grid[j+3][i]==1:
                result = 1
            elif grid[j][i]==2 and grid[j+1][i]==2 and grid[j+2][i]==2 and grid[j+3][i]==2:
                result = 2
    
    #check diagonal 1
    for i in range(4):
        for j in range(3):
            if grid[j][i]==1 and grid[j+1][i+1]==1 and grid[j+2][i+2]==1 and grid[j+3][i+3]==1:
                result = 1
            elif grid[j][i]==2 and grid[j+1][i+1]==2 and grid[j+2][i+2]==2 and grid[j+3][i+3]==2:
                result = 2

    #check diagonal 2
    for i in range(3,7):
        for j in range(3):
            if grid[j][i]==1 and grid[j+1][i-1]==1 and grid[j+2][i-2]==1 and grid[j+3][i-3]==1:
                result=1
            elif grid[j][i]==2 and grid[j+1][i-1]==2 and grid[j+2][i-2]==2 and grid[j+3][i-3]==2:
                result=2

    

    return result


def get_moves(grid):
    xs=[]
    moves=[]
    for i in range(1,7):
        for j in range(7):
            if grid[-i][j]==0 and not j in xs:
                moves.append([j,-i])
                xs.append(j)
    return sorted(moves)
            
class TreeNode:
    def __init__(self,move,deep=0):
        self.deep=deep
        self.children=[]
        self.value=None
        self.move=move
        #si 2 joueur joue parfaitement la valeur de la position la plus loi sur cette ligne calculé
        self.move_value=None

    def add_children(self,moves):
        for move in moves:
            child = TreeNode(move,deep=self.deep+1)
            self.children.append(child)


def main(grid,tree,deepmax,tour):
    #évaluation de la position
    tree.value=get_value(grid)


    moves = get_moves(grid)
    tree.add_children(moves)

    r=get_result(grid)

    if not tree.deep==deepmax and r==0:
        for child in tree.children:
            move = child.move
            if tour%2==0:
                grid[move[1]][move[0]]=1
            else:
                grid[move[1]][move[0]]=2

            main(grid,child,deepmax=deepmax,tour=tour+1)
            if tour%2==0:
                grid[move[1]][move[0]]=0
            else:
                grid[move[1]][move[0]]=0

        #trouve à partir des enfants la valeur du move
        if tour%2==1:
            values = []
            for child in tree.children:
                values.append(child.move_value)
            tree.move_value = min(values)
        else:
            values = []
            for child in tree.children:
                values.append(child.move_value)
            #print(values)
            tree.move_value = max(values)
    
    #si le bot gagne
    elif r==1:
        tree.move_value=1000
    #si le bot perd
    elif r==2:
        tree.move_value=-1000
    elif r==None:
        tree.move_value=0
    else:
        tree.move_value = tree.value
        








grid = [[0 for i in range(7)]for i in range(6)]

x = input("qui commence?\n0 pour moi\n1 pour vous\n").replace(" ","")
while x!="0" and x!="1":
    x = input("qui commence?\n0 pour moi\n1 pour vous\n").replace(" ","")

starter = int(x)


tree = TreeNode([100,-100])
main(grid,tree,deepmax=2,tour=starter)


pomme=False
if starter==0:
    pomme=True

while True:
    if pomme:
        pomme=False
    else:
        for i in grid:
            print(i)
        print(get_value(grid))
        r =get_result(grid)
        if r==1:
            print("j'ai gagné")
            break
        elif r==2:
            print("impossible!!!")
            break
        elif r==None:
            print("coup de chance")
            break

        x = input("entrez votre coup\n")
        #!!!vérifiez la disponibilité de la ligne
        while not x.isdigit() and not 0<int(x)<=7 :
            x = input("entrez un coup valide\n")
        x=int(x)-1
        temp=None
        for child in tree.children:
            if child.move[0]==x:
                temp=child.move
        tree=TreeNode(temp,deep=0)
        #print(tree.move)
        grid[temp[1]][temp[0]]=2
        starter+=1
    for i in range(100):
        if len(tree.children)**(i+1)>20000:
            deepmax=i
            break
    deepmax=5
    main(grid,tree,deepmax=deepmax,tour=0)


    
    for i in grid:
        print(i)
    print(get_value(grid))
    r =get_result(grid)
    if r==1:
        print("j'ai gagné")
        break
    elif r==2:
        print("impossible!!!")
        break
    elif r==None:
        print("coup de chance")
        break


    maxi=-10000
    move=6666
    for child in tree.children:
        print(child.move_value)
        print(child.value)
        print(child.move)
        if child.move_value>maxi:
            maxi=child.move_value
            #print("truc: "+str(child.move))
            move=child.move
    
    print(move[0]+1)
    tree=TreeNode(move,deep=0)
    grid[move[1]][move[0]]=1
    main(grid,tree,deepmax=1,tour=0)
    starter+=1