from collections import deque


D = deque()
# len(D)
# D.appendleft()
#D.append()
#D.popleft()
#D.pop()
#D[0]
#D[-1]
#D[j]
#D[j] = val
#D.clear()
#D.rotate(k) - rightwards shift
#D.remove(e) - remove first elemet e
#D.count(e) - count number of occurences

D.append(5)
D.appendleft(3)
D.appendleft(7)
print(D[0])
print(D.pop())
print(len(D))
print(D.pop())
print(D.pop())
D.appendleft(6)
print(D[-1])
D.appendleft(8)
print(len(D) == 0)
print(D[-1])
D.rotate(2)
print(D)

