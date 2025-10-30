import sys
import json
import shlex

DEFAULT_FILENAME = "FM26 Club Names by FMScout.lnc"
CODES_JSON = "codes.json"

filename = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILENAME

with open(filename, "r") as f:
    content = f.readlines()

with open(CODES_JSON, "r") as f:
    codes = json.load(f)

club_entries = []
for line in content:
    parts = shlex.split(line)
    if len(parts) >= 3:
        key = parts[0]
        if key in ('CLUB_NAME_CHANGE', 'CLUB_SHORT_NAME_CHANGE'):
            club_name = parts[2]
            club_number = parts[1]
            code = codes.get(club_name)
            if code is not None:
                entry = (
                    '"CLUB_6LETTER_NAME_CHANGE"'
                    f'\t{club_number}\t{code}\t""'
                )
                club_entries.append(entry)

codes_index = None
for i, line in enumerate(content):
    if line.strip() == '#Codes':
        codes_index = i
        break

if codes_index is not None:
    content = content[:codes_index]

content.append('\n#Codes\n')
content.extend(entry + '\n' for entry in club_entries)

with open(filename, "w") as f:
    f.writelines(content)

print(f"Updated {len(club_entries)} clubs.")
