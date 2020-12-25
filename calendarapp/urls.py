from django.urls import path

from calendarapp import views

app_name = 'calendarapp'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    path('delete/<int:event_id>', views.delete_event, name='delete_event'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
]