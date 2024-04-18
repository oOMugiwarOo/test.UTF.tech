from rest_framework.routers import DefaultRouter

from .views import (
    FoodListView,
)

router = DefaultRouter()
router.register("v1/foods", FoodListView, basename="food_lists")

urlpatterns = router.urls
