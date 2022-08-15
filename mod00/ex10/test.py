from loading import ft_progress
from time import sleep

ret = 0
X = range(100)
for elem in ft_progress(X):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
