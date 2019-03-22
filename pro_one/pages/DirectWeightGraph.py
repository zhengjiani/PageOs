class Node(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        return ''

    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __le__(self, obj):
        return self.name <= self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)

    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name

class Weight(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        return ''

    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __le__(self, obj):
        return self.name <= self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)

    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name
class DirectedWeightedEdge(object):
    def __init__(self, node_from, node_to,weight):
        self.nf = node_from
        self.nt = node_to
        self.wt = weight
    def __eq__(self, obj):
        if isinstance(obj, DirectedWeightedEdge):
            return obj.nf == self.nf and obj.nt == self.nt and obj.wt == self.wt
        return False

    def __repr__(self):
        return '({0} ->{1} {2})'.format(self.nf, self.nt,self.wt)
class DirectedWeightGraph(object):
    def __init__(self, load_dict={}):
        self.nodes = []
        self.edges = []
        self.weights = []
        self.adjmt = {}
        if load_dict and type(load_dict) == dict:
            for v,method in load_dict.items():
                node_from = self.add_node(v)
                self.adjmt[node_from]={}
                for w,n in method.items():
                    node_to = self.add_node(n)
                    weight = self.add_weight(w)
                    self.adjmt[node_from][weight]=node_to
                    self.add_edge(v,n,w)

                # self.adjmt[node_from][method] = []
                # for w in self.adjmt[node_from].values():
                #     for n in self.adjmt[node_from].values():
                #         node_to = self.add_node(n)
                #         self.adjmt[node_from].append(node_to)
                #         self.add_edge(v, n, k)

    def add_node(self, node_name):
        try:
            return self.nodes[self.nodes.index(node_name)]
        except ValueError:
            node = Node(node_name)
            self.nodes.append(node)
            return node
    def add_weight(self, weight_name):
        try:
            return self.weights[self.weights.index(weight_name)]
        except ValueError:
            weight = Weight(weight_name)
            self.weights.append(weight)
            return weight
    def add_edge(self, node_name_from, node_name_to,weight):
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            edge_weight = self.weights[self.weights.index(weight)]
            self.edges.append(DirectedWeightedEdge(node_from, node_to,edge_weight))
        except ValueError:
            pass
if __name__ == '__main__':
    g=DirectedWeightGraph({'LoginPage':{
                                            'login':'HomePage',
                                            'other':'ErrorPage',
                                        },
                            'HomePage':{
                                            'goto_user':'UserPage',
                                            'goto_good':'GoodPage',
                            }

    })
    print(g.edges)