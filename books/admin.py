from django.contrib import admin
from books.models import Book
from publication.models import Publication


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'authors_list',
        'genres_list',
        'synopsis',
        'isbn',

    )

    list_filter=(
        'title',
        'author',
        'genres',

    )

    list_display_links = ('id', 'title')
    readonly_fields = ('publication_details',)

    def genres_list(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    genres_list.short_description='Genres'

    def authors_list(self, obj):
        return ", ".join([author.name for author in obj.author.all()])

    authors_list.short_description='Authors'

    def publication_details(self, obj):
        try:
            publication = Publication.objects.get(book=obj)
            return (f"Release Date: {publication.release_date};"
                    f"\nEdition: {publication.edition};"
                    f"\nStatus: {publication.status};"
                    f"\nQuantity: {publication.quantity}"
                    f"\nAssembly:{publication.assembly}")
        except Publication.DoesNotExist:
            return "No publication details available"
        except Exception as e:
            return f"Error fetching publication details: {str(e)}"
    publication_details.short_description = 'Publication Details'
