# USAGE
## Downloading the EPGCATS
The `1-epgcats_downloader.py` downloads the epgcats with to improve. After downloading it does the folder modification and file rename.

For downloading the requested epgcats change in the `configs/variables.py` for example:
TARGET_FOLDER = "/lab/epg_st_sandbox/erkmiap/PCEPGST-2857/"
EPGCATS_VERSION = "EPG_28R252VY1"

The first value is the destination folder from where the tests can be triggered from the EPG portal.
The second value is the version of the epgcats.

## Improving the values
The `2-improve_values.py` improves the checkpoints based on 3 run and modifies in the downloaded epgcats.

To have the checkpoints improved based on 3 new runs modify the `configs/new_values.csv` with keeping the first line as a header for example:
checkpoint,new_value1,new_value2,new_value3
PDCdb_ssc_psc_cpu_peak,40.9,39.9,43.4
PDCdb_ssc_psc_cpu_avg,33.7,33,35.1

And add the file path for the checkpoint file to the `configs/variables.py` starting from the epgcats folder for example:
FILE_TO_IMPROVE = "epgcats/tools/verdict/user_checkpoints/stability_checkpoints/tc37540_1_6_16.py"  # starting from epgcats folder
TARGET_FOLDER = "/lab/epg_st_sandbox/erkmiap/PCEPGST-2857/"

The first value is the file which contains the checkpoints which are supposed to be improved.
The second value is the destination folder from where the tests can be triggered from the EPG portal.

Attention!! This does only the checkpoint tuning, if other values need to be changed then change it manually! Like the subscribers value.

## Uploading to the repo
The `3-comapre_and_upload_to_repo.py` calculates the changes from the original downloaded epgcats and uploads to the repo but only the changes.

To upload the changes to the repo for commit change the `configs/variables.py` values for example:
FILE_TO_IMPROVE = "epgcats/tools/verdict/user_checkpoints/stability_checkpoints/tc37540_1_6_16.py"  # starting from epgcats folder
REPO_FOLDER = '/workspace/git/erkmiap/epg'
EPGCATS_VERSION = "EPG_28R252VY1"

The first value is the file which contains the checkpoints which are supposed to be improved.
The second value is the folder where the repo is. WARNING!! the git repo should be clean and updated!!!
The third value is for comparison to the downloaded epgcats file.
