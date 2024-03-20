def call_api(str_method, config, *path_parts, **params) -> dict:
    import urllib, requests, os
    debug=True
    noproxy='s2ch-adm-c-lab.ad.univ-paris1.fr:8000' + ','+ 'localhost:8000'
    if not 'NO_PROXY' in os.environ: os.environ['NO_PROXY']=noproxy
    # else: os.environ['NO_PROXY'] = os.environ['NO_PROXY'] + ','+ noproxy
    if debug: print('NO_PROXY:',os.environ['NO_PROXY'])
    GET = requests.get
    POST = requests.post
    method = POST if "POST" in str_method else GET

    # if using Heroku, change this to https://YOURAPP.herokuapp.com
    SERVER_URL = config['SERVER_URL'] #'http://localhost:8000'
    REST_KEY = config['REST_KEY'] #''  # fill this later
    # print("call_api started",SERVER_URL,path_parts,params)
    # print("REST_KEY",REST_KEY)
    path_parts = '/'.join(path_parts)
    url = f'{SERVER_URL}/api/{path_parts}'
    done=False; nloops=0; error=False
    while not done and not error and nloops<100:
        nloops+=1
        resp = method(url, json=params, headers={'otree-rest-key': REST_KEY}, allow_redirects=False)
        done=True
        if not resp.ok or resp.status_code >= 300:
            done=False
            print(done,debug)
            if debug : print("resp.ok:",resp.ok)
            msg = (
                f'Request to "{url}" failed on loop {nloops} '
                f'with status code {resp.status_code}: {resp.text}'
            )
            if debug : print("msg:",msg)
            if resp.status_code >= 400:
                error=True
                break
            if debug : 
                print('headers:'); print(resp.headers)
            new_location = resp.headers['Location']
            url_splitted = url.split('://')
            if 'http' in url_splitted[0] : new_location = new_location.replace('http://', url_splitted[0]+'://', 1)
            redirected_url = urllib.parse.urljoin(url, new_location)
            if debug : print("redirected_url:",redirected_url)
            url=redirected_url
    if not done or error:
        if "1" in str_method: raise Exception(msg)
        return dict(error=True, msg=msg)
    return resp.json()
