# End2EndTitanic

## Descrição do Projeto

## Previsão de Sobrevivência com Flask

Este projeto é um aplicativo web desenvolvido com Flask que prevê a probabilidade de sobrevivência de passageiros a partir de dados do Titanic. A aplicação utiliza técnicas de machine learning para treinar um modelo de Random Forest e fornece uma interface web para que os usuários insiram os dados dos passageiros e obtenham as previsões.

## Estrutura do Projeto

O projeto está organizado em três camadas principais, dentro da pasta `src`:

1. **Camada de Dados (Data Layer)**:
   - Responsável pela extração e transformação dos dados.
   - Implementada no arquivo `src/data_layer.py`.

2. **Camada de Negócios (Business Layer)**:
   - Responsável pelo treinamento do modelo de machine learning e pelas previsões.
   - Implementada no arquivo `src/business_layer.py`.

3. **Camada de Apresentação (Presentation Layer)**:
   - Responsável pela interface do usuário utilizando Flask.
   - Implementada no arquivo `src/presentation_layer.py`.

### Estrutura de Diretórios

```
project/
│
├── src/
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── data_layer.py
│   ├── business_layer.py
│   ├── presentation_layer.py
│
└── app.py
```

### Arquivos Principais

- **src/data_layer.py**:
  Contém a classe `DataLayer`, que realiza a extração e transformação dos dados.

- **src/business_layer.py**:
  Contém a classe `BusinessLayer`, que treina o modelo de Random Forest e realiza as previsões.

- **src/presentation_layer.py**:
  Contém a classe `PresentationLayer`, que cria a aplicação Flask e define as rotas para a interface do usuário.

- **app.py**:
  Script principal que integra todas as camadas e inicia o aplicativo Flask.

### Templates HTML

- **src/templates/index.html**:
  Formulário para entrada de dados dos passageiros.

- **src/templates/result.html**:
  Página de resultados que exibe a probabilidade de sobrevivência e a classificação.

## Configuração e Execução

### Pré-requisitos

- Python 3.x
- Flask
- pandas
- requests
- scikit-learn

### Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

### Execução

1. Execute o script principal:
   ```sh
   python app.py
   ```

2. Abra o navegador e acesse:
   ```
   http://127.0.0.1:5000/
   ```

## Uso

1. Insira os dados do passageiro no formulário.
2. Clique em "Prever Sobrevivência".
3. Veja a probabilidade de sobrevivência e a classificação na página de resultados.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License.

---

Este é um projeto de exemplo para ilustrar a implementação de um modelo de machine learning em um aplicativo web utilizando Flask. Espero que sirva como um ponto de partida para seus próprios projetos de machine learning e desenvolvimento web.

---