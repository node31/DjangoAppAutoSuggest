from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import json
from author_book.models import AB

from django_mongokit import connection,get_database

from django.template import RequestContext

from bson.json_util import dumps



def index(request):
	#return HttpResponse("You are at Index Page")
	return render(request,'author_book/index.html',{})
	
def ajax_call(request):
	#print 'AJAX REACHED HERE'
	#print request.GET['sVal']
	#x = request.GET['sVal']+" returned"
	#print 'x is ',x
	#my_own_dict = {'result':x}
	
	x = request.GET['sVal']
#	print x
		
	connection.register([AB])
	
#	print '2',x
	
	collName = get_database().autoSuggestCollection
# 	collName = get_database().examples	
	
#	print '3',x

	#conditions = {'author':{'$regex':'/^'+x+'/'}}
	#conditions = {u"author":'/^'+x+'/'}
	#conditions = { 'author': { '$regex': '/^v/'} }
	#print conditions
	
	
	#regex = re.compile("/^v/")
	#print 'REGEX:::::::::::::::::::::::::::::::::::::',regex
	
	
	instances = collName.AB.find( { "author": { '$regex' : '^' + x} })
	
# 	instances = collName.AB.find({u"author":u"/^v/"})
	#instances = collName.AB.find()
	
	#instances = collName.AB.find({"author":regex})
	#instances = collName.AB.find({"author":"vlt"})
	#instances = collName.AB.find({"author":"/^v/"})				
	
	print 'CURSORLLLLL',instances,'\n\n\n\n\n'
	"""
	my_own_list = list(instances)
	print my_own_list
	
	
	#print '\n\n\n0'
	#print my_own_list[0]
	
	#i=0
	my_own_dict = {}
	
	print 'HELLO\n'
	j=0
	
	for i in my_own_list:
		print 'xxxx',i
		my_own_dict[j] = i
		j=j+1
	
	for node in instances:
		json.dumps(node,)	"""
	#print my_own_dict
	print 'TRYING TO ENCODE'
	# instances.rewind()
	print "\n count: ", instances.count(), "\n"
	#y = json.dumps(my_own_dict)
	#print 'PRINTING JSON DUMP'
	#print y
	#return HttpResponse(json.dumps(my_own_dict))
	return HttpResponse(dumps(list(instances)))		
	#return HttpResponse("You are at the AJAX CALL")
	#return render_to_response('author_book/output.html',{'all_list':instances},context_instance=RequestContext(request))
	#return render(request,'author_book/index.html',{'all_list':instances})
	
	
def ab_show(request,ab_id):
	#return HttpResponse("You are at the Page of ab  %s" %ab_id )
	return render(request,'author_book/ab_show.html',{'ab_author':'ALPHA','ab_book':'BETA'})

# Create your views here.
