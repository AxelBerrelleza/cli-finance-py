* How `hello` looks like:

```bash
$ python hello.py
Hello World!
```

And the corresponding help page:

```bash
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit.
```

* How `nested` looks like:
```bash
$ python3.11 nested.py
Usage: nested.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dropdb
  initdb
```

- Ref to docs using parameters: https://click.palletsprojects.com/en/8.1.x/quickstart/#adding-parameters
