import os
import django
from faker import Faker
import random
from datetime import timedelta, date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

from django.contrib.auth.models import User
from tasks.models import Project, Task, TaskDetail  # update "tasks" to your app name


def populate_db():

    fake = Faker()

    # ------------------------------------------------
    # Create USERS
    # ------------------------------------------------
    users = []
    for _ in range(5):
        username = fake.user_name()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": fake.email(),
                "password": "password123"
            }
        )
        users.append(user)

    print(f"Created/loaded {len(users)} users.")



    # ------------------------------------------------
    # Create PROJECTS
    # ------------------------------------------------
    projects = []
    for _ in range(5):
        project = Project.objects.create(
            name=fake.bs().title(),
            description=fake.text(),
            start_date=fake.date_this_year(before_today=True, after_today=False)
        )
        projects.append(project)

    print(f"Created {len(projects)} projects.")



    # ------------------------------------------------
    # Create TASKS
    # ------------------------------------------------
    tasks = []
    for _ in range(20):
        task = Task.objects.create(
            project=random.choice(projects),
            title=fake.sentence(nb_words=4),
            description=fake.paragraph(),
            due_date=fake.date_between(start_date="-30d", end_date="+60d"),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED'])
        )

        # assign 1-3 users
        assigned = random.sample(users, random.randint(1, len(users)))
        task.assigned_to.set(assigned)

        tasks.append(task)

    print(f"Created {len(tasks)} tasks.")



    # ------------------------------------------------
    # Create TASK DETAILS
    # ------------------------------------------------
    for task in tasks:
        TaskDetail.objects.create(
            task=task,
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph(),
            # image left as default
        )

    print("Created TaskDetail entries for all tasks.")
    print("Database populated successfully!")


if __name__ == '__main__':
    populate_db()
