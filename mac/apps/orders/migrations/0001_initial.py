# Generated by Django 3.0.5 on 2020-04-08 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.TextField(choices=[('produce', 'Произвоственный тикет'), ('request', 'Запрос изделий')], default=('produce', 'Произвоственный тикет'), verbose_name='Тип тикета')),
                ('logistics', models.TextField(choices=[('can_deliver', 'Могу доставить по адресу'), ('need_delivery', 'Нужно чтобы кто-то привез/забрал')], default=('can_deliver', 'Могу доставить по адресу'), verbose_name='Логистика')),
                ('product', models.TextField(choices=[('shield', 'Защитный Экран'), ('valve', 'Клапан')], default='shield', verbose_name='Изделие')),
                ('city', models.TextField(choices=[('moscow', 'Москва'), ('spb', 'Санкт Петербург')], default=('moscow', 'Москва'), verbose_name='Город')),
                ('amount', models.IntegerField(default=10, verbose_name='Количество')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('is_production_ready_cached', models.BooleanField(default=False, verbose_name='Производство завершено')),
                ('is_production_delivered_cached', models.BooleanField(default=False, verbose_name='Изделия доставлены получателю')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.TextField(choices=[('comment', 'Комментарий'), ('is_ready', 'Партия готова'), ('propose_ticket', 'Предложить партию')], default=('comment', 'Комментарий'), verbose_name='Тип тикета')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_updates', to=settings.AUTH_USER_MODEL)),
                ('target_ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='updates', to='orders.Ticket')),
            ],
        ),
    ]
