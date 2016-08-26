# sosh-availability
The script monitor a list of mobile phones and send a notification when one of them is available

# Installation:
```
  git clone https://github.com/Thomas-Negrault/sosh-availability.git
  cd sosh-availability
  sudo pip install -r requirements.txt
  mv config.example.ini config.ini
  [your text editor (vi,vim,nano..)] config.ini
```
- Go to the sosh website, find the phone you want to monitor and grab the end of the URL:
- For https://shop.sosh.fr/mobile/apple-iphone6s-64Go-argent put *apple-iphone6s-64Go-argent* in the array
- Set the interval (in seconds)
- Put your phpbullet token (go to https://www.pushbullet.com/#settings/account and click on "Create Access Token")

Then run the script:

```
  python run.py
```
