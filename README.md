# codename

**codename** is a simple CLI tool that generates random codenames using your system dictionary files.

Each codename is made by combining random words, like `silent-harbor` or `lucky-wolf`.

## Installation

### From PyPI (recommended)

```bash
pip install codename-cli
```

### From source

```bash
# Clone the repository
git clone https://github.com/hernamesbarbara/codename.git
cd codename

# Install in development mode
pip install --editable .
```

## Usage

Generate a codename with default settings (2 words joined by hyphen):
```bash
codename
# Example output: silent-harbor
```

Generate a codename with custom number of words:
```bash
codename -n 3
# Example output: silent-harbor-wolf
```

Generate a codename with custom delimiter:
```bash
codename -d _
# Example output: silent_harbor
```

Available delimiters: `-`, `,`, `_`, `|`, `;`, `:`

## Requirements

- Python 3.6+
- System dictionary file (typically at `/usr/share/dict/words`)

## License

MIT License - see [LICENSE](LICENSE) for details.
