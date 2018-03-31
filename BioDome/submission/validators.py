from django.core.validators import RegexValidator

class ExtensionValidator(RegexValidator):
    def __init__(self, extensions, message=None):
        if not hasattr(extensions, '__iter__'):
            extensions = [extensions]
        regex = '\.(%s)$' % '|'.join(extensions)
        if message is None:
            message = 'File type not supported. Accepted types are: %s.' % ', '.join(extensions)
        super(ExtensionValidator, self).__init__(regex, message)

    def __call__(self, value):
        super(ExtensionValidator, self).__call__(value.name)


def docx_path_handler(instance, filename):
    return "files/{id}/manuscript_{file}.docx".format(id=instance.slug, file=instance.slug)

def fig1_path_handler(instance, filename):
    return "files/{id}/figure_1_{file}.jpg".format(id=instance.slug, file=instance.slug)
def fig2_path_handler(instance, filename):
    return "files/{id}/figure_2_{file}.jpg".format(id=instance.slug, file=instance.slug)
def fig3_path_handler(instance, filename):
    return "files/{id}/figure_3_{file}.jpg".format(id=instance.slug, file=instance.slug)
def fig4_path_handler(instance, filename):
    return "files/{id}/figure_4_{file}.jpg".format(id=instance.slug, file=instance.slug)
def fig5_path_handler(instance, filename):
    return "files/{id}/figure_5_{file}.jpg".format(id=instance.slug, file=instance.slug)
def fig6_path_handler(instance, filename):
    return "files/{id}/figure_6_{file}.jpg".format(id=instance.slug, file=instance.slug)
def suppl_path_handler(instance, filename):
    return "files/{id}/supplemental_{file}.pdf".format(id=instance.slug, file=instance.slug)
