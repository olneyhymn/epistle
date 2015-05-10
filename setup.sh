set -e
conda create -n epistles python=3
source activate epistles
pip install -r requirements.txt
echo "use_env epistle" > .env
echo "export S3_ACCESS_KEY=''" >> .env
echo "export S3_SECRET_KEY=''" >> .env
echo
echo
echo "####################################"
echo "Don't forget to set AWS keys in .env"
echo "####################################"