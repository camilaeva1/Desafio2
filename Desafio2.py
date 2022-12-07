class Topo(object): #Classe topo, representando os topos das árvores no plano cartesiano
	def __init__(self, x, y): #Método que inicializar as instâncias das coordenadas x, y
		self.x = x 
		self.y = y
	def __lt__(self, other): #Método que compara a posição dos topos no plano cartesiano
		return self.x < other.x or (self.x == other.x and self.y < other.y)

def prodvetor (p0, p1, p2): 
	return (p1.x - p0.x)*(p2.y - p0.y) - (p2.x - p0.x)*(p1.y - p0.y)

n = int(input()) #Número de árvores
t = list(Topo(0,0) for i in range(n)) #lista de topos das árvores
ch = list(0 for i in range(n))

for i in range(n):
	l = list(int(x) for x in input().split())
	t[i].x, t[i].y = l[0], l[1] #Atribui (x,y) a cada topo

t.sort() #Ordenar a lista de topos
cont = 0 

for i in range(n):
	while (cont > 1 and prodvetor(t[ch[cont-2]], t[ch[cont-1]], t[i]) >= 0): #Realiza a verificação, enquantro houver mais de um ponto na lista e analisando os dois últimos topos em relação ao que o macaco está (t[i])
		cont -= 1;
	ch[cont] = i
	cont += 1;

print(cont - 1)
