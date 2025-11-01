from treelib import Node, Tree
import json
data = json.load(open('topology.json', 'r'))
_make_name = lambda srv: f"{srv['name']} port: {srv['port']} cpu: {srv['cpu']}"
def visualize(data):
    global t
    t=Tree()
    t.create_node(_make_name(data), data['name'])
    def rec(server):
        global t
        for i in server['children']:
            t.create_node(_make_name(i), i['name'], parent=server['name'])
            rec(i)
    rec(data)
    t.show()
if __name__ == '__main__':
    visualize(data)