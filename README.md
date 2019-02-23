# MangAdventure [![release](https://img.shields.io/github/release/mangadventure/MangAdventure/all.svg)](https://github.com/mangadventure/MangAdventure/releases)

MangAdventure, aka MangADV, is a simple manga hosting CMS.

It is fully written in Django, SCSS and Vanilla JS.
No PHP, no Node.js, no Bootstrap, no jQuery.

## Features

* Open source.
* Includes JSON API.
* Simple and configurable.
* Upload chapters as zip files.
* Search for series.
* More features coming.

## Documentation

The documentation is available on [Read the Docs](https://mangadventure.rtfd.io).

## Configuration

You can configure the site via the admin panel
If you want to overwrite the styling of the site,
you can write some SCSS (or regular CSS) in the
`static/extra/styles.scss` file.

## Development

To debug the server set the environment variable `MANGADV_DEBUG`
to `true`. **Don't do this in production.**

You shouldn't use the production server during development.
You can use Django's `runserver` command to run a development
server on `127.0.0.1:8000` (or any other address you specify).

## Credits

* Inspired by [FoOlSlide 2](https://github.com/chocolatkey/FoOlSlide2)
* Search results are sorted using [tristen/tablesort](https://github.com/tristen/tablesort)
* Info pages use the [TinyMCE editor](https://www.tiny.cloud/)
* Browser logos from [alrra/browser-logos](https://github.com/alrra/browser-logos)

## License

[MIT](LICENSE)


