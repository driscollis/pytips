import time

def fast():
    print("I am fast!")
    
def slow():
    time.sleep(2)
    print("I am slow")
    
def snail():
    time.sleep(10)
    print("snail!")
    
def main():
    fast()
    slow()
    snail()
    
main()