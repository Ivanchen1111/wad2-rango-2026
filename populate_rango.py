import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'https://docs.python.org/3/tutorial/',
         'views': 50},
        {'title': 'Python Package Index',
         'url': 'https://pypi.org/',
         'views': 40},
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/stable/intro/tutorial01/',
         'views': 60},
        {'title': 'Django Documentation',
         'url': 'https://docs.djangoproject.com/',
         'views': 55},
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
    }

    for cat_name, cat_data in cats.items():
        category = add_cat(cat_name, cat_data['views'], cat_data['likes'])
        for page in cat_data['pages']:
            add_page(category, page['title'], page['url'], page['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c.name} -> {p.title}')


def add_cat(name, views=0, likes=0):
    category, created = Category.objects.get_or_create(name=name)
    category.views = views
    category.likes = likes
    category.save()
    return category


def add_page(category, title, url, views=0):
    page, created = Page.objects.get_or_create(
        category=category,
        title=title
    )
    page.url = url
    page.views = views
    page.save()
    return page


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
