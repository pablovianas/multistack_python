# Multistack Python

### Installing 


#### Cloning 
`git clone https://github.com/pablovianas/multistack_python`

#### Dependencies 
` pip install -r requirements.txt`

#### Modify database settings of file `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': 'porta_bd',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'
    }
}

```

#### Migrate database
`python manage.py migrate`

#### Start server

`python manage.py runserver`