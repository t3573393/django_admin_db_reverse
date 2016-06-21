#coding:utf8
from django.template import loader, Context


def render_models(render_data):
    template = loader.get_template('db_reverse/models.html')
    context = Context({
        'render_data': render_data
    })
    return template.render(context)


def render_admin(render_data):
    template = loader.get_template('db_reverse/admin.html')
    context = Context({
        'render_data': render_data
    })
    return template.render(context)


def render_markdown(render_data):
    template = loader.get_template('db_reverse/markdown.html')
    context = Context({
        'render_data': render_data
    })
    return template.render(context)