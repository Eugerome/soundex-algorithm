## Soundex CLI implementation

CLI implementation of American Soundex

### Installation Instructions

Have docker installed. Build the image beforehand with:
```
docker-compose build
```

### Usage

Copy `.txt` you want processed into `soundex/input` folder. 

First, install all main dependencies (there are none, so optional)
```
docker-compose up


Then run the following command:
```
docker-compose run soundex python soundex/app.py
```

This should build the image (if you haven't already) and run the CLI script.

The script should prompt you with insctructions.

### Testing and debugging

For debugging run 

```
docker-compose -f docker-compose.debug.yml up -d
```

This should install additional dev dependencies and prevent the image from exiting upon completion.

To debug/run tests from within the container



