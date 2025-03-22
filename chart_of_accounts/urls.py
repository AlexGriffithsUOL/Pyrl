from django.contrib import admin
from django.urls import path, include
from .views import ChartOfAccountsViews, AccountTypeViews, FinancialStatementViews, AccountViews, CoaAccountLinkViews

app_name = 'chart_of_accounts'
account_type_urlpatterns = [
        path('customer/<int:customer_id>/account_type/create/', view=AccountTypeViews.AccountTypeCreateView.as_view(), name='at_create'),
        path('customer/<int:customer_id>/account_type/<int:at_id>/edit/', view=AccountTypeViews.AccountTypeEditView.as_view(), name='at_edit'),        
    ]

financial_statements_urlpatterns = [
    path('customer/<int:customer_id>/financial_statement/create/', view=FinancialStatementViews.FinancialStatementCreateView.as_view(), name='fs_create'),
    path('customer/<int:customer_id>/financial_statement/<int:fs_id>/edit/', view=FinancialStatementViews.FinancialStatementEditView.as_view(), name='fs_edit'),
]

account_urlpatterns = [
    path('customer/<int:customer_id>/account/create/', view=AccountViews.AccountCreateView.as_view(), name='acc_create'),
    path('customer/<int:customer_id>/account/<int:acc_id>/edit/', view=AccountViews.AccountEditView.as_view(), name='acc_edit'),
]

chart_of_accounts_urlpatterns = [
    path('customer/<int:customer_id>/coa/list/', view=ChartOfAccountsViews.ChartOfAccountsListView.as_view(), name='coa_list'),
    path('customer/<int:customer_id>/coa/create/', view=ChartOfAccountsViews.ChartOfAccountsCreateView.as_view(), name='coa_create'),
    path('customer/<int:customer_id>/coa/<int:coa_id>/edit/', view=ChartOfAccountsViews.ChartOfAccountsEditView.as_view(), name='coa_edit'),
]

coa_link_urlpatterns = [
        path('customer/<int:customer_id>/link/create/', view=CoaAccountLinkViews.CoaAccountLinkCreateView.as_view(), name='cal_create'),
        path('customer/<int:customer_id>/link/<int:cal_id>/edit/', view=CoaAccountLinkViews.CoaAccountLinkEditView.as_view(), name='cal_edit')
]

urlpatterns = [
    *account_type_urlpatterns,
    *financial_statements_urlpatterns,
    *account_urlpatterns,
    *chart_of_accounts_urlpatterns,
    *coa_link_urlpatterns
]