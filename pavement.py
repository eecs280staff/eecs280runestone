import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
from runestone.server import get_dburl
from sphinxcontrib import paverutils
import pkg_resources
from runestone import get_master_url

sys.path.append(os.getcwd())

home_dir = os.getcwd()

####################
project_name ='eecs280umich'
####################

master_url = None
if not master_url:
    master_url = get_master_url()

master_app = 'runestone'
serving_dir = "./build/eecs280umich"
dynamic_pages = False
if dynamic_pages:
    dest = "./published"
else:
    dest = "../../static"


options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/eecs280umich",
        sourcedir="_sources",
        outdir="./build/eecs280umich",
#        warnerror=True,
        confdir=".",
        project_name = "eecs280umich",
        template_args={'course_id': 'eecs280umich',
                       'login_required':'false',
                       'course_title': project_name,
                       'appname':master_app,
                       'dynamic_pages': dynamic_pages,
                       'loglevel': 10,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'dburl': 'postgresql://user:password@localhost/runestone',
                       'default_ac_lang': 'python',
                       'basecourse': 'eecs280umich',
                       'jobe_server': 'http://jobe2.cosc.canterbury.ac.nz',
                       'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                       'proxy_uri_files': '/jobe/index.php/restapi/files/',
                       'downloads_enabled': 'false',
                       'enable_chatcodes': 'false',
                       'allow_pairs': 'false'
                        }
    )
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# If DBURL is in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.