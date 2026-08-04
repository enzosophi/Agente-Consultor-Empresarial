# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Contexto de Utilização |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as necessidades de aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponiveis para que eles possam ser ensinados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar as informações de forma de didática |

---

## Adaptações nos Dados
 
> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.
>
> '''
> import pandas as pd
> import json
>
> historico = pd.read_csv("data/historico_atendimento.csv")
> transações = pd.read_csv("data/transacoes.csv")

with open("data/perfil_investidor.json", 'r', encoding='utf-8') as f:
perfil = json.load(f)
with open("data/produtos_financeiros.json", 'r', encoding='utf-8') as f:
produto = json.load(f)
> '''

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

para simplificar, podemos injetar os dados no prompt garantindo melhor contexto possivel

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
