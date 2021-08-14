from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "website/index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] ="長谷川"
        return ctxt

class AboutView(TemplateView):
    template_name = "website/about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] ="11111111"
        ctxt["skills"] =["aaa","aaab","ppp",]
        return ctxt