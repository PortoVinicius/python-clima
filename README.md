# python-clima - Informações Climáticas

Este é um aplicativo simples em Python que utiliza a [OpenWeather API](https://home.openweathermap.org/) para fornecer informações climáticas em tempo real para uma determinada localização. O aplicativo permite consultar a previsão do tempo atual, incluindo temperatura, umidade, condições climáticas e muito mais.

## Funcionalidades

- Consultar a temperatura atual de uma cidade.
- Obter a condição climática (ex: ensolarado, chuvoso).
- unidades de medida (Celsius).

## Requisitos

Antes de rodar o app, você precisa garantir que tenha os seguintes requisitos:

- Python 3.x ou superior.
- Conta na [OpenWeather API](https://home.openweathermap.org/), para obter a chave da API.


## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/WeatherApp.git

## Crie um ambiente virtual 

    source venv/bin/activate

## Instale as dependências necessárias

    pip install -r requirements.txt

## Configure sua chave da API

### Crie um arquivo .env no diretório raiz do projeto e adicione a chave da API no formato:

    WEATHER_API_KEY=SuaChaveDaAPI


## Como Usar

### Execute o script principal:

    python server.py
