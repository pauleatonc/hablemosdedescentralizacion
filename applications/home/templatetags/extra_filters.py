from django import template

register = template.Library()

@register.filter
def has_documents(tipo_documento, is_public=None):
    for seccion_documento in tipo_documento.secciondocumentos_set.all():
        if is_public is None:
            if seccion_documento.seccion_documentos.all():
                return True
        elif is_public:
            if seccion_documento.seccion_documentos.filter(public=True):
                return True
    return False

@register.filter
def has_public_documents(seccion_documento):
    return seccion_documento.seccion_documentos.filter(public=True).exists()


@register.filter
def public_documents(seccion_documento):
    return seccion_documento.seccion_documentos.filter(public=True)

