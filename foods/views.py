from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import (
    Food,
)
from .serializers import (
    FoodSerializer,
)


class FoodListView(ViewSet):
    def list(self, request):
        published_foods = Food.objects.filter(is_publish=True)

        categories = {}
        for food in published_foods:
            if food.category not in categories:
                categories[food.category] = []
            categories[food.category].append(food)

        categories_with_published_foods = {
            category: foods for category, foods in categories.items() if foods
        }

        serialized_data = {}
        for category, foods in categories_with_published_foods.items():
            serialized_data[category.id] = {
                "id": category.id,
                "name_ru": category.name_ru,
                "name_en": category.name_en,
                "name_ch": category.name_ch,
                "order_id": category.order_id,
                "foods": FoodSerializer(foods, many=True).data,
            }

        return Response(list(serialized_data.values()))
