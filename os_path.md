## os.path

#### os.path.basename
> Return the base name of pathname path.

```python
>>> import os.path
>>> p1 = 'a/b/c/d.png'
>>> p2 = 'a/b/c'
>>> p3 = 'a'
>>> p4 = '4'
>>> p5 = ''
>>> print(os.path.basename(p1))
d.png
>>> print(os.path.basename(p2))
c
>>> print(os.path.basename(p3))
a
>>> print(os.path.basename(p4))
4
>>> print(os.path.basename(p5))

>>> print(len(os.path.basename(p5)))
0
```

#### 文件后缀操作
```python
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
```