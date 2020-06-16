from src.handler.sunrise import SunriseHandler


def config_resources(api):
    api.add_resource(SunriseHandler, '/sunrise')
