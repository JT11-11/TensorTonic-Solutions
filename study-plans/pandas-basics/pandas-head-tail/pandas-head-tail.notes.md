Not much except

1. If you want to get the top/bottom of head and tail use .head/tail(number)
2. if u want to control type returned by to_dict(), use:

```
.to_dict(orient="list)
```

this controls return format of the dictionary values



Alternative is: 

```
.to_dict(orient="record") 
```

which gives 

```
[
    {"name": "A", "val": 1},
    {"name": "B", "val": 2}
]
```

whcih is a list of dictionary