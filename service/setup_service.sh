#!/bin/bash
SCRIPT_NAME=$(basename $0)
CWD=$(pwd)
cd "$CWD"

VERBOSE=false



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

function logger(){

}


function clean_old_services(){
        system_service_folder="/etc/systemd/system/"
        rc=0 
        for i in $(ls $CWD/services/*.{service,timer})
        do
                # remove from dest target because we will reinstall the new service
                rm -vf "$system_service_folder$i" 
                rc=$?
        done
        return $rc
}


function install_services (){
        mv "$CWD/services/*.{service,timer}"  /etc/systemd/system/
        sudo systemctl daemon-reload
}



while getopts ":vh" o; do
        case "${o}" in
        v)
                VERBOSE=true
                ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

echo -en 'cleaning services that will be replaced by the new ones'
clean_old_services
if [$? -eq 0 ]

echo -en 'copying the new units that will be ativated'
install_services




