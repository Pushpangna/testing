import json
import os


def update_config(file_data, version):
    if float(version) < 1.1:
        file_data["migrated"] = False
    else:
        file_data["migrated"] = True

    file_data["is_migratable"] = True
    return file_data


file = open("file.json", "r")
data = json.loads(file.read())
file.close()
ver = os.getenv("VERSION", "1.2")

if ver is None:
    raise Exception("No version is defined! Existing.")

updated_config = update_config(data, ver)
file = open("file.json", "w")
file.write(json.dumps(updated_config))
file.close()
