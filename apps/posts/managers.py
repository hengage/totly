from django.db import models
from django.db.models import Q

class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query=='':
            return self.none()
        lookups = (
            Q(title__icontains=query) 
            |Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)
            | (Q(author__first_name__icontains=query) & Q(author__last_name__icontains=query))
        ) 

        # When there is a whitespace in the search query, split the query from the whitepace
        # and search using either of the terms
        for term in query.split():
            lookups |= Q(author__first_name__icontains=term) | Q(author__last_name__icontains=term)
        return self.filter(lookups)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)