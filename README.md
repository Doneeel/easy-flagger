# Flag library
Simple flag processing for Python

### Supported types:

| type   | implemented |
|--------|-------------|
| int    | True        |
| float  | True        |
| str    | True        |
| bool   | True        |
| list   | True        |
| custom | True        |

## Installation

```bash
$ pip install easy-flagger
```

## Simple usage example
```python
# python example.py -f 10.3
from flagger import Flagger

if __name__ == "__main__":
    flag = Flagger()
    f_flag = flag.parse_flag("-f", float)

    print(f_flag) # >> 10.3
```

## List usage example
```python
# python example.py -l 1,2,3
from flagger import Flagger

if __name__ == "__main__":
    flag = Flagger()
    l_flag = flag.parse_flag("-l", list, sep=",")

    print(l_flag) # >> ['1', '2', '3']
```

## Checks flag for existence example
```python
# python example.py --flag
from flagger import Flagger

if __name__ == "__main__":
    flag = Flagger()
    l_flag = flag.parse_flag("--flag")

    print(l_flag) # >> True
```

## Using custom types flags
```python
# python example.py -e Aerendyl
from flagger import Flagger

class Elven:
    allowed = {
        "aerendyl": 1,
        "erendriel": 2,
        "galadriel": 3
    }
    
    @staticmethod
    def check(value: str):
        value = value.lower()
        is_allowed = value in Elven.allowed
        if not is_allowed:
            raise ValueError("the language is that of Mordor, which I will not utter here")
        
        return Elven.allowed.get(value) 

if __name__ == "__main__":
    flag = Flagger()
    flagger.types.add_parser(Elven, Elven.check)
    
    elf = flagger.parse_flag("-e", Elven)
    
    print(elf) # >> Aerendyl
```
