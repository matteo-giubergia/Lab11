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
        print(color)
        anno = self._view._ddyear.value
        print(anno)
        self._view.txtOut.controls.clear()
        self._model.buildGraph(color, anno)
        self._view.txtOut.controls.append(ft.Text("grafo creato"))
        self._view.txtOut.controls.append(ft.Text(f"il grafo ha {self._model.numNodes()} nodi e {self._model.numArchi()} archi"))
        self._view.update_page()



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
