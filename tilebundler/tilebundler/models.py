from django.db import models
from django.conf import settings

class Tileset(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)
    #geom = models.MultiPolygonField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: add a map proxy layer here
    #layer = models.ForeignKey(Layer)

    def __unicode__(self):
        return self.name
        #return "name: {}, created_at: {}".format(self.name, self.created_at)