from django.urls import path
from .views import affirmation, get_random_affirmation
from favorites.views import add_to_favorites

urlpatterns = [
    # URL pattern for random affirmation without category
    path('affirmation/', affirmation, name='affirmation'),
    # URL pattern for affirmation with category
    path('affirmation/<slug:category_slug>/', affirmation, name='affirmation_by_category'),
    path('get_random_affirmation/', get_random_affirmation, name='get_random_affirmation'),
    # add to favorites
    path('favorite/<int:affirmation_id>/', add_to_favorites, name='favorite'),
]