import glob
import json
import os
import shutil

if os.path.isdir("BACAP"):
    shutil.rmtree("BACAP")
shutil.copytree("before_translate","BACAP")

dirs = glob.glob("BACAP/data/*")
with open("ja_jp.json") as f:
    lang_data = json.load(f)
for i in dirs:
    if not os.path.isdir(i + "/advancements"):
        continue

    advancement_dir = glob.glob(i + "/advancements/*")
    for j in advancement_dir:
        for k in glob.glob(j + "/*"):
            print(k)
            with open(k) as f:
                d = json.load(f)
                try:
                    title = d["display"]["title"]["translate"]
                    if title in lang_data:
                        d["display"]["title"]["translate"] = lang_data[title]
                    else:
                        lang_data[title] = title
                    desc = d["display"]["description"]["translate"]
                    if desc in lang_data:
                        d["display"]["description"]["translate"] = lang_data[desc]
                    else:
                        lang_data[desc] = desc
                except KeyError:
                    pass
            with open(k, "w") as f:
                json.dump(d, f, indent=4, ensure_ascii=False)

    with open("ja_jp.json", "w") as f:
        json.dump(lang_data, f, indent=4, ensure_ascii=False)
