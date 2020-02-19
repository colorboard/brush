# Brush

Software environment for executing and configuring packages.

## Structure

In root of the project it has two submodules.

- `core` – basic classes and functions implementations
- `packages` – directory that contains packages itself

## Package

Well, package is a ZIP archive, that contains `__init__.py` file and the `manifest.json` file. Also package can contain required libraries or code can be splitted in the files. Initialization file needs to contain two methods:

### Initialization file

That file needs to be named `__init__.py`. In that file you can call other libraries that can required.

- `setup` - method that will be called at the start of application
- `loop` - that method will be called at every frame

### Manifest

That files contains package information in the JSON format. It has primary keys:

- `title` : `string` - title of the package that will be displayed in menu
- `description` : `string` - short description of the package
- `identifier` : `string` – identifier of the package
- `developer` : `dict` - developer information
- `version` : `string` - version of the package
- `icon` : `string` - image 16x16 that encoded in `base64`

Example of manifest file:

```json
{
  "title": "Example",
  "description": "This is example",
  "identifier": "com_example_example",
  "developer": {
    "name": "Example",
    "id": 1,
    "email": "example@example.com",
    "website": "https://example.com"
  },
  "version": "1.0.0",
  "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAW0lEQVQ4jWNkYGD4z0ABYKJEMwiwwBj//xPnEEZGRuwGgEDYjJd4Na/KEMcQI9kLaWlpYEy2AbdZzChzAToYNQAtHWCLZ3Sg+ucUigjFLoBnJnKT8gDnRgYGBgD8yhKu0Tq+5gAAAABJRU5ErkJggg=="
}
```
