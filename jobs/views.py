from django.shortcuts import render
from django.views import View
from base.views import page_view
from utils.views import message_manager

# Create your views here.
class calendar(page_view):
    page_title = "Calendar"
    page_description = "Calendar view"
    page_keywords = "Calendar"
    template = "main_app/calendar/base.html"

    def get(self, request):
        super().__init__(request=request, page_title=self.page_title)
        message_manager.attach_message(request, message_manager.STATUS.INFO, 'Our page has been updated! Scroll down to see more!', length_of_time=3)
        return render(request, self.template, self.context)