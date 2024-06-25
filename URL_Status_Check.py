# example of pinging the status of a set of websites asynchronously
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
 
# get the status of a website
def get_website_status(url):
    # handle connection errors
    try:
        # open a connection to the server with a timeout
        with urlopen(url, timeout=3) as connection:
            # get the response code, e.g. 200
            code = connection.getcode()
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason
    except:
        return e
 
# interpret an HTTP response code into a status
def get_status(code):
    if code == HTTPStatus.OK:
        return 'OK'
    return 'ERROR'
 
# check status of a list of websites
def check_status_urls(urls):
    # create the thread pool
    with ThreadPoolExecutor(len(urls)) as executor:
        # submit each task, create a mapping of futures to urls
        future_to_url = {executor.submit(get_website_status, url):url for url in urls}
        # get results as they are available
        for future in as_completed(future_to_url):
            # get the url for the future
            url = future_to_url[future]
            # get the status for the website
            code = future.result()
            # interpret the status
            status = get_status(code)
            # report status
            print(f'{url:20s}\t{status:20s}\t{code}')
 
# list of urls to check
URLS = ['https://rnd-sonar.brilife.co.id/',
        'https://rnd-jenkins.brilife.co.id/',
        'https://rnd-gitlab.brilife.co.id/',
        'https://rnd-portainer.brilife.co.id/',
        'https://rnd-kubedash.brilife.co.id/',
        'https://rnd-graph.brilife.co.id/',
        'http://10.28.3.68:8080/',
        'https://rnd-registry.brilife.co.id/',
        'https://rnd-testing.brilife.co.id/',
        'https://rnd-minio-operator.brilife.co.id/',
        'https://rnd-minioconsole.brilife.co.id/']
# check all urls
check_status_urls(URLS)
