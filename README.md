# webscraping_scrapy
webscraping utilizando scrapy para coletar dados do site https://www.imdb.com/chart/top/

Tutorial de `Scraping` utilizando `Scrapy` apresentado pelo canal do Youtube `Hashtag Programação`.

Ele acessa o link https://www.imdb.com/chart/top/ e coleta o título, ano e avaliação dos top 250 filmes e salva em um arquivo .JSON

## Executando

- Baixe o repositório e abra o terminal no projeto
```shell
git clone https://github.com/felixrodrigo19/webscraping_scrapy.git
```
```console
$ cd webscraping_scrapy
```
- Digite os seguintes comandos
```console
$ conda create -n tutorial_scrapy -y
$ conda activate tutorial_scrapy
$ conda install pip -y
$ pip install scrapy
$ scrapy crawl imdb -O result.json
```
Do comando scrapy crawl imdb -O result.json:
- scrapy crawl imdb: Inicia crawling usando um spider chamado imdb
- -O result.json: Armazena os resultados em um arquivo chamado result.json sempre reescrevendo a cada execução. Para inserir no final do arquivo em cada execução, troque o `-O` por `-o`
