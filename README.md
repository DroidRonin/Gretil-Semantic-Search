# Sanskrit Text Extractor for GRETIL HTML Files

This script parses `.htm` files from the GRETIL repository and extracts only the main Sanskrit body text.  
It skips the metadata block (editorial notes, copyright info, encoding tables) and outputs clean `.txt` files, one per source file.

---

## Features

- **Skips front matter:** ignores everything before the line  
  `For further information see: http://gretil.sub.uni-goettingen.de/gretil.htm`  
- **HTML parsing with BeautifulSoup:** strips all tags and keeps plain text  
- **IAST Sanskrit filtering:** automatically removes most English-only lines  
- **Per-file output:** saves each `.htm` as a `.txt` with the same base filename

---

## Requirements

Install the required Python libraries:
```bash
pip install beautifulsoup4 lxml
