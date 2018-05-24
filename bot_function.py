import subprocess
from subprocess import check_output,CalledProcessError,PIPE

def create_org(api_key,username,password,orgname,orgrole):
#    subprocess.call(["/bin/sh", "/home/ec2-user/recent_inbuilt_indent/PCF_login.sh"])
    subprocess.call([ "cf", "login", "-a", api_key, "-u", username, "-p", password, "--skip-ssl-validation", "-o", "system", "-s", "system"])
    output=check_output(["cf", "create-org", orgname])
    print(output)
    subprocess.call(["cf", "orgs", "|", "grep", orgname])
    return output

def create_space(api_key,username,password,spacename,spacerole,orgname):
    subprocess.call([ "cf", "login", "-a", api_key, "-u", username, "-p", password, "--skip-ssl-validation", "-o", "system", "-s", "system"])
#    s=userInput.split("_")
#    subprocess.call(["/bin/sh", "/home/ec2-user/recent_inbuilt_indent/PCF_login.sh"])
    subprocess.call(["cf", "target", "-o",orgname])
    output1=check_output(["cf", "create-space",spacename])
    print(output1)
    subprocess.call(["cf", "spaces", "|", "grep", spacename])
    return output1
