# create a folder in the sandbox, and use that
import re
import subprocess

TARGET_FOLDER = "/lab/epg_st_sandbox/erkmiap/PCEPGST-2857/"
EPGCATS_VERSION = "EPG_28R252XS1"

if __name__ == '__main__':
    subprocess.call(
        ["cp", "/lab/epg_scm4_builds/program/ci/" + EPGCATS_VERSION + "/epgcats", TARGET_FOLDER, "-r"])
    subprocess.call(
        ["cp", "/lab/epg_scm4_builds/program/ci/" + EPGCATS_VERSION + "/vipp/test-tools.info", TARGET_FOLDER])
    subprocess.call(
        ["mv", TARGET_FOLDER + "test-tools.info", TARGET_FOLDER + "paths"])

    with open(TARGET_FOLDER + "paths", "r+") as file:
        file_contents = file.read()
        old_config_path_text = r'configpath=.*'
        new_config_path_text = "configpath=" + TARGET_FOLDER + "epgcats"
        file_contents = re.sub(old_config_path_text, new_config_path_text, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

    subprocess.call(
        ["chmod", "-R", "777", TARGET_FOLDER])
