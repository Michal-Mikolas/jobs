from jobs import Jobs
import pytest
from datetime import time



jobs = Jobs(cache=JobsFileCache('temp/tests.json'))

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



def test_get_steps():
    assert False
