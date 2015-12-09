from django.db import models
from users.models import User
from sitetree.models import TreeItemBase, TreeBase


class TagsMixin:
    """ Tags model mixin """

    def get_tags_as_string(self):
        """
        Return tags as formatted string
        :return: formatted string
        """
        return ', '.join([tag.name for tag in self.tags.all()])

    get_tags_as_string.short_description = 'Tags'


class CommonInfo(models.Model):
    """ CommonInfo abstract model """

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="%(app_label)s_%(class)s_created_by")
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, editable=False,
                                    related_name="%(app_label)s_%(class)s_modified_by")

    class Meta:
        abstract = True


class SiteTreeTree(TreeBase):
    """ FH tree model."""
    pass


class SiteTreeItem(TreeItemBase):
    """ FH tree item model."""

    icon = models.CharField(max_length=50, null=True, help_text='FontAwesome icon. Example: fa-user.')
