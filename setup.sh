conda create -n epistles python3
source activate epistles
pip install -r requirements.txt
echo "use_env epistle" > .env
echo "export S3_ACCESS_KEY=''" >> .env
echo "export S3_SECRET_KEY=''" >> .env
echo "\n####################################"
echo "Don't forget to set AWS keys in .env"
echo "\n####################################"