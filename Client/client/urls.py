from django.urls import path
from Client.client.views import home, analytics, balance, add_book, book_shelf, book_detail, edit_book, authors_list, \
    books_by_genre, author_detail, supplier_analytics, suppliers_list, supplier_detail, add_supplier, buyer_analytics, \
    buyers_list, buyer_detail, add_buyer, create_sale, sales_list, coming_soon, author_edit, sale_edit, sale_detail, \
    add_author, add_genre, add_assembly, add_publication

urlpatterns=[
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('analytics/', analytics, name='analytics'),
    path('balance/', balance, name='balance'),
    path('add-book/', add_book, name='add_book'),
    path('add-author/', add_author, name='add_author'),
    path('add-genre/', add_genre, name='add_genre'),
    path('add-assembly/', add_assembly, name='add_assembly'),
    path('add-publication/', add_publication, name='add_publication'),
    path('shelf/', book_shelf, name='book_shelf'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('authors/', authors_list, name='authors-list'),
    path('authors/<int:author_id>', author_detail, name='authors-detail'),
    path('authors/<int:pk>/edit/', author_edit, name='author-edit'),
    path('books/by-genre/', books_by_genre, name='books_by_genre'),
    path('supplier/analytics/', supplier_analytics, name='supplier-analytics'),
    path('suppliers/', suppliers_list, name='suppliers-list'),
    path('supplier/<int:supplier_id>/', supplier_detail, name='supplier_detail'),
    path('supplier/add/', add_supplier, name='add_supplier'),
    path('buyer/analytics/', buyer_analytics, name='buyer-analytics'),
    path('buyers/', buyers_list, name='buyers-list'),
    path('buyer/<int:buyer_id>/', buyer_detail, name='buyer_detail'),
    path('buyer/add/', add_buyer, name='add_buyer'),
    path('sales/', sales_list, name='sales_list'),
    path('sales/new/', create_sale, name='new_sale' ),
    path('sales/<int:pk>/', sale_detail, name='sale-detail'),
    path('sales/<int:pk>/edit/', sale_edit, name='sale-edit'),

    path('coming-soon/', coming_soon, name='#'),


]