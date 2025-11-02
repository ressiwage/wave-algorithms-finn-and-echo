from subprocess import Popen
import json, os, shlex
from visualize import visualize
topology = json.load(open('topology.json', 'r'))
this_dir = os.path.dirname(__file__)
visualize(topology)
# commands = ['command1', 'command2']
# procs = [ Popen(i) for i in commands ]
# for p in procs:
#    p.wait()

launch_commands = []
def rec(server, parents=0):
    global launch_commands
    launch_commands.append(f"python3 {os.path.join(this_dir, 'unit.py')} --num_parents {parents} --cpu {server['cpu']} --port {server['port']} --name {server['name']}")
    if len(server['children']):
        launch_commands[-1]+= f" --children {' '.join([str(i['port']) for i in server['children']])}"
    for child in server['children']:
        rec(child, parents=1)
rec(topology)
print(*launch_commands, sep='\n')

procs = [ Popen(shlex.split(i)) for i in launch_commands ]
for p in procs:
   p.wait()