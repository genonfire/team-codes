# LNC Club Code Updater

This Python script reads a `.lnc` file containing football club information, extracts club names, maps them to 3-letter codes from a `codes.json` file, and appends updated club code entries to the file.

## Features

* Reads club names from a `.lnc` file.
* Supports both `CLUB_NAME_CHANGE` and `CLUB_SHORT_NAME_CHANGE` entries.
* Correctly handles club names with spaces.
* Looks up 3-letter club codes from `codes.json`.
* Appends new entries in the format:

  ```
  "CLUB_3LETTER_NAME_CHANGE"\t<club_number>\t<3-letter code>\t""
  ```
* Prints a summary of the number of clubs updated.

## Requirements

* Python 3.7 or higher

## Usage

1. Place your `.lnc` file and `codes.json` in the same directory as the script.
2. Run the script:

   ```bash
   python change.py [filename.lnc]
   ```

   If no filename is provided, `FM26 Club Names by FMScout.lnc` is used by default.

## Example

```bash
python change.py
Updated 406 clubs.
```

This will read `FM26 Club Names by FMScout.lnc`, update the club codes, and print how many clubs were updated.

### Output

- Updates the original `.lnc` file by adding club codes under `#Codes`
- Also creates a separate file `FM26 Club Codes.lnc` containing only the generated lines

## Source

* The 3-letter club codes were obtained from Reuters Sports Team Codes:
  [https://liaison.reuters.com/tools/sports-team-codes](https://liaison.reuters.com/tools/sports-team-codes)
* The FM26 LNC file was obtained from FMScout:
  [https://www.fmscout.com/a-fm26-real-names-license-fix.html](https://www.fmscout.com/a-fm26-real-names-license-fix.html)
