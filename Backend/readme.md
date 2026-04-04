# Como rodar o projeto

*Importante*: Antes de rodar o projeto, é preciso ter o docker instalado.

1° - Abra a pasta raiz do back-end no terminal (/Controle-Certificados/backend);

2° - Faça o build dos containers e faça-os rodar em background com o seguinte comando:

```bash
docker compose up --build -d
```

3° - Se quiser adicionar alguma biblioteca ao projeto, adicione-a no arquivo "requirements.txt" em "/backend/python_api" e rode novamente o comando do passo 2 para rebuildar os dockers e a biblioteca ser instalada.

Importante:
O comando pode variar um pouco a depender da forma como o docker foi instalado, esse que eu passei funciona perfeitamente no docker instalado nativamente no linux, porém se você usa windows e instalou o docker via wsl por exemplo, pode ser que a sintaxe não seja exatamente essa.


## Conexão com os containers

- MySQL: O container do mysql está rodando na porta `3306` e usando as credenciais que estão no arquivo "docker-compose.yml", use elas para fazer conexão no mysql workbench ou em qualquer outro app de gerenciamento de banco de dados.
- Python_api: O container do python está originalmente escutando a porta `5000`, vcs terão que configurar o fastAPI para rodar nessa porta também, ou o container não vai receber as requisições, se surgir a necessidade de muda-la, avise os tech-leads na comunidade e informe o motivo.