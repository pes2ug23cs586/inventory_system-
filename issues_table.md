# Issues Identified from Static Code Analysis

| Issue  | Tool | Type | Line(s)  | Description  | Fix Approach |
|--------|------|------|----------|--------------|----------------|
| Missing module & function docstrings | Pylint | Style | 1, 8, 14, 22, 25, 31, 36, 41, 48 | No docstrings explaining code purpose | Added short docstrings to each function and module |
| Function names not in `snake_case` | Pylint | Convention | Multiple | Naming not PEP 8-compliant | Renamed to `add_item`, `remove_item`, `get_qty`, etc. |
| Dangerous default argument `[]` | Pylint | Bug | 8 | Mutable list used as default parameter | Changed default to `None` and initialized inside function |
| Bare `except:` block | Bandit + Pylint | Security / Logic | 19 | Hides actual errors and suppresses debugging info | Replaced with `except Exception as e:` |
| `eval()` used | Bandit | Security | 59 | Executes arbitrary code (high risk) | Removed and replaced with safe alternative |
| `open()` without encoding / missing `with` | Pylint | Maintainability | 26, 32 | File handles not safely closed; encoding unspecified | Used `with open(..., encoding='utf-8'):` |
| Unused import `logging` | Pylint + Flake8 | Style | 2 | `logging` imported but never used | Used `logging` for messages instead of `print()` |
| Missing blank lines (E302/E305) | Flake8 | Formatting | Multiple | Functions not separated by 2 blank lines | Added proper blank lines between functions |


