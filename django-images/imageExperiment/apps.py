from django.apps import AppConfig


class ImageExperimentConfig(AppConfig):
    name = 'imageExperiment'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import imageExperiment.signals
