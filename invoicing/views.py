from django.shortcuts import render, redirect
from django.views import View
from invoicing.models import invoice
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from uuid import uuid4
import random

class entity_info:
    # internal object address
    class entity_address:
        line_1 = ''
        line_2 = ''

        def __init__(self, line_1, line_2):
            self.line_1 = line_1
            self.line_2 = line_2
    
    name = ''
    address = None
    def __init__(self, name, address):
        self.name = name
        self.address = address

class invoice_object:
    table = None
    currency = None
    terms = None
    invoice_date = None
    invoice_due_date = None
    notes = 'Notes holder'
    terms_conditions = 'Terms and Conditions holder'

    def __init__(self, table, currency: str, terms: str, invoice_date: str, invoice_due_date, notes, terms_conditions, *args, **kwargs):
        self.table = table
        self.currency = currency
        self.terms = terms
        self.invoice_date = invoice_date
        self.invoice_due_date = invoice_due_date
        self.notes = notes
        self.terms_conditions = terms_conditions

class invoice_table:
    class invoice_row:
        invoice_number = None
        label = None
        description = None
        quantity = None
        rate = None
        total = None

        def __init__(self, invoice_number, label, description, quantity, rate, *args, **kwargs):
            self.invoice_number = invoice_number
            self.label = label
            self.description = description
            self.quantity = quantity
            self.rate = rate
            self.total = quantity * rate

    rows = None
    table_total = None
    discount = 0
    discount_total = 0
    sales_tax = 0
    sales_tax_total = 0
    subtotal = 0

    def __init__(self, rows, discount, sales_tax):
        self.rows = rows
        
        total = 0

        for row in rows:
            total += row.total

        self.subtotal = total
        self.discount = discount
        self.sales_tax = sales_tax
        self.discount_total = discount * total
        self.sales_tax_total = sales_tax * total
        self.table_total = total - self.discount_total - self.sales_tax_total

class pdf_page:
    table = None
    page_number = None

    def __init__(self, table, page_number, *args, **kwargs):
        self.table = table
        self.page_number = page_number

def generate_invoice_table(n):
    rows = []
    total = 0
    for i in range(0, n):
        random_qty = random.randint(1, 10)
        random_rate = random.randint(1, 10)
        temp_total = random_qty * random_rate
        row_element = invoice_table.invoice_row(i + 1, uuid4(), uuid4(), random_qty, random_rate)
        rows.append(row_element)
        total += temp_total
    table = invoice_table(rows=rows, discount=0.1, sales_tax=0.14)
    return table

def generate_pages(table, pag, middle_pag):
    pages = []
    if (len(table) <= 7):
        print('1 page')
        pages.append(pdf_page(table[:], 1))
    elif (len(table) <= 32):
        print('2 pages')
        pages.append(pdf_page(table[:16], 1))
        pages.append(pdf_page(table[16:], 2))
    elif (len(table) > 32):
        pages.append(pdf_page(table[:16], 1))
        remaining_rows = len(table[16:]) % middle_pag
        number_middle_rows = 0
        if remaining_rows > 0:
            number_middle_rows = len(table[16:-remaining_rows])
        else:
            number_middle_rows = len(table[16:])
        number_middle_pages = number_middle_rows / middle_pag
        
        for i in range(int(number_middle_pages)):
            pdf_table = table[16 + (i * middle_pag) : 16 + ((i + 1) * middle_pag)]
            pages.append(pdf_page(pdf_table, i + 1))
        pages.append(pdf_page(table[-remaining_rows:], len(pages) + 1))
    return pages

# Create your views here.
class index(View):
    def get(self, request):
        if request.user.is_authenticated:
            total_invoices = invoice.objects.all()
            selected_invoice = total_invoices[0]
            print(User.objects.all())
            print(dir(selected_invoice))
            print(selected_invoice.pid)
            print(selected_invoice.invoice_id)
            print(selected_invoice.company_id)
            print(selected_invoice.date_of_invoice)
            return render(request, 'invoice/index.html', {'total_invoices': total_invoices, 'selected_invoice': selected_invoice})
        else:
            return redirect('base:index')
        
class create_invoice(View):
    def get(self, request):
        pass

def pdf_generator(request, company_id):
    if request.method == "GET":
        invoice_id = uuid4()
        from_entity = entity_info('Pyrl', entity_info.entity_address('45 Monkston Ave.', 'Bethlehem, Oxfordshire'))
        to_entity = entity_info('Alex & co.', entity_info.entity_address('29 Leaberry', 'New Bradwell, Milton Keynes'))

        currency = None
        if random.random() > 0.5:
            currency = '£'
        else:
            currency = '$'

        n_items = 60
        pag_number = 10
        middle_pag = 22

        table = generate_invoice_table(n_items)
        pages = generate_pages(table.rows, pag_number, middle_pag)
        current_invoice = invoice_object(table, currency, 'Net 10', '11/10/2001', '21/10/2001', 'This is the notes', 'These are ts & cs')

        will_fit = len(pages[-1].table) < 16

        if len(pages) == 1:
            first_page = [pages[0]]
            return render(request, 'pdf/single_page.html', { 'invoice_id': invoice_id, 
                        'to_entity': to_entity, 
                        'from_entity': from_entity, 
                        'current_invoice': current_invoice, 
                        'first_page': first_page,
                       })
        elif len(pages) == 2:
            will_fit = len(pages[-1].table) > 0
            first_page = [pages[0]]
            last_page = [pages[1]]
            return render(request, 'pdf/double_page.html', { 'invoice_id': invoice_id, 
                        'to_entity': to_entity, 
                        'from_entity': from_entity, 
                        'current_invoice': current_invoice, 
                        'first_page': first_page,
                        'last_page': last_page,
                        'will_fit': will_fit
                       })
        elif len(pages) >= 3:
            first_page = [pages[0]]
            last_page = [pages[-1]]
            middle_pages = pages[1:-1]

            return render(request, 'pdf/multi_page.html', { 'invoice_id': invoice_id, 
                        'to_entity': to_entity, 
                        'from_entity': from_entity, 
                        'current_invoice': current_invoice, 
                        'first_page': first_page,
                        'middle_pages': middle_pages,
                        'last_page': last_page,
                        'will_fit': will_fit
                       })
        return render(request, '404.html', {})
    elif request.method == "POST":
        return redirect('base:index')