from django.shortcuts import render
from django.views import View
from website.models import Food

class index(View):

    def get(self, request):
        return render(request, 'index.html', {})
    
    def post(self, request):
        return render(request, 'index.html', {'breakfest': str(Food.generate_combo("Breakfest")),'lunch':str(Food.generate_combo("Lunch")), 'dinner':str(Food.generate_combo("Dinner"))})