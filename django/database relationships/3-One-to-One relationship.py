
############### models declarations #################
class User(models.Model):
    name = models.CharField(max_length=300)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # alternative way
    profile_picture = models.BooleanField(default=False)


# users creation
>>> amine = User(name='amine'); amine.save();
>>> ahmed = User(name='ahmed'); ahmed.save();
# profiles creations
>>> amine_p = Profile(user=amine, profile_picture=True)
>>> ahmed_p = Profile(user=ahmed, profile_picture=False)

# fetch user objects
>>> amine.name
'amine'
>>> amine.profile.profile_picture
True
>>> ahmed.name
'ahmed'
>>> ahmed.profile.profile_picture
False

# fetch profile objects
>>> amine_p.profile_picture
True
>>> amine_p.user.name
'amine'
>>> ahmed_p.profile_picture
False
>>> ahmed_p.user.name
'ahmed'


