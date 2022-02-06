from sys import maxsize

grafo = [[maxsize, 16, 12, 18, 16],
         [10, maxsize, 18, 20, 20],
         [18, 20, maxsize, 18, 16],
         [14, 18, 10, maxsize, 8],
         [8, 12, 12, 12, maxsize]
         ]

vertices = [0, 1, 2, 3, 4]

class CaixeiroViajante():

    def __init__(self, grafo, vertices, vertice_inicial) -> None:
        self.grafo = grafo
        self.vertices = vertices
        self.distancias = [0]
        self.vertice_inicial = self.decode(vertice_inicial)
        self.vertice_atual = self.vertice_inicial
        self.visitados = []
        self.visitados.append(self.vertice_inicial)
        self.caminho_str = ""

    def decode(self, entrada):
        if entrada == "A":
            return 0
        elif entrada == "B":
            return 1
        elif entrada == "C":
            return 2
        elif entrada == "D":
            return 3
        elif entrada == "E":
            return 4

    def decode2(self, entrada2):
        saida = []
        for i in range(len(entrada2)):
            if entrada2[i] == 0:
                saida.append("A")
            elif entrada2[i] == 1:
                saida.append("B")
            elif entrada2[i] == 2:
                saida.append("C")
            elif entrada2[i] == 3:
                saida.append("D")
            elif entrada2[i] == 4:
                saida.append("E")
        return saida

    def encontra_proximo_vertice(self, vertice):
        menor_custo = maxsize
        vizinhos = self.grafo[vertice]
        if not self.vertices:
            self.distancias.append(self.grafo[vertice][self.vertice_inicial])
            proximo_vertice = self.vertice_inicial
        else:
            for i in range(len(vizinhos)):
                if i not in self.visitados:
                    for aux in self.grafo[vertice]:
                        valor = self.grafo[vertice][i]
                        if menor_custo > valor:
                            menor_custo = valor
                            proximo_vertice = i
            self.distancias.append(menor_custo)
        return proximo_vertice

    def percorre(self):
        while self.vertices:
            self.vertices.remove(self.vertice_atual)
            self.vertice_atual = self.encontra_proximo_vertice(self.vertice_atual)
            self.visitados.append(self.vertice_atual)
        self.caminho = self.decode2(self.visitados)
        total = 0
        for i in range(len(self.visitados)):
            if i == 0:
                print("Vértice Inicial: {}".format(self.caminho[i]))
                caminho_str = self.caminho[i]
            else:
                print ("Vértice, não selecionado, mais próximo de {}: {} ({}Km)".format(self.caminho[i-1], self.caminho[i], str(self.distancias[i])) )
                total = total + self.distancias[i]
                caminho_str = caminho_str + "," + self.caminho[i]


        print ("Circuito quase ótimo: {}: Distância total = {}Km".format(caminho_str, str(total)))
        

if __name__ == "__main__":
    v_inicial = input("Digite o Vertice Atual: ")
    c = CaixeiroViajante(grafo, vertices, v_inicial)
    c.percorre()
