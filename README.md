# File Parser

>Sei stanco di dover scrivere sempre lo stesso codice per aprire file **csv** o **xlsx** ?  

![](./docs/patrick.jpg)

> Ogni tanto ti trovi ad aprire dei **json** o degli **ini** di configurazione ?

> Getti la spugna quando ti trovi davanti a degli **xml** ?

Bene, allora **FileParser** puo' fare al caso tuo!


## Che cos'e'?
**FileParser** e' una libreria Python che ti permette di aprire qualsiasi tipo di file e convertirli in un meta-dizionario.

Attualmente **FileParser** supporta i seguenti tipi di file: **json, csv, xlsx, ini, xml**, ma ne potrebbe contenere molti altri!

## Come funziona?
Facile, se vuoi parsere dei json cosi'

```{.py}
from file_parser import FileParser

fp = FileParser()
fp.read('file.json')
_res = fp.parse('json')

print(_res)

```

Banale no ?

Be', la cosa forte e' che puoi usare lo stesso metodo per qualsiasi tipo di file supportato!

```{.py}
# ini
_res = fp.parse('ini')

# xml
_res = fp.parse('xml')

# xlsx
_res = fp.parse('xlsx')

# csv
_res = fp.parse('csv')

```

## Dimmi di piu'
Con **FileParser** si possono fare tante altre cose, come:
* convertire un tipo di file in un altro (xml -> json, xlsx -> csv )
* parsare del testo grezzo in un formato specifico (raw -> json )
* importare agevolmente dei dati xlsx, modificarli e salvarli in csv 

>**E tanto altro!**

Se sei interessato guarda pure altri esempi in `/example`

---

## Classics Usage

```
from file_parser import FileParser
from typing import Dict, List
fp = FileParser()
fp.read('data.xlsx')

_content:List[Dict] = fp.parse('xlsx')
```

---

### Esempio 1: Conversione
xlsx -> csv

``` {.py}
from file_parser import FileParser
fp = FileParser()
fp.read('sample.xlsx')
fp.parse('xlsx')
fp.write('csv', 'test.csv')
```

xml -> json
``` {.py}
from file_parser import FileParser
fp = FileParser()
fp.read('sample.xml')
fp.parse('xml')
fp.write('json', 'test.json')
```

### Esempio 2: Parsing
```{.py}
from file_parser import FileParser

_json:str = """{"EmployerData": [{"firstName": "Rachel", "lastName": "Booker", "userName": "booker12"}, {"firstName": "Laura", "lastName": "Grey", "userName": "grey07"}, {"firstName": "Craig", "lastName": "Johnson", "userName": "johnson81"}, {"firstName": "Mary", "lastName": "Jenkins", "userName": "jenkins46"}]}"""

fp = FileParser()
setattr(fp, 'raw_content', _json)
parsed_json = fp.parse('json')

isinstance(parsed_json, dict) # True
```

### Esempio 3: Data Cleaning / Processing
```{.py}
from file_parser import FileParser
from typing import Dict, List
from copy import deepcopy

fp = FileParser()
fp.read('sample.xlsx')
rows:List[Dict] = fp.parse('xlsx')

# add column
i:int = 0
for row in rows:
    row['Extra Column'] = i
    i += 1

# rename columns
_rows = deepcopy(rows)
rows  = []
for _row in _rows:
    d = {}
    for k,v in _row.items():
        d[k.lower().strip()] = v
    rows.append(d)
del _rows

# save in a new file
_headers = list(rows[0].keys())

fp.write('csv', output_path='test.csv', content=rows, delimiter=';', headers=_headers)

```


---
## Installazione

**FileParser** richiede `python` >= `3.8` 


```{.sh}
make install
make build
make pip-install # per installare la libreria
```
