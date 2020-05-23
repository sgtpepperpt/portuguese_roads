Tool to get the most popular road types in Portugal, as well as the top road names.

Example usage:
```
wget http://centraldedados.pt/codigos_postais.csv -P /tmp
python3 roads.py /tmp/codigos_postais.csv
```

```
usage: roads.py [-h] [-t] [-n [NAMES]] [-s [SPECIAL]] file

Analyse Portuguese road types and names.

positional arguments:
  file                  Source CSV

optional arguments:
  -h, --help            show this help message and exit
  -t, --types           Print road types
  -n [NAMES], --names [NAMES]
                        Print road names
  -s [SPECIAL], --special [SPECIAL]
                        Print special places
```