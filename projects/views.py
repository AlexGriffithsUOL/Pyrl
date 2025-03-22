from django.shortcuts import render, redirect
from base.views import PageView
from base.models import PyrlClient
from .models import Project
from datetime import date
from .forms import ProjectForm
from customers.models import Customer

# Create your views here.

class ProjectDetailsView(PageView):
    template = 'main_app/projects/details.html'
    page_title = 'Project Details'

    def get(self, request):
        super().__init__(request=request,page_title=self.page_title)
        return render(request, self.template, self.context)

class ProjectCreateView(PageView):
    template = 'main_app/projects/create.html'
    page_title = 'Create Project'

    def get(self, request):
        super().__init__(request=request,page_title=self.page_title)
        project_creation_form = ProjectForm()
        self.add_to_context(project_creation_form=project_creation_form)
        return render(request, self.template, self.context)
    
    def post(self, request):
        print(request.POST['project_name'])
        project_name = request.POST['project_name']
        customer_id = request.POST['customer_id']
        customer = Customer.objects.get(customer_id=customer_id)
        user_id = request.user.id
        client = PyrlClient.objects.get(client_id=request.user.client_id)
        print(customer)
        print(request.POST['customer_id'])
        Project(project_name=project_name, customer_id=customer, client_id=client).save()
        print('saved!')
        return redirect('main_app:customers:list')