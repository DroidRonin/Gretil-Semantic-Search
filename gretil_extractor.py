import os
import re
from bs4 import BeautifulSoup

input_folder = " "   # path of the input folder location which contains the data in htm format
output_folder = " "  # output path where the txt files are to be saved
os.makedirs(output_folder, exist_ok=True)

# regex to detect sanskrit IAST-encoded characters
sanskrit_re = re.compile(r"[āīūṛṝḷṅñṭḍṇśṣḥ]")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".htm"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".htm", ".txt"))

        with open(input_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")

        # retrieving the full-body text
        body = soup.find("body")
        text_lines = body.get_text(separator="\n", strip=True).splitlines()

        # the pages inside the gretil documents have a common pattern from where the main-body of the Sanskrit text starts. This identifies that block and starts extraction from there     
        main_text_started = False
        main_lines = []
        for line in text_lines:
            if not main_text_started:
                if "For further information see:" in line:
                    main_text_started = True
                continue
            # get only sanskrit lines
            if sanskrit_re.search(line) or re.match(r'^\d+\.', line.strip()):
                main_lines.append(line.strip())

        with open(output_path, "w", encoding="utf-8") as out:
            out.write("\n".join(main_lines))

        print(f"extracted data from {filename} -> {output_path}")
