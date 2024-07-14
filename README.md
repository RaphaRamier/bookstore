Link para interface do projeto(Apenas para PC): https://rapharamier.github.io/bookstore/

# Sistema de Gerenciamento de Livraria API

A API do Sistema de Gerenciamento de Livraria fornece um conjunto abrangente de endpoints para gerenciar vários aspectos das operações de uma livraria. Isso inclui o gerenciamento de livros, autores, publicações, compradores, fornecedores, vendas e fluxo de caixa. Abaixo está uma visão geral dos principais recursos e componentes da API.

## Principais Recursos

1. **Gerenciamento de Montagem de Livros**:
   - Gerenciar detalhes da montagem do livro, incluindo tipo de encadernação, tipo de papel, tipo de capa e peso.

2. **Gerenciamento de Livros**:
   - Gerenciar detalhes dos livros, incluindo título, autor(es), ISBN, gêneros e sinopse.

3. **Gerenciamento de Autores**:
   - Gerenciar perfis de autores, incluindo nome, biografia, data de nascimento e nacionalidade.

4. **Gerenciamento de Publicações**:
   - Gerenciar detalhes das publicações, incluindo livro, data de lançamento, edição, status, quantidade, número de páginas, idioma e preços.

5. **Gerenciamento de Fornecedores**:
   - Gerenciar detalhes dos fornecedores, incluindo nome, informações de contato, endereço, número de documento e número da conta.
   - Acompanhar o tipo de fornecedor (Material ou Serviço) com base em seus componentes ou serviços fornecidos.

6. **Gerenciamento de Compradores**:
   - Gerenciar detalhes dos compradores, incluindo nome, informações de contato, endereço, número de documento e número da conta.
   - Validar informações dos compradores, como CPF/CNPJ e formato do telefone de contato.

7. **Gerenciamento de Vendas**:
   - Gerenciar detalhes das vendas, incluindo comprador, livro, quantidade, data da venda, valor total, número da venda e status.
   - Acompanhar a descrição de cada venda e lidar com a criação de entrada de caixa com base em vendas bem-sucedidas.

8. **Gerenciamento de Fluxo de Caixa**:
   - Acompanhar entradas de caixa de vendas bem-sucedidas e saídas de caixa para serviços e componentes de fornecedores.
   - Gerenciar detalhes do fluxo de caixa, incluindo fonte, valor, data e descrição para entradas e fornecedor, tipo, valor, data e descrição para saídas.

9. **Gerenciamento de Componentes**:
   - Gerenciar detalhes de componentes fornecidos, incluindo nome, descrição, quantidade, preço unitário, preço total, fornecedor e data.

10. **Gerenciamento de Gêneros**:
    - Gerenciar detalhes dos gêneros, incluindo nome do gênero.
    - Acompanhar estatísticas de gêneros, como quantidade total, preço total e preço médio dos livros em cada gênero.

11. **Gerenciamento de Serviços**:
    - Gerenciar detalhes de serviços fornecidos, incluindo nome, descrição, tipo de serviço, preço total, fornecedor e data.
  
11. **Análise e Relatórios**:
    - Fornecer estatísticas detalhadas e análises para livros, autores, publicações, compradores, fornecedores e vendas.
    - Acompanhar tendências mensais e anuais para vendas e transações de fornecedores.

## Endpoints da API

### Montagem de Livros
- `GET /api/assembly/`: Listar todas as montagens de livros.
- `POST /api/assembly/`: Criar uma nova montagem de livro.
- `GET /api/assembly/<id>/`: Obter detalhes de uma montagem de livro específica.
- `PUT /api/assembly/<id>/`: Atualizar uma montagem de livro específica.
- `DELETE /api/assembly/<id>/`: Excluir uma montagem de livro específica.

### Livros
   - `GET /books/` - Listar todos os livros
   - `POST /books/` - Criar um novo livro
   - `GET /books/{id}/` - Detalhar um livro
   - `PUT /books/{id}/` - Atualizar um livro
   - `DELETE /books/{id}/` - Deletar um livro
   - `GET /books/statistics/` - Estatísticas dos livros

### Autores
- `GET /api/authors/`: Listar todos os autores.
- `POST /api/authors/`: Criar um novo autor.
- `GET /api/authors/<id>/`: Obter detalhes de um autor específico.
- `PUT /api/authors/<id>/`: Atualizar um autor específico.
- `DELETE /api/authors/<id>/`: Excluir um autor específico.

### Publicações
- `GET /api/publications/`: Listar todas as publicações.
- `POST /api/publications/`: Criar uma nova publicação.
- `GET /api/publications/<id>/`: Obter detalhes de uma publicação específica.
- `PUT /api/publications/<id>/`: Atualizar uma publicação específica.
- `DELETE /api/publications/<id>/`: Excluir uma publicação específica.

### Fornecedores
- `GET /api/suppliers/`: Listar todos os fornecedores.
- `POST /api/suppliers/`: Criar um novo fornecedor.
- `GET /api/suppliers/<id>/`: Obter detalhes de um fornecedor específico.
- `PUT /api/suppliers/<id>/`: Atualizar um fornecedor específico.
- `DELETE /api/suppliers/<id>/`: Excluir um fornecedor específico.
- `GET /api/suppliers/statistics/`: Obter estatísticas dos fornecedores.

### Compradores
- `GET /api/buyers/`: Listar todos os compradores.
- `POST /api/buyers/`: Criar um novo comprador.
- `GET /api/buyers/<id>/`: Obter detalhes de um comprador específico.
- `PUT /api/buyers/<id>/`: Atualizar um comprador específico.
- `DELETE /api/buyers/<id>/`: Excluir um comprador específico.
- `GET /api/buyers/statistics/`: Obter estatísticas dos compradores.

### Vendas
- `GET /api/sales/`: Listar todas as vendas.
- `POST /api/sales/`: Criar uma nova venda.
- `GET /api/sales/<id>/`: Obter detalhes de uma venda específica.
- `PUT /api/sales/<id>/`: Atualizar uma venda específica.
- `DELETE /api/sales/<id>/`: Excluir uma venda específica.
- `GET /api/sales/daily-trend/`: Obter tendências diárias de vendas.
- `GET /api/sales/monthly-trend/`: Obter tendências mensais de vendas.
- `GET /api/sales/yearly-trend/`: Obter tendências anuais de vendas.

### Fluxo de Caixa
- `GET /api/cashflow/`: Obter detalhes do fluxo de caixa.
- `GET /api/cashflow/inflow/`: Listar todas as entradas de caixa.
- `POST /api/cashflow/inflow/`: Criar uma nova entrada de caixa.
- `GET /api/cashflow/inflow/<id>/`: Obter detalhes de uma entrada de caixa específica.
- `PUT /api/cashflow/inflow/<id>/`: Atualizar uma entrada de caixa específica.
- `DELETE /api/cashflow/inflow/<id>/`: Excluir uma entrada de caixa específica.
- `GET /api/cashflow/outflow/`: Listar todas as saídas de caixa.
- `POST /api/cashflow/outflow/`: Criar uma nova saída de caixa.
- `GET /api/cashflow/outflow/<id>/`: Obter detalhes de uma saída de caixa específica.
- `PUT /api/cashflow/outflow/<id>/`: Atualizar uma saída de caixa específica.
- `DELETE /api/cashflow/outflow/<id>/`: Excluir uma saída de caixa específica.
- `GET /api/cashflow/performance-data/`: Obter dados de desempenho do fluxo de caixa.
- `GET /api/cashflow/suppliers/monthly-trend/`: Obter tendências mensais de fornecedores.
- `GET /api/cashflow/buyers/monthly-trend/`: Obter tendências mensais de compradores.

### Componentes
- `GET /api/components/`: Listar todos os componentes.
- `POST /api/components/`: Criar um novo componente.
- `GET /api/components/<id>/`: Obter detalhes de um componente específico.
- `PUT /api/components/<id>/`: Atualizar um componente específico.
- `DELETE /api/components/<id>/`: Excluir um componente específico.
- `GET /api/components/statistics/monthly/`: Obter estatísticas mensais de componentes.
- `GET /api/components/statistics/yearly/`: Obter estatísticas anuais de componentes.

### Gêneros
- `GET /api/genres/`: Listar todos os gêneros.
- `POST /api/genres/`: Criar um novo gênero.
- `GET /api/genres/<id>/`: Obter detalhes de um gênero específico.
- `PUT /api/genres/<id>/`: Atualizar um gênero específico.
- `DELETE /api/genres/<id>/`: Excluir um gênero específico.
- `GET /api/genres/stash/`: Obter estoque de gêneros.

### Serviços
- `GET /api/services/`: Listar todos os serviços.
- `POST /api/services/`: Criar um novo serviço.
- `GET /api/services/<id>/`: Obter detalhes de um serviço específico.
- `PUT /api/services/<id>/`: Atualizar um serviço específico.
- `DELETE /api/services/<id>/`: Excluir um serviço específico.

# Sistema de Gestão de Livraria

## Visão Geral do Cliente

A aplicação cliente é responsável por fornecer uma interface intuitiva e amigável para gerenciar os diferentes aspectos da livraria. Abaixo estão as principais funcionalidades e interfaces disponíveis na aplicação cliente.



### Funcionalidades Principais

1. **Dashboard**
    - Visão geral das métricas financeiras e operacionais.
    - Gráficos de tendências de vendas e despesas.
    - Resumo dos fornecedores e compradores mais ativos.

2. **Gestão de Livros**
    - Adição, edição de livros.
    - Visualização de detalhes de cada livro.
    - Busca e filtragem de livros por diferentes critérios.

3. **Gestão de Autores**
    - Adição, edição de autores.
    - Visualização de detalhes de cada autor.
    - Busca e filtragem de autores.

4. **Gestão de Gêneros**
    - Adição, edição de gêneros.
    - Visualização de detalhes de cada gênero.
    - Estatísticas de estoque e valor médio dos livros por gênero.

5. **Gestão de Publicações**
    - Adição, edição de publicações.
    - Visualização de detalhes de cada publicação.
    - Busca e filtragem de publicações.

6. **Gestão de Compradores**
    - Adição, edição de compradores.
    - Visualização de detalhes de cada comprador.
    - Estatísticas de compras e tendências de gasto.

7. **Gestão de Vendas**
    - Registro de novas vendas.
    - Visualização de histórico de vendas.
    - Tendências mensais de vendas.

8. **Gestão de Fornecedores**
    - Adição, edição de fornecedores.
    - Visualização de detalhes de cada fornecedor.
    - Estatísticas de despesas e tendências de fornecimento.

9. **Gestão de Componentes e Serviços**
    - Registro de componentes e serviços fornecidos.
    - Visualização de detalhes e histórico de fornecimento.
    - Estatísticas de gastos por tipo de fornecimento.

10. **Fluxo de Caixa**
    - Visualização de entradas e saídas de caixa.
    - Relatórios de desempenho financeiro.
    - Gráficos de fluxo de caixa mensal.

## Observação a cerca da Exclusão de dados

**Qualquer exclusão, de qualquer item do banco de dados, deve ser feita somente no Admin. Por usuários autorizados.**

## Instalação e Configuração

Para configurar e executar o projeto, siga as etapas abaixo:

- Caso não use o Docker:

1. Clone o repositório:
    ```sh
    git clone <URL-do-repositório>
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd bookstore
    ```

3. Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências do projeto:
    ```sh
    pip install -r requirements.txt
    ```

5. Execute as migrações para criar o banco de dados:
    ```sh
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o admin do Django:
    ```sh
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

8. Acesse a aplicação no navegador em `http://127.0.0.1:8000/`.

- Caso use o Docker:

1. Clone o repositório:
    ```sh
    git clone <URL-do-repositório>
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd bookstore
    ```

3. Use o comando no terminal:
   ```sh
    docker-compose up db --build
    docker-compose up
    ```
   
4. Acesse o Bash do Container :
   ```sh
   docker exec -it bookstore-bookstore-1 /bin/bash
   ```

6. Crie um superusuário para acessar o admin do Django:
    ```sh
    python manage.py createsuperuser
    ```

7. Acesse a aplicação no navegador em `localhost:8000/`.


## Contribuição

Para contribuir com o projeto, siga as etapas abaixo:

1. Crie um fork do repositório.
2. Crie um branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Minha nova feature'`).
4. Faça um push para o branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
