
## STEM framework installation

0. Install Python 3.

1. Create virtual env.
```
python3 -m venv venv_name
```
2. Activate virtual env.
```
# Linux/macOS
source venv_name/bin/activate  
```
```
# Windows
venv_name\Scripts\activate.bat
```

3. Deployment virtual enviroment, install packages from ```requirements.txt``` (Install packages in the virtual env.):
```
cd ./stem_framework
pip install package-name
pip install -r requirements.txt
```

4. Install stem packages in ```editable mode```:
```
pip install -e .
```
It find and run setup.py in ```editable mode```. It means than any changes to the original package would reflect directly in your environment.
