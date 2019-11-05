n=8 #number of nodes
edges=[[1,2],
[3,4],
[5,6],
[7,8],
[2,4],
[2,5],
[1,3],
[6,8],
[5,7]]

def disjint():
  parent=[-1 for i in range(n+1)]
  for u,v in edges:
    parent_u,parent_v=parent[u],parent[v]
    if(parent_u==v or parent_v==u):
      print("cycle detected..")
    elif(parent_u<0 and parent_v<0): #means both have diffrent parent
      if(parent_u<=parent_v):
        parent[u]+=parent[v]  #node's count
        parent[v]=u  #parent info
      else:
        parent[v]+=parent[u]  #node's count
        parent[u]=v  #parent info
    else:
      if(parent[parent[u]]<=parent[parent[v]]):
        parent[parent[u]]+=parent[parent[v]]
        parent[parent[v]]=parent[u]
        parent[v]=parent[u]
      else:
        parent[parent[v]]+=parent[parent[u]]
        parent[parent[u]]=parent[v]
        parent[u]=parent[v]

      
    print(u,v,'parent',parent_u,parent_v,parent)
  return parent


print(disjint()) 
