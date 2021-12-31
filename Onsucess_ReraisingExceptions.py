"""
On-success Block

Re-raising Exceptions
"""
class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    #returns user's name
    def __repr__(self):
        return f'<User {self.name}>'

#uses the Class User
def get_user_score(user):
    try:
       return perform_calculation(user.engagement_metrics)
    except KeyError: #may or may not run
        print('Incorrect values provided to our calculation function.')
        raise #provides a traceback of the error after printing out the above statement
    finally: #runs everytime
    # else: #only gonna run if an error doesnt happen
        send_engagement_notification(user)


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to {user}.')


my_user = User('Rolf', {'click': 61, 'hits': 100})
get_user_score(my_user)