# Django USWDS Theme

USWDS Documentation: https://designsystem.digital.gov/documentation/developers/

To add to your Django project, from the base directory:

```sh
git submodule add https://github.com/ChrisCompton/django-uswds
```

Submodules can be confusing to manage in your project, but are very powerful.  You can [learn more here](https://www.atlassian.com/git/tutorials/git-submodule).


In `settings.py`:

```python
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ['django-uswds/templates'],
            "APP_DIRS": True,
            ...
        },
    ]
```

```python
    STATICFILES_DIRS = [
        ("uswds", BASE_DIR / "django-uswds/vendor/dist")
    ]
```

See `templates/index.html` to get started, or copy into your own app.