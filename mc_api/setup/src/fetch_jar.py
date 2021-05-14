import urllib.request, json
import subprocess

def download_jar_and_generate(url):
    download = f'wget {url} -O server.jar'.split(" ")
    subprocess.run(download)
    return

def get_jar_from_url(latest_url):
    with urllib.request.urlopen(latest_url) as url:
        latest_version_info = json.loads(url.read().decode())
        download_jar_and_generate(latest_version_info['downloads']['server']['url'])
        return

def browse_mc_versions():
    with urllib.request.urlopen("https://launchermeta.mojang.com/mc/game/version_manifest.json") as url:
        server_jar_version_list = json.loads(url.read().decode())

        latest_version = server_jar_version_list["latest"]["release"]

        for version in server_jar_version_list["versions"]:
            if version['id'] == latest_version:
                latest_url = version['url']
                get_jar_from_url(latest_url)
                return
        
browse_mc_versions()
