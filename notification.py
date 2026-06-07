class NotificationEngine:
    
    def notify(self, missed_tasks):

        if not missed_tasks:

            return "No Alerts"

        return f"{len(missed_tasks)} Tasks Missed Deadline ⚠"