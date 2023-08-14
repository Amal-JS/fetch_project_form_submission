from django.http import JsonResponse
from django.shortcuts import redirect, render
from . forms import Custom_Form

# Create your views here.
from django.http import JsonResponse

def index(request):

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest': #we are using fetch using header set to 'X-Requested-With': 'XMLHttpRequest' ajax header
        form = Custom_Form(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
        else:
            
            '''
            form.errors
            <ul class="errorlist"><li>name<ul class="errorlist"><li>Name with &#x27;a&#x27; 
            not allowed</li><li>Name should be atleast 5 characters</li></ul></li><li>email
            
            <ul class="errorlist"><li> &#x27;a&#x27; 
            want to be in email</li><li>account want to be in Gmail</li></ul></li></ul>
            
            '''
            
            '''
            form.errors.items()

            dict_items([('name', ["Name with 'a' not allowed", 'Name should be atleast 5 characters']),
              ('email', [" 'a' want to be in email", 'account want to be in Gmail'])])
            '''
            errors = [{'field': field, 'message': messages} for field, messages in form.errors.items()]
            return JsonResponse({
                'message': 'rejected',
                'errors': errors  #sending this errors as list inside their will be object with field name and errors in array  js 
            })
    form = Custom_Form()
    return render(request, 'index.html', {'form': form})








def success(request):
    return render(request,'success.html')