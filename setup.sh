#!/usr/bin/bash
COMMAND=$1

THIS=setup.sh

function export_path {
    export PYTHONPATH=$PWD:$PYTHONPATH
}

function compile_cython {
    python setup.py develop
}

function clean {
    echo "Cleaning IC generated files:"
    FILETYPES='*.c *.so *.pyc __pycache__'
    for TYPE in $FILETYPES
    do
                echo Cleaning $TYPE files
        REMOVE=`find . -name $TYPE`
        if [ ! -z "${REMOVE// }" ]
        then
            for FILE in $REMOVE
            do
               rm -rf $FILE
            done
        else
            echo Nothing found to clean in $TYPE
        fi
    done
}

case $COMMAND in
    export_path)    export_path ;;
    compile_cython) compile_cython  ;;
    clean)          clean ;;

    *) echo Unrecognized command: ${COMMAND}
       echo
       echo Usage:
       echo
       echo "source $THIS export_path"
       echo "source $THIS compile_cython"
       echo "source $THIS clean"
       ;;
esac
