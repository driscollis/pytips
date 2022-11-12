# read_source.py

def do_nothing():
    pass

def do_almost_nothing():
    print("5")
    
with open(__file__) as f:
    print(f.read())