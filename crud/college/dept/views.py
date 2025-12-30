
from django.shortcuts import render,redirect
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["products"] #db_name

col = db["national_products"] #collection_name

product = [];id=0


def about(request):
    global id
    if request.method == "POST":
        a = request.POST['pro_name']
        b = request.POST['desc']
        c = request.POST['category']
        d = request.POST['price']

        id+=1
        col.insert_one({
            'pro_id': id,
            'product_name': a,
            'description': b,
            'category': c,
            'price': d,
            })
        # print(product)
        # return redirect('/read-pro')
    return render(request,'sample.html')

def read(request):
    read_data = list(col.find())
    return render(request, 'read.html', {'data': read_data})

def update_product(request,id):
    update_data = list(col.find({'pro_id': id}))
    l=[]
    for i in range(len(update_data)):
        l=update_data[i]
    # print(l)
    if request.method == "POST":
        a = request.POST['pro_name']
        b = request.POST['desc']
        c = request.POST['category']
        d = request.POST['price']


        # col.update_one(
        #     {'pro_id': id},
        #     {"$set": {
        #         'product_name': request.POST['pro_name'],
        #         'description': request.POST['desc'],
        #         'category': request.POST['category'],
        #         'price': request.POST['price']
        #     }}
        # )
        col.update_one(
            {'pro_id': id},
            {"$set": {
                'product_name': a,
                'description': b,
                'category': c,
                'price': d
            }}
        )

        return redirect('/read-pro')

    return render(request, 'update.html', {'pro':l})


def delete_product(request,id): #2
    col.delete_one({'pro_id': id}) #
    return redirect('/read-pro')
from django.shortcuts import render

# Create your views here.
