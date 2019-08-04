import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = threading.Barrier(2)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):          
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barrier.wait()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.barrier.wait()
            printBar()
