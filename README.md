# Test Técnico BackEnd

> O projeto foi desenvolvivo com foco em receber arquivos .txt sem formatação e conseguir retornar ele de forma formatada, e inserido a um banco de dados relacional, retornando inicialmente, nome da loja, transações realizadas e seu saldo atual com base nas transações, podendo escalonar ao usar os demais dados que são passados e guardados no banco.

## Tecnologias Utilizadas:
    Python, Django (DRF), Docker, Heroku,

## Instalação Rápida:
    instalar máquina virtual:
> python -m venv venv

    instalar dependencias:
> pip install -r requirements.txt

    configurar .env:
    > copiar ou renomear .env.example inserindo os dados pedidos no arquivo

    banco de dados:
> criar banco de dados para inserção de dados

    instalar migrations:
> python manage.py migrate


## Rotas:
    heroku: https://backend-django-tiblazy.herokuapp.com/api/upload/
    local: http://127.0.0.1:8000/api/upload/

## Formato de Retorno:
>   POST

>   Arquivo não enviado:

    {
        "file_uploaded": [
            "The submitted data was not a file. Check the encoding type on the form."
        ]
    }

>   Arquivo .txt enviado:
    
    {
    "file_uploaded": null
    }

>   GET

>   Lista vazia:

    []

>   Lista populada e tratada:

    [
        {
            "store": "LOJA DO Ó - FILIAL",
            "currency": 456.96,
            "transactions": [
                {
                    "type": "Credit",
                    "value": 152.32
                },
                {
                    "type": "Credit",
                    "value": 152.32
                },
                {
                    "type": "Credit",
                    "value": 152.32
                }
            ]
        }
    ]