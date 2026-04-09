# Analise de dados BACEN

## Como estou desenvolvendo as analises

Primeiramente, para facilitar na hora do desenvolvimento estou usando o Jupyter para separar as celulas e conseguir testar individualmente elas.

### Primeira célula é responsavel por importar as bibliotecas

```python
import pandas as pd
import requests
from sqlalchemy import create_engine,types
from datetime import datetime,timedelta
```

**Pandas:** é a biblioteca que vamos usar para analisar os dados e criar os dataframes

**Requests:** a biblioteca responsavel por pegar os dados das API por meio das URL, no nosso caso responsavel por se comunicar com a API do BACEN

**SQLalchemy:** responsavel por fazer a comunicação do Python com o banco de dados SQL, no nosso caso estamos usando o postgresql
