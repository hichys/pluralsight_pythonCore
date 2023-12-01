def squence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


seq = squence_class(immutable=True)
t = seq("this is tuple")
print(t, type(t))
seq = squence_class(immutable=False)
l = seq("this is list")
print(l, type(l))
