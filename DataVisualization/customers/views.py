from django.shortcuts import render
import pandas as pd
import matplotlib as plt
import seaborn as sns
from .models import *
from products.utils import get_image
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Customer_corr_view(req):
    err_msg=None
    corr=None
    graph=None
    df = pd.DataFrame(Customers.objects.all().values())
    if df.empty:
        err_msg="There are no records of Customers !!"
    else:
        corr=round(df['budget'].corr(df['employment']),2)
        plt.switch_backend('Agg')
        sns.jointplot(x='budget',y='employment',kind='reg',data=df).set_axis_labels('Company Budget','Number of Employees')
        graph = get_image()

    context={
        'graph':graph,
        'corr':corr,
        'err_msg':err_msg
    }

    return render(req,'customers/main.html',context)