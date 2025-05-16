# tvangspugging

*__Note:__ The project is currently only made to work on Windows, but can probably be customized to work on other operating systems pretty easily.*

## Get started

Clone repository (with `git clone`).

Create and activate virutal environment:
```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependencies:
```cmd
pip install -r requirements.txt
```

Run installation file:
```cmd
python install.py
```

Add the created run.bat file as a task in Windows Task Scheduler on every unlock.
(TODO: Automate this process)

## Configuration
TODO

## Hvordan fungerer det?

Programmet velger ut en kategori ved å trekke en tilfeldig fil fra mappen questions. 

### Format

Spørsmålene spesifiseres gjennom JSON-formatet. Et eksempelspørsmål finnes under. Flere eksempler ligger i mappen [example questions](<./example questions/>).

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

### Current categories
- US States (based on map)
- Capitals of the world (based on name of country)
- Which weekday is this date? (Doomsday algorithm)

#### Want to add
- Oversettelser av ord på toki pona
- Hvilken kommune er dette (basert på bilde)?
