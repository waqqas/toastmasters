from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PollType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Poll(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="polls_created"
    )
    candidates = models.ManyToManyField(User, related_name="polls_as_candidate")
    poll_type = models.ForeignKey(
        PollType, on_delete=models.CASCADE, related_name="polls"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Voting for {self.poll_type}"


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votes")
    candidate = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="votes_received"
    )

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.username}"
