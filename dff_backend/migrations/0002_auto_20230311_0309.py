# Generated by Django 3.0.3 on 2023-03-11 03:09

from django.db import migrations
def load_country_state_data(apps, schema_editor):
    Country = apps.get_model('dff_backend', 'Country')
    State = apps.get_model('dff_backend', 'State')

    States = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chattisgarh','Goa','Gujarat','Haryana',
                'Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur',
                'Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana',
                'Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Chandigarh',
                'Daman','Delhi','Jammu & Kashmir','Ladakh','Lakshadweep','Puducherry']
    country = Country.objects.create(name='India')
    for state in States:
        State.objects.create(name=state, country=country)


class Migration(migrations.Migration):

    dependencies = [
        ('dff_backend', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_country_state_data),
    ]
