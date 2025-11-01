import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useEffect, useState } from 'react';
import { GraphCanvas } from "reagraph";
import chroma from 'chroma-js';

function App() {
  var [refresh, setRefresh] = useState(0);
  var [data, setData] = useState({})
  var [nodesData, setNodesData] = useState({ nodes: [], edges: [] })
  useEffect(() => {
    var nodes = [];
    var edges = [];
    var rg = chroma.scale(['green', 'red'])

    function rec(serv) {
      nodes.push({ id: serv.name, label: serv.name, fill:rg(Math.min(1, serv.load/serv.cpu)).hex() })
      if (serv.children) {
        serv.children.forEach(element => {
          edges.push({ id: `${serv.name}->${element.name}`, source: serv.name, target: element.name, label: ' ' })
          rec(element)
        })
      };
    };
    rec(data);
    setNodesData({ nodes, edges })
  }, [data])
  useEffect(() => {
    fetch("http://localhost:7999/echo", { method: "GET", headers: { 'accept': 'application/json' } }).then(r => r.json()).then(json => {
      setData(json);
      setTimeout(() => { setRefresh(refresh + 1) }, 3000)
    })

    
  }, [refresh])

  return (
    <div className="App">
      {JSON.stringify(data)}
      {JSON.stringify(nodesData)}
      <GraphCanvas
        nodes={nodesData.nodes}
        edges={nodesData.edges}
      />
    </div>
  );
}

export default App;
