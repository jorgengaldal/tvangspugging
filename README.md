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

### Testing

To test the visual program, navigate to the tvangspugging directory and run `python run.py`


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
### Kategorier

#### Vil legge til

- Oversettelser av ord på toki pona
- Hovedsteder i land
- Hvilken kommune er dette (basert på bilde)?
- Doomsday algorithm: Ukedag basert på dato


TODO: Make requirements.txt-file