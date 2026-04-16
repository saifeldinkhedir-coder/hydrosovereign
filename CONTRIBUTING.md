# Contributing to HydroSovereign

Thank you for your interest in contributing to HSAE!

## Ways to Contribute

- **Bug reports** — open an issue with a minimal reproducible example
- **New basins** — add entries to `hydrosovereign/basins.py`
- **New indices** — add to `hydrosovereign/indices.py` with unit tests
- **Documentation** — improve examples, docstrings, or the README

## Development Setup

```bash
git clone https://github.com/saifeldinkhedir-coder/hydrosovereign
cd hydrosovereign
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
pip install pytest pytest-cov
pytest tests/ -v
```

## Code Style

- Follow PEP 8
- Add docstrings to all public functions (NumPy style)
- Add a unit test for every new function in `tests/`

## Submitting a Pull Request

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes with a clear message
4. Push and open a Pull Request against `main`

## Scientific Contributions

If you use HSAE in research and find issues with ATDI/HIFD calibration
or wish to add validated basin data, please open an issue with your
data source and methodology.

## Questions

Open an issue or contact:
**Seifeldin M.G. Alkedir** · saifeldinkhedir@gmail.com · ORCID: 0000-0003-0821-2991
