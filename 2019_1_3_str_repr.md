## \_\_str\_\_ vs \_\_repr\_\_

### 情况一
> 两函数同时存在时,print()和str()方法使用__str__    
> repr()函数使用__repr__
```python
class Test:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "str:<Test> {}".format(self.value)

    def __repr__(self):
        return "repr:<Test> {}".format(self.value)


if __name__ == "__main__":
    t = Test("hello")
    print(t)        # 输出 str:<Test> hello
    print(str(t))   # 输出 str:<Test> hello
    print(repr(t))  # 输出 repr:<Test> hello
```

### 情况二
> 仅存在__str__时, print()和str()方法使用__str__    
> repr()函数使用默认返回, 包括对象类及内存地址
```python
class Test:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "str:<Test> {}".format(self.value)


if __name__ == "__main__":
    t = Test("hello")
    print(t)        # 输出 str:<Test> hello
    print(repr(t))  # 输出 <__main__.Test object at 0x10351f2e8>


class Test:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "repr:<Test> {}".format(self.value)


if __name__ == "__main__":
    t = Test("hello")
    print(t)        # 输出 repr:<Test> hello
    print(repr(t))  # 输出 repr:<Test> hello
```

### 情况三
> 仅存在__repr__时, print()\repr()\str()方法均使用__repr__
```python
class Test:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "repr:<Test> {}".format(self.value)


if __name__ == "__main__":
    t = Test("hello")
    print(t)        # 输出 repr:<Test> hello
    print(repr(t))  # 输出 repr:<Test> hello
```

### 补充交互模式下
> 只有__repr__时, str()也会使用__repr__   
> 只有__str__时, repr默认返回对象类名和内存地址, str()和print()使用__str__
```python
# 只有__repr__
>>> class Test:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return "<Test>__repr__"
...
>>> t = Test('hello')
>>> t
<Test>__repr__
>>> print(t)
<Test>__repr__

# 只有__str__
>>> class Test:
...     def __init__(self, value):
...         self.value = value
...     def __str__(self):
...         return "<Test>__str__"
...
>>> t = Test('hello')
>>> t
<__main__.Test object at 0x102f1bc18>
>>> print(t)
<Test>__str__

```


### 总结
* __repr__主要面向开发者, 提供repr()函数和交互模式下直接输出对象使用
* __str__主要面向用户, 在print(obj)和str(obj)时提供相关信息
* 如果想统一输出, 可以考虑仅实现__repr__(实际上__str__只是覆盖了__repr__以得到更友好的用户显示)


### 参考
[Python中__repr__和__str__区别](https://blog.csdn.net/luckytanggu/article/details/53649156)




