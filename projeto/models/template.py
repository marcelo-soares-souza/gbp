class TemplateModelMixin(object):

    def get_detail_url(self):
        return u"/%s/detail/%i" % (str(self.__class__.__name__).lower(), self.id)

    def get_update_url(self):
        return u"/%s/update/%i" % (str(self.__class__.__name__).lower(), self.id)

    def get_delete_url(self):
        return u"/%s/delete/%i" % (str(self.__class__.__name__).lower(), self.id)
