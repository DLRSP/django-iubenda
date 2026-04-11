# Templates

You can override django-iubenda’s templates from your project by placing files under your templates directory using the same paths as the app.

## App template names

Under `iubenda/templates/iubenda/` the package ships:

| Template | Purpose |
|----------|---------|
| `privacy.html` / `privacy-compress.html` | Privacy policy page (`IUBENDA_USE_COMPRESS` selects the compressed variant). |
| `cookie.html` / `cookie-compress.html` | Cookie policy page. |
| `include-content.html` | Fragment included in the site footer (or elsewhere) for scripts and policy links. |

## Override in your project

1. Ensure your `TEMPLATES` `DIRS` includes a folder that wins over app templates (for example `templates/` at the project root).
2. Copy the file you need and edit it, keeping the path:

```text
your_project/templates/iubenda/privacy.html
your_project/templates/iubenda/include-content.html
```

Django resolves templates in app order and `DIRS` first (depending on your `OPTIONS`), so a file in your project with the path `iubenda/privacy.html` overrides the packaged version.

## Compressor

When `django_compressor` is enabled and **`USE_COMPRESS`** / **`IUBENDA_USE_COMPRESS`** is true (via `iubenda.conf`, including `APP_CONFIG["iubenda"]`), the views render `*-compress.html` templates. Override those if you customize the compressed pipeline.
