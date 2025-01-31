# PyMetaFile
pyfilemeta é uma biblioteca Python leve para extração de metadados de arquivos, incluindo tamanho, datas de criação e modificação, tipo MIME e hashes (MD5, SHA256). Ideal para verificação de integridade e organização de arquivos. 🚀

## Bulld local

### Execute tests
```bash
pip install pytest
pytest
```

### Install tools
```bash
pip install build twine
```

### Build the package
```bash
python -m build
```

### Test install on PyPI
```bash
twine upload --repository testpypi dist/*
```
(Go to: https://test.pypi.org to test the installation)


## How to use this package
```bash
pip install PyMetaFile
``` 