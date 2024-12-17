# Flag library
Simple flag processing for Python

### Supported types:

| type | implemented |
|------|-------------|
| int  | True        |
| float| True        |
| str  | True        |
| bool | True        |
| list | True        |

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