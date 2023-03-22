import urllib.request, json
import subprocess

class JarParser():
    def __init__(self, version, verbose=False):
        self.jar_name = 'server.jar'
        self.version_manifest = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'
        self.verbose = verbose
        self.stdout = subprocess.DEVNULL if not self.verbose else 1
        self.stderr = subprocess.DEVNULL if not self.verbose else 2
        self.version = version

    def run(self):
        print("Browsing minecraft versions...")
        version_url = self.browse_mc_versions()
        print(f"Getting {self.version} version info...")
        version_url_info = self.get_jar_from_url(version_url)
        print(f"Downloading {self.version} version jar...")
        self.download_jar_and_generate(version_url_info)
        print("Parsing jar...")
        self.parse_jar()
        print("Moving .json...")
        self.move_json()
        print("Cleaning up...")
        self.clean_up()

    def clean_up(self):
        instructions = [
            f'rm -rf {self.jar_name}',
            f'rm -rf logs',
            f'rm -rf generated',
            f'rm -rf libraries',
            f'rm -rf test',
            f'rm -rf versions'
        ]
        for instruction in instructions:
            subprocess.run(instruction.split(" "), stdout=self.stdout, stderr=self.stdout)
    
    def move_json(self):
        instructions = [
            f'mv ./generated/reports/blocks.json ./data/block_list.json',
            f'mv ./generated/reports/commands.json ./data/commands.json',
            f'mv ./generated/reports/registries.json ./data/registries.json',
        ]
        for instruction in instructions:
            subprocess.run(instruction.split(" "), stdout=self.stdout, stderr=self.stdout)
        
    def parse_jar(self):
        cmd = 'java -DbundlerMainClass=net.minecraft.data.Main -jar server.jar --all'.split(" ")
        subprocess.run(cmd, stdout=self.stdout, stderr=self.stdout)

    def download_jar_and_generate(self, url):
        download = f'wget {url} -O {self.jar_name}'.split(" ")
        subprocess.run(download, stdout=self.stdout, stderr=self.stdout)

    def get_jar_from_url(self, latest_url):
        with urllib.request.urlopen(latest_url) as url:
            latest_version_info = json.loads(url.read().decode())
            return latest_version_info['downloads']['server']['url']

    def browse_mc_versions(self):
        with urllib.request.urlopen(self.version_manifest) as url:
            server_jar_version_list = json.loads(url.read().decode())
            for version in server_jar_version_list["versions"]:
                if version['id'] == self.version:
                    latest_url = version['url']
                    return latest_url

