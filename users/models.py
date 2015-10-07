from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    class Meta:
        proxy = True

    def __unicode__(self):

        if self.first_name:
            return u'%s %s' % (self.last_name, self.first_name)
        else:
            return u'%s' % self.username
