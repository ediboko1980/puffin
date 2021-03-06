import flask_analytics

from puffin import app


analytics = None

def init():
    global analytics
    if app.config['ANALYTICS_PIWIK_BASE_URL']:
        app.config['ANALYTICS'] = {}
        app.config['ANALYTICS']['PIWIK'] = {}
        app.config['ANALYTICS']['PIWIK']['BASE_URL'] = app.config['ANALYTICS_PIWIK_BASE_URL']
        app.config['ANALYTICS']['PIWIK']['SITE_ID'] = app.config['ANALYTICS_PIWIK_SITE_ID']
    analytics = flask_analytics.Analytics(app)
