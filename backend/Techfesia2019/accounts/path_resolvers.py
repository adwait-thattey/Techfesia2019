import os

from accounts.models import Profile
from registration.models import User


def resolve_accounts():
    return 'accounts'

def resolve_user_data_folder(user:User):
    return os.path.join(resolve_accounts(),user.username)

def resolve_user_profile_path(user:User):
    return os.path.join(resolve_user_data_folder(user), 'profile_pictures')
