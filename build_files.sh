
echo "BUILD START"
pip install -r requirements.txt
pip manage.py collectstatic --noinput
echo "BUILD END"