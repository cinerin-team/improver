# USAGE
## Downloading the EPGCATS
The `1-epgcats_downloader.py` downloads the epgcats which will be updated. After downloading it modifies the folder and renames the file.

For downloading the requested epgcats change in the `configs/variables.py` for example: 
TARGET_FOLDER = "/lab/epg_st_sandbox/erkmiap/PCEPGST-2857/" 
EPGCATS_VERSION = "EPG_28R252VY1"

The first value is the destination folder from where the tests can be triggered from the EPG portal. 
The second value is the version of the epgcats.

## Improving the values
The `3-improve_values.py` improves the checkpoints based on 3 runs and modifies the downloaded epgcats.

To have the checkpoints improved based on 3 new runs you must modify the `configs/new_values.csv` with keeping the first line as a header. For example: 
checkpoint,new_value1,new_value2,new_value3 
PDCdb_ssc_psc_cpu_peak,40.9,39.9,43.4 
PDCdb_ssc_psc_cpu_avg,33.7,33,35.1

Add the file path for the checkpoint file to the `configs/variables.py` starting from the epgcats folder. For example: 
FILE_TO_IMPROVE = "epgcats/tools/verdict/user_checkpoints/stability_checkpoints/tc37540_1_6_16.py"  # starting from epgcats folder 
TARGET_FOLDER = "/lab/epg_st_sandbox/erkmiap/PCEPGST-2857/"

The first value is the file which contains the checkpoints that are supposed to be improved. 
The second value is the destination folder from where the tests can be triggered from the EPG portal.

Attention!! This does only the checkpoint tuning, if other values are needed to be changed then change it manually! Like the subscribers value.
 
 ## Uploading to the repo
The `4-comapre_and_upload_to_repo.py` calculates the changes from the original downloaded epgcats and uploads the changes to the repo.
To upload the changes to the repo and commit changes of the `configs/variables.py` values. For example: 
FILE_TO_IMPROVE = "epgcats/tools/verdict/user_checkpoints/stability_checkpoints/tc37540_1_6_16.py" # starting from epgcats folder 
REPO_FOLDER = '/workspace/git/erkmiap/epg/' 
EPGCATS_VERSION = "EPG_28R252VY1"
ADDITIONAL_FILES_TO_COPY = ["epgcats/tcdb/TC_TID_general/TC_TID_stability.db"]  # like TC_TID_

The first value is the file which contains the checkpoints that are supposed to be improved. 
The second value is the folder where the repo is. WARNING!! the git repo should be clean and updated!!! 
The third value is for comparison to the downloaded epgcats file.
The fourth value is for additional files like starting with TC_TID_ or others and give the files in array elements.
