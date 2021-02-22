import matplotlib.pyplot as plt
import networkx as net

G = net.DiGraph() 
C = net.DiGraph()

lst = []
var = str(input(print("Enter schedule: ")))
#print(var)
size = len(var)
 
op = []
txn = []
item = []
 
for i in range(0,size,4):
  op.append(var[i])
  txn.append(var[i+1])
  item.append(var[i+2])
 
#count no. of transactions
new_set = set(txn) 
print("No of transactions:", len(new_set))
 
 
for i in range(0,len(op)):
  if op[i] == 'w':
    for j in range(i+1,len(op)):
      if op[j] =='r' or op[j] =='w':
        if  txn[i] != txn[j] and item[i] == item[j]:
          G.add_edge(txn[i],txn[j])
          print(txn[i],"-->",txn[j])
          

  elif op[i] == 'r':
    for j in range(i+1,len(op)):
      if op[j] == 'w':
        if  txn[i] != txn[j] and item[i] == item[j]:
          G.add_edge(txn[i],txn[j])
          print(txn[i],"-->",txn[j])
          





## DISPLAY OF GRAPH USING networkx and matplotlit.pyplot libraries

lay = net.spring_layout(G)#Specifies the layout in which graph is to be shown

net.draw_networkx_nodes(G,lay,node_size=500)
net.draw_networkx_edges(G,lay,edgelist=G.edges(), edge_color='black')
net.draw_networkx_labels(G,lay)

cycle =[]

try:
  cycle = net.find_cycle(G,orientation="original")        #Throws an exception if no cycle is found, hence we need to handle it using try
except:
  pass

if not cycle:                                   #If not cycle means if list Cycle is NULL
  print("Given schedule is serializable")
else:
  print("Given schedule is not serializable as the precedence graph contains cycle (highlighted in red)")
  for item in range(0,len(cycle)):
    C.add_edge(cycle[item][0],cycle[item][1])
  net.draw_networkx_nodes(C,lay,node_size=500)
  net.draw_networkx_edges(C,lay,edgelist=C.edges(), edge_color='red')
  net.draw_networkx_labels(C,lay)
plt.show()
