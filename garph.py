# -*- coding: UTF-8 -*-

from graphviz import Digraph
import networkx as nx
import matplotlib.pyplot as plt
from tests.demo.page import LoginPage,HomePage,ProductPage,BackendPage,BrandPage,LogoutPage,SuccessfulPage,\
    ResultPage,RegionPage,CreatePage,NonePage,OrderPage,IssuePage,AdminPage,KeywordPage
# dot = Digraph(name='navgarphPython+Selenium学习总结(一)',comment='first draw')
# dot.node('A','LoginPage')
# dot.node('B','HomePage')
# dot.node('C','LogoutPage')
# dot.edges(['AB','AC'])
# dot.edge('B','A','back')
# print(dot.source)
# dot.render('test-output/test-table.gv', view=True)
class graph:
        G = nx.DiGraph()
        nodes=[LoginPage.name,HomePage.name,ProductPage.name,BackendPage.name,BrandPage.name,LogoutPage.name,SuccessfulPage.name,
               ResultPage.name,RegionPage.name,CreatePage.name,NonePage.name,OrderPage.name,IssuePage.name,AdminPage.name,KeywordPage.name]
        G.add_nodes_from(nodes)
        edges=(
            [
                (LoginPage.name,HomePage.name),
                (HomePage.name,RegionPage.name),
                ()
            ]
        )
        G.add_edges_from(edges)
        nx.draw(G)
        plt.show()