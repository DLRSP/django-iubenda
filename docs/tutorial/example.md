# Example project

The reference demo uses the **[DLRSP/example](https://github.com/DLRSP/example)** repository on the **`django-iubenda`** branch. It shows a minimal Django site with `iubenda` and `requests_api` installed, policy URLs, and the usual Iubenda context processor.

## Clone and run

```shell
git clone --depth=50 --branch=django-iubenda https://github.com/DLRSP/example.git example-iubenda
cd example-iubenda

python -m venv env
source env/bin/activate
# On Windows: env\Scripts\activate

pip install -r requirements/py38-django32.txt

python manage.py migrate
python manage.py runserver
```

Adjust the `requirements/*.txt` file to match your Python and Django versions if needed.

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) and use the privacy and cookie policy routes provided by django-iubenda (see the main [installation guide](../index.md#installation)).
