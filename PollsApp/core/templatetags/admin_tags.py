from django import template
from django.http import QueryDict
from django.core.paginator import Page, Paginator

register = template.Library()

# Pagination Tags

@register.simple_tag
def get_pagination_url(query_url: QueryDict, page: int):
    _copy_dict = query_url.copy()
    if _copy_dict.get('page', None):
        del _copy_dict['page']

    _copy_dict['page'] = page
    return _copy_dict.urlencode()

@register.inclusion_tag("base/components/pagination.html", takes_context=True)
def pagination(context):
    request = context.get("request")
    page_obj: Page = context.get('page_obj')

    return {
        "request": request,
        "page_obj": page_obj,
        "pages_number": page_obj.paginator.get_elided_page_range(on_each_side=1, number=page_obj.number)
    }


# Modals Tags

@register.tag
def modal(parser, token):
    nodelist = parser.parse(('endmodal', ))
    parser.delete_first_token()
    return ModalNode(nodelist)

class ModalNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        _out = template.loader.render_to_string("base/components/modals/base_modal_render.html"
            , { "content": output })
        return _out