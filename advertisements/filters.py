from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, ChoiceFilter, ModelChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateTimeFromToRangeFilter()
    # фильтр по статусу объявления
    # status = filters.ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at']
