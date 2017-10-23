from rest_framework import generics

from catalog.models import Author
from api.catalog.serializers import AuthorSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        """
        List all the authors.
        ---
        tags:
            - Author
        operationId: listAuthors
        """
        return super(AuthorList, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create an Author instance.
        ---
        tags:
            - Author
        operationId: createAuthor
        """
        return super(AuthorList, self).create(request, *args, **kwargs)


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve an Author instance.
        ---
        tags:
            - Author
        operationId: getAuthor
        """
        return super(AuthorDetail, self).retrieve(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update an Author instance.
        ---
        tags:
            - Author
        operationId: updateAuthor
        """
        return super(AuthorDetail, self).update(request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Patch an Author instance.
        ---
        tags:
            - Author
        operationId: patchAuthor
        """
        return super(AuthorDetail, self).partial_update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an Author instance.
        ---
        tags:
            - Author
        operationId: deleteAuthor
        """
        return super(AuthorDetail, self).destroy(request, args, kwargs)
