import json
import requests
from bs4 import BeautifulSoup

__author__ = 'Kozo Nishida'
__email__ = 'knishida@riken.jp'
__version__ = '0.0.1'
__license__ = 'MIT'

API_BASE = 'http://rest.kegg.jp/'

def kegg2cyjs(identifier):
    kgml = requests.get(API_BASE + 'get/' + identifier + '/kgml').content
    soup = BeautifulSoup(kgml, "xml")
    entries = soup.find_all('entry')
    d = {}
    elements = {}
    nodes = []
    edges = []
    for e in entries:
        g = e.find("graphics")
        data = {}
        data["id"] = e["id"]
        if e["type"] != "group":
            data["label"] = g["name"].split(", ")[0]
            data["name"] = g["name"]
        data["x"] = int(g["x"])
        data["y"] = int(g["y"])
        data["fgcolor"] = g["fgcolor"]
        data["bgcolor"] = g["bgcolor"]
        data["type"] = g["type"]
        data["width"] = g["width"]
        data["height"] = g["height"]
        node = {"data":data, "position":{"x":int(g["x"]), "y":int(g["y"])}, "selected":"false"}
        nodes.append(node)
    relations = soup.find_all('relation')
    for rel in relations:
        stype = rel.find("subtype")
        data = {}
        data["source"] = stype["value"]
        data["target"] = rel["entry1"]
        data["type"] = rel["type"]
        edge = {"data":data}
        edges.append(edge)
        data["target"] = rel["entry2"]
        edge = {"data":data}
        edges.append(edge)
    elements["nodes"] = nodes
    elements["edges"] = edges
    d["elements"] = elements
    return json.dumps(d, indent=4)
