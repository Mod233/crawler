import os
import requests
import sys

user = '623257096@qq.com'
pwd = 'cS10241024'


def get_jwt():
    login_info = {'username': user, 'password': pwd}  # dictionary
    try:
        respond = requests.post(url='https://api.zoomeye.org/user/login', json=login_info)
    except requests.RequestException as e:
        print("[-] %s" % e)
        print("[-] fail to connect" % e)
    else:
        if respond.status_code == 200:
            access_token = respond.json()
            # print("access_token is %s\n" % access_token)
            return access_token
        else:
            print("[-] %s %s \n[-] %s" % (respond.status_code, respond.json()["error"], respond.json()["message"]))
            print("[-] fail to connect!")


def useage():
    global mode, query
    mode = raw_input("Please input the type searched: host | web\n")
    if mode != "web" and mode != "host":
        mode = raw_input("Please input the type searched: host | web\n")
    query = raw_input("Please input the keyword\n")


def get_result(jwt):
    authorization = {'Authorization': 'JWT ' + jwt["access_token"]}
    try:
        respond = requests.get(url='https://api.zoomeye.org/' + mode + '/search?query=' + query + "&page=" + str(page),
                               headers=authorization)
    except requests.RequestException as e:
        print("[-] %s" % e)
        print("[-] %s fail to search!" % mode.capitalize())
    else:
        if respond.status_code == 200:
            # print respond.json()
            return respond.json()
        else:
            print("[-] %s %s\n[-] %s" % (respond.status_code, respond.json()["error"], respond.json()["message"]))
            print("[-] %s fail to search!" % mode.capitalize())


def get_info(jwt):
    authorization = {'Authorization': 'JWT ' + jwt["access_token"]}  # dictionary
    try:
        respond = requests.get(
            url='https://api.zoomeye.org/resources-info',
            headers=authorization
        )
    except requests.RequestException as e:
        print("[-] %s" % e)
    else:
        if respond.status_code == 200:
            print respond.json()
            return
        else:
            print("[-] %s %s\n[-] %s" % (respond.status_code, respond.json()["error"], respond.json()["message"]))


def output_data(msg):
    result = list()
    if mode == "host":
        for line in msg["matches"]:
            result.append(line["ip"] + ":" + str(line["portinfo"]["port"]) + "\n")
    else:
        for line in msg["matches"]:
            result.append(line["site"] + "\n")
    return result


def main():
    JWT = get_jwt()
    get_info(JWT)
    global max_page, page
    print("")
    useage()
    if not JWT:
        sys.exit()
    result = list()
    max_page = int(raw_input("Please input the max_page:\n"))
    page = 0
    while page < max_page:
        msg = get_result(JWT)
        if not msg:
            print("[-] finish searching!")
            break
        else:
            if not msg["matches"]:
                print("[-] no data!")
                break
            else:
                result.extend(output_data(msg))
                print("[-] begin page %s" % page)
        page += 1
    result = set(result)
    filename = mode + '-', query, '-', max_page, '.txt'
    with open('filename', 'w') as f:
        f.writelines(result)
    f.close


if __name__ == "__main__":
    main()
