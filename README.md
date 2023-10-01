# tvangspugging

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
