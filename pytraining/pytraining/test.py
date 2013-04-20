from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner


class TestRunner(DjangoTestSuiteRunner):
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        if not test_labels:
            test_labels = [app.split('.')[-1] for app in settings.APPS_TO_TEST]
        suite = super(TestRunner, self).build_suite(test_labels, extra_tests, **kwargs)
        return suite