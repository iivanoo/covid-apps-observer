import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import zipfile
from subprocess import call
import sys
import os
import configuration as c

# Credits to https://github.com/HamidrezaMoradi/APK-Downloader        
def downloader(downloadURL, path):
    try:
        r_downloadURL = requests.get(downloadURL, stream=True)
        with open(path, "wb") as handle:
            for data in tqdm(r_downloadURL.iter_content()):
                handle.write(data)
        return True
    except Exception:
        return False

# Credits to https://github.com/HamidrezaMoradi/APK-Downloader        
def apkdl_in(package_id):
    apkdl = 'https://apkdl.in/app/details?id=' + package_id
    r = requests.get(apkdl)
    App_Page = BeautifulSoup(r.text, 'html.parser')
    downloadUrl = App_Page.find("a", itemprop='downloadUrl')

    downloadUrl = 'https://apkdl.in'+downloadUrl['href']
    r = requests.get(downloadUrl)
    DownloadPage = BeautifulSoup(r.text, 'html.parser')
    downloadUrl = DownloadPage.find("a", rel='nofollow')
    return downloadUrl

# Credits to https://github.com/HamidrezaMoradi/APK-Downloader        
def apkplz_net(package_id):
    url = 'https://apkplz.net/app/' + package_id
    r = requests.get(url)
    App_Page = BeautifulSoup(r.text, 'html.parser')
    downloadUrl = App_Page.find("div", attrs={'class':'col-sm-12 col-md-12 text-center'})

    downloadUrl = downloadUrl.find("a", rel='nofollow')['href']
    r = requests.get(downloadUrl)
    DownloadPage = BeautifulSoup(r.text, 'html.parser')
    downloadUrl = DownloadPage.find("a", string='click here')
    return downloadUrl['href']

# Credits to https://github.com/HamidrezaMoradi/APK-Downloader        
def apktada_com(package_id):
    url = 'https://apktada.com/download-apk/' + package_id
    r = requests.get(url)
    App_Page = BeautifulSoup(r.text, 'html.parser')
    downloadUrl = App_Page.find("a", string='click here')
    return downloadUrl['href']

# Credits to https://github.com/HamidrezaMoradi/APK-Downloader        
def m_apkpure_com(package_id):
    url = 'https://m.apkpure.com/android/' + package_id + '/download?from=details' 
    r = requests.get(url)
    App_Page = BeautifulSoup(r.text, 'html.parser')
    downloadUrl = App_Page.find("a", string='click here')
    return downloadUrl['href']

# Credits to Gian Luca Scoccia - https://github.com/S2-group/apkDownloader/
def apk_is_valid(_apk_name):
    with open(os.devnull, "w") as null:
        try:
            error_state = call(["aapt", "dump", "permissions", _apk_name], stdout=null)
            if error_state != 0:
                print("It seems we downloaded an XAPK, we unpack it now...")
        except:
            pass
        return error_state == 0

# Credits to Gian Luca Scoccia - https://github.com/S2-group/apkDownloader/
def xapk_is_valid(_xapk_name, _package_name):
    with zipfile.ZipFile(_xapk_name) as zfile:
        if _package_name in zfile.namelist():
            return True
        else:
            return False

# Credits to Gian Luca Scoccia - https://github.com/S2-group/apkDownloader/
def unpack_xapk(_xapk_name: str, _package_name: str) -> None:
    with zipfile.ZipFile(os.path.join(c.APKS_PATH, _xapk_name)) as zfile:
        zfile.extract(_package_name, c.APKS_PATH)

# Credits to Gian Luca Scoccia - https://github.com/S2-group/apkDownloader/
def verify_apk(apk_name: str, apk_path: str, app_suffix_path: str) -> None:
    if not apk_is_valid(apk_path):
        if xapk_is_valid(apk_path, apk_name + ".apk"):
            new_name = apk_path.split(".apk")[0] + ".xapk"
            os.rename(apk_path, new_name)
            unpack_xapk(app_suffix_path + ".xapk", apk_name + ".apk")
            os.rename(c.APKS_PATH + apk_name + ".apk", apk_path)
            os.remove(new_name)
            if not apk_is_valid(apk_path):
                os.remove(apk_path)
                print("Invalid file {}, removed".format(apk_path))
                return False
            else:
                print("Xapk unpacked successfully!")
                return True
        else:
            os.remove(apk_path)
            print("Invalid file {}, removed".format(apk_path))
            return False
    else:
        return True

def download_apk(app_id, path):
    download_URL = m_apkpure_com(app_id)
    if(downloader(download_URL, path)):
        return True
    download_URL = apkplz_net(app_id)
    if(downloader(download_URL, path)):
        return True
    download_URL = apktada_com(app_id)
    if(downloader(download_URL, path)):
        return True
    download_URL = apkdl_in(app_id)
    if(downloader(download_URL, path)):
        return True
    return False
