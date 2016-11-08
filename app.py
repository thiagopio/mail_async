# -*- coding: utf-8 -*-
from bottle import Bottle, run, request, HTTPError, HTTPResponse
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from model.mail_parse import Parse
from model.exception import FieldsException


scheduler = BackgroundScheduler()
app = Bottle()


@app.route('/healthcheck', method='GET')
def healthcheck():
    return 'WORKING'


@app.route('/ispmailws/fila', method='POST')
def schedule():
    if request.content_type != 'text/xml':
        return HTTPError(status=415)

    try:
        xml = request.body.read()
        parse_mail = Parse(xml)
        print parse_mail.__dict__
    except FieldsException, e:
        return HTTPError(status=400, exception=e)
    except Exception, e:
        raise e

    return HTTPResponse(status=202)


@app.route('/envio/ativar', method='GET')
def start_schedule():
    scheduler.start()
    return HTTPResponse(body='ATIVADO')


@app.route('/envio/desativar', method='GET')
def stop_schedule():
    scheduler.remove_all_jobs()
    return HTTPResponse(body='DESATIVADO')


def verify(event):
    if event.exception:
        print('------------')
    else:
        print('---> ok <---')


scheduler.add_job(healthcheck, 'interval', seconds=5)
scheduler.add_listener(verify, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

run(app, host='127.0.0.1', port=8080, debug=True, reloader=True)