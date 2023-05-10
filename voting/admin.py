from django.contrib import admin

from .admin_models import PollAdmin, PollTypeAdmin, VoteAdmin
from .models import Poll, PollType, Vote

admin.site.register(PollType, PollTypeAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
