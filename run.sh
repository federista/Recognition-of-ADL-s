file_list=( "/home/zaid/project/Recognition-of-ADL-s/PrepareData.py" "/home/zaid/project/Recognition-of-ADL-s/TrainModel.py" "//home/zaid/project/Recognition-of-ADL-s/PrepareSimulationData.py" "/home/zaid/project/Recognition-of-ADL-s/Model_Prediction.py" )


for py_file in "${file_list[@]}"
do
    python ${py_file}
done
