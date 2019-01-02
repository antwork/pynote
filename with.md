## with语法

### 示例
```python
# 不使用with打开文件
f = open('hello.txt')
for line in f.readline():
    print(line)
f.close()

# 使用with打开文件
with open('hello.txt') as f:
    for line in f.readline():
        print(line)
```

### with魔法
> with主要使用两个方法   
> \_\_enter\_\_() 进入    
> \_\_exit\_\_() 退出

### with使用实例

```python
class WithDemo:
    def __init__(self):
        print("__init__")

    # 注意这里需要返回self, 否则以下代码会输出None
    # print("with process {}".format(obj)) -> with process None
    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exc_type {}".format(exc_type))
        print("exc_value {}".format(exc_value))
        print("traceback {}".format(traceback))

    def __repr__(self):
        return "__repr__ of WithDemo"

if __name__ == "__main__":
    with WithDemo() as obj:
        print("with process {}".format(obj))

    print("leave")


# 输出
__init__
__enter__
with process __repr__ of WithDemo
exc_type None
exc_value None
traceback None
leave

```

### with中抛出异常
> 使用with语句, 即使执行中抛出异常, 也会执行__exit__方法  
> 实际上异常当做参数被传入了__exit__方法
```python
class WithDemo:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exc_type {}".format(exc_type))
        print("exc_value {}".format(exc_value))
        print("traceback {}".format(traceback))

    def __repr__(self):
        return "__repr__ of WithDemo"

if __name__ == "__main__":
    with WithDemo() as obj:
        print("with process {}".format(obj))
        raise Exception("raise a Exception")
    print("leave")

# 输出

__init__
__enter__
with process __repr__ of WithDemo
exc_type <class 'Exception'>
exc_value raise a Exception
traceback <traceback object at 0x10340e1c8>
Traceback (most recent call last):
  File "with_demo.py", line 20, in <module>
    raise Exception("raise a Exception")
Exception: raise a Exception

```