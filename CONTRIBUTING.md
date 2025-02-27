# Contribuindo

## Tipos de contribuição

### Enseridos novas startups

1. Você pode utilizar o `scraping.py` e os parsers json ( ex.: [usp](./scraping_and_parsers/parsers/usp_scraping.json) ) e colocando o markedown resultante na [pasta de tabelas](./tables/). `ex.: python scraping.py "parsers/ufpe.json > tables/ufpe.md"`

### Atualizando dados de uma startup

1. Basta modificar diretamente o markedown referente a startup na [pasta de tabelas](./tables/)

## Enviando um pull request

1. Fork e clone o repositório
1. Crie um novo branch: `git checkout -b my-branch-name`
1. Altere o [README](./README) caso haja necessidade ( qualquer alteração neste arquivo irá repercutir no README.md gerado automaticamente pelo Github Actions )

    - toda chave do tipo `![[<tables/qualquer-nome.md>]]` será inserida ao README.md automaticamente
    
1. Faça um push para o seu fork e envie o pull request
1. Aguarde que sua solicitação de pull seja revisada e mesclada

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)
- [Writing good commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

Thanks! :heart: :heart: :heart: