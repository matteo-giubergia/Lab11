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
            self._grafo.add_edge(arco[0], arco[1])

    def numNodes(self):
        print(len(self._grafo.nodes))
        return len(self._grafo.nodes)

    def numArchi(self):
        return len(self._grafo.edges)


