from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import date

GENDER = (
    (1, 'ذكر'),
    (2, 'أنثى'),
)
C_GENDER = (
    (1, 'ذكور'),
    (2, 'إناث'),
    (3, 'ذكور وإناث'),
)
AGE = (
    (1, 'أقل من 7 سنوات'),
    (4, 'من 7 - 18 سنة'),
    (3, 'من 19 - 35 سنة'),
    (2, 'أكثر من 60 سنة'),
)

STATUS = (
    (1, 'تم التقديم'),
    (2, 'جاري المراجعة'),
    (3, 'جاري الإعانة'),
    (4, 'تمت الإعانة'),
    (5, 'مرفوض'),
)


class Users(models.Model):
    id_no = models.CharField(_('رقم الهوية/الإقامة'), max_length=10, unique=True)
    phone_no = models.CharField(_('رقم الجوال'), max_length=20, unique=True)
    region = models.CharField(_('المنطقة'), max_length=30)
    age = models.IntegerField(_('العمر'))
    gender = models.IntegerField(_('الجنس'), choices=GENDER, default=1)
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'المحتاجين'

    def __str__(self):
        return self.id_no


class Charities(User):
    name = models.CharField(_('اسم الجمعية'), max_length=100, unique=True)
    region = models.CharField(_('المنطقة'), max_length=30)
    age = models.IntegerField(_('الفئة العمرية'), choices=AGE, default=1)
    gender = models.IntegerField(_('الفئة النوعية'), choices=C_GENDER, default=1)
    employee_no = models.IntegerField(_('عدد الموظفين'))
    volunteers_no = models.IntegerField(_('عدد المتطوعين'))
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'الجمعيات الخيرية'

    def __str__(self):
        return self.name


class Donations(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name=_('المحتاج'))
    charity = models.ForeignKey(Charities, on_delete=models.CASCADE, verbose_name=_('الجمعية'), null=True)
    donated_type = models.ForeignKey('DonationType', on_delete=models.CASCADE, verbose_name=_('نوع الإعانة'))
    segment_type = models.ForeignKey('Segment', on_delete=models.CASCADE, verbose_name=_('نوع فئة الإعانة'))
    status = models.IntegerField(_('حالة الإعانة'), choices=STATUS, default=1)
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'طلبات الإعانات'

    def __str__(self):
        return '{} - {}'.format(self.user.name, self.charity.name)


class DonationType(models.Model):
    type = models.CharField(_('نوع الإعانة'), max_length=100)
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'نوع الإعانات'

    def __str__(self):
        return self.type

class Segment(models.Model):
    type = models.CharField(_('نوع فئة الإعانة'), max_length=100)
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = ' فئة المحتاجين'

    def __str__(self):
        return self.type

class SegmentActivity(models.Model):
    charity = models.ForeignKey(Charities, on_delete=models.CASCADE, verbose_name=_('الجمعية'))
    segment_type = models.ForeignKey(Segment, on_delete=models.CASCADE, verbose_name=_('نوع فئة الإعانة'))
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'الفئة المستهدفة للجمعية'

    def __str__(self):
        return '{} - {}'.format(self.charity.name, self.donated_type.type)


class DoinationActivity(models.Model):
    charity = models.ForeignKey(Charities, on_delete=models.CASCADE, verbose_name=_('الجمعية'))
    donated_type = models.ForeignKey(Segment, on_delete=models.CASCADE, verbose_name=_('نوع الإعانة'))
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'نوع انشطة الجميعات'

    def __str__(self):
        return '{} - {}'.format(self.charity.name, self.donated_type.type)


class Revenues(models.Model):
    charity = models.ForeignKey(Charities, on_delete=models.CASCADE, verbose_name=_('الجمعية'))
    donations = models.IntegerField(_('التبرعات والهبات والإشتراكات'))
    service_fees = models.IntegerField(_('رسوم الخدمات'))
    zakat = models.IntegerField(_('الزكاة'))
    investments = models.IntegerField(_('الإستثمارات والأوقاف'))
    others = models.IntegerField(_('أخرى'))
    # total
    year = models.DateTimeField(_('السنة'))
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'الإيرادات'

    def __str__(self):
        return self.charity


class Expenses(models.Model):
    charity = models.ForeignKey(Charities, on_delete=models.CASCADE, verbose_name=_('الجمعية'))

    expenses = models.IntegerField(_('مصاريف تنفيذ الخدمات'))
    donations = models.IntegerField(_('المساعدات والتبرعات'))
    admin_expenses = models.IntegerField(_('مصاريف عمومية وإدارية'))
    invest_losses = models.IntegerField(_('خسائر استثمارات'))
    others = models.IntegerField(_('أخرى'))
    # total
    year = models.DateTimeField(_('السنة'))
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-year']
        verbose_name_plural = 'المصروفات'

    def __str__(self):
        return self.charity


class Rates(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name=_('المحتاج'))
    charity = models.ForeignKey(Charities, on_delete=models.CASCADE, verbose_name=_('الجمعية'))
    rate = models.IntegerField(_('التقييم'))
    date_created = models.DateTimeField(_('تاريخ الانشاء'), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'تقييم الجميعات'

    def __str__(self):
        return self.rate
