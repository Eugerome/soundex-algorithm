## Soundex CLI implementation

CLI implementation of American Soundex

### Installation Instructions

Have docker installed. Build the image beforehand with:
```
docker-compose build
```

### Usage

Copy `.txt` you want processed into `soundex/input` folder. 

Then run the following command:
```
docker-compose run soundex python soundex/app.py
```

The script should prompt you with insctructions.

### Testing and debugging

For debugging run 

```
docker-compose -f docker-compose.debug.yml up -d
```

This should install additional dev dependencies and prevent the image from exiting upon completion.

To debug/run tests from within the container



