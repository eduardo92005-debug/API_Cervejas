# Cervejas API

A Cervejas API disponibiliza uma API RESTFUL que permite recomendar uma cerveja e uma playlist de acordo com uma temperatura dada.

## Recursos
- [Listar todas as cervejas no banco](#listar-todas-cervejas)
- [Detalhar uma cerveja no banco](#detalhar-uma-cerveja)
- Listar as temperaturas associadas as cervejas no banco.
- Detalhar uma temperatura.
- Consultar uma playlist recomendada dada uma temperatura
- Inserir uma cerveja no banco
- Inserir uma temperatura no banco
- Deletar uma cerveja no banco
- Deletar uma temperatura no banco
- Atualizar uma cerveja no banco
- Atualizar uma temperatura no banco


## Métodos

Requisicoes para API devem estar no padrao:
| Metodo | Descricao |
|----------|----------|
| GET    | Retorna informações de um ou mais registros.  |
| POST    | Cria um novo registro.  |
| PUT    | Atualiza completamente um registro. |
| DELETE    | Deleta um registro.  |

## Respostas

| Codigo | Descricao |
|----------|----------|
| 200    | Requisicao feita com sucesso. |
| 201    | Registro inserido com sucesso. |
| 204    | Registro deletado com sucesso, sem conteudo para exibir. |
| 400    | Dados inseridos sao invalidos. |
| 404  | Registro nao encontrado. |
| 500  | Erro interno de servidor. |


## Endpoints
### Listar TODAS cervejas
Exibe todas as cervejas inseridas no banco.

``` GET /beers/ ```

### Detalhar uma cerveja
Exibe uma cerveja inserida no banco.

``` GET /beers/1 ```

### Listar TODAS temperaturas
Exibe todas as temperaturas que estao associadas as cervejas.

``` GET /beers/temperature```

### Detalhar uma temperatura
Exibe uma temperatura especifica.

``` GET /beers/temperature/1```

### Recomenda uma playlist e tipos de cervejas
Exibe uma recomendacao de tipo de cerveja e playlist para uma dada temperatura

``` GET /beers/temperature/playlist```
#### Request Body
```json 
{
  temperature: 7
}
```

# Utilizacao


