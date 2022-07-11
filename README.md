### beecrowd-stream-overlay

aplicação simples usando FastAPI para exibir dados do [beecrowd](https://beecrowd.com.br/) em livestreams usando Open
Broadcaster Software e derivados.

---

### Para iniciar o servidor:

- instale as dependencias usando o comando:

```shell
pip3 install -r requirements.txt
# ou
python -m pip install -r requirements.txt
```

- altere as configurações, como host e porta da aplicações no arquivo `config.py`
- execute o servidor usando

```shell
python3 main.py
# ou
python main.py
```

- adicione uma nova source de navegador no OBS, com a url indicada no terminal
- :3