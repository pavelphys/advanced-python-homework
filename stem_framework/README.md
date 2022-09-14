
## STEM framework installation
1. Deployment virtual enviroment, install packages from ```requirements.txt```:
```
cd ./stem_framework
pip install -r requirements.txt
```
2. Install stem packages in ```editable mode```:
```
pip install -e .
```
It find and run setup.py in ```editable mode```. It means than any changes to the original package would reflect directly in your environment.
