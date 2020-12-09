#!/usr/bin/env bash
set -ex

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && cd .. && pwd)"
NOTEBOOK_DIR=${PROJECT_DIR}/notebooks
OUTPUT_DIR=${PROJECT_DIR}/tmp
NBCONVERT=${CONDA_PREFIX}/bin/jupyter-nbconvert

mkdir -p ${OUTPUT_DIR}

find ${PROJECT_DIR} -type f \( -iname "*.ipynb" ! -iname "*checkpoint.ipynb" \) | while read f
do
    # skip in the following cases:
    # - when notebook runs a local docker compose and it is not necessary for the tests
    # - when notebook connects to omnisci using localhost address
    # - when notebook uses demo_vote_clean table: 'utf-8' codec can't decode byte
    if \
        [ "$f" == "${NOTEBOOK_DIR}/01_Introduction.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/additional_examples/A01_Getting_Started_OmniSciDB_and_Ibis.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/additional_examples/A02_Omnisci_Runtime_UDF.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/02_Querying_Data.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/04_Advanced-Using_UDFs_and_UDTFs.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/workshop/User_Defined_Algorithms_on_Big_Data.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/workshop/Altair_Ibis_Vega_for_Interactive_Exploration.ipynb" ] || \
        [ "$f" == "${NOTEBOOK_DIR}/workshop/Connecting_Holoviz_Visualization_Ecosystem_to_OmniSci_part_1.ipynb" ] \
    ; then
        echo "[II] Skipping ${f}"
        continue;
    fi

    ${NBCONVERT} --to notebook --execute --output ${OUTPUT_DIR}/test.html ${f}
    if [ $? -ne 0 ]
    then
        break
    fi
done

set +ex
