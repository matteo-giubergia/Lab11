import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni = DAO.getAnni()
        self.colori = DAO.getColori()
        self.nodi = None
        self.archi = None
        self.idMap = {}
        self._grafo = nx.Graph()
        self._bestPath = []



    def buildGraph(self, color, anno):
        # nodi
        self.nodi = DAO.getNodes(color)
        # mappa con id

        for prod in self.nodi:
            self.idMap[prod.Product_number] = prod
        # archi
        self.archi = DAO.getArchi(color, color, anno, self.idMap)
        self._grafo.add_nodes_from(self.nodi)

        for arco in self.archi:
            self._grafo.add_edge(arco[0], arco[1], weight=arco[2])


    def ordinaArchi(self):
        res = []

        for arco in self.archi:
            res.append(arco)
        res = sorted(res, key=lambda x: x[2], reverse = True)

        return res[:3]
    def nodiRipetuti(self):
        lista = []
        res=[]
        for arco in self.ordinaArchi():
            lista.append(arco[0])
            lista.append(arco[1])
        for i in range(len(lista)):
            for j in range(i, len(lista)):
                if i!=j and lista[i]==lista[j]:
                    res.append(lista[i].Product_number)
        return res

    def numNodes(self):
        return len(self._grafo.nodes)

    def numArchi(self):
        return len(self._grafo.edges)

    def percorso(self, product_number):
        source = self.idMap[product_number]

        peso = 999
        parziale = [source]

        for n in self._grafo.neighbors(source):
            parziale.append(n)
            self._ricorsione(parziale) # qualosa è sbagliato con 2015-RED-12110
            parziale.pop()
        for n in self._bestPath:
            print(n.Product_number)
        return len(self._bestPath)

    def _ricorsione(self, parziale):
        if len(self.trovaCandidati(parziale[-1], parziale[-2], parziale))==0:  # if lunghezza candidati == 0 allora calcolo il costo del cammino e se è maggiore del precedente faccio la deepcopy in una var solBest
            if len(parziale) > len(self._bestPath):
                self._bestPath = copy.deepcopy(parziale)

        else:
            candidati = self.trovaCandidati(parziale[-1], parziale[-2], parziale) # posso usare il meotodo has_edge per verificare se c'è l'arco(?)
            for nodo in candidati:
                parziale.append(nodo)
                self._ricorsione(parziale)
                parziale.pop() # controlla se va all'interno del ciclo

    def trovaCandidati(self, source, pred, parziale):
        res = []
        peso_precedente = self._grafo.get_edge_data(pred, source)['weight']
        for node in self._grafo.neighbors(source): # controllo che l'arco successivo abbia un peso maggiore
            if self._grafo.get_edge_data(source, node)['weight'] > peso_precedente:
                res.append(node)
        return res





