# 🔍 File Type Identifier

Identify file types via **magic bytes**, **file extensions**, and **MIME type** fallback — with zero third-party dependencies.

[![CI](https://github.com/yourusername/file-type-identifier/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/file-type-identifier/actions)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

- **Magic byte detection** — reads binary signatures from file headers (PNG, JPEG, PDF, ELF, ZIP, and 30+ more)
- **Extension fallback** — covers 60+ file extensions including source code, config, and data files
- **MIME type fallback** — uses Python's built-in `mimetypes` module as a last resort
- **Color-coded CLI output** — beautifully categorized terminal output
- **Directory scanner** — scan entire folders with optional recursion and summary stats
- **JSON output** — pipe-friendly `--json` flag for scripting and automation
- **Zero dependencies** — runs on pure Python 3.9+ stdlib

---

## 📦 Installation

### From source (recommended)

```bash
git clone https://github.com/yourusername/file-type-identifier.git
cd file-type-identifier
pip install -e .
```

### Or run directly (no install)

```bash
python src/cli.py identify myfile.pdf
```

---

## 🚀 Usage

### CLI

#### Identify one or more files

```bash
filetype identify photo.jpg document.pdf archive.tar.gz
```

```
  TYPE        CATEGORY              FILE
  ──────────  ────────────────────  ────────────────────────────────────────
  JPEG        [image]               photo.jpg          4.2 MB
  PDF         [document]            document.pdf       1.1 MB
  GZIP        [archive]             archive.tar.gz     823.0 KB

  3 file(s) identified.
```

#### Verbose mode (show detection method + MIME)

```bash
filetype identify --verbose report.pdf
```

```
  PDF         [document]            report.pdf         512.0 KB
           Description : PDF Document
           Method      : magic
           MIME        : application/pdf
           Extension   : .pdf
```

#### JSON output

```bash
filetype identify --json photo.jpg
```

```json
[
  {
    "file_name": "photo.jpg",
    "file_size": 4412931,
    "type_name": "JPEG",
    "category": "image",
    "description": "JPEG Image",
    "method": "magic",
    "mime_type": "image/jpeg",
    "extension": ".jpg",
    "color": "#6EE7B7"
  }
]
```

#### Scan a directory

```bash
filetype scan ./my-project
filetype scan ./my-project --recursive
filetype scan ./my-project --recursive --json
```

```
  Scan: ./my-project  (42 files)

  By Category:
    code          ████████████████████████████ 28
    config        ████ 4
    text          ███ 3
    data          ██ 2
    image         █ 1
    archive       █ 1

  Top File Types:
    Python        18
    JavaScript    6
    YAML          3
    Markdown      2
    ...
```

---

## 🐍 Python API

```python
from src.identifier import identify_file, identify_files

# Single file
result = identify_file("photo.jpg")
print(result.type_name)    # "JPEG"
print(result.category)     # "image"
print(result.description)  # "JPEG Image"
print(result.method)       # "magic" | "extension" | "mime" | "unknown"
print(result.file_size)    # 4412931
print(result.to_dict())    # serializable dict

# Multiple files
results = identify_files(["a.png", "b.pdf", "c.py"])
for r in results:
    print(f"{r.file_name}: {r.type_name} ({r.category})")
```

---

## 🗂️ Supported Types

### Magic Byte Detection (header signatures)
| Format   | Category  |
|----------|-----------|
| JPEG, PNG, GIF, BMP, TIFF, WEBP, ICO | image |
| PDF, RTF, OLE (doc/xls/ppt) | document |
| ZIP / Office Open XML | archive |
| MP3, FLAC, OGG, WAV | audio |
| MP4, MKV, FLV | video |
| EXE/DLL, ELF, Mach-O | binary |
| GZIP, BZIP2, XZ, 7ZIP, RAR, TAR | archive |
| TTF, OTF, WOFF, WOFF2 | font |
| SQLite | database |

### Extension Fallback (60+ types)
Python, JavaScript, TypeScript, Go, Rust, Ruby, PHP, Java, Kotlin, Swift, C/C++, C#, Shell scripts, JSON, YAML, TOML, XML, Markdown, CSV, SQL, SVG, APK, IPA, DEB, RPM, and more.

---

## 🧪 Running Tests

```bash
pip install -r requirements-dev.txt
pytest tests/ -v --cov=src
```

---

## 📁 Project Structure

```
file-type-identifier/
├── src/
│   ├── identifier.py      # Core detection logic
│   └── cli.py             # CLI interface
├── tests/
│   └── test_identifier.py # Unit tests
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI
├── setup.py
├── requirements.txt
├── requirements-dev.txt
├── LICENSE
└── README.md
```

---

## 🤝 Contributing

1. Fork the repo and create a feature branch
2. Add your changes (new magic signatures go in `MAGIC_SIGNATURES`, extensions in `EXTENSION_MAP`)
3. Add/update tests in `tests/test_identifier.py`
4. Open a pull request

---

## 📄 License

MIT — see [LICENSE](LICENSE).
