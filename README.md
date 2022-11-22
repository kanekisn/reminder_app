### Reminder App works only for Linux, MacOS  

### 1. Update system and install cron --->

```
sudo apt update
sudo apt-get install cron -y
```

###  2. Install of all requirements --->

`pip install -r requirements.txt`

###  3. Open config/.env/ and then specify parameters for mailing --->

```
EXAMPLE:

EMAIL_HOST=smtp-mail.outlook.com # SMPT Server
EMAIL_HOST_USER=YOUR_EMAIL@outlook.com # Your Email
EMAIL_HOST_PASSWORD=PASSWORD # Should use 'APP Password'
EMAIL_PORT=587 # SMPT Port for most services is 587
```

### 4. Generate django secret key by console command --->

`python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

### 5. Open config/config/settings.py then past your generated secret key --->
```
EXAMPLE:

SECRET_KEY = YOUR_SECRET_KEY
```

### 6. Working with migrations --->
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### 7. Start cron --->

`sudo service cron start`

### 8. Add all cron jobs --->

`python3 manage.py crontab add`

### 9. Run django app --->

`python3 manage.py runserver`

- P.S Cron jobs work each 2 min so it takes a time to get the reminder for your mail (wait 2 min or less)
