from django.db import models


status_choices = [
    ('T', 'Todo'),
    ('D', 'Done'),
    ('C', 'Canceled'),
]

priority_choices = [
    ('S', 'S-Rank'),
    ('A', 'A-Rank'),
    ('B', 'B-Rank'),
]

class Quest(models.Model):
    text = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=status_choices, default="T")
    priority = models.CharField(max_length=1, choices=priority_choices, default="S")

    def status_translation(self):
        status_texts = {
            "T": "Zu tun",
            "D": "Erledigt",
            "C": "Gecancelt",
            }
        return status_texts[self.status]

    def priority_translation(self):
        priority_texts = {
            "S": "Heute",
            "A": "Diese Woche",
            "B": "Diesen Monat",
            }
        return priority_texts[self.priority]
    
    def __str__(self):
        return f"{self.text} {self.status[0]} {self.priority[0]}"