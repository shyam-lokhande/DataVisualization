import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.contrib.auth.models import User
def get_image():
    # create a bytes buffer for the image to save
    buffer=BytesIO()
    # create the plot with the use of bytesIO object as its 'file'
    plt.savefig(buffer,format='png')
    # set the cursor to the beginning of the stream
    buffer.seek(0)
    #retrieve the entire content of the file
    image_png=buffer.getvalue()

    graph=base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    #free the memory of the buffer
    buffer.close()
    return graph


def get_simple_plot(chart_type,*args,**kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x=kwargs.get('x')
    y=kwargs.get('y')
    df=kwargs.get('df')

    #bar plot
    if chart_type=='Bar Plot':
        title = "Total Price by Day - Bar Plot"
        plt.title(title)
        plt.bar(x,y)

    elif chart_type=='line':
        title = "Total Price by Day - Line "
        plt.title(title)
        plt.plot(x,y)
    else:
        title = "Product Count - Count Plot"
        plt.title(title)
        sns.countplot(x='name',data=df)
    plt.xticks(rotation=45)
    plt.tight_layout()


    graph=get_image()
    return graph

def get_salesman_from_id(val):
    salesman=User.objects.get(id=val)
    return salesman

