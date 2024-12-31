from app.models.meals_models import DailyUserDishes


def get_daily_user_dishes(request):
    try:
        kwargs = {}
        user = request.get('user', None)
        print(type(user))
        dish_name = request.get('dish_name', None)
        dish_type = request.get('dish_type', None)
        offset = request.get('offset',0)
        limit = request.get('limit',10)

        if user:
            kwargs['user'] = user
        if dish_name:
            kwargs['dish_name'] = dish_name
        if dish_type:
            kwargs['dish_type'] = dish_type
        kwargs['is_active'] = True
        records = DailyUserDishes.objects.filter(**kwargs)[offset:offset+limit]
        count = DailyUserDishes.objects.filter(**kwargs).count()
        return records, count
    except Exception as ex:
        return False