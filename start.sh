if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Aradhyaph/renamerbot       
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /renamerbot
fi
cd /RENAMER_BOT-5
pip3 install -U -r requirements.txt
echo "🔥🔥🔥BOT IS STARTING🔥🔥🔥"
python3 bot.py
