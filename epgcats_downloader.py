# create a folder in the sandbox, and use that
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
    subprocess.call(
        ["chmod", "-R", "777", TARGET_FOLDER])
