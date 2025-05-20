import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        for anno in self._model.anni:
            self._view._ddyear.options.append(ft.dropdown.Option(anno))

        for color in self._model.colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(color))

        


    def handle_graph(self, e):
        color = self._view._ddcolor.value
        anno = self._view._ddyear.value
        self._view.txtOut.controls.clear()
        self._model.buildGraph(color, anno)
        self._view.txtOut.controls.append(ft.Text("grafo creato"))
        self._view.txtOut.controls.append(ft.Text(f"il grafo ha {self._model.numNodes()} nodi e {self._model.numArchi()} archi"))
        for arco in self._model.ordinaArchi():
            self._view.txtOut.controls.append(ft.Text(f"arco da {arco[0].Product_number} a {arco[1].Product_number}, peso = {arco[2]}"))
        self._view.txtOut.controls.append(ft.Text(f"nodi ripetuti: {self._model.nodiRipetuti()}"))
        self._view.update_page()

        # riempio il secondo dd
        self.fillDDProduct()
        self._view.update_page()



    def fillDDProduct(self):
        for node in self._model._grafo.nodes:
            self._view._ddnode.options.append(ft.dropdown.Option(key=node.Product_number, text = node.Product_number))


    def handle_search(self, e):
        self._view.txtOut2.controls.clear()
        product_number = self._view._ddnode.value

        self._view.txtOut2.controls.append(ft.Text(f"Numero archi percorso piu lungo: {self._model.percorso(int(product_number))-1}"))
        self._view.update_page()
