import re
import sys
import json


def main():
    with open('target.conf', "r") as f:
        conf = f.read()
    f.close()
    paras = json.loads(conf)
    pattern = paras['pattern']
    filename = paras['filename']
    print("paras is %s \nfilename is %s") % (pattern, filename)
    rule = re.compile(r'.*:4.[^9]\d.*')
    with open("target-ip.txt", 'wa') as f2:
        with open(filename, "r") as f:
            for msg in f:
                item = re.search(rule, msg)
                if item:
                    print item.group()
                    ip = re.match(r'(.*):(.*):(.*):(.*)', str(item.group()))
                    if ip:
                        f2.writelines(str(ip.group(1)) + '\n')
        f.close()

if __name__ == "__main__":
    main()