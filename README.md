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


## 🚀  Endpoints
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

# 🔧 Instalação
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.
Antes de tudo, é necessário baixar o **[codigo-fonte](https://github.com/eduardo92005-debug/API_Cervejas/archive/refs/heads/main.zip)**  da API e a outra api de servico **[codigo-fonte-2](https://github.com/eduardo92005-debug/API_Playlist/archive/refs/heads/main.zip)**. Daí, basta
seguir os passos abaixo:
* Extraia o zip da API dentro de uma pasta que desejar.
* Abra um terminal dentro da pasta.
* Se necessário instale o pacote de ambientes virtuais do python, use: ``` python -m pip install venv ```
* Escreva o seguinte comando no terminal e aguarde: ``` python -m venv api_venv ```
* Se estiver no sistema operacional Windows use: ``` api_venv\Scripts\Activate ```
* Caso esteja num sistema Linux use: ``` source  api_venv/bin/activate```
* Feito isso, agora é necessário instalar os pacotes para o funcionamento correto da api
* Para isso, use o comando: ``` pip install requirements.txt ```
* Feito isso no primeiro codigo-fonte, faca os mesmos comandos acima com o segundo **[codigo-fonte-2](https://github.com/eduardo92005-debug/API_Playlist/archive/refs/heads/main.zip)**
*  ** DISPONIBILIZACAO EM DOCKER, EM BREVE **
* Feito tudo, va na pasta do API_Cervejas e va no arquivo config.py e insira as credenciais do teu banco de dados local, trocando os valores de PASSWORD,USERNAME e DB.
* Os inserts de exemplo para adicionar no banco de dados para teste, esta no arquivo comandos gerais.
* Execute agora o arquivo python run_test, verifique se os testes passaram, se sim, execute o run.py
* Execute tambem o run.py do API_Playlist
* Acesse o localhost:4444/
* Pronto, agora so usar.


