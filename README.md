## Soundex CLI implementation

CLI implementation of American Soundex

### Installation Instructions

Have docker installed. Build the image beforehand if you want with:
```
docker-compose build
```

### Usage

Copy `.txt` you want processed into `soundex/input` folder

Then process them using:
```
docker-compose up
```

This should build the image (if you haven't already) and run the CLI script.

The script should prompt you with insctructions.

### Testing and debugging

For debugging run 

```
docker-compose -f docker-compose.debug.yml up
```

This should install additional dev dependencies and prevent the image from exiting upon completion.



