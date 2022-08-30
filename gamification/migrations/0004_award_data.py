# Generated by Django 4.1 on 2022-08-30 02:32

from django.db import migrations

from gamification.models import Award

award_data = [
    {"name": "I am Everywhere", "description": "Consecutively attends 4 meetings"},
    {
        "name": "Master of Momentum",
        "description": "2 speeches and a Tag role in a month ",
    },
    {
        "name": "Been there, Done that",
        "description": "TOE, TTM, GE (all three in a month) and One TAG roles",
    },
    {
        "name": "You Need Me",
        "description": "2 speech evaluations and 1 table topic evaluation (in a month) and a  Tag role",
    },
    {
        "name": "Club Star",
        "description": "1 speech, 1 evaluation, 1 Big three ,Perfect presence with one Tag role",
    },
    {
        "name": "Solid Foundation",
        "description": "Ah counter, vote counter, grammarian, timer, table topic master, chat master (Any 4 out of above in a month) vote counter and timer is a MUST",
    },
    {
        "name": "Standard Bearer",
        "description": "Take up a role in every meeting for 4 weeks",
    },
    {"name": "Hello! Hello!", "description": "Bring one guest to the meeting"},
    {
        "name": "Welcome to the Party!",
        "description": "Bring three guests to the meeting",
    },
    {"name": "Good News!", "description": "Help convert a guest into a member"},
    {"name": "One of Us!", "description": "Help convert three guests into members"},
    {"name": "Halfway there!", "description": "Cross 50 points"},
    {"name": "On Fire!", "description": "Win Best Big 3, 3 times"},
    {"name": "Silver-tongue", "description": "Win Best Speaker 3 times"},
    {"name": "Craft & Candour", "description": "Win Best Evaluator 3 times"},
    {"name": "The Tourist", "description": "Visit two other clubs (online/offline)"},
    {"name": "The Ambassador", "description": "Take up a role in another club"},
    {"name": "Candle in the Wind", "description": "Take up mentorship"},
    {"name": "Puppet Master", "description": "Organize a contest"},
    {"name": "Gladiator", "description": "Participate in a contest"},
    {"name": "All Rounders", "description": "Performed all these roles"},
    {
        "name": "Balance Master",
        "description": "Deliver 4 speeches in 4 months each per month",
    },
    {
        "name": "Cry Havoc!",
        "description": "Use the communication skills you learned in Toastmasters, A outside the club",
    },
    {"name": "Century!", "description": "Cross 100 points"},
]


class Migration(migrations.Migration):
    def add_award_data(app, schema_editor):
        awards = [Award(**data) for data in award_data]
        Award.objects.bulk_create(awards)

    def remove_award_data(app, schema_editor):
        award_names = [data["name"] for data in award_data]
        Award.objects.filter(award__name__in=award_names).delete()

    dependencies = [
        ("gamification", "0003_award"),
    ]

    operations = [
        migrations.RunPython(add_award_data, remove_award_data),
    ]
