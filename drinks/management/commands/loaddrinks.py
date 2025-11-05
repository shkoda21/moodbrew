import json
from django.core.management.base import BaseCommand
from drinks.models import Drink
from django.conf import settings
import os


class Command(BaseCommand):
    help = "Load drinks from a JSON file into the Drink model"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            help="Path to the drinks JSON file",
            default=os.path.join(settings.BASE_DIR, "drinks.json"),
        )

    def handle(self, *args, **options):
        file_path = options["file"]

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            count = 0
            for item in data:
                Drink.objects.create(
                    name=item["name"],
                    category=item["category"],
                    description=item["description"],
                    moods=item["moods"],
                    weather=item["weather"],
                    time_of_day=item["time_of_day"],
                    season=item["season"],
                    image_url=item.get("image_url", "")
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"✅ Loaded {count} drinks successfully!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error loading drinks: {e}"))