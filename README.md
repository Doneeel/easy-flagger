# Flag library
Simple flag processing for Python

### Supported types:
    
- [x] int
- [x] float
- [x] str
- [x] bool
- [x] list

## Installation

```bash
pip install simple-flagger
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