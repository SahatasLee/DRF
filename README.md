# Django Rest Framework

## Install tools
install env
`python3 -m venv drf`
activate
`Source <env>/bin/activate # สำหรับ mac หรือ linux`
`.\<env>\Scripts\activate #สำหรับฝั่ง windows`
install requirements
`python install -r requirements.txt`
or run container docker
`docker-compose up`

run web
1. `python manage.py migrate`
2. `python manage.py createsuperuser`
3. `python manage.py runserver`