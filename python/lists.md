# Lists

List variables are references to underlying data structure.

```
x = ["a", "b", "c"]
y = x
y[1] = "d"
>>>y
['a', 'd', 'c']
>>>x
['a', 'd', 'c']
```
To make a copy of a list:
```
y = list(x)
y = x[:]
```

Last item of a list:
```
>>>x[-1]
'c'
```
