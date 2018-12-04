## OS.Path

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