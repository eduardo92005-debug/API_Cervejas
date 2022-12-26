# Cervejas API

A Cervejas API disponibiliza uma API RESTFUL que permite gerar te recomendar uma cerveja e uma playlist de acordo com uma temperatura dada.

## Recursos 
- Listar todas cervejas do banco.
- Detalhar uma cerveja do banco.
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
| PATCH    | Atualiza parcialmente um registro. |
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

