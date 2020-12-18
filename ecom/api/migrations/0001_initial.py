from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
            name="munisiva",
            email="muni@dev.com",
            is_staff=True,
            is_superuser=True,
            phone="9502413125",
            gender="Male"
        )
        user.set_password("12345678")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]