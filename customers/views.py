from django.shortcuts import render, redirect
from base.views import PageView
from .models import Customer, EntityTypes, CustomerContact, CustomerGroup, CustomerGroupCustomerLink
from .forms import CustomerForm, CustomerContactForm
from projects.models import Project
from banking.models import BankAccount, BankInstitution
from base.helpers import build_base_url
# Create your views here.

def get_active_customers_without_group(client_id):
    customers_without_group = Customer.objects.filter(client_id=client_id, deleted=False).exclude(
        customer_id__in=CustomerGroupCustomerLink.objects.values_list("customer_id", flat=True)
    )
    
    customers = {}
    
    for customer in customers_without_group:
        customers[customer.display_name] = customer
    
    return customers

def get_customer_groups_with_customers(client_id):
    groups = CustomerGroup.objects.filter(client_id=client_id).prefetch_related("customergroupcustomerlink_set__customer")

    group_dict = {
        group.name: [link.customer for link in group.customergroupcustomerlink_set.all()]
        for group in groups
    }

    return group_dict


class CustomerListView(PageView):
    template = 'main_app/customers/list.html'
    page_title = 'Customers'

    def get(self, request):
        super().__init__(request=request,page_title=self.page_title)
        
        customer_filters = dict()
        customer_filters['client'] = request.user.client
        
        if not request.user.is_client_admin:
            customer_filters['deleted'] = False


        
        customers = get_active_customers_without_group(request.user.client_id)
        customer_groups = get_customer_groups_with_customers(request.user.client_id)
        customer_list = {**customers, **customer_groups}

        self.add_to_context(customer_list = customer_list)
        return render(request, self.template, self.context)

class CustomerDetailsView(PageView):
    template = 'main_app/customers/details.html'
    page_title = 'Customer Details'

    def get(self, request, customer_id):
        super().__init__(request=request,page_title=self.page_title)
        customer = Customer.objects.get(customer_id=customer_id)
        
        projects = Project.objects.filter(customer_id=customer_id)
        
        if len(projects) == 1:
            projects = [projects]
            
        try:
            customer_bank_accounts = BankAccount.objects.filter(customer_id=customer_id)
            self.add_to_context(customer_bank_accounts=customer_bank_accounts)
        except:
            pass
        
        contacts = CustomerContact.objects.filter(customer_id=customer_id, deleted=False)
        
        self.add_to_context(customer=customer, projects=projects, customer_id=customer_id, contacts=contacts)
        return render(request, self.template, self.context)
    
class CustomerAddEditContact(PageView):
    template = 'main_app/customers/contacts/add_edit_contact.html'
    page_title = 'Contact'
    
    def get(self, request, customer_id, contact_id=None):
        
        if contact_id is not None:
            self.page_title = 'Edit Contact'
            self.page_header = 'Edit Contact'
            contact = CustomerContact.objects.get(customer_contact_id=contact_id)
            self.contact_name = f'{contact.forename} {contact.surname}'
            self.mode = 'edit'
            contact_form = CustomerContactForm(instance=contact)
        else:
            self.page_title = 'Add Contact'
            self.page_header = 'Add Contact'
            self.contact_name = 'New Contact'
            self.mode='add'
            contact_form = CustomerContactForm()
            
        self.add_to_context(
            contact_form=contact_form, 
            page_title=self.page_title, 
            page_header=self.page_header, 
            contact_name=self.contact_name, 
            mode=self.mode, 
            customer_id=customer_id
            )
        return render(request, self.template, self.context)
    
    def post(self, request, customer_id, contact_id=None):
        
        contact_data = request.POST.dict()
        
        if 'csrfmiddlewaretoken' in contact_data:
            del contact_data['csrfmiddlewaretoken']
        
        contact_data['customer'] = Customer.objects.get(customer_id=customer_id)
        
        if contact_id is not None:
            contact_data['customer_contact_id'] = contact_id
        
        if 'submit' in contact_data:
            del contact_data['submit']
            contact = CustomerContact(**contact_data)
            contact.save()
            
            if contact_id is None:
                base_url = build_base_url(request.user.client.client_id)
                url = f'http://{base_url}/app/customers/activate/{contact.customer_contact_uuid}/'
                
                send_email([contact_data['email_address']], 'Welcome to Pyrl!', f'Hi {contact.forename} {contact.surname}, welcome to Pyrl, to activate your account please click the link below, {url}')
            
            return redirect('main_app:customers:edit-contact', customer_id=customer_id, contact_id=contact.customer_contact_id)
        elif 'delete' in contact_data:
            del contact_data['delete']
            contact = CustomerContact(**contact_data)
            contact.delete()
            return redirect('main_app:customers:details', customer_id=customer_id)
        else:
            raise Exception('wtf is goin on boyo')

class CustomerCreateView(PageView):
    template = 'main_app/customers/create.html'
    page_title = 'Create Customer'

    def get(self, request):
        super().__init__(request=request,page_title=self.page_title)
        customer_form = CustomerForm()
        self.add_to_context(customer_form=customer_form)
        return render(request, self.template, self.context)
    
    def post(self, request):
        display_name = request.POST['display_name']
        legal_entity = EntityTypes.objects.get(entity_id=request.POST['legal_entity'])
        Customer(display_name=display_name, legal_entity=legal_entity, client=request.user.client).save()
        return redirect('main_app:customers:list')

class CustomerGroupListView(PageView):
    template = 'main_app/customers/customer_groups/list.html'
    page_title = 'Customer Groups'
    
    def get(self, request):
        customer_groups = CustomerGroup.objects.filter(client_id=request.user.client.client_id)
        self.add_to_context(
            customer_groups=customer_groups
        )
        return render(request, self.template, self.context)

class CustomerGroupCreateView(PageView):
    template = 'main_app/customers/customer_groups/create.html'
    page_title = 'Add a Customer Group'

def send_email(recipients: list, subject, html:str = 'An error has occured, email creation has not been completed', sender: str = 'admin@pyrl.uk'):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    api_key = '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'
    staging_api_key = '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'
    message = Mail(
        from_email=sender,
        to_emails=recipients,
        subject=subject,
        html_content=html
        )
    try:
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(message)
    except Exception as e:
        print(e.message)
        
class CustomerContactActivationView(PageView):
    template = 'main_app/customers/contacts/activate.html'
    page_title = 'Thank you!'
    
    def get(self, request, customer_contact_uuid):
        try:
            contact = CustomerContact.objects.get(customer_contact_uuid=customer_contact_uuid)
            contact.activated = True
            contact.save()
            message = 'Thank you for activating your Pyrl Contact Account.'
        except:
            message = "Something's gone wrong, please contact admin@pyrl.uk for more information."
        
        self.add_to_context(message=message)
        return render(request, self.template, self.context)
            
        
    