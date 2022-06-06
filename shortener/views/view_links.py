from django.views.generic import  ListView
from ..models.urls_model import Urls
from ..mixins import SuperuserRequiredMixin

# View links View

class URLSListView(SuperuserRequiredMixin, ListView, ):

    login_url = 'login'
    redirect_field_name = 'login'

    model = Urls
    template_name = "shortener/view_links.html"
    context_object_name = "links"
    paginate_by = 10
    ordering = ["-date_created"]
