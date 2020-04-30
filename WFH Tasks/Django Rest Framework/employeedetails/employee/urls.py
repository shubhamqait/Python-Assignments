from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

from employee.views import EmployeeViewSet, UserViewSet, api_root
from rest_framework import renderers

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
# employee_list = EmployeeViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# employee_detail = EmployeeViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# employee_highlight = EmployeeViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('employee/', employee_list, name='employee-list'),
#     path('employee/<int:pk>/', employee_detail, name='employee-detail'),
#     path('employee/<int:pk>/highlight/', employee_highlight, name='employee-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

# urlpatterns = [
#     path('', views.api_root),
#     path('employee/', views.EmployeeList.as_view()),
#     path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
#     path('employee/<int:pk>/highlight/', views.EmployeeHighlight.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# API endpoints
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('employee/',
#         views.EmployeeList.as_view(),
#         name='employee-list'),
#     path('employee/<int:pk>/',
#         views.EmployeeDetail.as_view(),
#         name='employee-detail'),
#     path('employee/<int:pk>/highlight/',
#         views.EmployeeHighlight.as_view(),
#         name='employee-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])