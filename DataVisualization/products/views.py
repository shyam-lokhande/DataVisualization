from django.shortcuts import render
from .models import *
import pandas as pd
from .utils import *
from .forms import *
import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def sales_dist_view(req):
    df=pd.DataFrame(Purchase.objects.all().values())
    df['salesman_id']=df['salesman_id'].apply(get_salesman_from_id)

    df.rename({'salesman_id':'salesman'},axis=1,inplace=True)
    df['date']=df['date'].apply(lambda x:x.strftime('%Y-%m-%d'))

    plt.switch_backend('Agg')
    plt.xticks(rotation=45)
    sns.barplot(x='date',y='total_price',data=df)
    plt.tight_layout()
    graph = get_image()

    context={
        'graph':graph
    }

    return render(req,'products/sales.html',context)

@login_required
def chart_select_view(req):
    graph=None
    err_msg = None
    df=None
    price=None

    try:
        product = pd.DataFrame(Product.objects.all().values())
        purchase_df = pd.DataFrame(Purchase.objects.all().values())
        product['product_id']=product['id']

        if purchase_df.shape[0]>0:
            df = pd.merge(purchase_df,product, on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
            price=df['price']
            if req.method=='POST':
                chart_type = req.POST['chart']
                date_from = req.POST['date_from']
                date_to = req.POST['date_to']

                df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                df2=df.groupby('date',as_index=False)['total_price'].agg('sum')
                # print(df['date'])
                # print(date_from)
                if chart_type!="":
                    if date_from!="" and date_to!="":
                        df=df[(df['date']>date_from) & (df['date']<date_to)]
                        df2=df.groupby('date',as_index=False)['total_price'].agg('sum')
                    # function to get a graph
                    if df.empty==False:
                        graph = get_simple_plot(chart_type,x=df2['date'] ,y=df2['total_price'] , df=df)
                    else:
                        err_msg="No records for this time period"
                else:
                    err_msg="Please select a chart type to continue"

        else:
            err_msg="No records for purchase"

    except:
        product=None
        purchase_df=None
        err_msg="No records for purchase"


    context = {
        "df": df.to_html(),
        "price":price,
        "err_msg":err_msg,
        "graph":graph
    }
    return render(req,'products/main.html',context)


@login_required
def add_purchase(req):
    add_msg=None

    form = PurchaseForm(req.POST or None)
    if form.is_valid():
        obj= form.save(commit=False)
        obj.salesman=req.user
        obj.save()     

        form=PurchaseForm()
        add_msg="Congratulations !!Your product has been added to the cart."    

    context={
        'form':form,
        'add_msg':add_msg,
    }

    return render(req,'products/add.html',context)