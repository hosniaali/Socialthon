from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id_no', 'region', 'gender', 'age', 'date_created')
    list_filter = ('region', 'age',)
    search_fields = ['id_no', ]


class CharitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'employee_no', 'volunteers_no', 'date_created')
    list_filter = ('region', 'date_created')
    search_fields = ['name']


class DonationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'charity', 'donated_type', 'segment_type', 'status')
    list_filter = ('charity', 'date_created',)
    search_fields = ['user', 'charity', ]


class DonationTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'date_created')
    list_filter = ('type', 'date_created',)
    search_fields = ['type', ]


class SegmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'date_created')
    list_filter = ('type', 'date_created',)
    search_fields = ['type', ]


class SegmentActivityAdmin(admin.ModelAdmin):
    list_display = ('charity', 'segment_type')
    list_filter = ('segment_type', 'charity',)
    search_fields = ['charity', ]


class DoinationActivityAdmin(admin.ModelAdmin):
    list_display = ('charity', 'donated_type')
    list_filter = ('charity', 'donated_type',)
    search_fields = ['charity', ]


class RevenuesAdmin(admin.ModelAdmin):
    list_display = ('charity', 'donations', 'service_fees', 'zakat', 'investments', 'others', 'year')
    list_filter = ('year',)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('charity', 'expenses', 'donations', 'admin_expenses', 'invest_losses', 'others', 'year')
    list_filter = ('year',)


class RatesAdmin(admin.ModelAdmin):
    list_display = ('charity', 'rate')
    list_filter = ('charity',)
    search_fields = ['charity']


admin.site.register(Users, UserAdmin)
admin.site.register(Charities, CharitiesAdmin)
admin.site.register(Donations, DonationsAdmin)
admin.site.register(DonationType, DonationTypeAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(SegmentActivity, SegmentActivityAdmin)
admin.site.register(DoinationActivity, DoinationActivityAdmin)
admin.site.register(Revenues, RevenuesAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Rates, RatesAdmin)
