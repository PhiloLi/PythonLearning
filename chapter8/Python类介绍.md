# Python 类介绍
1、为了挂接‘with’语句，需要创建一个实现并遵循上下文管理协议的类。
2、Python编程语言支持面向对象，函数式和过程式编程，并鼓励混合使用这三种编程方式，以合适的方式使用。

## 面向对象入门

类的声明和调用

pass语法

编程规范（区分方法调用和对象实例化）

为类增加方法

self的作用


Bullet points
* Python类允许你共享行为和状态
* class关键字在代码中引入一个新类
* 如果从一个类创建一个对象，这个对象会从这个类创建的所有其他对象共享这个类的代码。不过，每个对象会维护自己的属性。
* 通过创建方法来为类增加行为。方法就是在类中定义的函数。
* 向每个方法传入当前对象的一个别名作为它的第一个参数。Python约定坚持第一个参数为self。
* 在方法代码组中，引用属性时要加self前缀，确保方法代码结束后属性值仍然存在。
* _init_方法是Python类的初始化方法，可以通过重写该方法为类的属性赋予初始值。


代码示例入下：
```python
class CountFromBy:
    def __init__(self, v: int =0, i: int =1) -> None:
        pass
    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

```

