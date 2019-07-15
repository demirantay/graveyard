# jokyjokes
Useless package built for learning packaging python projects that provides you jokes.

## Usage

There are 3 modules so far, which are the following:
```python
from jokyjokes import chucknorris  # chuck norris jokes
from jokyjokes import yomama       # yo mama jokes
from jokyjokes import topkek       # topkek jokes
```
And each module contain 10 jokes with 3 methods, which are the following:
```python
chucknorris.random()     # returns a random joke

chucknorris.joke(0)      # returns the first joke

chucknorris.all_jokes()  # returns all jokes as one str
```

### FAQ

Q: Why code something like this at all?

A: I wanted to learn how to package my python projects and upload them to PyPi. The content of the package is insignificant
