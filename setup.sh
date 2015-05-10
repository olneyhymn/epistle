virtualenv -p python3 ~/.virtualenvs/epistle
pip install -r requirements.txt
echo "use_env epistle" > .env
echo "export S3_ACCESS_KEY=''" > .env
echo "export S3_SECRET_KEY=''" > .env
echo "Don't forget to set AWS keys in .env"