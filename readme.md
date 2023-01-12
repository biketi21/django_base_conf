
# Tweaked allauth Templates.

This is a personal project made to save me the hustle of setting up authentication everytime I start a new Django Project.

I use django-allauth, and as you know its templates are unstyled. (not visually appealing.)  
I make use of MDBootstrap to style the basic authentication templates from the MDB directory in the static folder.  
I added a navbar for ease of use, acknowledging how uncormfortable styling is to backend developers.

I make use of a custom user model with both the firstname and email field, using the email field as the username field. This is in the 'accounts' app.

### Installation

Clone this repository to your local environment:

```bash
git clone https://github.com/biketi21/django_base_conf.git
```

then install dependencies like so:

```bash
pip3 install -r requirements.txt
```

spin up a demo:

```bash
python3 manage.py runserver
```

and make the necessary tweaks that suit your needs.


### Contributing

You are welome to make a pull request and contribute.

### Licence

MIT
