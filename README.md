importo
=======

Python import time profiler.


Installing
----------

You must be running Python3.7+ for `importo` to work.

To install run

```
$ pip install importo
```

Usage
-----

`importo` can profile any Python module currently installed in your enviroment (virtual or otherwise).


```
$ importo datetime
cum	    self    import
24219   957     runpy
13814   2181    contextlib
11998   2051    site
9016    2735    collections
7796    1934    os
4770    1689    encodings
3438    1328    pkgutil
3349    3349    _collections_abc
2878    661     importlib
```

By default, `importo` will only stay at the root module level, and order by cumulative time.

You can sort by `cumulative` time (time the import and all its child imports took),
`self` (time spent on just this particular import, child imports excluded) and module `name`.
You can also choose the depth of import to go into, much like `du` and other tools do as well as
pipe into other unix commands.

For example
```
$ importo datetime -d 1 -m encodings | head
cum	    self    import
2312    1068    encodings
649     649     encodings.aliases
400     400     encodings.latin_1
273     273     encodings.utf_8
```
> instead of `--match`/`-m` you could also just pipe to grep and it would probably work just fine.

If you're looking for more statistical relevance in import times other than just a couple of runs,
you can specify the number of iterations the profiler goes through.

```
$ importo datetime -i 400 -d 1 -m encodings
cum	    self    import
2071    899     encodings
530     530     encodings.aliases
349     349     encodings.latin_1
332     332     encodings.cp437
246     246     encodings.utf_8
```

For multiple iterations, the p99 values are used as it's probably the most useful.


### Other

For more information on the available options run

```
$ importo -h
```

About
-----
This tool was motivated by the fact that Python3.7 introduced a new feature to show cumulative module import times.

An explanation and use case for this new feature can be found in this [blog entry](https://dev.to/methane/how-to-speed-up-python-application-startup-time-nkf) from a CPython core dev.

This is a wrapper on top of `python -X importtime`.
For small import trees I suggest using that tool first, it will probably suffice for your use case.

For actual production applications for my job, I've found that this tools helps me in narrowing down culprits and statistically tracking improvements.


**Notes**
> I've noticed that the sum of `self` times doesn't fully add to the `cumulative` value of the root module. I don't yet know why this is the case.
