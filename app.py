from bottle import Bottle, route, run, request, response
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


scheduler = BackgroundScheduler()
scheduler.start()

app = Bottle()
app.mount('/email', app)

@app.route('/enviar')
def enviar():
	raise Exception(" error")
	print 'enviando e-mails...'

@app.route('/json')
def json():
	return {'idade': 31, 'endereco': 'rua andre rocha'}

@app.route('/xml')
def get_xml():
	# response.headers['Content-Type'] = 'xml/application'
	response.content_type = 'xml/application'
	xml_xpto = ''
	return xml_xpto

@app.route('/xml', method='POST')
def post_xml():
	# import ipdb; ipdb.set_trace()
	# print request 
	return request.body

def my_listener(event):
	if event.exception:
		print('ops!')
	else:
		print('ok')

scheduler.add_job(enviar, 'interval', seconds=10)
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

run(app, host='127.0.0.1', port=8080, debug=True, reloader=True)