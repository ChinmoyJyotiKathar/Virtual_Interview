import multiprocessing
import time

# Your foo function

def thus(mine):
    print("i'm here")
    print(mine)

def foo(n,mylist):
    
    print("hey now brown cow")
    print("About to return")
    mylist.append(1)
    print(mylist)
        
if __name__ == '__main__':
    # Start foo as a process
    mylist = []
    p = multiprocessing.Process(target=foo, name="Foo", args=(1,mylist,))
    p.start()

    # Wait 10 seconds for foo
    time.sleep(3)
    print(mylist)
    thus(mylist[0])

    # Terminate foo
    if p.is_alive():
        print("foo is running... let's kill it...")
        p.terminate()

    # Cleanup
    p.join()