#!/bin/bash
SCRIPT_NAME=$(basename $0)


function usage(){

echo -e <<EOF

usage: ${SCRIPT_NAME} [-h|--help] [-v|--verbose] 

description: 
        this script will move the systemd units from the ./ servce folder to the /etc/systemd/system/ folder 
        and perform a daemon-reload to load the new/updated units.

arguments: 
    -h,--help       print this message 
    -v,--verbose    output more info on actions performed

EOF

}

while getopts ":vh" o; do
        case "${o}" in
        v)
                verbose=true
                ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

