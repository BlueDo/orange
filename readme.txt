
# Venv
virtualenv --system-site-packages -p python ./venv
source "venv\Scripts\activate"
pip install -r requirements.txt

deactivate
