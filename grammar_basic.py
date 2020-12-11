# 문법
import random
adj =['beautiful','smart','slim','thin','gorgeous','good-looking']
i = 0
while i < len(adj) - 1:
    print('I am %s as well as %s.' %(adj[random.randint(0, len(adj)-1)],adj[random.randint(0, len(adj)-1)]))
    i += 1

