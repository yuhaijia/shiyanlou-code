def dfs(G,s,S=None,res=None):
    if S is None:
        # 储存已经访问节点
        S=set()
    if res is None:
        # 存储遍历顺序
        res=[]
    res.append(s)
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        S.add(u)
        dfs(G,u,S,res)

    return res

G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(dfs(G, '0'))

# 打印结果为：
# ['0', '1', '2', '3', '4', '5']
