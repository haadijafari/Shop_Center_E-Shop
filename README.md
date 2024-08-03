# Shop Center E-Shop

My first E-shop django application!\
I try to make it as good as it could be and improve it over time :D


![EShop](/src/main.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.\
For development:
```bash
pip install eshop/requirements/development.txt
```
For production:
```bash
pip install eshop/requirements/production.txt
```
After installing the requirements you should create a ``.end`` file inside eshop directory (project root directory) and fill out these values:
```text
SECRET_KEY=
DEBUG=True or False
RECAPTCHA_PUBLIC_KEY_V2=
RECAPTCHA_PRIVATE_KEY_V2=
RECAPTCHA_PUBLIC_KEY_V3=
RECAPTCHA_PRIVATE_KEY_V3=
SQL_NAME=
SQL_USER=
SQL_PASS=
```

## Usage

Just use it as you would use a Django project.\
Use ``wsgi.py`` or ``asgi.py`` for production or use the ``manage.py`` for development.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
