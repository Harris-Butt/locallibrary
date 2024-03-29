from django.contrib import admin

# Register your models here.
from .models import Author,Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('status','due_back','id', 'borrower','book')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
class BookInline(admin.TabularInline):
    model  = Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
#admin.site.register(Author,AuthorAdmin)
#admin.site.register(Book,BookAdmin)
admin.site.register(BookInstance,BookInstanceAdmin)
