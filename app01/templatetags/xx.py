from django import template
register=template.Library()

@register.inclusion_tag('ul.html')
def show_ul(num):
    data = [f'第{i:0>3}号技师' for i in range(1, num)]
    return {'data':data}