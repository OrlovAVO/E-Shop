from django.contrib.postgres.search import SearchVector

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 6:
        return Products.objects.filter(id=int(query))

    return Products.objects.annotate(search=SearchVector('name', 'description')).filter(search=query)

