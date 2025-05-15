# tvangspugging

## Get started

- Clone repository with `git clone`
- run `python installToStartup.py`

TODO: Update "installation guide" and make new installation script.
Has been added as a task in Windows Task Scheduler.

### Activating virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### Cannot import bottle.ext.websocket

Følg workaround her: https://stackoverflow.com/questions/77232001/python-eel-module-unable-to-use-import-bottle-ext-websocket-as-wbs-modulenotfoun

### Testing

To test the visual program, navigate to the tvangspugging directory and run `python run.py`


## Hvordan fungerer det?

Programmet velger ut en kategori ved å trekke en tilfeldig fil fra mappen questions. 

### Format

```json
{
  "type": "image",
  "question": "Hvem regisserte filmen Interstellar?",
  "resources": [
    {
      "type": "image",
      "path": "./media/interstellar.jpg"
    }
  ],
  "acceptedAnswers": ["Christopher Nolan", "Nolan"],
  "caseSensitive": false
}
```
### Kategorier

#### Vil legge til

- Oversettelser av ord på toki pona
- Hovedsteder i land
- Hvilken kommune er dette (basert på bilde)?
- Doomsday algorithm: Ukedag basert på dato


TODO: Make requirements.txt-file