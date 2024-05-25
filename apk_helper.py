from apkutils import APK
import xmltodict

def get_apk_info(file_path: str):
    with APK.from_file(file_path) as apk:
        apk.parse_resource()
        manifest = xmltodict.parse(apk.get_manifest())
        package = manifest["manifest"]["@package"]
        activity = manifest["manifest"]["application"]["activity"]["@android:name"]
        return package, activity