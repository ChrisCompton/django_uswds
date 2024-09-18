# Django USWDS Theme

Documentation: https://designsystem.digital.gov/documentation/developers/

In `settings.py`:

```python
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ['uswds/templates'],
            "APP_DIRS": True,
            ...
        },
    ]
```

```python
    STATICFILES_DIRS = [
        ("uswds", BASE_DIR / "uswds/vendor/dist")
    ]
```

See `templates/index.html` to get started, or copy into your own app.