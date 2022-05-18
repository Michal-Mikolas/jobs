class JobsFileCache():
    def __init__(self, file_path):
        self.file_path = file_path


class Jobs():
    def __init__(self, cache):
        self.cache = cache
        self.jobs = {}

    def define(self, name:str, callback:function,
        args=None,
        kwargs:dict=None,
        description:str=None,
        depends_on=None,
        repeat=None,
        on_success:function=None
    ):
        self.jobs[name] = {
            'name': name,
            'callback': callback,
            'args': args,
            'kwargs': kwargs,
            'description': description,
            'depends_on': depends_on,
            'repeat': repeat,
            'on_success': on_success,
        }

    def _get_steps(self):
        return []




if __file__ == '__main__':
    def simple_job(a, b, c):
        pass


    from datetime import time

    jobs = Jobs(cache=JobsFileCache('temp/jobs.json'))

    jobs.define('zz-general',
        ZZGeneral.run,
        description='Refreshes [zz_davka|zz_doklad].[_insurance|_icz]',
    )

    jobs.define('zz-year',
        ZZYear.run,
        args=['Foo', jobs.result('zz_general')],  # or kwargs={'foo': 'Foo', 'general': jobs.result('zz_general')}
        description='Refreshes [zz|zz_davka|zz_doklad]._year',
        depends_on=['zz-general', 'faktura-year'],
    )

    jobs.define('medibot',
        Medibot.run,
        description='Runs Medibot instance',
        repeat=-1,  # -1 means forever
        on_success=lambda: (print('Waiting 10 seconds...'), time.sleep(10)),
    )

    jobs.define('zz-all',
        None,
        depends_on=['zz-general', 'zz-year', 'zz-opravitelne'],
    )

    jobs.run_by_args()


    import pytest

    def test_get_steps():
        assert False
