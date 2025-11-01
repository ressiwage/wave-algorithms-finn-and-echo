import json, random
from random_word import RandomWords

r=RandomWords()
port = 7999

def _make_server(id, num_children, restriction):
    global port
    port+=1
    serv = {
        "name": id,
        "port": port,
        "cpu": random.randint(1,4)*2,
        "children": [_make_server(r.get_random_word(), min(random.randint(0, 3), restriction), restriction-1) for i in range(num_children)]
    }
    return serv

data = _make_server('root', 2, 3)
json.dump(data, open("topology.json", 'w+'), indent=2)