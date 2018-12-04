

def del_ext(path):
    if '.' in path:
        return path.rsplit('.', 1)[0]
    return path

print(del_ext('a/b/c.png')) # a/b/c
print(del_ext('c.png'))     # c
print(del_ext('c'))         # c

def get_ext(path):
    if '.' in path:
        return path.rsplit('.', 1)[1]
    return None

print(get_ext('a/b/c.png')) # png
print(get_ext('c.png'))     # png
print(get_ext('c'))         # None

# >dirname(p)
#     Returns the directory component of a pathname

path = "a/b/c.png"
import os.path
print(os.path.dirname(path))

