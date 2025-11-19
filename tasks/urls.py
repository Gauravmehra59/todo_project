from django.urls import path
from . import api_views, web_views
from .db import init_db

# Initialize DB at first import
init_db()

urlpatterns = [
    # Web
    path("", web_views.task_list),
    path("add/", web_views.add_task),
    path("detail/<int:id>/", web_views.detail_task),

    # APIs
    path("api/list/", api_views.api_list),
    path("api/create/", api_views.api_create),
    path("api/delete/<int:id>/", api_views.api_delete),
    path("api/detail/<int:id>/", api_views.api_detail),
    path("api/update/<int:id>/", api_views.api_update),
]
