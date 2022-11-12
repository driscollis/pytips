class dog:
    ...
    
@(lambda f: setattr(dog, "on_leash", f))
def walk():
    print("bark, bark")
    
print(dog.on_leash())